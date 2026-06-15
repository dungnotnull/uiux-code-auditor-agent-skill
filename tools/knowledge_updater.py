"""
knowledge_updater.py — uiux-code-auditor
Crawls authoritative UI/UX sources and appends new knowledge entries to SECOND-KNOWLEDGE-BRAIN.md.

Requirements:
    pip install crawl4ai requests python-dateutil

Usage:
    python knowledge_updater.py               # Full run (all sources)
    python knowledge_updater.py --source nngroup   # Single source
    python knowledge_updater.py --query "WCAG 2.2 mobile"  # Custom query override
    python knowledge_updater.py --dry-run     # Print entries without writing
"""

import argparse
import hashlib
import json
import logging
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)

BRAIN_FILE = Path(__file__).parent.parent / "SECOND-KNOWLEDGE-BRAIN.md"
DEDUP_FILE = Path(__file__).parent / ".seen_urls.json"
UPDATE_LOG_HEADER = "## Knowledge Update Log"

# ---------------------------------------------------------------------------
# Source configurations
# ---------------------------------------------------------------------------

SOURCES = {
    "arxiv": {
        "name": "ArXiv cs.HC",
        "url": "https://export.arxiv.org/api/query",
        "params": {
            "search_query": "cat:cs.HC AND (usability OR accessibility OR heuristic OR WCAG OR UX evaluation)",
            "sortBy": "submittedDate",
            "sortOrder": "descending",
            "max_results": 15,
        },
        "parser": "arxiv",
    },
    "semantic_scholar": {
        "name": "Semantic Scholar",
        "url": "https://api.semanticscholar.org/graph/v1/paper/search",
        "params": {
            "query": "UI UX heuristic evaluation source code accessibility",
            "fields": "title,authors,year,externalIds,abstract,url",
            "limit": 10,
        },
        "parser": "semantic_scholar",
    },
    "nngroup": {
        "name": "Nielsen Norman Group",
        "url": "https://www.nngroup.com/articles/",
        "parser": "nngroup_html",
    },
    "w3c_wcag": {
        "name": "W3C WCAG News",
        "url": "https://www.w3.org/WAI/news/",
        "parser": "w3c_html",
    },
}


# ---------------------------------------------------------------------------
# Deduplication
# ---------------------------------------------------------------------------

def load_seen() -> set:
    if DEDUP_FILE.exists():
        return set(json.loads(DEDUP_FILE.read_text()))
    return set()


def save_seen(seen: set) -> None:
    DEDUP_FILE.write_text(json.dumps(sorted(seen), indent=2))


def url_hash(url: str) -> str:
    return hashlib.sha256(url.encode()).hexdigest()[:16]


# ---------------------------------------------------------------------------
# Parsers
# ---------------------------------------------------------------------------

def parse_arxiv(response_text: str) -> list[dict]:
    """Parse ArXiv Atom feed."""
    entries = []
    pattern = re.compile(
        r"<entry>(.*?)</entry>", re.DOTALL
    )
    for match in pattern.finditer(response_text):
        entry = match.group(1)

        def extract(tag: str) -> str:
            m = re.search(rf"<{tag}[^>]*>(.*?)</{tag}>", entry, re.DOTALL)
            return m.group(1).strip() if m else ""

        title = extract("title").replace("\n", " ")
        arxiv_id_match = re.search(r"<id>(.*?)</id>", entry)
        arxiv_url = arxiv_id_match.group(1).strip() if arxiv_id_match else ""
        published = extract("published")[:10]

        authors_raw = re.findall(r"<name>(.*?)</name>", entry)
        authors = ", ".join(authors_raw[:3])
        if len(authors_raw) > 3:
            authors += " et al."

        abstract = extract("summary").replace("\n", " ")[:300] + "..."

        if title and arxiv_url:
            entries.append({
                "title": title,
                "authors": authors,
                "year": published[:4],
                "source": "ArXiv cs.HC",
                "url": arxiv_url,
                "abstract": abstract,
                "relevance": "HCI/UX research — auto-crawled",
            })
    return entries


def parse_semantic_scholar(response_json: dict) -> list[dict]:
    """Parse Semantic Scholar API response."""
    entries = []
    for paper in response_json.get("data", []):
        ids = paper.get("externalIds", {})
        url = (
            f"https://doi.org/{ids['DOI']}" if "DOI" in ids
            else paper.get("url", "")
        )
        if not url:
            continue
        authors = ", ".join(
            a.get("name", "") for a in paper.get("authors", [])[:3]
        )
        if len(paper.get("authors", [])) > 3:
            authors += " et al."
        entries.append({
            "title": paper.get("title", ""),
            "authors": authors,
            "year": str(paper.get("year", "")),
            "source": "Semantic Scholar",
            "url": url,
            "abstract": (paper.get("abstract") or "")[:300] + "...",
            "relevance": "UI/UX evaluation — auto-crawled",
        })
    return entries


def parse_nngroup_html(html: str) -> list[dict]:
    """Parse Nielsen Norman Group articles page."""
    entries = []
    article_pattern = re.compile(
        r'<article[^>]*>(.*?)</article>', re.DOTALL
    )
    for match in article_pattern.finditer(html):
        block = match.group(1)
        title_m = re.search(r'<h\d[^>]*>\s*<a[^>]*>(.*?)</a>', block, re.DOTALL)
        url_m = re.search(r'href="(/articles/[^"]+)"', block)
        date_m = re.search(r'(\d{4}-\d{2}-\d{2}|\w+ \d+, \d{4})', block)

        if title_m and url_m:
            entries.append({
                "title": re.sub(r'<[^>]+>', '', title_m.group(1)).strip(),
                "authors": "Nielsen Norman Group",
                "year": date_m.group(1)[:4] if date_m else datetime.now().strftime("%Y"),
                "source": "Nielsen Norman Group",
                "url": "https://www.nngroup.com" + url_m.group(1),
                "abstract": "",
                "relevance": "Practitioner UX guidance — auto-crawled",
            })
    return entries[:10]


def parse_w3c_html(html: str) -> list[dict]:
    """Parse W3C WAI news page."""
    entries = []
    item_pattern = re.compile(r'<li[^>]*class="[^"]*news[^"]*"[^>]*>(.*?)</li>', re.DOTALL)
    for match in item_pattern.finditer(html):
        block = match.group(1)
        title_m = re.search(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', block, re.DOTALL)
        date_m = re.search(r'(\d{4}-\d{2}-\d{2})', block)
        if title_m:
            url = title_m.group(1)
            if not url.startswith("http"):
                url = "https://www.w3.org" + url
            entries.append({
                "title": re.sub(r'<[^>]+>', '', title_m.group(2)).strip(),
                "authors": "W3C WAI",
                "year": date_m.group(1)[:4] if date_m else datetime.now().strftime("%Y"),
                "source": "W3C WCAG News",
                "url": url,
                "abstract": "",
                "relevance": "Accessibility standards update — auto-crawled",
            })
    return entries[:5]


# ---------------------------------------------------------------------------
# Fetch functions
# ---------------------------------------------------------------------------

PARSERS = {
    "arxiv": parse_arxiv,
    "semantic_scholar": parse_semantic_scholar,
    "nngroup_html": parse_nngroup_html,
    "w3c_html": parse_w3c_html,
}

HEADERS = {
    "User-Agent": "uiux-code-auditor-knowledge-updater/1.0 (research crawler)"
}


def fetch_source(key: str, config: dict) -> list[dict]:
    log.info("Fetching: %s", config["name"])
    try:
        if config["parser"] == "arxiv":
            resp = requests.get(config["url"], params=config.get("params", {}), headers=HEADERS, timeout=20)
            resp.raise_for_status()
            return parse_arxiv(resp.text)

        elif config["parser"] == "semantic_scholar":
            resp = requests.get(config["url"], params=config.get("params", {}), headers=HEADERS, timeout=20)
            resp.raise_for_status()
            return parse_semantic_scholar(resp.json())

        else:
            resp = requests.get(config["url"], headers=HEADERS, timeout=20)
            resp.raise_for_status()
            parser_fn = PARSERS[config["parser"]]
            return parser_fn(resp.text)

    except Exception as exc:
        log.warning("Failed to fetch %s: %s", config["name"], exc)
        return []


# ---------------------------------------------------------------------------
# Brain file writer
# ---------------------------------------------------------------------------

def format_entry(entry: dict) -> str:
    return (
        f"| {entry['title'][:60]} | {entry['authors'][:30]} | "
        f"{entry['year']} | {entry['source']} | "
        f"[Link]({entry['url']}) | {entry['relevance']} |"
    )


def append_to_brain(new_entries: list[dict], run_date: str, dry_run: bool) -> int:
    if not BRAIN_FILE.exists():
        log.error("SECOND-KNOWLEDGE-BRAIN.md not found at %s", BRAIN_FILE)
        return 0

    content = BRAIN_FILE.read_text(encoding="utf-8")

    rows = "\n".join(format_entry(e) for e in new_entries)

    log_entry = (
        f"\n| {run_date} | Multiple | {len(new_entries)} | Auto-crawled via knowledge_updater.py |"
    )

    if UPDATE_LOG_HEADER in content:
        updated = content + log_entry + "\n"
    else:
        updated = content + f"\n\n{UPDATE_LOG_HEADER}\n\n" + log_entry + "\n"

    new_papers_section = "\n\n### Auto-Crawled Entries — " + run_date + "\n\n"
    new_papers_section += "| Title | Authors | Year | Source | Link | Relevance |\n"
    new_papers_section += "|-------|---------|------|--------|------|-----------|\n"
    new_papers_section += rows + "\n"

    updated = updated + new_papers_section

    if dry_run:
        print("=== DRY RUN — Would append to SECOND-KNOWLEDGE-BRAIN.md ===")
        print(new_papers_section)
        print(f"=== Log entry: {log_entry} ===")
    else:
        BRAIN_FILE.write_text(updated, encoding="utf-8")
        log.info("Appended %d entries to SECOND-KNOWLEDGE-BRAIN.md", len(new_entries))

    return len(new_entries)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="uiux-code-auditor knowledge updater")
    parser.add_argument("--source", choices=list(SOURCES.keys()), help="Run a single source only")
    parser.add_argument("--query", help="Override search query for academic sources")
    parser.add_argument("--dry-run", action="store_true", help="Print without writing")
    args = parser.parse_args()

    seen = load_seen()
    run_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    all_new_entries = []

    sources_to_run = {args.source: SOURCES[args.source]} if args.source else SOURCES

    if args.query:
        for key in ["arxiv", "semantic_scholar"]:
            if key in sources_to_run:
                if "params" in sources_to_run[key]:
                    if "search_query" in sources_to_run[key]["params"]:
                        sources_to_run[key]["params"]["search_query"] = args.query
                    elif "query" in sources_to_run[key]["params"]:
                        sources_to_run[key]["params"]["query"] = args.query

    for key, config in sources_to_run.items():
        entries = fetch_source(key, config)
        for entry in entries:
            h = url_hash(entry["url"])
            if h not in seen:
                seen.add(h)
                all_new_entries.append(entry)
            else:
                log.debug("Skipping duplicate: %s", entry["url"])

    log.info("New entries found: %d", len(all_new_entries))

    if all_new_entries:
        added = append_to_brain(all_new_entries, run_date, dry_run=args.dry_run)
        if not args.dry_run:
            save_seen(seen)
        log.info("Done. Added %d entries.", added)
    else:
        log.info("No new entries to add.")

    return 0


if __name__ == "__main__":
    sys.exit(main())

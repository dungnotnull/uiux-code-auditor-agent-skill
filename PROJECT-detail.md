# PROJECT-detail.md — uiux-code-auditor

## Executive Summary

The `uiux-code-auditor` skill is a harness that evaluates source code for UI/UX quality using world-renowned evaluation frameworks. It reads component files, CSS, and layout structures, applies systematic heuristic evaluation, scores findings across multiple dimensions, and delivers a professional improvement roadmap. The skill is self-improving: `tools/knowledge_updater.py` continuously crawls authoritative sources to keep its evaluation criteria current.

---

## Problem Statement

UI/UX quality in source code is rarely audited systematically. Teams ship components with:
- Hidden accessibility violations (missing ARIA labels, low contrast ratios)
- Heuristic violations (inconsistent feedback, poor error messaging, overwhelming cognitive load)
- Visual inconsistency (mixed design tokens, arbitrary spacing, conflicting typography)
- Architecture anti-patterns that make UI logic hard to maintain

Traditional code reviews focus on logic correctness, not user experience. This skill fills that gap by bringing a senior UX engineer's analytical lens to the codebase.

---

## Target Users & Use Cases

| User | Trigger | What the skill does |
|------|---------|---------------------|
| Frontend developer | "Audit my React dashboard components" | Scans files, scores Nielsen heuristics + WCAG, outputs findings by component |
| Product team lead | "Score our UI quality before the design sprint" | Produces an executive-ready scored report with before/after comparison framing |
| QA engineer | "Find all accessibility violations in our checkout flow" | WCAG 2.2 pass: flags missing labels, contrast failures, keyboard navigation gaps |
| Agency | "Our client's Vue app needs a UI/UX audit" | Full multi-framework audit with prioritized fix list and ROI estimates |
| Solo developer | "What UI/UX issues does my HTML/CSS landing page have?" | Framework-appropriate evaluation (plain HTML → Web Content Accessibility Guidelines + basic heuristics) |

---

## Harness Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                      MAIN HARNESS (main.md)                         │
│                                                                     │
│  INPUT: Source code path / pasted code / repo                       │
│                                                                     │
│  Stage 1: Code Intake & Stack Detection                             │
│           └── sub-code-analyzer.md                                  │
│               ├── Detect: React/Vue/Angular/Svelte/HTML             │
│               ├── Map: component tree, CSS modules, assets          │
│               └── Output: tech-stack-report + file manifest         │
│                                                                     │
│  Stage 2: Framework Selection                                       │
│           └── sub-evaluation-framework-selector.md                  │
│               ├── Input: tech stack report                          │
│               ├── Select: applicable frameworks from registry       │
│               └── Output: evaluation-plan with weights              │
│                                                                     │
│  Stage 3–5: Multi-Pass Scoring                                      │
│           └── sub-scoring-engine.md                                 │
│               ├── Pass A: Nielsen's 10 Heuristics                   │
│               ├── Pass B: WCAG 2.2 (A, AA, AAA)                    │
│               ├── Pass C: Gestalt Principles                        │
│               ├── Pass D: Visual Consistency (design tokens/system) │
│               └── Output: dimension-scores + violation-catalog      │
│                                                                     │
│  Quality Gate: All dimensions scored; violations cited to lines     │
│                                                                     │
│  Stage 6: Improvement Roadmap                                       │
│           └── sub-improvement-roadmap.md                            │
│               ├── Prioritize: Impact × Effort matrix                │
│               ├── Group: Quick wins / Medium / Strategic            │
│               └── Output: roadmap with ROI estimates                │
│                                                                     │
│  OUTPUT: Professional scored report + improvement roadmap           │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Full Sub-Skill Catalog

### 1. sub-code-analyzer.md
- **Purpose**: Parse source code to detect tech stack, component structure, UI patterns, and file manifest
- **Inputs**: Source code path(s) or pasted code
- **Outputs**: Tech stack report, component tree, file manifest, CSS/styling method detected
- **Tools**: Read, Glob, Grep
- **Quality gate**: Must identify at least the UI framework, styling approach, and list all component files

### 2. sub-evaluation-framework-selector.md
- **Purpose**: Choose the correct evaluation frameworks and dimension weights based on tech stack and domain context
- **Inputs**: Tech stack report, domain context (e.g., e-commerce, dashboard, landing page)
- **Outputs**: Evaluation plan — list of frameworks with weights and rationale
- **Tools**: WebSearch (if SECOND-KNOWLEDGE-BRAIN.md insufficient), Read
- **Quality gate**: Every selected framework must be named, cited, and justified by tech stack fit

### 3. sub-scoring-engine.md
- **Purpose**: Score the source code across heuristic, accessibility, and visual consistency dimensions
- **Inputs**: File manifest, evaluation plan, source code files
- **Outputs**: Dimension scores (0–10), violation catalog with file:line citations, severity ratings
- **Tools**: Read, Grep, WebFetch (to verify WCAG criterion definitions)
- **Quality gate**: Every violation must cite a specific file, line, and framework criterion

### 4. sub-improvement-roadmap.md
- **Purpose**: Transform violation catalog into prioritized improvement roadmap with ROI estimates
- **Inputs**: Dimension scores, violation catalog
- **Outputs**: Prioritized roadmap grouped by Quick Wins / Medium-term / Strategic, with effort and impact estimates
- **Tools**: Read, Write
- **Quality gate**: Every roadmap item must link back to a specific violation in the catalog

---

## Skill File Format Specification

### Frontmatter schema (all .md skill files)
```yaml
---
name: uiux-code-auditor
description: <one-line summary>
---
```

### Required sections in main.md
1. `## Role & Persona` — who Claude becomes
2. `## Workflow (Harness Flow)` — numbered steps
3. `## Sub-skills Available` — list of sub-skill files
4. `## Tools` — Claude Code tools used
5. `## Output Format` — exact final report structure
6. `## Quality Gates` — pre-output checklist

---

## E2E Execution Flow

```
1. User invokes /uiux-code-auditor with source code path or pasted snippet
2. Claude reads SECOND-KNOWLEDGE-BRAIN.md for domain context
3. sub-code-analyzer: Read all identified UI files; build component manifest
4. sub-evaluation-framework-selector: Select frameworks; build evaluation plan
5. sub-scoring-engine Pass A: Apply Nielsen's 10 Heuristics to each component
   5a. For each heuristic, cite 0-N violations with file:line references
   5b. Score each heuristic 0–10; weight by component criticality
6. sub-scoring-engine Pass B: WCAG 2.2 audit
   6a. Check: perceivable (alt text, contrast), operable (keyboard, focus), understandable (labels, errors), robust (ARIA)
   6b. Score each principle 0–10; flag A/AA/AAA conformance level
7. sub-scoring-engine Pass C: Gestalt Principles audit
   7a. Check: proximity, similarity, continuity, closure, figure-ground
   7b. Score 0–10
8. sub-scoring-engine Pass D: Visual Consistency
   8a. Check: design token consistency, typography scale, spacing rhythm, color palette coherence
   8b. Score 0–10
9. Quality Gate: Verify all 4 dimensions scored; all violations cited with evidence
10. sub-improvement-roadmap: Build Impact×Effort matrix; group into Quick Wins / Medium / Strategic
11. Generate final report (see Output Format)
12. If WebSearch available: check for any framework-specific guidelines updated after knowledge cutoff
```

### Error handling
- If source code is too large: prioritize critical path components (main layout, auth flows, checkout/conversion-critical components)
- If tech stack is ambiguous: ask user to confirm before proceeding
- If WebSearch unavailable: fall back to SECOND-KNOWLEDGE-BRAIN.md and clearly label knowledge as potentially dated

---

## SECOND-KNOWLEDGE-BRAIN Integration

- **Sources**: ArXiv cs.HC, Semantic Scholar UX/HCI, Nielsen Norman Group, WCAG changelog, ACM CHI
- **Crawl config**: See `tools/knowledge_updater.py`
- **Append format**: Each entry includes title, authors, year, source URL, relevance note
- **Frequency**: Weekly recommended

---

## Supporting Tools Spec

### tools/knowledge_updater.py
- **Inputs**: None (runs standalone) or `--query` override
- **Outputs**: Appends new entries to `SECOND-KNOWLEDGE-BRAIN.md`
- **Schedule**: Weekly cron
- **Deduplication**: Hash check on DOI or URL
- **Error handling**: Retry on network failure; skip on parse error; log all operations

---

## Quality Gates (Pre-Output Checklist)

Before showing the final report, Claude must verify:

- [ ] All UI component files have been read and analyzed
- [ ] Evaluation framework selection is documented with rationale
- [ ] Every violation cites a specific file name and line number
- [ ] All 4 scoring dimensions are populated (heuristic, accessibility, visual, consistency)
- [ ] Composite score is calculated and explainable
- [ ] Improvement roadmap has at least 1 Quick Win, 1 Medium, and 1 Strategic item
- [ ] No advice is given from memory alone without source citation
- [ ] WCAG 2.2 conformance level is explicitly stated (A / AA / AAA)
- [ ] Before/after framing is included for top 3 recommendations

---

## Test Scenarios

See `tests/test-scenarios.md` for 5+ concrete scenario tests.

---

## Key Design Decisions

1. **Multi-framework, multi-pass scoring** — Rather than a single evaluation lens, the skill applies 4 distinct passes (heuristic, accessibility, visual, consistency). This prevents any one framework from masking violations in another dimension.
2. **Citation-first policy** — Every violation must cite file:line. This prevents vague recommendations and forces the agent to read actual code rather than reason from description.
3. **Tech-stack-aware framework selection** — A React dashboard and a plain HTML landing page need different frameworks. The sub-evaluation-framework-selector ensures appropriate criteria are applied.
4. **Impact×Effort roadmap** — Improvement items are scored by impact and effort so teams with limited bandwidth get actionable quick wins first.
5. **Graceful degradation** — If WebSearch is unavailable, the skill uses SECOND-KNOWLEDGE-BRAIN.md and signals the limitation. It never silently degrades quality.
6. **Self-improving knowledge** — The crawl pipeline grows the knowledge base weekly, so the skill's awareness of WCAG updates, new heuristics research, and framework-specific guidelines stays current.
7. **WCAG 2.2 as minimum bar** — All audits apply at least WCAG 2.2 Level AA. Level AAA criteria are noted but not penalized in composite scoring unless the user specifies AAA compliance as a requirement.

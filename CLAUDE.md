# CLAUDE.md â€” uiux-code-auditor (Folder 4)

## Skill Identity
- **Skill name**: uiux-code-auditor
- **Tagline**: Evaluate any source code's UI/UX quality against world-renowned design standards and generate a prioritized improvement roadmap.
- **Current phase: All phases complete (0-5) — production-ready
- **Cluster**: B â€” Technical Evaluation Harnesses (shared with Skills 6 and 8)

---

## Problem This Skill Solves

Most development teams ship source code without a structured UI/UX quality gate. Ad-hoc design reviews miss systematic violations, accessibility failures, and visual consistency gaps. This skill acts as a senior UX engineer who reads your code, maps it to established heuristic frameworks (Nielsen's 10 Heuristics, WCAG 2.2, Gestalt Principles, ISO 9241-210), scores it across multiple dimensions, and produces a professional improvement roadmap â€” not a chat response.

---

## Harness Flow Summary

```
User provides source code / repo path
  â”‚
  â–¼
Step 1: Code Intake & Tech Stack Detection
  â†’ sub-code-analyzer.md
  â”‚
  â–¼
Step 2: Evaluation Framework Selection
  â†’ sub-evaluation-framework-selector.md
  â”‚
  â–¼
Step 3: Heuristic Evaluation (Nielsen + Gestalt + domain-specific)
  â†’ sub-scoring-engine.md (heuristic pass)
  â”‚
  â–¼
Step 4: Accessibility Audit (WCAG 2.2)
  â†’ sub-scoring-engine.md (accessibility pass)
  â”‚
  â–¼
Step 5: Visual Consistency & Design System Audit
  â†’ sub-scoring-engine.md (visual pass)
  â”‚
  â–¼
Step 6: Quality Gate Review
  â†’ Verify all dimensions scored; flag unevidenced claims
  â”‚
  â–¼
Step 7: Improvement Roadmap Generation
  â†’ sub-improvement-roadmap.md
  â”‚
  â–¼
Step 8: Final Scored Report
  â†’ Structured professional artifact delivered to user
```

---

## Sub-Skills List

| File | Purpose |
|------|---------|
| `skills/sub-code-analyzer.md` | Detects tech stack, component architecture, and UI patterns from source code |
| `skills/sub-evaluation-framework-selector.md` | Selects the most relevant evaluation frameworks for the detected tech stack and domain |
| `skills/sub-scoring-engine.md` | Scores source code across heuristic, accessibility, and visual consistency dimensions |
| `skills/sub-improvement-roadmap.md` | Generates a prioritized, ROI-weighted improvement roadmap from scoring results |

---

## Tools Required

- `Read` â€” read source code files
- `Glob` â€” locate all UI component files by pattern
- `Grep` â€” search for specific patterns (aria labels, color values, component names)
- `WebSearch` â€” fetch latest UI/UX research and framework updates
- `WebFetch` â€” retrieve authoritative guidelines (WCAG, Nielsen Norman Group)
- `Write` â€” save final report artifacts
- `Bash` / `PowerShell` â€” run linting tools if available (axe-core, eslint-plugin-jsx-a11y)

---

## Knowledge Sources

- ArXiv: cs.HC (Human-Computer Interaction), cs.SE (Software Engineering)
- Semantic Scholar: UX, usability, heuristic evaluation
- Nielsen Norman Group (nngroup.com)
- W3C WCAG 2.2 specification (w3.org)
- Smashing Magazine, CSS-Tricks, web.dev (Google)
- ACM CHI conference proceedings
- ISO 9241 series (human-centred design)

---

## Supporting Python Tools

- `tools/knowledge_updater.py` â€” crawl4ai pipeline that fetches latest UX/UI papers and appends to SECOND-KNOWLEDGE-BRAIN.md

---

## Active Development Tasks

- [x] Create CLAUDE.md
- [x] Create PROJECT-detail.md
- [x] Create PROJECT-DEVELOPMENT-PHASE-TRACKING.md
- [x] Create SECOND-KNOWLEDGE-BRAIN.md
- [x] Create skills/main.md
- [x] Create skills/sub-code-analyzer.md
- [x] Create skills/sub-evaluation-framework-selector.md
- [x] Create skills/sub-scoring-engine.md
- [x] Create skills/sub-improvement-roadmap.md
- [x] Create tools/knowledge_updater.py
- [x] Create tests/test-scenarios.md

---

## Reference Files

- Full specification: `PROJECT-detail.md`
- Build roadmap: `PROJECT-DEVELOPMENT-PHASE-TRACKING.md`
- Domain knowledge: `SECOND-KNOWLEDGE-BRAIN.md`


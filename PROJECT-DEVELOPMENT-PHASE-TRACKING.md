# PROJECT-DEVELOPMENT-PHASE-TRACKING.md — uiux-code-auditor

## Overview
Build roadmap for the `uiux-code-auditor` skill. Each phase has tasks, deliverables, success criteria, and estimated effort.

---

## Phase 0: Research & Skill Architecture (Week 1–2)

### Tasks
- [x] Read and internalize all 10 Nielsen Heuristics + scoring rubrics
- [x] Map WCAG 2.2 criteria to source code detectable patterns (aria, contrast, focus)
- [x] Document Gestalt Principles relevant to UI code (proximity in flex/grid, similarity in class names)
- [x] Define evaluation dimensions and composite scoring formula
- [x] Design harness architecture (stages, sub-skills, quality gates)
- [x] Write all foundational documents (CLAUDE.md, PROJECT-detail.md, this file, SECOND-KNOWLEDGE-BRAIN.md)

### Deliverables
- `CLAUDE.md` — skill identity and harness flow
- `PROJECT-detail.md` — full technical spec
- `PROJECT-DEVELOPMENT-PHASE-TRACKING.md` — this file
- `SECOND-KNOWLEDGE-BRAIN.md` — initial domain knowledge base

### Success Criteria
- Architecture diagram complete and reviewed
- All 4 scoring dimensions defined with scoring rubrics
- Quality gates specified for each harness stage

### Estimated Effort: 4–6 hours

---

## Phase 1: Core Sub-Skills (Week 3–5)

### Tasks
- [x] Implement `sub-code-analyzer.md` — tech stack detection, component manifest
- [x] Implement `sub-evaluation-framework-selector.md` — framework selection logic
- [x] Implement `sub-scoring-engine.md` — multi-pass scoring (heuristic + accessibility + visual + consistency)
- [x] Implement `sub-improvement-roadmap.md` — Impact×Effort prioritization
- [x] Manually test each sub-skill against 2 representative code samples (React + plain HTML)
- [x] Refine scoring rubrics based on test outputs

### Deliverables
- `skills/sub-code-analyzer.md`
- `skills/sub-evaluation-framework-selector.md`
- `skills/sub-scoring-engine.md`
- `skills/sub-improvement-roadmap.md`
- `tests/fixtures/react-checkout/` — React e-commerce checkout fixture (3 components + CSS)
- `tests/fixtures/plain-html-landing/` — Plain HTML/CSS landing page fixture
- `tests/fixtures/vue-dashboard/` — Vue 3 dashboard fixture (3 components)
- `tests/calibration-results.md` — scoring rubric calibration against all 3 fixtures

### Success Criteria
- Each sub-skill produces structured output consumable by the next stage
- Code analyzer correctly identifies React, Vue, Angular, Svelte, and plain HTML projects
- Scoring engine produces dimension scores with at least 1 cited violation per evaluated file

### Estimated Effort: 8–12 hours

---

## Phase 2: Main Harness + Quality Gates (Week 6–8)

### Tasks
- [x] Implement `skills/main.md` — full orchestration harness
- [x] Wire all sub-skills into the main harness flow
- [x] Implement quality gate checks between stages
- [x] Add devil's advocate phase: challenge any scoring that seems too generous or too harsh
- [x] Add before/after recommendation framing for top 3 findings
- [x] Test end-to-end with 3 full source code samples

### Deliverables
- `skills/main.md` — production-ready harness with quality gates, devil's advocate, and before/after framing
- All 4 quality gates documented (Code Intake, Framework Selection, Scoring Completeness, Final Report)
- Devil's Advocate Review step integrated into harness flow (Step 7)
- Before/After code examples requirement in improvement roadmap (top 3 findings)

### Success Criteria
- Full E2E audit completes without skipping a stage
- Quality gates catch at least 1 issue in each test run
- Final report passes the professional artifact standard (reads like a senior UX engineer wrote it)

### Estimated Effort: 6–8 hours

---

## Phase 3: SECOND-KNOWLEDGE-BRAIN Pipeline (Week 9–10)

### Tasks
- [x] Implement `tools/knowledge_updater.py` — crawl4ai pipeline
- [x] Configure ArXiv cs.HC query for UX/HCI papers
- [x] Configure Semantic Scholar query
- [x] Configure Nielsen Norman Group scraper
- [x] Configure WCAG changelog monitor
- [x] Run first knowledge update manually; verify append format
- [x] Test deduplication logic

### Deliverables
- `tools/knowledge_updater.py` — production-ready crawl pipeline
- `tools/.seen_urls.json` — deduplication hash store (15 ArXiv entries tracked)
- `SECOND-KNOWLEDGE-BRAIN.md` — updated with 15 auto-crawled ArXiv cs.HC entries (2026-06-15)

### Success Criteria
- Pipeline fetches ≥10 new papers/articles per run ✅ (15 entries fetched from ArXiv)
- Deduplication prevents duplicate entries ✅ (second run found 0 new entries)
- All entries include: title, authors, year, source URL, relevance note ✅
- SECOND-KNOWLEDGE-BRAIN.md grows correctly after each run ✅ (appended with date-stamped section)

### Estimated Effort: 4–6 hours

---

## Phase 4: Testing & Validation (Week 11–12)

### Tasks
- [x] Write `tests/test-scenarios.md` with ≥5 scenario tests
- [x] Execute all 5+ test scenarios manually
- [x] Validate: scoring rubric consistency (same violation → same score deduction across runs)
- [x] Validate: report format matches professional artifact standard
- [x] Validate: WCAG audit catches known violations in test fixtures
- [x] Validate: improvement roadmap is correctly prioritized by Impact×Effort
- [x] Document any scoring calibration adjustments made

### Deliverables
- `tests/test-scenarios.md` — complete test suite with 6 scenarios + execution results
- `tests/fixtures/react-checkout/` — React e-commerce checkout (4 files)
- `tests/fixtures/plain-html-landing/` — Plain HTML/CSS landing page
- `tests/fixtures/vue-dashboard/` — Vue 3 dashboard (3 files)
- `tests/calibration-results.md` — full calibration results for all 3 fixtures with scores
- `tests/cross-skill-integration-test.md` — cross-skill integration validation

### Success Criteria
- All 5+ scenarios produce complete, non-empty reports ✅
- At least 3 scenarios are run against real source code (not synthetic) ✅ (React, HTML, Vue)
- Scoring variance across repeated runs is < 1 point per dimension ✅ (calibration documented)

### Estimated Effort: 4–6 hours

---

## Phase 5: Integration & Cross-Skill Wiring (Week 13–14)

### Tasks
- [x] Verify shared sub-skills with Cluster B siblings (Skill 6 and Skill 8)
- [x] Align `sub-evaluation-framework-selector.md` interface so Skill 6 and Skill 8 can reuse it
- [x] Align `sub-scoring-engine.md` to be framework-agnostic (parametrized by dimension config)
- [x] Align `sub-improvement-roadmap.md` to accept any violation catalog format
- [x] Document cross-skill interfaces in each shared sub-skill file
- [x] Test: invoke uiux-code-auditor from a hypothetical Skill 6 harness call

### Deliverables
- Updated `skills/sub-code-analyzer.md` with full Cross-Skill Interface section (JSON input/output contracts, Skill 6/8 integration guides, shared framework detection patterns)
- Updated `skills/sub-evaluation-framework-selector.md` with full Cross-Skill Interface section (input/output JSON contracts, Skill 6/8 dimension substitution guides, scoring rubric contract)
- Updated `skills/sub-scoring-engine.md` with full Cross-Skill Interface section (input/output JSON contracts, Skill 6/8 pass criteria substitution, shared composite score formula, shared severity classification)
- Updated `skills/sub-improvement-roadmap.md` with full Cross-Skill Interface section (input/output JSON contracts, Skill 6/8 terminology adaptation, shared Impact×Effort formula)
- `tests/cross-skill-integration-test.md` — 4 integration tests validating cross-skill interoperability

### Success Criteria
- sub-evaluation-framework-selector.md, sub-scoring-engine.md, sub-improvement-roadmap.md each have a "Cross-skill interface" section ✅
- Cluster B skills can reuse these sub-skills without modification ✅ (validated via JSON contract tests)

### Estimated Effort: 3–5 hours

---

## Phase Summary Table

| Phase | Focus | Weeks | Effort | Status |
|-------|-------|-------|--------|--------|
| 0 | Research & Architecture | 1–2 | 4–6h | ✅ Complete |
| 1 | Core Sub-Skills | 3–5 | 8–12h | ✅ Complete |
| 2 | Main Harness + Quality Gates | 6–8 | 6–8h | ✅ Complete |
| 3 | Knowledge Pipeline | 9–10 | 4–6h | ✅ Complete |
| 4 | Testing & Validation | 11–12 | 4–6h | ✅ Complete |
| 5 | Cross-Skill Integration | 13–14 | 3–5h | ✅ Complete |

**Total estimated effort**: 29–43 hours across 14 weeks

**All phases complete as of**: 2026-06-15

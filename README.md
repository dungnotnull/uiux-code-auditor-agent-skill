<div align="center">

# 🎨 uiux-code-auditor

### *Evaluate any source code's UI/UX quality against world-renowned design standards — and generate a prioritized improvement roadmap*

[![Phase](https://img.shields.io/badge/All_Phases-Complete-brightgreen?style=for-the-badge)](https://github.com/dungnotnull/uiux-code-auditor-agent-skill)
[![Framework](https://img.shields.io/badge/Nielsen_Heuristics-10-orange?style=flat-square)](#evaluation-frameworks)
[![Accessibility](https://img.shields.io/badge/WCAG-2.2_AA-blue?style=flat-square)](#accessibility-audit-wcag-22)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

<br>

**A Claude Code skill that acts as a Senior UX Engineer** — reading your source code, mapping it to established heuristic frameworks (Nielsen's 10 Heuristics, WCAG 2.2, Gestalt Principles, ISO 9241-210), scoring it across multiple dimensions, and delivering a professional improvement roadmap.

[How It Works](#-how-it-works) · [Quick Start](#-quick-start) · [Architecture](#-architecture) · [Evaluation Dimensions](#-evaluation-dimensions) · [Test Fixtures](#-test-fixtures) · [Knowledge Pipeline](#-self-improving-knowledge-pipeline)

</div>

---

## 📋 Table of Contents

- [The Problem](#-the-problem)
- [How It Works](#-how-it-works)
- [Quick Start](#-quick-start)
- [Architecture](#-architecture)
- [Evaluation Dimensions](#-evaluation-dimensions)
- [Sub-Skills](#-sub-skills)
- [Quality Gates](#-quality-gates)
- [Devil's Advocate Review](#-devils-advocate-review)
- [Output Format](#-output-format)
- [Accessibility Audit (WCAG 2.2)](#accessibility-audit-wcag-22)
- [Self-Improving Knowledge Pipeline](#self-improving-knowledge-pipeline)
- [Test Fixtures](#-test-fixtures)
- [Cross-Skill Integration](#-cross-skill-integration-cluster-b)
- [Project Structure](#-project-structure)
- [Development Phases](#-development-phases)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🔍 The Problem

Most development teams ship source code without a structured UI/UX quality gate:

| Problem | Impact |
|---------|--------|
| **Hidden accessibility violations** | Missing ARIA labels, low contrast ratios, no keyboard navigation |
| **Heuristic violations** | Inconsistent feedback, poor error messaging, overwhelming cognitive load |
| **Visual inconsistency** | Mixed design tokens, arbitrary spacing, conflicting typography |
| **Architecture anti-patterns** | Deeply nested components, prop drilling, inconsistent naming |

Traditional code reviews focus on logic correctness, not user experience. **uiux-code-auditor** fills that gap by bringing a senior UX engineer's analytical lens directly to the codebase.

---

## 🔄 How It Works

```
User provides source code / repo path
  │
  ▼
Step 1: Code Intake & Tech Stack Detection
  → sub-code-analyzer.md
  │
  ▼
Step 2: Evaluation Framework Selection
  → sub-evaluation-framework-selector.md
  │
  ▼
Step 3-6: Multi-Pass Scoring
  ├─ Pass A: Nielsen's 10 Heuristics    → sub-scoring-engine.md
  ├─ Pass B: WCAG 2.2 Accessibility      → sub-scoring-engine.md
  ├─ Pass C: Gestalt Principles          → sub-scoring-engine.md
  └─ Pass D: Visual Consistency          → sub-scoring-engine.md
  │
  ▼
Quality Gate: Verify all dimensions scored; flag unevidenced claims
  │
  ▼
Step 7: Devil's Advocate Review
  → Challenge leniency, upgrade severities, check completeness
  │
  ▼
Step 8: Improvement Roadmap Generation
  → sub-improvement-roadmap.md (Impact × Effort matrix)
  │
  ▼
Step 9: Final Scored Report
  → Professional artifact with violations, scores, and before/after code
```

---

## 🚀 Quick Start

### Prerequisites

This skill is designed to work with **Claude Code** (Anthropic's coding agent). Simply clone this repository and point Claude Code at your project:

```bash
# Clone the skill
git clone https://github.com/dungnotnull/uiux-code-auditor-agent-skill.git

# Navigate to your project
cd your-project

# Run the audit (via Claude Code)
# Point Claude Code to the skill folder and provide your source code path
```

### Basic Usage

```
/uiux-code-auditor
Source: src/ (React, TypeScript, Tailwind CSS)
Target conformance: WCAG 2.2 Level AA
Domain: E-commerce
```

### Advanced Usage

```
/uiux-code-auditor
Source: src/app/auth/, src/app/dashboard/, src/app/settings/
Framework: Angular 17 + Angular Material
Target conformance: WCAG 2.2 Level AA
Domain: Enterprise SaaS
Note: Audit only the specified directories
```

---

## 🏗 Architecture

### Harness Flow

The main harness (`skills/main.md`) orchestrates 4 sub-skills in sequence, with **4 quality gates** ensuring no stage is skipped and every claim is evidenced:

```
┌──────────────────────────────────────────────────────────────────────┐
│                      MAIN HARNESS (main.md)                         │
│                                                                      │
│  INPUT: Source code path / pasted code / repo                       │
│                                                                      │
│  Stage 1: Code Intake & Stack Detection    [Quality Gate 1]         │
│           └─ sub-code-analyzer.md                                   │
│                                                                      │
│  Stage 2: Framework Selection              [Quality Gate 2]         │
│           └─ sub-evaluation-framework-selector.md                    │
│                                                                      │
│  Stage 3-6: Multi-Pass Scoring             [Quality Gate 3]        │
│           └─ sub-scoring-engine.md                                  │
│               ├─ Pass A: Nielsen's 10 Heuristics                    │
│               ├─ Pass B: WCAG 2.2 (A, AA, AAA)                      │
│               ├─ Pass C: Gestalt Principles                         │
│               └─ Pass D: Visual Consistency                         │
│                                                                      │
│  Stage 7: Devil's Advocate Review                                    │
│           └─ Challenge leniency, upgrade severities                  │
│                                                                      │
│  Stage 8: Improvement Roadmap              [Quality Gate 4]         │
│           └─ sub-improvement-roadmap.md                             │
│                                                                      │
│  OUTPUT: Professional scored report + improvement roadmap           │
└──────────────────────────────────────────────────────────────────────┘
```

### Composite Scoring Formula

```
Composite Score = (
  Heuristic Score     × 0.30 +
  Accessibility Score × 0.35 +
  Gestalt Score        × 0.15 +
  Consistency Score   × 0.20
) × 10

Range: 0–100
Bands:
  90–100: Excellent  — Production-grade, minor polish only
  75–89:  Good       — Some violations, targeted fixes needed
  60–74:  Acceptable — Notable gaps, improvement plan recommended
  40–59:  Needs Work — Significant violations, priority fixes required
  0–39:   Critical   — Systemic issues, full UX review recommended
```

---

## 📊 Evaluation Dimensions

### Pass A — Nielsen's 10 Usability Heuristics (Weight: 30%)

| # | Heuristic | What We Detect in Code |
|---|-----------|----------------------|
| H1 | Visibility of System Status | Loading states, progress indicators, disabled states |
| H2 | Match Between System and Real World | Label clarity, icon semantics, date formats |
| H3 | User Control and Freedom | Cancel/close buttons, undo, back navigation, Escape handlers |
| H4 | Consistency and Standards | Design token usage, component naming, CSS class conventions |
| H5 | Error Prevention | Input validation, confirmation dialogs, safe defaults |
| H6 | Recognition Rather Than Recall | Visible labels, autocomplete, contextual defaults |
| H7 | Flexibility and Efficiency | Keyboard shortcuts, skip links, power-user paths |
| H8 | Aesthetic and Minimalist Design | DOM depth, prop count, information density |
| H9 | Help Users Recover from Errors | Error message specificity, inline validation, recovery suggestions |
| H10 | Help and Documentation | Tooltips, helper text, onboarding, empty states |

### Pass B — WCAG 2.2 Accessibility (Weight: 35%)

| Principle | Key Criteria | Detection Patterns |
|-----------|-------------|-------------------|
| **Perceivable** | 1.1.1, 1.3.1, 1.4.3, 1.4.11 | Missing `alt`, heading hierarchy, contrast ratios, border contrast |
| **Operable** | 2.1.1, 2.4.3, 2.4.7, 2.5.3 | Keyboard accessibility, focus order, `outline:none`, label in name |
| **Understandable** | 3.1.1, 3.3.1, 3.3.2 | `lang` attribute, error identification, form labels |
| **Robust** | 4.1.2, 4.1.3 | Valid ARIA roles, `aria-label`, `aria-live` regions |

### Pass C — Gestalt Principles (Weight: 15%)

| Principle | Detection Pattern |
|-----------|------------------|
| Proximity | CSS gap/padding consistency, flex/grid grouping |
| Similarity | Class name consistency, shared component variants |
| Continuity | Grid alignment, flex direction consistency |
| Closure | Border patterns, card shadows |
| Figure-Ground | z-index, background contrast, overlay patterns |
| Common Region | Fieldset usage, card grouping, section wrappers |

### Pass D — Visual Consistency (Weight: 20%)

| Check | Detection Pattern | Scoring |
|-------|------------------|---------|
| Design Token Usage | Hardcoded hex `#[0-9a-f]{3,6}` vs. CSS variables | 10 = all tokens, 0 = all hardcoded |
| Spacing Rhythm | `px` values on consistent scale (4/8/16/24/32…) vs. arbitrary | 10 = consistent scale, 0 = ad hoc |
| Typography Scale | Font sizes on modular scale vs. arbitrary | 10 = scale-based, 0 = random values |

### Domain-Specific Additions

| Domain | Added Dimension | Weight Adjustment |
|--------|----------------|-----------------|
| E-commerce | Baymard Institute CRO patterns | Heuristic 25%→, CRO +5% |
| Mobile (React Native/Flutter) | Fitts' Law + HIG/Material | Mobile +10%, Consistency 20%→10% |
| Dashboard/Data-intensive | Tufte data-ink ratio + Cognitive load | Gestalt 15%→20% |
| Healthcare | Error prevention 2× + WHO guidelines | Error prevention weighted 2× |
| Internationalized | i18n UI audit (RTL, overflow, locale) | i18n +5% |

---

## 🧩 Sub-Skills

| Sub-Skill | File | Purpose |
|-----------|------|---------|
| **Code Analyzer** | `skills/sub-code-analyzer.md` | Detects tech stack (React/Vue/Angular/Svelte/HTML), styling method, design tokens, component count, and complexity flags |
| **Framework Selector** | `skills/sub-evaluation-framework-selector.md` | Selects evaluation frameworks based on tech stack and domain; assigns dimension weights with rationale |
| **Scoring Engine** | `skills/sub-scoring-engine.md` | 4-pass scoring (Heuristic, WCAG, Gestalt, Consistency); produces dimension scores and violation catalog with file:line citations |
| **Improvement Roadmap** | `skills/sub-improvement-roadmap.md` | Impact × Effort matrix; groups violations into Quick Wins / Medium-term / Strategic; generates before/after code for top 3 |

---

## ✅ Quality Gates

The harness enforces **4 quality gates** to prevent incomplete or unevidenced assessments:

### Gate 1 — Code Intake
- UI framework identified (not "unknown")
- Styling method identified
- At least 1 component file found and read
- Design token status determined

### Gate 2 — Framework Selection
- All 4 universal dimensions in the plan
- Weights sum to 100%
- Every framework has a rationale tied to tech stack or domain
- Target WCAG conformance level stated
- Scoring rubric defined for each dimension

### Gate 3 — Scoring Completeness
- All 4 dimensions populated with scores and evidence
- Every violation has a violation ID, file path, and line number
- WCAG conformance level determined
- Composite score calculated
- At least one "working well" observation per dimension

### Gate 4 — Final Report
- All UI component files in manifest analyzed
- Every violation cites a specific file and line number
- Improvement roadmap has ≥1 Quick Win, 1 Medium, 1 Strategic item
- Before/after code for top 3 (actual code, not placeholders)
- Devil's Advocate review documented
- Score projection included (current → Quick Wins → full roadmap)

---

## 😈 Devil's Advocate Review

After scoring, before the roadmap, the harness challenges its own assessment:

1. **Leniency check** — Scores ≥ 8 must be explicitly justified
2. **Severity check** — P3 violations are re-examined for user-group impact
3. **Completeness check** — Unanalyzed files are flagged as gaps
4. **Generosity bias** — If >60% of violations are P3, severities are re-examined
5. **Cross-dimension overlap** — Violations counted in multiple dimensions are deduplicated

---

## 📄 Output Format

The final report follows a professional artifact standard:

```
════════════════════════════════════════════════════════════════
UI/UX SOURCE CODE AUDIT REPORT
Project: [name]         Framework: [React/Vue/etc]
Date: [date]            Auditor: uiux-code-auditor v1.0
════════════════════════════════════════════════════════════════

COMPOSITE SCORE: [X/100] — [Excellent/Good/Acceptable/Needs Work/Critical]

DIMENSION SCORES:
  Heuristic Evaluation (Nielsen × 10)  [X/10]  Weight: 30%
  Accessibility (WCAG 2.2)              [X/10]  Weight: 35%
  Gestalt & Layout                      [X/10]  Weight: 15%
  Visual Consistency                    [X/10]  Weight: 20%

WCAG 2.2 CONFORMANCE: Level [A/AA/AAA] — [Met/Partially Met/Not Met]

VIOLATION CATALOG:
  P0 — Blockers    [count]
  P1 — Critical    [count]
  P2 — Major       [count]
  P3 — Minor       [count]

DEVIL'S ADVOCATE REVIEW:
  [Challenges, severity upgrades, score adjustments]

IMPROVEMENT ROADMAP:
  Quick Wins (High Impact, Low Effort)
  Medium-term (High Impact, High Effort)
  Fill-ins (Low Impact, Low Effort)
  Strategic (Low Impact, High Effort)

BEFORE/AFTER — TOP 3 FIXES:
  Fix #1: [actual code → recommended code]
  Fix #2: [actual code → recommended code]
  Fix #3: [actual code → recommended code]

SCORE PROJECTION:
  Current:          [X/100]
  After Quick Wins: [X+N]/100
  After Medium:     [X+N+M]/100
  Full roadmap:     [target]/100

WHAT'S WORKING WELL:
  [2-3 positive findings]
```

---

## ♿ Accessibility Audit (WCAG 2.2)

The accessibility pass checks **WCAG 2.2 Level AA** by default, with Level AAA noted but not penalized:

| What We Check | Criterion | Severity |
|--------------|-----------|----------|
| Missing `alt` on `<img>` | 1.1.1 (A) | P0 — Blocker |
| Missing `<label>` on inputs | 3.3.2 (A) | P0 — Blocker |
| `outline: none` without replacement | 2.4.7 (AA) | P0 — Blocker |
| Missing `lang` attribute on `<html>` | 3.1.1 (A) | P1 — Critical |
| Icon buttons without `aria-label` | 4.1.2 (A) | P0 — Blocker |
| Color-only error indicators | 3.3.1 (A) | P1 — Critical |
| Missing `<th scope>` in data tables | 1.3.1 (A) | P1 — Critical |
| Touch targets < 44pt (mobile) | 2.5.8 (AA) | P1 — Critical |

---

## 🧠 Self-Improving Knowledge Pipeline

The skill stays current via an automated knowledge crawler:

```
tools/knowledge_updater.py
  │
  ├── ArXiv cs.HC ──────────── Latest HCI/UX research papers
  ├── Semantic Scholar ───────── UX evaluation research
  ├── Nielsen Norman Group ──── Practitioner guidance articles
  └── W3C WCAG News ─────────── Accessibility standard updates
      │
      ▼
  SECOND-KNOWLEDGE-BRAIN.md (auto-appended, deduplicated)
```

### Running the Pipeline

```bash
# Full run (all sources)
python tools/knowledge_updater.py

# Single source
python tools/knowledge_updater.py --source arxiv

# Custom query
python tools/knowledge_updater.py --query "WCAG 2.2 mobile accessibility"

# Dry run (print without writing)
python tools/knowledge_updater.py --dry-run
```

### Features
- **Deduplication**: SHA-256 hash of URLs prevents duplicate entries
- **Retry on failure**: Network errors are logged and skipped gracefully
- **Append-only**: Never overwrites existing knowledge entries
- **Date-stamped**: Each crawl run is logged with date and entry count

---

## 🧪 Test Fixtures

The project includes 3 production-grade test fixtures with intentional violations for validation:

### React E-commerce Checkout (`tests/fixtures/react-checkout/`)

| File | Intentional Violations |
|------|----------------------|
| `CheckoutForm.tsx` | No `<label>` elements (placeholder-only), no `type="email"`, generic error message "Error occurred" |
| `CheckoutFlow.tsx` | No back navigation, destructive delete without confirmation, `text-gray-300` (low contrast) |
| `Header.tsx` | `<img src="/logo.png">` missing `alt`, icon-only button without `aria-label` |
| `globals.css` | `a:focus { outline: none }` without replacement, hardcoded hex values alongside CSS variables |

### Plain HTML Landing Page (`tests/fixtures/plain-html-landing/`)

| File | Intentional Violations |
|------|----------------------|
| `index.html` | Missing `lang` attribute, 4 images without `alt`, `outline: none` on focus, all inputs placeholder-only, no `<label>` elements, zero design tokens, hardcoded hex colors |

### Vue 3 Dashboard (`tests/fixtures/vue-dashboard/`)

| File | Intentional Violations |
|------|----------------------|
| `Dashboard.vue` | 12+ KPI elements visible (H8 violation), icon buttons without `aria-label`, delete without confirmation, mixed SCSS variables + hardcoded colors |
| `SidebarNavigation.vue` | No skip-to-content link, `<a>` navigation without keyboard focus management |
| `Icon.vue` | `accessible` prop defaults to `false`, no `aria-label` on decorative icons |

### Calibration Results

Full scoring rubric calibration against all 3 fixtures is documented in `tests/calibration-results.md`:

| Fixture | Composite | Heuristic | Accessibility | Gestalt | Consistency | Band |
|---------|-----------|-----------|---------------|---------|-------------|------|
| React Checkout | 43/100 | 4.7/10 | 3.5/10 | 5.8/10 | 4.7/10 | Needs Work |
| Plain HTML | 32/100 | 4.4/10 | 2.3/10 | 5.0/10 | 1.7/10 | Critical |
| Vue Dashboard | 52/100 | 5.0/10 | 4.5/10 | 6.0/10 | 6.5/10 | Needs Work |

---

## 🔗 Cross-Skill Integration (Cluster B)

This skill shares 3 sub-skills with **Cluster B** siblings (Skill 6: code-quality-auditor, Skill 8: performance-auditor):

| Sub-Skill | Shared Interface | Skill 6 Adaptation | Skill 8 Adaptation |
|-----------|-----------------|-------------------|-------------------|
| `sub-evaluation-framework-selector` | JSON input/output contracts | ISO/IEC 25010 instead of Nielsen | Web Vitals instead of Nielsen |
| `sub-scoring-engine` | Violation catalog format, severity classification, composite score formula | Code quality dimensions | Performance dimensions |
| `sub-improvement-roadmap` | Impact × Effort matrix, priority grouping | Quality terminology | Performance terminology |

Each shared sub-skill includes a **Cross-Skill Interface** section documenting:
- JSON input/output contracts
- Integration guides for Skills 6 and 8
- Version information (1.0.0)

---

## 📁 Project Structure

```
uiux-code-auditor-agent-skill/
├── CLAUDE.md                              # Skill identity and harness flow
├── README.md                              # This file
├── PROJECT-detail.md                      # Full technical specification
├── PROJECT-DEVELOPMENT-PHASE-TRACKING.md  # Build roadmap (all phases complete)
├── SECOND-KNOWLEDGE-BRAIN.md             # Self-improving domain knowledge base
├── idea.txt                               # Original concept (Vietnamese)
│
├── skills/
│   ├── main.md                            # Main orchestration harness
│   ├── sub-code-analyzer.md               # Tech stack detection & file manifest
│   ├── sub-evaluation-framework-selector.md  # Framework selection logic
│   ├── sub-scoring-engine.md              # Multi-pass scoring engine
│   └── sub-improvement-roadmap.md         # Impact×Effort prioritization
│
├── tools/
│   ├── knowledge_updater.py               # Self-improving crawl pipeline
│   └── .seen_urls.json                    # URL deduplication store
│
└── tests/
    ├── test-scenarios.md                  # 6 scenario tests with execution results
    ├── calibration-results.md             # Scoring rubric calibration (3 fixtures)
    ├── cross-skill-integration-test.md     # Cross-skill interface validation
    └── fixtures/
        ├── react-checkout/                 # React + TypeScript + Tailwind
        │   ├── CheckoutForm.tsx
        │   ├── CheckoutFlow.tsx
        │   ├── Header.tsx
        │   └── globals.css
        ├── plain-html-landing/            # Plain HTML5 + CSS3
        │   └── index.html
        └── vue-dashboard/                  # Vue 3 + SCSS + Composition API
            ├── Dashboard.vue
            ├── SidebarNavigation.vue
            └── Icon.vue
```

---

## 📈 Development Phases

| Phase | Focus | Status |
|-------|-------|--------|
| 0 | Research & Architecture | ✅ Complete |
| 1 | Core Sub-Skills | ✅ Complete |
| 2 | Main Harness + Quality Gates | ✅ Complete |
| 3 | Knowledge Pipeline | ✅ Complete |
| 4 | Testing & Validation | ✅ Complete |
| 5 | Cross-Skill Integration | ✅ Complete |

All 38 tasks across 6 phases are complete. See [`PROJECT-DEVELOPMENT-PHASE-TRACKING.md`](PROJECT-DEVELOPMENT-PHASE-TRACKING.md) for full details.

---

## 🤝 Contributing

Contributions are welcome! This project follows a structured skill architecture:

1. **Sub-skill changes** — Modify the relevant `skills/sub-*.md` file
2. **Knowledge updates** — Run `python tools/knowledge_updater.py` or add entries manually to `SECOND-KNOWLEDGE-BRAIN.md`
3. **Test fixtures** — Add new fixtures to `tests/fixtures/` and update `tests/test-scenarios.md`
4. **Scoring calibration** — Document any adjustments in `tests/calibration-results.md`

### Running Tests

```bash
# Validate knowledge pipeline (dry run)
python tools/knowledge_updater.py --dry-run

# Run ArXiv source only
python tools/knowledge_updater.py --source arxiv

# Run with custom query
python tools/knowledge_updater.py --query "WCAG 2.2 mobile"
```

### Adding a New Evaluation Dimension

1. Add the dimension criteria to `skills/sub-scoring-engine.md`
2. Add the framework to the registry in `skills/sub-evaluation-framework-selector.md`
3. Update the composite scoring formula in `SECOND-KNOWLEDGE-BRAIN.md`
4. Add test scenarios to `tests/test-scenarios.md`
5. Update `skills/main.md` workflow to include the new pass

---

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Built with rigor and evidence-first methodology.**

*Every violation cites a file:line. Every score follows a rubric. Every recommendation has a before/after.*

</div>

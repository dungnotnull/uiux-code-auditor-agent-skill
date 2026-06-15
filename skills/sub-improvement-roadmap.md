---
name: sub-improvement-roadmap
description: Transform the violation catalog into a prioritized improvement roadmap using Impact Ă— Effort analysis. Groups findings into Quick Wins, Medium-term, and Strategic items with ROI estimates and before/after code examples.
---

## Purpose

Raw violation catalogs are not actionable for engineering teams. This sub-skill:
1. Scores each violation by **Impact** (user experience damage) and **Effort** (engineering time)
2. Groups violations into strategic categories using the Impact Ă— Effort matrix
3. Generates code-level before/after examples for the top 3 findings
4. Produces a professional improvement roadmap ready to paste into a sprint backlog

---

## Inputs

- Violation Catalog (from sub-scoring-engine)
- Dimension scores and composite score
- Tech Stack Report (for framework-specific fix examples)
- Source code files (for before/after code generation)

---

## Impact Ă— Effort Scoring

### Impact Score (1â€“5)
| Score | Definition |
|-------|-----------|
| 5 | P0 violation: blocks a user group, legal/accessibility liability |
| 4 | P1 violation: significant usability friction, affects primary user flow |
| 3 | P2 violation: noticeable quality gap, affects secondary flows |
| 2 | P3 violation: cosmetic or minor inconsistency |
| 1 | Enhancement: no current violation, but could improve experience |

### Effort Score (1â€“5)
| Score | Definition |
|-------|-----------|
| 1 | < 1 hour: add attribute, change class name, update text |
| 2 | 1â€“4 hours: refactor one component, add a state, update CSS |
| 3 | 4â€“8 hours: modify shared component, update multiple files |
| 4 | 1â€“3 days: design system change, accessibility refactor |
| 5 | > 3 days: architectural change, new component library |

### Matrix Placement
```
Impact Ă· Effort â†’ Priority Group:

Impact 4â€“5 + Effort 1â€“2 â†’ QUICK WIN (highest priority)
Impact 4â€“5 + Effort 3â€“5 â†’ MEDIUM-TERM
Impact 1â€“3 + Effort 1â€“2 â†’ FILL-IN (do alongside other work)
Impact 1â€“3 + Effort 3â€“5 â†’ STRATEGIC (plan carefully, may defer)
```

---

## Workflow

### Step A â€” Score Each Violation
For each item in the Violation Catalog:
1. Assign Impact score (1â€“5) based on severity and affected user flow
2. Assign Effort score (1â€“5) based on fix complexity
3. Calculate Priority = Impact Ă· Effort (higher = do first)
4. Assign matrix group (Quick Win / Medium / Fill-in / Strategic)

### Step B â€” Sort and Group

**Quick Wins** â€” sorted by Priority (descending)
**Medium-term** â€” sorted by Impact (descending)
**Fill-ins** â€” sorted by Effort (ascending)
**Strategic** â€” sorted by Impact (descending)

### Step C â€” Before/After for Top 3

For the top 3 Quick Wins (or highest priority items overall):
1. Read the source file at the cited line
2. Show the current code snippet (3â€“10 lines of context)
3. Show the recommended fix
4. Add a brief explanation of why the fix addresses the criterion

### Step D â€” ROI Estimates

For each Quick Win, add:
- **User group impacted**: who benefits (e.g., "keyboard users, ~15% of users")
- **Risk removed**: what liability or friction is eliminated
- **Effort**: precise time estimate
- **ROI note**: qualitative statement (e.g., "Fixes WCAG A violation â€” legal compliance risk removed")

### Step E â€” Assemble Roadmap

```
IMPROVEMENT ROADMAP
===================

COMPOSITE SCORE: [X/100] â†’ Target: [X+15/100] after Quick Wins

---

## Quick Wins (High Impact, Low Effort â€” Do First)
Expected score improvement: +[N] points

| # | ID   | Issue                    | Fix                              | Impact | Effort | ROI |
|---|------|--------------------------|----------------------------------|--------|--------|-----|
| 1 | V001 | Missing alt on hero img  | Add descriptive alt attribute    | 5      | 1h     | WCAG A compliance |
| 2 | V003 | No loading state on CTA  | Add isLoading state + spinner    | 4      | 2h     | Eliminates H1 violation |
| 3 | V012 | outline:none on focus    | Replace with custom focus ring   | 4      | 1h     | WCAG 2.4.7 AA compliance |

### Before/After â€” Top 3 Fixes

**Fix #1: [Violation ID] â€” [Title]**
Current code (`[file]:[line]`):
```[language]
[current code snippet]
```
Recommended:
```[language]
[fixed code snippet]
```
Why: [one sentence linking to the criterion violated]

---

## Medium-term (High Impact, High Effort â€” Plan for Next Sprint)

| # | ID   | Issue                    | Fix                              | Impact | Effort |
|---|------|--------------------------|----------------------------------|--------|--------|
| 1 | V008 | No error recovery text   | Rewrite all error messages       | 4      | 1 day  |
| 2 | V015 | Design token inconsist.  | Migrate to CSS variable system   | 3      | 3 days |

---

## Fill-ins (Low Impact, Low Effort â€” Do Alongside Other Work)

| # | ID   | Issue                    | Fix                              | Effort |
|---|------|--------------------------|----------------------------------|--------|
| 1 | V020 | Redundant div wrapper    | Remove one nesting level         | 30min  |

---

## Strategic (Low Impact or High Effort â€” Plan Carefully)

| # | ID   | Issue                    | Fix                              | Impact | Effort | Recommendation |
|---|------|--------------------------|----------------------------------|--------|--------|----------------|
| 1 | V031 | No keyboard shortcuts    | Implement command palette        | 2      | 5 days | Defer to v2    |

---

## SCORE PROJECTION

Current:        [X/100]
After Quick Wins: +[N] â†’ [X+N]/100
After Medium:   +[M] â†’ [X+N+M]/100
Full roadmap:   [target]/100
```

---

## Outputs

- **Impact Ă— Effort scored violation table**
- **Grouped roadmap** (Quick Wins / Medium / Fill-ins / Strategic)
- **Before/After code examples** (top 3)
- **Score projection** (current â†’ after quick wins â†’ after full roadmap)
- **ROI estimates** (per Quick Win)

---

## Tools Used

- `Read` â€” re-read source files for before/after code examples
- `Write` â€” save roadmap as a separate file if user requests it

---

## Quality Gate

Before delivering roadmap to main harness:
- [ ] Every violation has been assigned an Impact and Effort score
- [ ] At least 1 Quick Win identified
- [ ] At least 1 Medium-term item identified
- [ ] Before/after examples written for top 3 items (with actual code, not placeholders)
- [ ] Score projection included
- [ ] ROI note added to every Quick Win
- [ ] Every roadmap item links back to a violation ID in the catalog

---

## Cross-skill Interface (Cluster B)

This sub-skill is fully reusable by Skills 6 and 8. The only dependency is the Violation Catalog format:

```json
{
  "violations": [
    {
      "id": "V001",
      "severity": "P0",
      "dimension": "Accessibility",
      "file": "src/Component.tsx",
      "line": 23,
      "criterion": "WCAG 1.1.1",
      "description": "..."
    }
  ]
}
```

Impact Ă— Effort scoring logic and roadmap format are identical across all Cluster B skills.


## Cross-Skill Interface (Cluster B) — Full Specification

This sub-skill is fully reusable by Skills 6 and 8. The only dependency is the Violation Catalog format.

### Input Contract (JSON)

`json
{
  "violation_catalog": [
    {
      "id": "V001",
      "severity": "P0",
      "dimension": "Accessibility",
      "file": "src/Component.tsx",
      "line": 23,
      "criterion": "WCAG 1.1.1",
      "description": "<img> missing alt attribute",
      "recommended_fix": "Add descriptive alt attribute"
    }
  ],
  "dimension_scores": [
    {"name": "Heuristic Evaluation", "weight": 0.30, "score": 4.7},
    {"name": "Accessibility", "weight": 0.35, "score": 3.5}
  ],
  "composite_score": 43.25,
  "tech_stack_report": {
    "framework": "React",
    "styling": "CSS Modules",
    "design_tokens": "CSS Variables"
  }
}
`

### Output Contract (JSON)

`json
{
  "roadmap": {
    "quick_wins": [
      {
        "id": "V001",
        "issue": "Missing alt on hero img",
        "fix": "Add descriptive alt attribute",
        "impact": 5,
        "effort": "1h",
        "effort_score": 1,
        "roi_note": "Fixes WCAG A violation - legal compliance risk removed",
        "priority_score": 5.0,
        "before_code": "<img src=\"hero.jpg\">",
        "after_code": "<img src=\"hero.jpg\" alt=\"Team working together in a modern office\">"
      }
    ],
    "medium_term": [
      {
        "id": "V008",
        "issue": "No error recovery text",
        "fix": "Rewrite all error messages with actionable guidance",
        "impact": 4,
        "effort": "1 day",
        "effort_score": 4
      }
    ],
    "fill_ins": [
      {
        "id": "V020",
        "issue": "Redundant div wrapper",
        "fix": "Remove one nesting level",
        "impact": 2,
        "effort": "30min",
        "effort_score": 1
      }
    ],
    "strategic": [
      {
        "id": "V031",
        "issue": "No keyboard shortcuts",
        "fix": "Implement command palette",
        "impact": 2,
        "effort": "5 days",
        "effort_score": 5,
        "recommendation": "Defer to v2"
      }
    ]
  },
  "score_projection": {
    "current": 43,
    "after_quick_wins": 55,
    "after_medium": 68,
    "full_roadmap": 78
  },
  "top_3_before_after": [
    {
      "violation_id": "V001",
      "title": "Missing alt on hero image",
      "file": "src/Header.tsx",
      "line": 8,
      "before": "<img src=\"/logo.png\">",
      "after": "<img src=\"/logo.png\" alt=\"Company logo\">",
      "why": "WCAG 1.1.1 requires text alternatives for all non-decorative images"
    }
  ]
}
`

### Integration for Skill 6 (code-quality-auditor)

The Impact x Effort matrix logic is identical. The only change:
- Replace "WCAG" references with the relevant quality standard (ISO/IEC 25010)
- Replace UX-specific language ("user experience damage") with quality language ("code quality impact")
- Keep the priority grouping (Quick Win / Medium / Fill-in / Strategic) unchanged

### Integration for Skill 8 (performance-auditor)

Same logic, different domain language:
- Replace violation criteria with performance thresholds (LCP, FID, CLS, TTFB)
- Replace "user group impacted" with "performance budget impacted"
- Replace "WCAG compliance risk" with "Core Web Vitals failure risk"

### Impact x Effort Scoring (Shared Formula)

`
Impact (1-5):
  5 = P0: blocks a user group or creates legal/compliance risk
  4 = P1: significant friction in primary user flow
  3 = P2: noticeable gap in secondary flows
  2 = P3: cosmetic or minor inconsistency
  1 = Enhancement opportunity, no current violation

Effort (1-5):
  1 = < 1 hour: add attribute, change class, update text
  2 = 1-4 hours: refactor one component, add state, update CSS
  3 = 4-8 hours: modify shared component, update multiple files
  4 = 1-3 days: design system change, accessibility refactor
  5 = > 3 days: architectural change, new component library

Priority = Impact / Effort
Quick Win: Impact 4-5, Effort 1-2
Medium:    Impact 4-5, Effort 3-5
Fill-in:   Impact 1-3, Effort 1-2
Strategic: Impact 1-3, Effort 3-5
`

This scoring system is shared across all Cluster B skills without modification.

### Version

Interface version: 1.0.0
Last updated: 2026-06-15
Maintainer: uiux-code-auditor (Skill 4)

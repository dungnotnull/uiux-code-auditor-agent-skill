---
name: sub-scoring-engine
description: Score source code across heuristic, accessibility, visual layout, and visual consistency dimensions. Produces dimension scores (0â€“10) and a violation catalog with file:line citations and severity ratings.
---

## Purpose

This is the core evaluation engine of the uiux-code-auditor harness. It executes 4 scoring passes against the source code files in the manifest, applying the frameworks selected by `sub-evaluation-framework-selector`. Every finding is:
- Tied to a specific file and line number
- Mapped to a named framework criterion
- Assigned a severity (P0â€“P3)

---

## Inputs

- File Manifest (from sub-code-analyzer)
- Evaluation Plan with dimension weights (from sub-evaluation-framework-selector)
- Source code files (read via Read + Grep)
- SECOND-KNOWLEDGE-BRAIN.md (for criterion definitions)

---

## Pass A â€” Nielsen's 10 Usability Heuristics

For each heuristic, read relevant files and look for violations:

### H1 â€” Visibility of System Status
**What to look for in code:**
- Loading states: `isLoading`, `isPending`, spinner components
- Progress indicators for multi-step flows
- Form submission feedback (success/error states)
- Disabled states with visual feedback

**Violation signals:**
```
- Button with onClick but no disabled state or loading indicator
- Form that submits without visual feedback
- Async operation with no pending state rendered
- Navigation without active state indicator
```
**Scoring**: 10 = all async operations have states; 0 = no loading/feedback patterns anywhere

---

### H2 â€” Match Between System and Real World
**What to look for in code:**
- Button and link labels (are they jargon-free?)
- Icon usage (are icons universally understood?)
- Error message text (plain language vs. technical codes)
- Date/time formats (locale-appropriate?)

**Violation signals:**
```
- Error messages showing raw API error codes to users
- Labels like "Submit Entity" instead of "Save Profile"
- Icon-only buttons without aria-label or title
```

---

### H3 â€” User Control and Freedom
**What to look for in code:**
- Cancel/close buttons on dialogs and modals
- Undo functionality for destructive actions
- Back navigation available on multi-step flows
- Modal/drawer dismissal (click outside, Escape key)

**Violation signals:**
```
- Modal with no close button
- Destructive action (delete) with no confirmation dialog
- Multi-step form with no "Back" button
- onKeyDown missing Escape handler on overlay components
```

---

### H4 â€” Consistency and Standards
**What to look for in code:**
- Button variants used consistently (primary = submit, secondary = cancel, always)
- Same action available through same UI patterns everywhere
- Naming conventions: component names, CSS classes, event handler names
- Design token usage vs. hardcoded values

**Violation signals:**
```
- "Delete" action shown as button in one place, link in another
- Inconsistent button color for same action type
- Mix of hardcoded colors and CSS variables
- Component named differently across files for same role
```

---

### H5 â€” Error Prevention
**What to look for in code:**
- Client-side validation before submission
- Confirmation dialogs for irreversible actions
- Input constraints (type="email", maxLength, pattern)
- Safe defaults pre-selected

**Violation signals:**
```
- <input type="text"> for email (no type="email")
- Delete button with no confirmation step
- Form submits empty required fields without validation
- No maxLength on text fields that have backend limits
```

---

### H6 â€” Recognition Rather Than Recall
**What to look for in code:**
- Visible labels on all form inputs
- Placeholder text used as label substitute (violation)
- Autocomplete attributes on form fields
- Contextual defaults and suggestions

**Violation signals:**
```
- <input placeholder="Email" /> with no associated <label>
- Search with no recent/suggested options
- Select with no default option selected
- No autocomplete attribute on name/email/address fields
```

---

### H7 â€” Flexibility and Efficiency of Use
**What to look for in code:**
- Keyboard shortcuts implemented
- Power-user paths (bulk actions, filters, search)
- Customizable settings or views
- Skip-to-content links for keyboard users

**Violation signals:**
```
- No skip-to-main-content link at top of page
- Data table with no keyboard column sorting
- No keyboard shortcut for frequently used actions
```

---

### H8 â€” Aesthetic and Minimalist Design
**What to look for in code:**
- DOM nesting depth (deeply nested = visual complexity)
- Information density per screen
- Decorative elements without purpose
- Component prop count (too many = too much visible at once)

**Violation signals:**
```
- Component with >15 props visible simultaneously
- Page section with >8 competing visual elements
- Decorative images without aria-hidden="true"
- Deeply nested divs (>8 levels) suggesting over-engineered layout
```

---

### H9 â€” Help Users Recognize, Diagnose, and Recover from Errors
**What to look for in code:**
- Error message text quality (specific, actionable)
- Error placement (inline next to field, not just toast)
- Recovery suggestions in error messages
- Error state styling (not just color â€” icon or text too)

**Violation signals:**
```
- Error message: "Error occurred" (not specific)
- Error shown only via toast, not inline
- Error identified by color alone (no icon or text)
- No recovery suggestion in error message
```

---

### H10 â€” Help and Documentation
**What to look for in code:**
- Tooltip components on complex fields
- Placeholder text quality (helpful examples, not just field name)
- Onboarding/empty-state components
- Help text proximity to form fields

**Violation signals:**
```
- Complex field with no helper text or tooltip
- Empty state with no guidance on what to do
- No onboarding for first-time users
```

---

## Pass B â€” WCAG 2.2 Audit

### Perceivable
```
1.1.1 â€” grep: <img without alt | alt="" on non-decorative img
1.3.1 â€” check heading hierarchy (h1 â†’ h2 â†’ h3, no skips), table has <th>
1.4.3 â€” estimate contrast from CSS color values (flag pairs that look low)
1.4.11 â€” check border/outline color on form inputs and interactive elements
```

### Operable
```
2.1.1 â€” grep: interactive elements not reachable via Tab (tabIndex="-1" on interactive elements)
2.1.2 â€” grep: keyboard traps (focus locked inside modal without Escape handler)
2.4.3 â€” check DOM order matches visual order (CSS order: N in flex/grid)
2.4.7 â€” grep: :focus { outline: none } or outline: 0 without custom focus style replacement
2.5.3 â€” button/input accessible name must contain visible label text
```

### Understandable
```
3.1.1 â€” grep: <html without lang attribute
3.3.1 â€” error identification: error messages must include text, not just color
3.3.2 â€” grep: <input without associated <label> or aria-label or aria-labelledby
```

### Robust
```
4.1.2 â€” ARIA audit:
  - role= values are valid WAI-ARIA roles
  - aria-label present on icon-only buttons
  - aria-expanded, aria-selected, aria-checked match component state
  - aria-required on required fields
4.1.3 â€” grep: status changes communicated via aria-live or role="status"
```

### WCAG Scoring
- Perceivable: 0â€“10
- Operable: 0â€“10
- Understandable: 0â€“10
- Robust: 0â€“10
- **Accessibility Score** = average of 4 principles
- **Conformance Level**: A (all A criteria), AA (all A+AA criteria), AAA (all criteria)

---

## Pass C â€” Gestalt Principles

```
Proximity:
  - flex/grid gap consistent with element relationships?
  - Related labels and inputs correctly grouped?
  
Similarity:
  - Consistent class names for same component variants?
  - Button variants aligned (primary/secondary/danger)?
  
Continuity:
  - Aligned column structures in lists/tables?
  - Consistent indentation signaling hierarchy?
  
Figure-Ground:
  - Modal overlays with background dim (z-index + overlay)?
  - Dropdown backgrounds distinct from page background?
  
Common Region:
  - Related form fields wrapped in fieldset or logical container?
  - Card components used consistently to group related content?
```

Score: 0â€“10 (10 = all principles applied consistently)

---

## Pass D â€” Visual Consistency

```
Design Token Check:
  - Grep for hardcoded hex values: #[0-9a-fA-F]{3,6}
  - Grep for hardcoded rgba/rgb: (rgba?|hsl)\(
  - Flag every occurrence outside of design token files
  - Score: 10 - (violations / total_color_usages Ă— 10)

Spacing Rhythm:
  - Grep for px values: \b\d+px\b (excluding 0px, 1px)
  - Check if values fall on a consistent scale (4/8/12/16/24/32px...)
  - Flag arbitrary values (e.g., 13px, 27px, 53px)

Typography Scale:
  - Check font-size values against a modular scale
  - Check line-height consistency
  - Flag: mixing px and rem/em units for font sizes
```

Score: 0â€“10 (10 = all values use design tokens / consistent scale; 0 = completely ad hoc)

---

## Violation Catalog Format

```
| ID   | Severity | Dimension      | File              | Line | Criterion       | Description                          |
|------|----------|---------------|-------------------|------|-----------------|--------------------------------------|
| V001 | P0       | Accessibility  | src/Form.tsx      | 23   | WCAG 1.1.1      | <img> missing alt attribute          |
| V002 | P1       | Heuristic      | src/Button.tsx    | 45   | Nielsen H9      | Error message "Error" lacks details  |
| V003 | P2       | Consistency    | src/theme.css     | 12   | Design Tokens   | Hardcoded #FF6B00 instead of token   |
```

---

## Outputs

- **Dimension scores** (4 Ă— 0â€“10)
- **Composite score** (weighted average per formula in SECOND-KNOWLEDGE-BRAIN.md)
- **Violation Catalog** (full table with IDs, severities, citations)
- **Conformance level** (WCAG 2.2 A / AA / AAA)

---

## Tools Used

- `Read` â€” read component files for detailed analysis
- `Grep` â€” search for violation patterns (alt attributes, focus styles, aria, design tokens)
- `WebFetch` â€” retrieve specific WCAG criterion text for citation if needed

---

## Quality Gate

Before handing off to `sub-improvement-roadmap`:
- [ ] All 4 passes complete (A, B, C, D)
- [ ] Every violation has a violation ID, file path, and line number
- [ ] WCAG conformance level determined
- [ ] Composite score calculated
- [ ] Severity assigned to every violation
- [ ] At least one "working well" observation per dimension

---

## Cross-skill Interface (Cluster B)

This scoring engine is parametrized by the Evaluation Plan. To use in Skills 6 or 8:
1. Replace the Pass A criteria with the relevant framework (e.g., ISO/IEC 25010 for Skill 6)
2. Keep the violation catalog format identical
3. Keep dimension weights configurable via Evaluation Plan


## Cross-Skill Interface (Cluster B) — Full Specification

This scoring engine is parametrized by the Evaluation Plan. To reuse it in another Cluster B skill:

### Input Contract (JSON)

`json
{
  "file_manifest": [
    {"path": "src/Layout.tsx", "priority": 1, "loc": 120, "props": 5}
  ],
  "evaluation_plan": {
    "dimensions": [
      {
        "name": "Heuristic Evaluation",
        "framework": "Nielsen's 10 Usability Heuristics",
        "weight": 0.30,
        "criteria": ["H1", "H2", "...", "H10"]
      }
    ],
    "wcag_level": "AA",
    "domain_additions": []
  },
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
  "dimension_scores": [
    {
      "name": "Heuristic Evaluation",
      "weight": 0.30,
      "score": 4.7,
      "details": {
        "H1": {"score": 5, "violations": ["V001"]},
        "H2": {"score": 7, "violations": []}
      }
    }
  ],
  "composite_score": 43.25,
  "score_band": "Needs Work",
  "wcag_conformance": {
    "level": "AA",
    "status": "Not Met",
    "perceivable_score": 4,
    "operable_score": 3,
    "understandable_score": 3,
    "robust_score": 4
  },
  "violation_catalog": [
    {
      "id": "V001",
      "severity": "P0",
      "dimension": "Accessibility",
      "file": "src/Header.tsx",
      "line": 8,
      "criterion": "WCAG 1.1.1",
      "description": "<img src='/logo.png'> missing alt attribute",
      "recommended_fix": "Add descriptive alt attribute: alt='Company logo'"
    }
  ],
  "working_well": [
    "Loading state implemented with isLoading pattern",
    "SCSS variables defined for primary design colors"
  ]
}
`

### Integration for Skill 6 (code-quality-auditor)

Replace Pass A criteria:
- Instead of Nielsen's 10 Heuristics, apply ISO/IEC 25010 quality characteristics
- Pass B (Accessibility) remains shared
- Pass C → Code readability and maintainability patterns
- Pass D → API consistency and naming convention audit

The violation catalog format and severity classification are identical across all Cluster B skills.

### Integration for Skill 8 (performance-auditor)

Replace Pass A criteria:
- Instead of Nielsen's Heuristics, apply Web Vitals thresholds
- Pass B → Performance-impacting accessibility (reflow, animations)
- Pass C → Render path optimization patterns
- Pass D → Bundle consistency and lazy loading patterns

### Composite Score Formula (Shared)

`
Composite = sum(dimension_score * dimension_weight for all dimensions) * 10

Bands:
  90-100: Excellent
  75-89:  Good
  60-74:  Acceptable
  40-59:  Needs Work
  0-39:   Critical
`

This formula is consistent across all Cluster B skills. Dimensions and weights change, but the calculation method is identical.

### Severity Classification (Shared)

| Level | Label | Definition |
|-------|-------|-----------|
| P0 | Blocker | Prevents task completion for >= 1 user group; legal/compliance risk |
| P1 | Critical | Significant usability/quality friction; affects primary flow |
| P2 | Major | Noticeable quality gap; affects secondary flows |
| P3 | Minor | Cosmetic or polish issue; enhancement opportunity |

This classification is shared across all Cluster B skills.

### Version

Interface version: 1.0.0
Last updated: 2026-06-15
Maintainer: uiux-code-auditor (Skill 4)

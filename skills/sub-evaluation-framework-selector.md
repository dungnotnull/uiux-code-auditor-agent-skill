---
name: sub-evaluation-framework-selector
description: Select the most relevant evaluation frameworks and dimension weights for the detected tech stack and domain context. Produces the Evaluation Plan that drives the scoring engine.
---

## Purpose

Different tech stacks, domains, and compliance requirements call for different evaluation criteria. This sub-skill:
1. Consults the Tech Stack Report from `sub-code-analyzer`
2. Selects the appropriate frameworks from the registry below
3. Assigns dimension weights
4. Documents the rationale for each selection
5. Outputs an **Evaluation Plan** to guide the scoring engine

---

## Inputs

- Tech Stack Report (from sub-code-analyzer)
- Domain context (e.g., e-commerce, dashboard, marketing site, healthcare, mobile)
- User-specified compliance requirements (WCAG AA mandatory? Mobile-first? etc.)
- SECOND-KNOWLEDGE-BRAIN.md (for framework descriptions)

---

## Framework Registry

### Always Applied (Universal)

| Framework | Dimension | Weight |
|-----------|-----------|--------|
| Nielsen's 10 Usability Heuristics | Heuristic Evaluation | 30% |
| WCAG 2.2 (minimum Level AA) | Accessibility | 35% |
| Gestalt Principles | Visual Layout | 15% |
| Design Token Standards | Visual Consistency | 20% |

### Domain-Specific Additions

#### E-commerce / Conversion-Critical
- Baymard Institute UX Research â€” checkout patterns, product page standards
- CRO (Conversion Rate Optimization) heuristics â€” trust signals, CTA clarity
- Adjust: Heuristic 30% â†’ 25%; add CRO dimension at 5%

#### Mobile (React Native / Flutter / responsive web)
- Fitts' Law â€” touch target size minimum 44Ă—44px
- Apple Human Interface Guidelines â€” iOS-specific patterns
- Material Design Guidelines â€” Android patterns
- Adjust: add Mobile Usability dimension at 10%; reduce Visual Consistency to 10%

#### Healthcare / High-Stakes Applications
- Add: Error prevention and recovery (Heuristic 5 & 9) weighted 2Ă— in heuristic score
- Add: WHO digital health UX guidelines check
- Add: HIPAA-relevant UI patterns (session timeout, PHI handling in UI)

#### Dashboard / Data-Intensive
- Add: Data visualization clarity check (Tufte's data-ink ratio)
- Add: Cognitive load assessment for information density
- Adjust: Gestalt weight â†’ 20% (visual hierarchy critical for dashboards)

#### Multilingual / Internationalized
- Add: i18n UI audit (text overflow with long strings, RTL layout support, date/number formatting)
- Check: `lang` attribute, locale-aware components, string externalization

---

## Selection Logic

```
IF domain == "e-commerce":
  Apply universal frameworks + Baymard + CRO heuristics
  
ELIF platform == "mobile" OR responsive == "mobile-first":
  Apply universal frameworks + Fitts' Law + platform HIG
  
ELIF domain == "healthcare":
  Apply universal frameworks + error prevention 2Ă— + WHO guidelines
  
ELIF domain == "dashboard" OR data-heavy:
  Apply universal frameworks + Tufte + cognitive load
  
ELSE:
  Apply universal frameworks only
  
IF user specifies WCAG AAA:
  Upgrade accessibility target from AA to AAA; note all AAA criteria in scoring
  
IF user specifies mobile-first:
  Add mobile dimension; reduce visual consistency weight
```

---

## Workflow

### Step A â€” Read Inputs
1. Load Tech Stack Report
2. Confirm domain with user if not specified
3. Note any explicit compliance requirements

### Step B â€” Select Frameworks
Apply selection logic above. For each selected framework:
- Name it
- State why it applies (linked to tech stack or domain signal)
- Assign dimension weight

### Step C â€” Produce Evaluation Plan

```
EVALUATION PLAN
===============
Project context: [React e-commerce / Vue dashboard / etc.]
Target conformance: WCAG 2.2 Level [AA / AAA]

DIMENSIONS & WEIGHTS:
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚ Dimension                            â”‚ Framework                             â”‚ Weight â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚ Heuristic Evaluation                 â”‚ Nielsen's 10 Usability Heuristics     â”‚  30%   â”‚
â”‚ Accessibility                        â”‚ WCAG 2.2 Level AA                     â”‚  35%   â”‚
â”‚ Visual Layout                        â”‚ Gestalt Principles                    â”‚  15%   â”‚
â”‚ Visual Consistency                   â”‚ Design Token Standards                â”‚  20%   â”‚
â”‚ [Domain addition if applicable]      â”‚ [Framework name]                      â”‚  [X%]  â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”´â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”´â”€â”€â”€â”€â”€â”€â”€â”€â”˜

RATIONALE:
[For each dimension, 1â€“2 sentences explaining why this framework was selected for this project]

SCORING RUBRIC:
[For each dimension: what constitutes a 10/10, 7/10, 5/10, 3/10, 0/10]
```

---

## Outputs

- **Evaluation Plan** (documented, shown to user for confirmation)
- Dimension weights (consumed by `sub-scoring-engine`)
- Domain-specific additions (consumed by `sub-scoring-engine`)

---

## Tools Used

- `Read` â€” SECOND-KNOWLEDGE-BRAIN.md for framework descriptions
- `WebSearch` â€” if a domain-specific framework needs verification or latest update
- `WebFetch` â€” retrieve specific guideline documents if needed for citation

---

## Quality Gate

Before handing off to `sub-scoring-engine`:
- [ ] All 4 universal dimensions are in the plan
- [ ] Weights sum to 100%
- [ ] Every framework has a rationale tied to the tech stack or domain
- [ ] Target WCAG conformance level is explicitly stated
- [ ] Scoring rubric is defined for each dimension

---

## Cross-skill Interface (Cluster B)

This sub-skill is shared across Cluster B (Skills 4, 6, 8). The Evaluation Plan format is framework-agnostic:

```json
{
  "dimensions": [
    {
      "name": "Heuristic Evaluation",
      "framework": "Nielsen's 10 Usability Heuristics",
      "weight": 0.30,
      "criteria": ["criterion_1", "criterion_2", "..."]
    }
  ],
  "wcag_level": "AA",
  "domain_additions": []
}
```

Skills 6 and 8 substitute their own framework registries while reusing this selection logic pattern.


## Cross-Skill Interface (Cluster B) — Full Specification

This sub-skill is shared across Cluster B (Skills 4, 6, 8). To reuse it in another skill:

### Input Contract (JSON)

`json
{
  "tech_stack_report": {
    "framework": "React",
    "styling": "CSS Modules",
    "design_tokens": "CSS Variables",
    "files": [
      {"path": "src/Layout.tsx", "priority": 1, "loc": 120, "props": 5}
    ],
    "complexity_flags": ["src/Dashboard.tsx (350 LOC, 12 props)"]
  },
  "domain": "e-commerce",
  "compliance_requirements": {
    "wcag_level": "AA",
    "mobile_first": false,
    "additional_frameworks": []
  }
}
`

### Output Contract (JSON)

`json
{
  "evaluation_plan": {
    "dimensions": [
      {
        "name": "Heuristic Evaluation",
        "framework": "Nielsen's 10 Usability Heuristics",
        "weight": 0.30,
        "criteria": [
          "H1: Visibility of System Status",
          "H2: Match Between System and Real World",
          "H3: User Control and Freedom",
          "H4: Consistency and Standards",
          "H5: Error Prevention",
          "H6: Recognition Rather Than Recall",
          "H7: Flexibility and Efficiency of Use",
          "H8: Aesthetic and Minimalist Design",
          "H9: Help Users Recognize and Recover from Errors",
          "H10: Help and Documentation"
        ]
      },
      {
        "name": "Accessibility",
        "framework": "WCAG 2.2 Level AA",
        "weight": 0.35,
        "criteria": [
          "Perceivable: 1.1.1, 1.3.1, 1.4.3, 1.4.11",
          "Operable: 2.1.1, 2.4.3, 2.4.7, 2.5.3",
          "Understandable: 3.1.1, 3.3.1, 3.3.2",
          "Robust: 4.1.2, 4.1.3"
        ]
      },
      {
        "name": "Visual Layout",
        "framework": "Gestalt Principles",
        "weight": 0.15,
        "criteria": [
          "Proximity", "Similarity", "Continuity",
          "Closure", "Figure-Ground", "Common Region"
        ]
      },
      {
        "name": "Visual Consistency",
        "framework": "Design Token Standards",
        "weight": 0.20,
        "criteria": [
          "Color token usage", "Spacing rhythm",
          "Typography scale", "Shadow/elevation scale"
        ]
      }
    ],
    "wcag_level": "AA",
    "domain_additions": [],
    "scoring_rubric": {
      "10": "No violations found; exemplary implementation",
      "8-9": "Minor issues only; best-practice patterns mostly followed",
      "6-7": "Noticeable gaps; some violations affecting secondary flows",
      "4-5": "Significant violations; primary user flows affected",
      "2-3": "Major violations; accessibility failures or systemic UX issues",
      "0-1": "Catastrophic; no UX patterns or accessibility present"
    }
  }
}
`

### Integration for Skill 6 (code-quality-auditor)

Replace the framework registry with quality-focused criteria:
- Heuristics → ISO/IEC 25010 quality characteristics
- Accessibility → Keep WCAG (shared dimension)
- Gestalt → Replace with code readability/maintainability patterns
- Visual Consistency → Replace with API consistency and naming conventions

### Integration for Skill 8 (performance-auditor)

Replace the framework registry with performance-focused criteria:
- Heuristics → Web Vitals thresholds (LCP, FID, CLS)
- Accessibility → Keep WCAG Performance criteria (1.4.10 Reflow, 2.3.1 Three Flashes)
- Gestalt → Replace with render performance patterns
- Visual Consistency → Replace with bundle size consistency and lazy loading patterns

### Version

Interface version: 1.0.0
Last updated: 2026-06-15
Maintainer: uiux-code-auditor (Skill 4)

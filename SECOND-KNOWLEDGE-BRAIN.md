# SECOND-KNOWLEDGE-BRAIN.md — uiux-code-auditor

> Self-improving domain knowledge base. Continuously updated by `tools/knowledge_updater.py`.
> Last manual update: 2026-06-11

---

## Core Concepts & Frameworks

### Nielsen's 10 Usability Heuristics (Jakob Nielsen, 1994)
The most widely applied UI evaluation framework. Each heuristic maps to detectable source code patterns:

| # | Heuristic | Code-detectable signals |
|---|-----------|------------------------|
| 1 | Visibility of system status | Loading states, progress indicators, disabled states |
| 2 | Match between system and real world | Label text, icon semantics, date/time formats |
| 3 | User control and freedom | Undo/cancel buttons, back navigation, modal dismissal |
| 4 | Consistency and standards | Design token usage, component naming, CSS class conventions |
| 5 | Error prevention | Input validation, confirmation dialogs, destructive action safeguards |
| 6 | Recognition rather than recall | Visible labels, contextual help, autocomplete, defaults |
| 7 | Flexibility and efficiency | Keyboard shortcuts, power-user paths, filter/search |
| 8 | Aesthetic and minimalist design | DOM depth, component prop count, information density |
| 9 | Help users recognize/recover from errors | Error message clarity, recovery suggestions, inline validation |
| 10 | Help and documentation | Tooltips, placeholder text, onboarding flows |

**Source**: Nielsen, J. (1994). Enhancing the explanatory power of usability heuristics. CHI '94.

---

### WCAG 2.2 — Web Content Accessibility Guidelines

Four principles (POUR), three conformance levels:

**Perceivable**
- 1.1.1 Non-text Content (A): All `<img>` must have `alt`; decorative images use `alt=""`
- 1.3.1 Info and Relationships (A): Semantic HTML; headings hierarchy
- 1.4.3 Contrast Minimum (AA): 4.5:1 for normal text; 3:1 for large text
- 1.4.11 Non-text Contrast (AA): UI components 3:1 against adjacent colors

**Operable**
- 2.1.1 Keyboard (A): All interactive elements reachable via Tab
- 2.4.3 Focus Order (A): Logical tab order through DOM
- 2.4.7 Focus Visible (AA): Visible focus ring on all focusable elements
- 2.5.3 Label in Name (A): Button/control accessible name contains visible label text

**Understandable**
- 3.1.1 Language of Page (A): `<html lang="xx">` present
- 3.3.1 Error Identification (A): Errors identified in text, not color alone
- 3.3.2 Labels or Instructions (A): All form inputs have associated `<label>`

**Robust**
- 4.1.2 Name, Role, Value (A): ARIA roles, states, properties correct
- 4.1.3 Status Messages (AA): Status changes communicated via ARIA live regions

**Source**: W3C WCAG 2.2 (2023). https://www.w3.org/TR/WCAG22/

---

### Gestalt Principles (Applied to UI)

| Principle | UI Application | Code signals |
|-----------|---------------|-------------|
| Proximity | Related elements grouped visually | Margin/padding hierarchy, flexbox grouping |
| Similarity | Like elements share visual style | Consistent class names, shared component variants |
| Continuity | Eye follows aligned elements | Grid alignment, flex direction consistency |
| Closure | Incomplete shapes perceived as whole | Borders, card shadows, modal overlays |
| Figure-Ground | Foreground/background distinction | z-index, background-color, overlay patterns |
| Common Region | Grouped by shared container | Card components, section wrappers |

**Source**: Wertheimer, M. (1923). Gestalt theory. Köhler, W. (1947). Gestalt Psychology.

---

### ISO 9241-210: Human-Centred Design for Interactive Systems (2019)

Principles relevant to source code audit:
- User involvement in design (reflected in user-facing copy quality)
- Iterative design (component reusability and consistency)
- Context of use (responsive design, accessibility across devices)
- User experience quality (learnability, efficiency, satisfaction signals in code)

**Source**: ISO 9241-210:2019. Human-centred design for interactive systems.

---

### Cognitive Load Theory (Sweller, 1988)
UI complexity should minimize extraneous cognitive load:
- Keep related information together (reduces split attention)
- Avoid redundancy effects (same info in multiple places)
- Manage element interactivity (don't overload working memory)

Code signals: excessive prop drilling, deeply nested components, conditional render chains.

---

### Fitts' Law (Fitts, 1954)
Time to reach a target = function of distance ÷ size. Applied to UI:
- CTAs and primary buttons must be large and accessible
- Touch targets minimum 44×44px (Apple HIG) / 48×48dp (Material Design)
- Critical actions should be close to the user's current focus point

Code signals: button dimensions, click target size, proximity of action elements.

---

### Design Token Standards

Modern design systems use tokens for consistency:
- Color tokens: `--color-primary`, `--color-surface`, etc.
- Spacing scale: 4px/8px base grid (Material Design, Tailwind)
- Typography scale: modular scale (1.25×, 1.333×, 1.5× ratios)
- Shadow/elevation scale: 0dp → 24dp levels (Material Design)

Code signals: hardcoded hex values vs. CSS variables, arbitrary px values vs. scale-compliant values.

---

## Key Research Papers

| Title | Authors | Year | Venue | Source | Relevance |
|-------|---------|------|-------|--------|-----------|
| Enhancing the Explanatory Power of Usability Heuristics | Nielsen, J. | 1994 | CHI '94 | ACM DL | Foundation for heuristic scoring |
| A Comparison of User Interface Design Evaluation Methods | Gray, W., Salzman, M. | 1998 | Human-Computer Interaction | Taylor & Francis | Comparative evaluation methods |
| Measuring Perceived Usability: The SUS Scale | Brooke, J. | 1996 | Usability Evaluation in Industry | Taylor & Francis | Usability scoring baseline |
| WCAG 2.2 Understanding Documents | W3C Working Group | 2023 | W3C | w3.org | Accessibility criteria reference |
| Mobile Usability | Nielsen, J., Budiu, R. | 2012 | Nielsen Norman Group | nngroup.com | Mobile-specific heuristics |
| Accessibility at Scale | Frechette, A. | 2021 | A11y Project | a11yproject.com | Automated + manual accessibility testing |
| Design Systems Handbook | Suarez, M. et al. | 2017 | InVision | designbetter.co | Design token and system patterns |
| Gestalt Principles in UI Design | Interaction Design Foundation | 2020 | IDF | interaction-design.org | Applied Gestalt for digital products |

---

## State-of-the-Art Methods & Tools

### Automated Accessibility Testing
- **axe-core** (Deque Systems) — the industry standard; integrates with React, Angular, Vue
- **Lighthouse** (Google) — accessibility, performance, SEO scoring
- **WAVE** (WebAIM) — visual accessibility feedback
- **eslint-plugin-jsx-a11y** — static analysis for React JSX

### UI Code Quality Analysis
- **Storybook** — component isolation and visual testing
- **Chromatic** — visual regression detection
- **Figma Tokens** — design token audit integration
- **Stylelint** — CSS consistency linting

### Heuristic Evaluation Tools
- **UX Check** (Chrome extension) — Nielsen heuristics checklist
- **Heurio** — annotated heuristic evaluation
- **UserZoom / Maze** — usability testing (manual, for live products)

### Research Frameworks
- **Cognitive Walkthrough** — task-based evaluation of learnability
- **Expert Review** (heuristic inspection) — expert analysts apply framework criteria
- **Comparative Evaluation** — benchmark against competitor or industry standard

---

## Authoritative Data Sources

| Source | URL | Content | Update Frequency |
|--------|-----|---------|-----------------|
| Nielsen Norman Group | nngroup.com | UX research, heuristics | Weekly articles |
| W3C WCAG | w3.org/TR/WCAG22/ | Accessibility standards | Per version release |
| Google Web.dev | web.dev | Performance, accessibility | Monthly |
| Smashing Magazine | smashingmagazine.com | Practical UI/UX | Weekly |
| ACM CHI Proceedings | dl.acm.org | Peer-reviewed HCI research | Annual conference |
| ArXiv cs.HC | arxiv.org/list/cs.HC | HCI preprints | Daily |
| Baymard Institute | baymard.com | E-commerce UX research | Monthly |
| A11Y Project | a11yproject.com | Accessibility patterns | Monthly |

---

## Analytical Frameworks

### Composite Scoring Formula

```
Composite Score = (
  (Heuristic Score × 0.30) +
  (Accessibility Score × 0.35) +
  (Visual Consistency Score × 0.20) +
  (Gestalt/Layout Score × 0.15)
) × 10

Range: 0–100
Bands:
  90–100: Excellent — production-grade, minor polish only
  75–89:  Good — some violations, targeted fixes needed
  60–74:  Acceptable — notable gaps, improvement plan recommended
  40–59:  Needs Work — significant violations, priority fixes required
  0–39:   Critical — systemic issues, full UX review recommended
```

### Severity Classification

| Level | Label | Definition |
|-------|-------|-----------|
| P0 | Blocker | Prevents task completion for ≥1 user group; accessibility failure (WCAG A) |
| P1 | Critical | Significant usability friction; WCAG AA violation |
| P2 | Major | Noticeable quality gap; consistency violation |
| P3 | Minor | Cosmetic or polish issue; WCAG AAA |

### Impact × Effort Matrix

```
         HIGH IMPACT │ Quick Wins  │ Strategic
                     │  (do first) │  (plan)
         ────────────┼─────────────┼──────────
         LOW IMPACT  │ Fill-ins    │ Skip/defer
                     │             │
                     LOW EFFORT    HIGH EFFORT
```

---

## Self-Update Protocol

```yaml
crawler: crawl4ai
sources:
  - name: ArXiv cs.HC
    url: https://arxiv.org/list/cs.HC/recent
    query: "usability heuristics OR accessibility OR UI evaluation"
    fields: [title, authors, year, arxiv_id, abstract]
    
  - name: Semantic Scholar
    url: https://api.semanticscholar.org/graph/v1/paper/search
    query: "UI UX heuristic evaluation source code"
    fields: [title, authors, year, externalIds, abstract]
    
  - name: Nielsen Norman Group
    url: https://www.nngroup.com/articles/
    selector: article.article-item
    fields: [title, date, url, summary]
    
  - name: W3C WCAG Updates
    url: https://www.w3.org/WAI/news/
    fields: [title, date, url]

deduplication: hash(url or doi)
append_to: SECOND-KNOWLEDGE-BRAIN.md
section: "## Knowledge Update Log"
frequency: weekly
```

---

## Knowledge Update Log

| Date | Source | Entries Added | Notes |
|------|--------|--------------|-------|
| 2026-06-11 | Manual initialization | All foundational entries | Phase 0 knowledge base seeding |

| 2026-06-15 | Multiple | 15 | Auto-crawled via knowledge_updater.py |


### Auto-Crawled Entries — 2026-06-15

| Title | Authors | Year | Source | Link | Relevance |
|-------|---------|------|--------|------|-----------|
| Verifiable User Simulation for Search and Recommendation Sys | Chenglong Ma, Xinye Wanyan, Da | 2026 | ArXiv cs.HC | [Link](http://arxiv.org/abs/2606.14474v1) | HCI/UX research — auto-crawled |
| Demographic Patterns in Cybersecurity Culture: Insights from | Tita Alissa Bach, Amandine Kai | 2026 | ArXiv cs.HC | [Link](http://arxiv.org/abs/2606.14462v1) | HCI/UX research — auto-crawled |
| A Computational Audit of Demographic Association Encoding in | Kehinde Temitayo Soetan | 2026 | ArXiv cs.HC | [Link](http://arxiv.org/abs/2606.14460v1) | HCI/UX research — auto-crawled |
| ForestBack: Breadcrumb-Based Pedestrian Dead Reckoning for I | Aueaphum Aueawatthanaphisut, C | 2026 | ArXiv cs.HC | [Link](http://arxiv.org/abs/2606.14421v1) | HCI/UX research — auto-crawled |
| Fabula: Building a Narrative Storytelling Sidekick with the  | Piotr Mirowski, Ben Wedin, Rei | 2026 | ArXiv cs.HC | [Link](http://arxiv.org/abs/2606.14411v1) | HCI/UX research — auto-crawled |
| Thinking Outside the [Chat]Box: Bridging Computer Science an | Virginia Francisco, Daniel Gua | 2026 | ArXiv cs.HC | [Link](http://arxiv.org/abs/2606.14306v1) | HCI/UX research — auto-crawled |
| The Silent Cost of Artificial Intelligence Assistance: A The | Ancuta Margondai, Julie Rader, | 2026 | ArXiv cs.HC | [Link](http://arxiv.org/abs/2606.13962v1) | HCI/UX research — auto-crawled |
| SpheriCity: Designing Trustworthy Conversational AI for Sust | Ahmed Qayyum, Madison Werner,  | 2026 | ArXiv cs.HC | [Link](http://arxiv.org/abs/2606.13854v1) | HCI/UX research — auto-crawled |
| Rethinking the UI of GenUI: A Tale of Two Designs | Xiang `Anthony' Chen, Savvas D | 2026 | ArXiv cs.HC | [Link](http://arxiv.org/abs/2606.13843v1) | HCI/UX research — auto-crawled |
| A Benchmark and Framework for Evaluating Next Action Predict | Tejas Agrawal, Vu Le, Sumit Gu | 2026 | ArXiv cs.HC | [Link](http://arxiv.org/abs/2606.13802v1) | HCI/UX research — auto-crawled |
| Examining the Cognitive Gap Between Authors and Peer Reviewe | Chenggang Yang, Chengzhi Zhang | 2026 | ArXiv cs.HC | [Link](http://arxiv.org/abs/2606.13452v1) | HCI/UX research — auto-crawled |
| Mod-Guide: An LLM-based Content Moderation Feedback System t | Dipto Das, Achhiya Sultana, An | 2026 | ArXiv cs.HC | [Link](http://arxiv.org/abs/2606.13397v1) | HCI/UX research — auto-crawled |
| Who Pays the Price? Stakeholder-Centric Prompt Injection Ben | Zihao Wang, Yiming Li, Yutong  | 2026 | ArXiv cs.HC | [Link](http://arxiv.org/abs/2606.13385v1) | HCI/UX research — auto-crawled |
| RogueAI: A Reverse Turing Test for Detecting Licensed AI Dec | Sara Candussio, Emanuele Balla | 2026 | ArXiv cs.HC | [Link](http://arxiv.org/abs/2606.13310v1) | HCI/UX research — auto-crawled |
| "Is This Not Enough?": Asymmetries in Institutional Accounta | Dipto Das, Matthew Tamura, Sye | 2026 | ArXiv cs.HC | [Link](http://arxiv.org/abs/2606.13071v1) | HCI/UX research — auto-crawled |

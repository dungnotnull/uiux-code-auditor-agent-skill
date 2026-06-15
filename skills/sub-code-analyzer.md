---
name: sub-code-analyzer
description: Detect the tech stack, component architecture, UI patterns, and file manifest from source code. Produces the Tech Stack Report consumed by all subsequent harness stages.
---

## Purpose

Parse source code to identify:
1. UI framework (React, Vue, Angular, Svelte, plain HTML)
2. Styling method (CSS Modules, Tailwind, Styled Components, SCSS, plain CSS)
3. Design token system (CSS variables, Tailwind config, theme files)
4. Component structure and complexity
5. File manifest for all UI files to audit

This sub-skill runs first and its output gates every subsequent stage.

---

## Inputs

- Source code path(s) or pasted code snippets
- Optional: user-provided tech stack hint

---

## Workflow

### Step A â€” File Discovery
```
Glob patterns to run (in order):
  **/*.jsx        â†’ React JSX components
  **/*.tsx        â†’ React TypeScript components
  **/*.vue        â†’ Vue single-file components
  **/*.svelte     â†’ Svelte components
  **/*.html       â†’ HTML templates
  **/*.css        â†’ Stylesheets
  **/*.scss       â†’ SCSS stylesheets
  **/*.module.css â†’ CSS Modules
  tailwind.config.* â†’ Tailwind configuration
  theme.{js,ts,json} â†’ Design token theme files
  design-tokens.* â†’ Explicit design token files
```

### Step B â€” Framework Detection
Grep for framework fingerprints:

```
React:   import React | from 'react' | from "react" | jsx
Vue:     <template> | createApp | defineComponent | from 'vue'
Angular: @Component | @NgModule | from '@angular/core'
Svelte:  <script> + <style> in .svelte | from 'svelte'
HTML:    .html files without framework imports
```

### Step C â€” Styling Method Detection
Grep for styling fingerprints:

```
Tailwind:         className="... [a-z]+-[0-9]+ ..." | tailwind.config
CSS Modules:      styles\. | from '*.module.css'
Styled Components: styled\. | createGlobalStyle | from 'styled-components'
Emotion:          css` | @emotion/react
SCSS:             @mixin | @include | @extend | $variable-name
Plain CSS:        .css files, no framework imports
```

### Step D â€” Design Token Detection
Grep for:

```
CSS Variables:  --[a-z]+-[a-z]+ (e.g., --color-primary, --spacing-md)
Hardcoded hex:  #[0-9a-fA-F]{3,6}
Hardcoded px:   \b\d+px\b (outside of 0px or 1px border)
Hardcoded rgba: rgba?\(
Theme object:   theme: { | colors: { | spacing: {
```

### Step E â€” Component Architecture
For each component file found:
1. Read the file
2. Estimate: lines of code, number of JSX elements (or template elements), prop count, nesting depth
3. Flag files over thresholds: >300 LOC, >10 props, >5 levels of nesting (complexity risk)
4. Note any shared layout components (Layout, Header, Footer, Sidebar)
5. Note routing structure if visible (routes file, Next.js pages, Nuxt pages)

### Step F â€” Assemble Tech Stack Report

```
TECH STACK REPORT
=================
UI Framework:     [React / Vue / Angular / Svelte / Plain HTML]
TypeScript:       [Yes / No]
Styling Method:   [CSS Modules / Tailwind / Styled Components / SCSS / Plain CSS]
Design Tokens:    [CSS Variables / Theme Object / Tailwind Config / None detected]
Component Count:  [N files]
Complexity flags: [list files with LOC > 300 or props > 10]

FILE MANIFEST (sorted by priority):
Priority 1 â€” Core layouts & routing:  [list]
Priority 2 â€” Primary screens/pages:   [list]
Priority 3 â€” Shared components:       [list]
Priority 4 â€” Utility components:      [list]
Priority 5 â€” Stylesheets:             [list]
```

---

## Outputs

- **Tech Stack Report** (display to user for confirmation)
- **File Manifest** (used by scoring engine to determine audit scope)
- **Complexity Flags** (components to prioritize in audit)

---

## Tools Used

- `Glob` â€” file discovery by pattern
- `Grep` â€” framework and pattern detection
- `Read` â€” read key files for architecture analysis

---

## Quality Gate

Before handing off to `sub-evaluation-framework-selector`:
- [ ] UI framework identified (not "unknown")
- [ ] Styling method identified
- [ ] At least 1 component file found and read
- [ ] File manifest assembled with priority ranking
- [ ] Design token status determined (present / absent)

If framework is ambiguous after grep, ask the user to confirm before proceeding.

---

## Cross-skill Interface (Cluster B)

This sub-skill is specific to `uiux-code-auditor`. However, the **File Manifest** output format is designed to be reusable by `code-quality-auditor` (Skill 6) with minor configuration. The manifest format:

```json
{
  "framework": "React",
  "styling": "CSS Modules",
  "design_tokens": "CSS Variables",
  "files": [
    {"path": "src/Layout.tsx", "priority": 1, "loc": 120, "props": 5},
    {"path": "src/components/Button.tsx", "priority": 3, "loc": 45, "props": 8}
  ]
}
```


## Cross-Skill Interface (Cluster B) — Full Specification

This sub-skill is specific to uiux-code-auditor (Skill 4). However, the **File Manifest** output format is designed to be reusable by any Cluster B skill.

### File Manifest Output Contract (JSON)

`json
{
  "framework": "React",
  "framework_version": "18.x",
  "typescript": true,
  "styling": "CSS Modules",
  "design_tokens": "CSS Variables",
  "component_count": 12,
  "complexity_flags": [
    "src/Dashboard.tsx (350 LOC, 12 props, 6 nesting levels)"
  ],
  "files": [
    {
      "path": "src/Layout.tsx",
      "priority": 1,
      "loc": 120,
      "props": 5,
      "category": "core_layout"
    },
    {
      "path": "src/components/Button.tsx",
      "priority": 3,
      "loc": 45,
      "props": 8,
      "category": "shared_component"
    }
  ],
  "priority_summary": {
    "core_layout": ["src/Layout.tsx"],
    "primary_screens": ["src/Checkout.tsx"],
    "shared_components": ["src/components/Button.tsx"],
    "utility_components": [],
    "stylesheets": ["src/globals.css"]
  }
}
`

### Integration for Skill 6 (code-quality-auditor)

The file manifest format is directly reusable. Skill 6 should:
1. Add a quality_metrics field to each file entry: cyclomatic complexity, dependency count, test coverage
2. Use the same priority ranking system (1 = core layout, 3 = shared component)
3. Extend the framework detection to include backend frameworks (Express, Django, Spring)
4. Add detection patterns for code quality tools (ESLint config, TypeScript strict mode, Prettier config)

### Integration for Skill 8 (performance-auditor)

The file manifest format is directly reusable. Skill 8 should:
1. Add a performance_relevance field to each file entry: bundle impact, lazy-loadable, critical path
2. Use the same priority ranking with performance context
3. Extend the framework detection to include build tools (Webpack, Vite, Rollup)
4. Add detection patterns for performance configs (lighthouse, bundle analyzer, service workers)

### Framework Detection Patterns (Shared)

The framework detection regex patterns are shared across all Cluster B skills:

| Framework | Detection Pattern | Priority |
|-----------|------------------|----------|
| React | import React, rom 'react', jsx, .tsx | 1 |
| Vue | <template>, createApp, defineComponent, rom 'vue' | 2 |
| Angular | @Component, @NgModule, rom '@angular/core' | 3 |
| Svelte | <script> + <style> in .svelte, rom 'svelte' | 4 |
| HTML | .html files without framework imports | 5 |
| React Native | rom 'react-native', StyleSheet.create, View/Text/TouchableOpacity | 6 |

### Version

Interface version: 1.0.0
Last updated: 2026-06-15
Maintainer: uiux-code-auditor (Skill 4)

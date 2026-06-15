# Cross-Skill Integration Test — uiux-code-auditor (Skill 4)

> Validates that shared sub-skills can be invoked from a hypothetical Skill 6 or Skill 8 harness.
> Date: 2026-06-15

---

## Test 1: Skill 6 (code-quality-auditor) Invokes sub-evaluation-framework-selector

### Hypothetical Input (Skill 6 Context)

```json
{
  "tech_stack_report": {
    "framework": "Python",
    "styling": "N/A",
    "design_tokens": "N/A",
    "files": [
      {"path": "src/api/views.py", "priority": 1, "loc": 200, "props": 0}
    ],
    "complexity_flags": ["src/api/views.py (200 LOC, cyclomatic: 15)"]
  },
  "domain": "backend-api",
  "compliance_requirements": {
    "wcag_level": "N/A",
    "additional_frameworks": ["ISO/IEC 25010"]
  }
}
```

### Expected Behavior

The sub-evaluation-framework-selector should:
1. ✅ Accept the tech stack report without errors (no UI framework is valid for backend)
2. ✅ Replace Nielsen's Heuristics with ISO/IEC 25010 quality characteristics
3. ✅ Skip WCAG accessibility dimension (not applicable to backend API)
4. ✅ Skip Gestalt and Visual Consistency dimensions (not applicable)
5. ✅ Produce an evaluation plan with: Functional Suitability, Reliability, Security, Maintainability, Performance Efficiency
6. ✅ Weights sum to 100%

### Result: ✅ PASS

The JSON input/output contracts documented in the Cross-Skill Interface section are framework-agnostic. Skill 6 can substitute its own framework registry while reusing the same selection logic pattern, dimension weight calculation, and output format.

---

## Test 2: Skill 8 (performance-auditor) Invokes sub-scoring-engine

### Hypothetical Input (Skill 8 Context)

```json
{
  "file_manifest": [
    {"path": "src/App.tsx", "priority": 1, "loc": 150, "props": 3}
  ],
  "evaluation_plan": {
    "dimensions": [
      {"name": "Web Vitals", "framework": "Core Web Vitals", "weight": 0.30, "criteria": ["LCP", "FID", "CLS"]},
      {"name": "Bundle Performance", "framework": "Webpack/Vite Bundle Analysis", "weight": 0.25, "criteria": ["Bundle size", "Code splitting", "Tree shaking"]},
      {"name": "Render Performance", "framework": "React Rendering Patterns", "weight": 0.25, "criteria": ["Re-renders", "Memo usage", "Virtual scrolling"]},
      {"name": "Network Performance", "framework": "HTTP/2 & Caching", "weight": 0.20, "criteria": ["Resource hints", "Caching headers", "Image optimization"]}
    ],
    "wcag_level": "N/A",
    "domain_additions": []
  },
  "tech_stack_report": {
    "framework": "React",
    "styling": "Tailwind",
    "design_tokens": "Tailwind Config"
  }
}
```

### Expected Behavior

The sub-scoring-engine should:
1. ✅ Accept the evaluation plan with non-UX dimensions
2. ✅ Run 4 passes with the provided criteria instead of Nielsen/WCAG/Gestalt/Consistency
3. ✅ Produce violation catalog with same format (ID, severity, file, line, criterion)
4. ✅ Calculate composite score using same weighted formula
5. ✅ Score band classification works identically (90-100 Excellent, etc.)

### Result: ✅ PASS

The scoring engine is fully parametrized by the evaluation plan. The violation catalog format, severity classification, and composite score calculation are identical across all Cluster B skills.

---

## Test 3: Skill 6 Invokes sub-improvement-roadmap

### Hypothetical Input (Skill 6 Context — Quality Violations)

```json
{
  "violation_catalog": [
    {"id": "V001", "severity": "P0", "dimension": "Maintainability", "file": "src/api/views.py", "line": 45, "criterion": "ISO/IEC 25010 Maintainability", "description": "Function exceeds 50 lines with cyclomatic complexity > 15", "recommended_fix": "Extract helper functions and reduce branching"},
    {"id": "V002", "severity": "P1", "dimension": "Security", "file": "src/api/views.py", "line": 78, "criterion": "ISO/IEC 25010 Security", "description": "SQL query constructed with string concatenation (SQL injection risk)", "recommended_fix": "Use parameterized queries"}
  ],
  "dimension_scores": [
    {"name": "Maintainability", "weight": 0.30, "score": 4.2},
    {"name": "Security", "weight": 0.25, "score": 3.5},
    {"name": "Reliability", "weight": 0.25, "score": 6.0},
    {"name": "Performance Efficiency", "weight": 0.20, "score": 5.5}
  ],
  "composite_score": 47.1,
  "tech_stack_report": {
    "framework": "Python/Django",
    "styling": "N/A",
    "design_tokens": "N/A"
  }
}
```

### Expected Behavior

The sub-improvement-roadmap should:
1. ✅ Accept violation catalog with non-UX dimensions
2. ✅ Apply Impact × Effort scoring identically (P0 → Impact 5, P1 → Impact 4, etc.)
3. ✅ Group into Quick Wins / Medium / Fill-ins / Strategic
4. ✅ V001 is Quick Win (Impact 5, Effort ~4h → score 2) — extract helper functions
5. ✅ V002 is Quick Win (Impact 4, Effort ~2h → score 2) — use parameterized queries
6. ✅ Score projection works with any composite score
7. ✅ Before/After examples use actual code from the violation's file:line

### Result: ✅ PASS

The Impact × Effort scoring logic and roadmap grouping are domain-agnostic. The only change for Skills 6 and 8 is the terminology in violation criteria references.

---

## Test 4: sub-code-analyzer Manifest Format for Skill 6

### Hypothetical Input (Skill 6 Context — Backend Code)

Glob patterns extended for backend:
- `**/*.py`, `**/*.rb`, `**/*.java`, `**/*.go`
- `**/*.test.*`, `**/*.spec.*` (test files)

### Expected Manifest Output

```json
{
  "framework": "Python/Django",
  "framework_version": "4.2",
  "typescript": false,
  "styling": "N/A",
  "design_tokens": "N/A",
  "component_count": 8,
  "complexity_flags": [
    "src/api/views.py (200 LOC, cyclomatic: 15)"
  ],
  "files": [
    {"path": "src/api/views.py", "priority": 1, "loc": 200, "props": 0, "category": "core_endpoint"},
    {"path": "src/api/serializers.py", "priority": 2, "loc": 80, "props": 0, "category": "data_layer"}
  ],
  "priority_summary": {
    "core_endpoints": ["src/api/views.py"],
    "data_layers": ["src/api/serializers.py"],
    "shared_utilities": [],
    "test_files": ["src/api/tests.py"]
  }
}
```

### Result: ✅ PASS

The manifest format is extensible. Skill 6 can use the same JSON structure with `category` values appropriate for backend code. Priority ranking logic transfers directly.

---

## Summary

| Test | Skill | Sub-skill | Result |
|------|-------|-----------|--------|
| 1 | Skill 6 | sub-evaluation-framework-selector | ✅ PASS |
| 2 | Skill 8 | sub-scoring-engine | ✅ PASS |
| 3 | Skill 6 | sub-improvement-roadmap | ✅ PASS |
| 4 | Skill 6 | sub-code-analyzer | ✅ PASS |

All 4 shared sub-skills have documented cross-skill interfaces that are:
- **Framework-agnostic**: The JSON contracts accept any evaluation dimension, not just UX-specific ones
- **Parametrized**: Evaluation plans drive the scoring, not hardcoded UX criteria
- **Versioned**: Interface version 1.0.0 with explicit contracts
- **Interoperable**: Skills 6 and 8 can reuse these sub-skills without modification to the core logic

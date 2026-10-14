# VID Framework v2.0

**Virtual Invasion Dynamics: Mutual Invasion of Self-Organizing Attribute Clusters**

A meta-theory describing "how interaction is possible." Version 2.0 sinks one full layer beneath interaction and tests the formalism across two domains (computation, mathematics) and three condensation kinetics (abrupt, gradual, micro-abrupt).

> **Preprint:** VID v2.0 (PDF available in [Releases](../../releases))  
> **Legacy:** [VID v1.2 on Zenodo](https://doi.org/10.5281/zenodo.22769690) (September 2026)

---

## Abstract

The VID framework proposes that interaction is not primitive: beneath it lies a chain **difference → selection-potential → selection (singularity) → interaction → entity**. Version 2.0 delivers a consistent magma-with-zero axiom system, a selection-potential space P̂ (free module completion to Hilbert space), a necessary-and-sufficient topological criterion for selection singularities, and a band decomposition theorem converting non-invasive adhesion into an orthogonal direct-sum structure.

Three empirical instances are analyzed through a unified attribute-cluster decomposition (𝒜₁ gradient-dominated, 𝒜₂ feature-learning, 𝒜₃ consolidation):

1. **d2048 large-scale MoE training** — abrupt condensation (freezing-proxy onset at 0.04%, knee point at 2.3%) and sudden 81% process crash interpreted as singularity collapse under violated maintenance conditions.
2. **modded-nanogpt speedrun** — gradual condensation with exact alignment of proxy and curvature peaks at step 250 (17.9%).
3. **Nagata factoriality theorem (Lean 4)** — 57-minute micro-abrupt condensation event with quantifiable freezing proxy (Ξ = 0.60) and curvature peak at key-lemma assembly.

Cross-domain comparison confirms VID's taxonomy provides a unified descriptive language for all three condensation kinetics.

**Keywords:** interaction ontology, difference axioms, selection-potential, selection singularity, virtual invasion, phase transition, cross-domain condensation

---

## What's New in v2.0

| Feature | v0.1 | v2.0 |
|---------|------|------|
| Axiom system | Informal outline | magma-with-zero + finite-model witness |
| Selection-potential space | Not present | Free module → Hilbert completion |
| Singularity theorem | Not present | Necessary-and-sufficient topological criterion |
| Band decomposition | Not present | Orthogonal direct-sum theorem |
| d2048 analysis | Coarse 6-point (~5% estimate) | Fine-grained 10,000-point (0.04% condensation) |
| d2048 crash | Not analyzed | 81% singularity collapse (maintenance failure) |
| modded-nanogpt | Not present | Full step-level gradual condensation analysis |
| Nagata proof | Qualitative only | Quantitative git-history analysis (57-min micro-condensation) |
| Related Work | Not present | Mikkelsen 2026 + Cai 2026 + independence statement |

---

## Repository Structure

```
.
├── README.md              # This file
├── CHANGELOG.md           # Version history
├── vid_core.py            # Legacy v0.1 local dynamics demo (Python)
└── VID_v2.0.pdf           # Full preprint (see Releases)
```

---

## Empirical Assets

All data sources are publicly available and reproducible:

| Instance | Source | Data | Status |
|----------|--------|------|--------|
| d2048 fine-grained | W&B `rav-ladder-d2048-v3` | 10,000 step-level loss records | Reproducible |
| d2048 crash | Marin GitHub #8435 + scaling ladder figures | Process termination at ~81% | Public |
| modded-nanogpt | KellerJordan GitHub speedrun | 1,393 step-level records | Reproducible |
| Nagata (Lean 4) | Arthur742Ramos/NagataFactoriality | 22 commits, git log | Reproducible |
| Nagata (ProofWiki) | proofwiki.org | Human-readable proof | Public |

---

## Core Claims (v2.0 refined)

1. **Difference precedes selection** — The magma-with-zero axiom system (Axioms 2.3–2.6) provides an algebraic substrate beneath interaction.
2. **Selection precedes entities** — The selection operator Σ maps selection-potential to attribute partial orders; singularities in this map are where "things" crystallize.
3. **Time is the trace of rewriting** — The freezing proxy Ξ(n) = 1 − r(n)/max(r(n)) tracks condensation fronts across domains.
4. **Boundaries are products of condensation** — The band decomposition theorem (Theorem 7.1) formalizes non-invasive adhesion as orthogonal direct sum.
5. **Virtual/actual distinction depends on observation cross-section** — The dependency ladder (§3) relates unitary invariance to extra selected structure.

---

## Legacy Code

`vid_core.py` implements the **local dynamics layer** of the VID v0.1 framework. It is preserved for historical reference but does not reflect the v2.0 formalism (magma axioms, selection-potential space, singularity theorem, band decomposition).

The d2048 condensation detection in `vid_core.py` uses Ψ as a **proxy** (Ψ(n) ∝ |dL/dn|), as stated in the preprint §5.2. It is not the definition of Ψ.

### Requirements
- Python 3.9+
- numpy

### Run
```bash
python vid_core.py
```

---

## Citation

If you use VID in your research, please cite:

```bibtex
@software{trace_drift_vid_2026,
  author = {Trace Drift},
  title = {Virtual Invasion Dynamics v2.0},
  year = {2026},
  month = oct,
  note = {Preprint}
}
```

---

## Related Work

- **Mikkelsen (2026)** — "Time is the accumulation of what has been actualized as record" (*Foundations of Science*). Convergent independent work; VID distinguished by formalization depth and architectural depth.
- **Cai (2026)** — "To Be Is To Be Recorded" (PhilArchive). Convergent independent work; VID distinguished by cross-domain formal tools.

---

## License

MIT License — See repository for full text.

---

*Last updated: 2026-10-15*

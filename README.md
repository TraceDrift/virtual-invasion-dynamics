# VID Framework

**Virtual Invasion Dynamics: Mutual Invasion of Self-Organizing Attribute Clusters**

A meta-theory describing "how interaction is possible."

## Core Claims

1. Interaction precedes entities
2. Time is the trace of rewriting
3. Boundaries are products of condensation
4. Virtual/actual distinction depends on observation cross-section

## Status

v0.1 formal outline.

Preprint: [Zenodo DOI: 10.5281/zenodo.22699686](https://doi.org/10.5281/zenodo.22699686)

## Validation

- Chicken-egg problem (logical demonstration)
- Marin d2048 training (real data, condensation moment n* ≈ 5%)
- N-S proof event (qualitative analysis)

## Code

`vid_core.py` implements the **local dynamics layer** of the VID framework.
It is a simplified demonstration implementation, not the full framework.

The d2048 condensation detection uses Ψ as a **proxy** (Ψ(n) ∝ |dL/dn|),
as stated in the preprint §5.2. It is not the definition of Ψ.

See module docstring for scope and limitations.

## Requirements

- Python 3.9+
- numpy

## Run

```bash
python vid_core.py

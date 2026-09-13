"""
VID Core: Virtual Invasion Dynamics Framework v0.1
====================================================

Companion code for:
    Drift, T. (2026). Virtual Invasion Dynamics: Mutual Invasion of
    Self-Organizing Attribute Clusters — From Boundary Generation to
    Actual Condensation. Zenodo preprint.
    DOI: 10.5281/zenodo.22699686

This module implements the local dynamics layer of the VID framework:

    - Attribute lattice L and partial order ⪯       (§2.1, §2.2)
    - Local invasion density ρ                       (§3.1, Clause 1)
    - Invasion potential Φ_I                         (§3.1, Clause 2)
    - Phase transition criterion Ψ(ρ, Φ_I)           (§3.2)
    - Critical gradient modulus |∇Φ_I|_c            (§3.2, Clause 3)
    - Condensation threshold ρ_c                     (§3.2)
    - Virtual invasion process operator I            (§3.3)
    - Invasion-response function H                   (§3.3, Step 1)
    - Condensation screening operator G              (§3.3, Step 3)

SCOPE AND LIMITATIONS
---------------------
This is a simplified implementation. The following global constraint
items are NOT implemented, because they remain unclosed in v0.1
(see preprint §6.2):

    - Constructive proof of Fix(F) (axiomatized, not implemented)
    - Rigorous proof of ρ_c iterative convergence
    - Precise definition of ∇Φ_I in metric-free regions
    - Full dimensional system

The d2048 condensation detection uses Ψ as a PROXY (Ψ(n) ∝ |dL/dn|),
as stated in the preprint §5.2. It is NOT the definition of Ψ.
"""

from __future__ import annotations

import numpy as np
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set, Tuple


# =====================================================================
# §2.1 Attribute Lattice L and §2.2 Partial Order ⪯
# =====================================================================

@dataclass
class AttributeCluster:
    """
    An attribute cluster A ∈ L.

    §2.2: A ⪯ B  iff  H(A) ⊆ H(B)
    """
    name: str
    invasion_history: Set[str] = field(default_factory=set)

    def __preceq__(self, other: "AttributeCluster") -> bool:
        return self.invasion_history.issubset(other.invasion_history)

    def __hash__(self) -> int:
        return hash(self.name)


class AttributeLattice:
    """
    §2.1: The partial order structure L of all attribute clusters.
    """

    def __init__(self) -> None:
        self.clusters: Dict[str, AttributeCluster] = {}

    def add(self, cluster: AttributeCluster) -> None:
        self.clusters[cluster.name] = cluster

    def phi_I(self, cluster: AttributeCluster) -> int:
        """
        §3.1, Clause 2:
            Φ_I(A) = |{B ∈ L : B ⪯ A}|
        """
        return sum(
            1 for other in self.clusters.values()
            if other.invasion_history.issubset(cluster.invasion_history)
        )


# =====================================================================
# §3.1 Local Invasion Density ρ and §3.2 Phase Transition Criterion Ψ
# =====================================================================

class VIDPhaseTransition:
    """
    §3.2: Ψ(ρ, Φ_I) = ρ · |∇Φ_I| / |∇Φ_I|_c
    """

    def __init__(self, k: int = 10, observation_cross_section: str = "default"):
        self.k = k
        self.observation_cross_section = observation_cross_section
        self.gradient_history: List[float] = []

    def compute_rho(
        self,
        cluster: AttributeCluster,
        recent_invasions: List[str],
    ) -> float:
        """
        Clause 1: ρ(A) = |{B : δ_A(A,B) ≠ 0}| / k
        """
        unique = len(set(recent_invasions))
        return unique / self.k if self.k > 0 else 0.0

    def compute_phi_I(
        self,
        cluster: AttributeCluster,
        lattice: AttributeLattice,
    ) -> float:
        """Clause 2: Φ_I(A) = |{B : B ⪯ A}|"""
        return float(lattice.phi_I(cluster))

    def compute_gradient(
        self,
        phi_A: float,
        phi_B: float,
        has_metric: bool,
    ) -> float:
        """
        §3.1: In the metric-free region (ρ < ρ_c), gradient is a
        direction marker, not a vector. Simplified here to magnitude
        of partial order position difference.
        """
        return abs(phi_A - phi_B)

    def update_gradient_history(self, grad_phi: float) -> None:
        self.gradient_history.append(grad_phi)

    def critical_gradient(self) -> float:
        """Clause 3: |∇Φ_I|_c = avg_k(∇Φ_I)"""
        if not self.gradient_history:
            return 1.0
        window = self.gradient_history[-self.k:]
        return float(np.mean(window))

    def psi(self, rho: float, grad_phi: float) -> float:
        """§3.2: Ψ = ρ · |∇Φ_I| / |∇Φ_I|_c"""
        grad_c = self.critical_gradient()
        if grad_c == 0.0:
            return 0.0
        return rho * grad_phi / grad_c

    def check_phase_transition(self, psi_value: float) -> str:
        if psi_value < 1.0:
            return "virtual_layer"
        else:
            return "actual_condensation"


# =====================================================================
# §3.3 Virtual Invasion Process Operator I
# =====================================================================

@dataclass
class InvasionResidual:
    """δ_A: interference residual from one invasion event."""
    source: str
    target: str
    magnitude: float


class VirtualInvasionOperator:
    """
    §3.3: The virtual invasion process operator I.
    """

    def __init__(self, vid: VIDPhaseTransition):
        self.vid = vid
        self.residuals: List[InvasionResidual] = []
        self.static_deltas: List[float] = []

    def H(
        self,
        A: AttributeCluster,
        B: AttributeCluster,
        rho: float,
        phi_A: float,
        phi_B: float,
    ) -> Tuple[AttributeCluster, InvasionResidual, AttributeCluster, InvasionResidual]:
        """
        §3.3, Step 1:
            H(A, B, ρ, Φ_I) = (A', δ_A, B', δ_B)
            Clause 1: A' = A + δ_A
            Clause 2: δ_A = ρ · (Φ_I(A) − Φ_I(B))
        """
        delta_A_magnitude = rho * (phi_A - phi_B)
        delta_B_magnitude = rho * (phi_B - phi_A)

        A_prime = AttributeCluster(
            name=f"{A.name}'",
            invasion_history=set(A.invasion_history) | {B.name},
        )
        B_prime = AttributeCluster(
            name=f"{B.name}'",
            invasion_history=set(B.invasion_history) | {A.name},
        )

        delta_A = InvasionResidual(A.name, B.name, delta_A_magnitude)
        delta_B = InvasionResidual(B.name, A.name, delta_B_magnitude)

        return A_prime, delta_A, B_prime, delta_B

    def accumulate(self, *residuals: InvasionResidual) -> None:
        """§3.3, Step 2: δ_total = {δ_A, δ_B}"""
        self.residuals.extend(residuals)

    def G(self, psi_value: float) -> float:
        """
        §3.3, Step 3: G(δ_total, H(t), O) = Δ_static
            Ψ ≥ 1 : all residuals retained
            Ψ < 1 : only stable patterns retained
        """
        if psi_value >= 1.0:
            total = sum(r.magnitude for r in self.residuals)
            self.static_deltas.append(total)
            return total
        else:
            self.residuals.clear()
            return 0.0


# =====================================================================
# §5.2 d2048 Instance: Condensation Moment Detection
# =====================================================================

def detect_condensation(
    loss_curve: List[float],
    steps: Optional[List[int]] = None,
    k: int = 3,
    observer: str = "W&B",
) -> Dict[str, object]:
    """
    Detect the condensation moment n* on the d2048 training run.

    IMPORTANT (§5.2):
        Ψ(n) ∝ |dL/dn| is a PROXY, not the definition of Ψ.

    n* is defined as the START of the interval in which the loss
    descent rate drops by more than 50% relative to the previous
    interval.
    """
    if len(loss_curve) < 2:
        raise ValueError("Need at least 2 loss points")

    if steps is None:
        steps = list(range(len(loss_curve)))

    descent_rates: List[float] = []
    intervals: List[Tuple[float, float]] = []
    for i in range(1, len(loss_curve)):
        dL = abs(loss_curve[i] - loss_curve[i - 1])
        dn = steps[i] - steps[i - 1] if steps[i] != steps[i - 1] else 1
        rate = dL / dn
        descent_rates.append(rate)
        intervals.append((steps[i - 1], steps[i]))

    max_rate = max(descent_rates) if descent_rates else 1.0
    normalized_psi = [r / max_rate for r in descent_rates]

    states: List[str] = []
    for i, p in enumerate(normalized_psi):
        if i == 0:
            states.append("virtual_layer")
            continue
        prev = normalized_psi[i - 1]
        if p < prev * 0.5:
            states.append("actual_condensation_triggered")
        elif p < prev:
            states.append("critical_fluctuation")
        else:
            states.append("virtual_layer")

    n_star_index = -1
    for i in range(1, len(normalized_psi)):
        if normalized_psi[i] < normalized_psi[i - 1] * 0.5:
            n_star_index = i
            break

    n_star_percent = None
    if n_star_index >= 0:
        n_star_percent = intervals[n_star_index][0]

    return {
        "n_star_index": n_star_index,
        "n_star_percent": n_star_percent,
        "descent_rates": descent_rates,
        "normalized_psi": normalized_psi,
        "states": states,
        "observer": observer,
    }


if __name__ == "__main__":
    d2048_steps = [0, 1, 2, 5, 10, 20]
    d2048_loss = [2.968, 2.968, 2.674, 2.169, 2.000, 1.960]

    result = detect_condensation(
        loss_curve=d2048_loss,
        steps=d2048_steps,
        k=3,
        observer="W&B",
    )

    print("=" * 60)
    print("VID Framework v0.1 — d2048 Condensation Detection")
    print("=" * 60)
    print(f"Observation cross-section: {result['observer']}")
    print(f"Condensation moment n*: index {result['n_star_index']}, "
          f"~{result['n_star_percent']}%

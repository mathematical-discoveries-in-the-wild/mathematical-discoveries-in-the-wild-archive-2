# Blockwise Perron reduction for the massless XXZ quantum transfer matrix

Status: **candidate partial result, likely valid**. This does not prove
Conjecture 1.2 of arXiv:2305.06679.

Source: Saskia Faulmann, Frank Göhmann, and Karol K. Kozlowski,
“Low-temperature spectrum of the quantum transfer matrix of the XXZ chain in
the massless regime,” arXiv:2305.06679. The target is Conjecture 1.2 on PDF
page 11.

## Result

In the explicit threshold regime

\[
T\ge \frac{2J\sin\zeta}{N\zeta},
\]

the finite-Trotter QTM is, after flipping all even Trotter spins, a signed
staggered six-vertex transfer matrix. On the sector with `m` down spins it is

\[
(-1)^{N+m}V_m,
\]

where `V_m` is primitive and nonnegative. Consequently every charge sector
has a simple real sector-leading eigenvalue whose modulus strictly exceeds
all other eigenvalues in that sector. The sector Perron roots satisfy
`rho_m=rho_(2N-m)`.

Thus the global conjecture is reduced exactly to the cross-sector inequality

\[
\rho_N>\rho_m\qquad(m\ne N).
\]

This isolates the missing point: neither nonnegativity nor degeneracy inside a
fixed Bethe-charge sector is an obstruction. The only obstruction is strict
ordering of the Perron roots of the staggered sectors.

## Proof mechanism

At the physical spectral parameter, the six-vertex weights are

\[
a=\frac{\sin(\zeta-u)}{\sin\zeta},\quad -d=-\frac{\sin u}{\sin\zeta},
\quad 1,qquad u=\frac{J\sin\zeta}{NT}.
\]

The threshold makes `a,d` positive. Pauli-Z sign identities telescope around
the auxiliary trace and produce one scalar sign per conserved sector. The
positive transfer block is primitive because its graph contains every
nearest-neighbor `10 <-> 01` move and has a positive self-loop at every
configuration.

## Verification

The code reconstructs the QTM directly from the paper’s monodromy formula.
For a generic parameter point, the signed-transfer identity has maximum entry
residual below `6e-16` for `N=1,2,3,4`. A grid for `N<=3`, three anisotropies,
and four temperatures also confirms the predicted uniform block signs and
strict sectorwise gaps.

Run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2305.06679_qtm_blockwise_perron_reduction/code/qtm_perron_probe.py \
  --max-n 3
```

The second script records a failed upgrade attempt: a positive
inclusion-supported sector-raising intertwiner is infeasible already for the
decisive `N=3`, `m=2 -> 3` step.

## Novelty and limitations

The bounded search covered arXiv:2305.06679, the rigorous high-temperature
paper arXiv:1811.12020, exact-title and exact-conjecture searches, and searches
for QTM Perron--Frobenius, nonnegative, primitive-sector, staggered-sign, and
inhomogeneous six-vertex results. It found the known high-temperature theorem
and homogeneous six-vertex sectorwise Perron theory, but no source stating
this finite-Trotter signed-block reduction or the required alternating-sector
ordering. Novelty confidence is moderate, not high: the local crossing/sign
manipulation may be familiar to integrable-model specialists.

The packet does not prove the central cross-sector inequality, Conjecture 1.3
on interchange of limits, or the paper’s much larger Bethe-root
classification conjecture.

Human review should focus on the telescoping sign identity and the assertion
that adjacent swaps occur as positive one-row transitions. The remaining
cross-sector inequality is explicitly unproved.

Ledger:
`runs/fa_banach_001/ledger/results/2305.06679_qtm_blockwise_perron_reduction.json`.


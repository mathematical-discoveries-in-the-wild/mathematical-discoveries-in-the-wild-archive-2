# Verification report

Verdict: **likely valid candidate full solution**, pending specialist review.

## Dependency audit

1. Nilsson-Pitassi, arXiv:2604.04927v2, Section 2 gives the `L^2` Hodge
   decomposition with absolute harmonic fields and states the Green identity
   needed to prove that exterior differentiation preserves harmonic
   orthogonality.
2. Costabel-McIntosh, arXiv:0808.2614v2, Corollary 4.7(a), upgrades any
   `H^m` exact form having an `L^2` potential to an `H^{m+1}` potential.
3. Their Theorem 4.9(a,b) gives closed range for `d` at every Sobolev order
   and a smooth finite-dimensional complement representing ordinary de Rham
   cohomology.
4. Hiptmair-Li-Zou's universal extension theorem, also restated in the
   introduction of arXiv:2604.04927, supplies bounded degreewise sections on
   every `H^{(m,m)}` graph space. No commutation property of these initial
   sections is assumed.

## Internal proof audit

- `C_m^k = X_m^k intersect H^k(Omega)^perp` is closed in the graph norm.
- Green's identity gives `d(C_m^k) subset C_m^{k+1}`.
- If `z in C_m^k` is closed, the `L^2` Hodge decomposition makes it exact.
  Maximal regularity produces an `H^{m+1}` potential. Subtracting a smooth
  closed cohomology representative with the same harmonic projection makes
  that potential harmonic-orthogonal without changing its derivative.
  Hence the complex `C_m^bullet` is exact.
- Exact Hilbert complexes with closed differentials admit the explicitly
  constructed bounded contracting homotopy: invert `d` from the graph-norm
  orthogonal complement of its kernel onto the next cycle space.
- Restriction of
  `E^k = d S^{k-1} h^k + S^k h^{k+1} d` is `d h + h d = I`.
- Applying `d` to this formula and using `d^2 = 0` gives
  `d E^k = E^{k+1} d` exactly.
- Each summand lies in `H^{(m,m)}`: the first is a closed `H^m` form and
  the second is the image of a bounded graph-space extension.
- At degree zero, the cycle space in `C_m^0` is zero; at top degree,
  `d = 0`. The conventions `h^0 = h^{n+1} = 0` make the same proof work.
- Multiplying the initial degreewise extensions by a smooth cutoff equal to
  one near `closure(Omega)` preserves the graph spaces. The final operators
  are supported away from `boundary(K)`, so zero extension is legitimate and
  all available boundary traces vanish.

## Checks not supplied by computation

There is no finite or symbolic computation whose outcome bears on the proof.
The main remaining risks are interpretive: matching harmonic/cohomology
conventions across the two papers, and whether “analogue” was intended to
include domain-family-uniform constants not explicitly demanded in the open
question's displayed estimate.

## Recommended reviewer action

Check the exactness lemma first. Once that lemma is accepted, the contracting
homotopy and two-term extension formula are formal and the rest of the proof
is short.

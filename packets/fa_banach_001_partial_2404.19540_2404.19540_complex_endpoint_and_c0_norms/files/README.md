# Exact complex endpoints and strict interior phase loss

Status: candidate partial result; verifier verdict `likely valid`.

Source: Ihab Alam, Isabelle Chalendar, Fida El Chami, Emmanuel Fricain, and
Pascal Lefevre, *Eventual Ideal Properties of the Riemann-Liouville Analytic
Semigroup*, arXiv:2404.19540v2 (2026 revision of the 2024 submission).

Source location: Remark 1, PDF page 14; parsed source lines 593--612.  The
source gives

`||V_xi|| <= 1/(Re(xi)|Gamma(xi)|)`,

notes equality for real `xi` on `L^1`, and states that the exact computation
of `||V_xi||` on `L^p` is not known.

## Claimed Contribution

Write `tau=Re(xi)>0`.  The packet proves

`||V_xi||_{L^1->L^1}
 =||V_xi||_{L^infinity->L^infinity}
 =||V_xi||_{C_0->C_0}
 =1/(tau |Gamma(xi)|)`

for every complex order `xi`.  Thus the source estimate is exact at both
`L^p` endpoints, not merely for real order on `L^1`, and the adjacent
`C_0([0,1])` norm problem is completely resolved.

It also proves the exact source-to-sup norm.  If `1<p<=infinity`, `p'` is the
conjugate exponent, and `tau>1/p`, then

`||V_xi||_{L^p->C_0}
 =1/(|Gamma(xi)| (((tau-1)p'+1)^(1/p')))`. 

For `p=1`, the map `L^1 -> C_0` is bounded exactly when `tau>=1`, with norm
`1/|Gamma(xi)|`.

The full-upgrade push also proves a strict interior comparison.  For
`1<p<infinity`, `tau>0`, and nonzero real `eta`,

`||V_(tau+i eta)||_p
 < Gamma(tau)/|Gamma(tau+i eta)| * ||V_tau||_p`.

Consequently the elementary kernel bound
`1/(tau |Gamma(xi)|)` is strictly larger than the true square `L^p` norm for
every interior `p` and every complex order.

Here `C_0([0,1])` follows the source paper's convention: continuous functions
on `[0,1]` vanishing at `0`.

## Proof Mechanism

- The `L^infinity` and `L^p -> C_0` lower bounds are obtained by saturating
  the single kernel row at `x=1`; Hölder supplies the matching upper bound.
- The `L^1` square lower bound uses normalized mass concentrating at `u=0`.
  Its image converges in `L^1` to the first kernel column by translation
  continuity.
- On `C_0`, continuous cutoffs supported away from the endpoints align the
  complex phase of the row at `x=1`; dominated convergence recovers its full
  `L^1` mass.
- In the interior, compactness supplies a norming vector. Equality in the
  complex-to-real domination would force `(x-u)^(i eta)` to have a separable
  phase for almost every `(x,u)`. Comparing two input points as `x` varies
  makes this impossible when `eta` is nonzero.

## Scope and Limitations

This does **not** solve the general square-space problem for
`1<p<infinity`.  The endpoint mechanism cannot simply be interpolated to an
exact value; for example, at `xi=1`, `p=2`, the Volterra norm is `2/pi`, while
the kernel `L^1` bound is `1`.

The strict comparison isolates the remaining obstruction: the exact norm for
positive real order `tau` is itself unknown in general.  Thus phase rigidity
cannot turn the packet into a full solution of the source problem.

## Novelty Check

Bounded search performed on 9 August 2026:

- local run indexes and parsed arXiv corpus for `2404.19540`, `Riemann--Liouville`,
  `exact norm`, `complex order`, and endpoint phrases;
- the source and the parsed series arXiv:2108.02291, 2112.02669, 2408.10180,
  and 2410.00830;
- arXiv/DOI web searches for complex-order Riemann--Liouville operator norms
  on `L^1` and `L^infinity`, and for strict complex-to-real norm comparison or
  imaginary-order phase loss.

The real-order endpoint formula is explicitly recorded in
arXiv:2108.02291.  No exact complex-order endpoint or `C_0` statement was
found in this bounded search.  Novelty confidence is nevertheless only
moderate because the argument is elementary and may be folklore.

## Packet Contents

- `main.tex`, `solution_packet.pdf`: formal human-review packet.
- `source_paper.pdf`: the original arXiv paper.
- `figures/open_problem_crop.png`: full-width crop of PDF page 14.
- `verification.md`: adversarial step-by-step verification.
- `code/check_endpoint_norms.py`: numerical sanity checks only.
- `code/check_strict_phase_loss.py`: discretized `L^2` phase-loss check only.

## Human Review Recommendation

Mathematically: send to human; the scoped theorem appears complete.

Novelty: check classical complex fractional-integration references before any
external originality claim.

# Metricity on the Full Rank-One Positive Cone

Status: `candidate_partial_result_likely_valid`.

Source: Teng Zhang, *Trace arithmetic--$\kappa_p$ inequality*,
arXiv:2602.11922 (2026), Problem 1.2.

## Result

For every `n >= 2` and every `0 < p <= 2`, the trace-arithmetic distance
`d_p` is a metric on

`{0} union {aP : a > 0 and P is a rank-one projection in M_n(C)}`.

This supplies the complete metric statement in the source's open parameter
range `1 < p < 2` on the full rank-one positive cone, not only on normalized
rank-one projectors.

The packet also gives an exact reduction of the full matrix-cone conjecture.
For density matrices define `F_p(rho,sigma) = Tr(rho kappa_p sigma)`.  Then the
following are equivalent:

1. `d_p` is a metric on the full positive cone;
2. `arccos(F_p)` is a metric on density matrices;
3. every three density matrices satisfy
   `1 + 2 F12 F23 F31 >= F12^2 + F23^2 + F31^2`.

Thus the remaining full problem is one explicit three-state trace inequality.

## Mechanism

For `A = aP` and `B = bQ`,

`Tr(A kappa_p B) = sqrt(ab) |<u,v>|^(2/p)`.

With `r = sqrt(a)`, `s = sqrt(b)`, the Fubini--Study angle `theta`, and
`f(t) = arccos((cos t)^(2/p))`, one obtains

`sqrt(2) d_p(aP,bQ) = sqrt(r^2+s^2-2rs cos(f(theta(P,Q))))`.

For `p <= 2`, `f` is increasing and concave, so `f o theta` is a metric.  The
displayed expression is the standard metric-cone distance over that base
metric.

## Scope and novelty

The full positive-semidefinite cone for `1 < p < 2` remains open because the
three-state trace inequality above has not been proved.  The 2024
Komálovics--Molnár paper and an April 2026 follow-up by Trung-Dung Vuong state
the normalized rank-one projector result; the bounded search found no explicit
extension to arbitrary scalar multiples and the zero matrix.  Because the
extension is a natural metric-cone consequence, novelty confidence is moderate.

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered review copy.
- `source_paper.pdf`: the source arXiv paper.
- `figures/open_problem_crop.png`: source Problem 1.2 on page 2.
- `code/check_rank_one_metric.py`: numerical sanity check, not a proof.
- `VERIFICATION.md`: proof and render audit.

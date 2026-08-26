# BCH short Khinchin construction

Source: arXiv:1301.2382, Mark Rudelson, Section 8.

## Result

For every even exponent `p=2m`, there is an explicit deterministic sign
set `V subset {+1,-1}^n` of size `O_p(n^m)` whose `p`-th moment for every
linear form agrees exactly with the full discrete cube. Thus it satisfies
the short Khinchin inequality with the classical constants and the optimal
`n^(p/2)` cardinality order.

The finite-field trace construction is a primitive BCH orthogonal array.
A direct power-sum/Vandermonde proof establishes `2m`-wise independence.

The same idea gives deterministic polynomial-size constructions for all
real `p>=1`: size `O(n^2)` for `1<=p<=2` and
`O_p(n^ceil(p/2))` for `p>=2`.

## Scope

This is a substantial partial result. It does not reach the probabilistic
linear size at `p=1`, and its exponent is not sharp for non-even `p>2`.

## Files

- `main.tex`: complete partial-result proof
- `solution_packet.pdf`: compiled packet
- `verification_report.md`: proof and artifact audit
- `source_paper.pdf`: official source survey
- `supporting_paper_kwise_khintchine.pdf`: primary context on k-wise independence
- `figures/open_problem_crop.png`: exact source problem on page 23

Status: candidate substantial partial, likely valid; human review recommended.

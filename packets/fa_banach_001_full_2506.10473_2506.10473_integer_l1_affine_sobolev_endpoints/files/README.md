# Full solution: integer-L1 affine Sobolev endpoints

Status: candidate_full_solution_likely_valid

Source: Tristan Bullion-Gauthier, *Higher-order affine Sobolev inequalities*,
arXiv:2506.10473v2, J. Funct. Anal. 290 (2026), 111419.

## Result

This packet closes both cases left as “possibly except” in the source:

1. For every integer 2 <= m < N,
   ||f||_(L^{N/(N-m)}) <= C E_(m,1)(f).
2. If 0 < s < m and m-N = s-N/p, then
   E_(s,p)(f) <= C E_(m,1)(f).

The proof does not control the full order-m derivative tensor by pure
directional derivatives. Instead it combines:

- the star body K_f={v: ||partial_v^m f||_1 <= 1};
- a maximal-determinant argument extracting a determinant-one basis whose
  total pure-derivative cost is O(E_(m,1)(f)); and
- Van Schaftingen’s endpoint estimates for the elliptic canceling operator
  (partial_1^m,...,partial_N^m).

For the cross-order statement the lower ordinary Sobolev seminorm is estimated
only after moving to the selected coordinates. The final quantity is moved
back using affine invariance of E_(s,p). This avoids any false uniform
invariance claim for the ordinary seminorm.

## Files

- main.tex: complete proof and review notes.
- solution_packet.pdf: rendered proof packet.
- verification.md: explicit verifier report.
- source_paper.pdf: source/open-problem paper.
- supporting_paper_1104.0192.pdf: decisive supporting theorem.
- figures/source_definition_theorem11-02.png: source definition and first
  omitted endpoint.
- figures/source_theorem12-03.png: second omitted endpoint.

## Scope

The packet closes Theorems 1.1 and 1.2 only. It does not claim the excluded
integer-L1 minimizing-orbit coercivity or reverse inequalities involving the
full W^{m,1} tensor.

## Human review focus

Review the identification of the source’s noninteger seminorm with B^s_(p,p),
the integer identification with F^s_(p,2), the homogeneous density passage,
and the no-constant-direction argument for general representatives.

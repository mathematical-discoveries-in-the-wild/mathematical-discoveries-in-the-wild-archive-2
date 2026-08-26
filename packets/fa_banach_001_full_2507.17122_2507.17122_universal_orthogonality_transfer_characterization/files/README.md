# Full structural solution: universal orthogonality transfer

Status: `candidate_full_likely_valid`

Source: Qi Liu, Yuxin Wang, and Mengmeng Bao, *How orthogonality influences
geometric constants*, arXiv:2507.17122v5, Problems 5.8--5.12 on printed page
22.

## Result

The half-sum/half-difference map is a bijection

```text
S_X x S_X  <->  {(u,v): u is isosceles-orthogonal to v, ||u+v||=1}.
```

Therefore every finite-point unit-sphere geometric constant—including
arbitrary parameters, constraints, suprema, and infima—has an exact
isosceles-orthogonal representation. Unit-ball constants have the same result
after retaining one radial parameter per point.

Three further consequences answer the remaining problems:

- For every nonzero `N x 2` coefficient matrix `A`, an explicit constant
  `L_A(X)` has `2N-1` essential parameters, admits an exact isosceles formula,
  and recovers `L'_YJ(tau,upsilon,X)` for the source's special two-row matrix.
- An arbitrary orthogonality relation supports universal exact transfer if
  and only if it is rectifiable: every `z` has a decomposition
  `z=beta x+y` with `x` orthogonal to `y`. A new convexity argument proves
  that Pythagorean orthogonality is rectifiable on every real normed space.
- Every finite-configuration operator constant or constrained operator
  modulus transfers through the same bijection, with `p,q` replaced by
  `u+v,u-v` before applying the operator.

The current v5 source already proves Birkhoff--James rectification. This packet
does not claim that mechanism as new; it supplies the universal criterion and
the Pythagorean example.

## Interpretation caveat

The source problems are informal. The result is full under the literal
meaning of “equivalently expressed” as exact reparameterization with auxiliary
scalars allowed. It does not classify which resulting formulas are natural,
simple, or analytically useful, because the source states no such criterion.

## Files

- `main.tex`: self-contained universal theorem, matrix family,
  rectifiability characterization, Pythagorean proof, and operator transfer.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: official current arXiv v5 PDF.
- `figures/open_problems_crop.png`: readable crop of Problems 5.8--5.12.
- `verification.md`: proof, version, source, render, and novelty checks.
- `tmp/`: LaTeX intermediates and rendered QA pages.

## Review focus

Check the interpretation boundary first, then the antipodal sphere boundary,
the necessity direction of the rectifiability criterion, and the convex
forward-difference proof for Pythagorean orthogonality.

Ledger:
`runs/fa_banach_001/ledger/results/2507.17122_universal_orthogonality_transfer_characterization.json`

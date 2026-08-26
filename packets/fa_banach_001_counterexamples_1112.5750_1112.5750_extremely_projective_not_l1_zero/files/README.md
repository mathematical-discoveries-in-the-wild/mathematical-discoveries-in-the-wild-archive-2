# An extremely projective normed space that is not `l_1^0(M)`

Status: `candidate full counterexample (likely valid)`

Source: A. Ya. Helemskii, *Metric freedom and projectivity for classical and
quantum normed modules*, arXiv:1112.5750v1 (2011), Section 3 on source PDF
page 10 and Remark 3.6 on page 12.

## Counterexample

In the standard `l_1`, let

`x = (2^{-2^j})_{j>=1}`

and equip

`P = c_00 + span{x}`

with the inherited `l_1` norm.  Then:

- `P` is extremely projective as a normed space;
- `P` is not isometrically isomorphic to `l_1^0(M)` for any set `M`;
- consequently, by Theorem 3.5 of the source paper, `P` is not metrically
  projective.

For each cutoff `N`, the first `N` coordinate vectors followed by the
normalized successive tails of `x` form a Hamel basis of `P`.  The associated
onto isomorphism from `c_00` differs from the identity by operator norm tending
to zero.  Thus `P` has Banach--Mazur distance one from `c_00`, and extreme
projectivity transfers through these arbitrarily small distortions.

If `P` were isometric to `c_00`, the isometry would extend to a surjective
isometry of `l_1`.  Such an isometry permutes the extreme points of the unit
ball and hence preserves `c_00`, contradicting the strict inclusion
`c_00 < P`.

## Packet contents

- `main.tex` and `solution_packet.pdf`: full statement and proof.
- `source_paper.pdf`: locally compiled cached arXiv source.
- `figures/open_problem_crop.png`: source-page crop of the conjecture.
- `code/check_superlacunary_tails.py`: exact finite arithmetic sanity check.
- `verification.md`: mathematical, computational, literature, and visual
  audit.

## Novelty bounds

On 2026-08-11, exact arXiv-id, title, and core-keyword searches of the run
indexes found no prior result.  Exact-phrase and close-keyword searches of the
local parsed arXiv corpus found the conjecture only in arXiv:1104.2463 and
1112.5750.  The only local later citation found, arXiv:1309.4974, uses the
projectivity framework but does not discuss or answer this conjecture.
Bounded external searches returned no usable records in this environment, so
novelty confidence is moderate.

Human review should focus on the onto property of the normalized-tail basis
and on the quantitative transfer lemma.  Both are proved explicitly in the
packet.

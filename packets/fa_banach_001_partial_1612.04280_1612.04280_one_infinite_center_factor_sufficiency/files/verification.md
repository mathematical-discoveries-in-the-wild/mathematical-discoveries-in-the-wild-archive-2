# Verification audit

Status: `candidate substantial partial; likely valid; human review requested`

## Mathematical audit

- The source open-status passage was checked in the official arXiv PDF, source p. 2.
- The conjectural criterion and constant were checked against Theorem 1.10 of arXiv:1505.00984.
- The proof uses only three standard permanence statements explicitly collected in Section 2 of arXiv:1612.04280: compact-normal quotient invariance, product multiplicativity, and equality for a closed normal subgroup with amenable quotient.
- The source's Theorem 3.1 supplies the local-form invariance of the simple-factor constants.
- The central kernel remains discrete after removing the finite center of `P`, because the quotient is by a finite group.
- In the cyclic lemma, the preimage of `closure(q(U))` is exactly `closure(U D) = closure(pr_A(D)) x U`.
- The cyclic-closure dichotomy was checked from the structure `R^p x T^q x Z^r x F` of an abelian Lie group: a dense cyclic subgroup either has compact closure or is closed infinite cyclic.
- In the compact alternative, the compact central group is covered by the finite union `B x {e,z,...,z^(ell-1)}`.
- The naive lattice route was explicitly rejected after checking the direction `Lambda_WA(Gamma_tilde) <= Lambda_WA(Gamma_tilde/Z)` in the source.
- No unproved multiplier-periodization or lattice-splitting claim is used.

## Scope audit

- Proved: the conjectured sufficiency direction, with exact constant, when at most one allowed rank-one factor has infinite center.
- Not proved: the necessity direction in arbitrary intermediate topology.
- Not proved: simultaneous mixing of two or more infinite cyclic simple centers with a noncompact central direction.
- The packet notes that arXiv:1612.04280 covers additional multiple-`sl(2,R)` cases by a different lattice method.

## Artifact audit

- `source_paper.pdf`: 14-page official arXiv PDF; SHA-256 `cffeb5d7b5f9a88227cae63c6eba6635a498fce2d8305b0b43477df9883a5a24`.
- `supporting_paper_1505.00984.pdf`: 9-page official arXiv PDF; SHA-256 `886a58b64e73d45da704c0ca03aa06a85292f9c513a13c95bc3f2015a56df419`.
- `figures/open_problem_crop.png` was rendered from source PDF page 2 at 180 dpi and visually checked.
- `solution_packet.pdf`: 5 A4 pages; SHA-256 `31ec16537fa50fe6fce8e2e70ebda8df7037ea3ab9831128fbe4ca2bcce5cb97`.
- Final LaTeX compilation completed without warnings, bad boxes, undefined references, or duplicate destinations.
- Ghostscript parsed the final PDF successfully.
- All five final pages were rendered at 170 dpi and inspected at original detail; no clipping, overlap, illegible text, or broken crop was found.

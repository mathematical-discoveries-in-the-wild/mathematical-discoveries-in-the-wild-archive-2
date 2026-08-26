# Tight probabilistic-frame couplings: literature-implied full answer

**Status:** `literature_implied_answer (complete for Problem 1(d))`.

**Source question:** Martin Ehler and Kasso A. Okoudjou, *Probabilistic
frames: An overview*, arXiv:1108.2169, Problem 1(d), PDF page 9.

**Supporting result:** Dongwei Chen and Martin Schmoll, *Probabilistic frames
and Wasserstein distances*, arXiv:2501.02602, Section 4.6, equation (4.7), PDF
page 13.

The supporting block-frame-operator identity gives a complete characterization:
if the tight marginal frame bounds are `A` and `B`, a coupling `gamma` is tight
on the product space exactly when `A=B` and
`integral x y^T d gamma = 0`.

Consequently, the Wasserstein optimizer need not be tight.  Taking `mu=nu`
equal to any nonzero zero-mean tight probabilistic frame makes the unique
zero-cost optimal coupling the diagonal plan; its cross block is `A I`, so it
is not tight and is not even a frame on the product space.  Conversely,
nonproduct tight couplings do exist: mixing `Y=X` and `Y=-X` equally for a
symmetric tight marginal cancels the cross block.  Adding an atom at zero
makes this coupling visibly different from the product measure in every
dimension.

Chen--Schmoll cite the source but do not explicitly state that equation (4.7)
answers Problem 1(d); this relation is agent-identified.  The packet does not
assess Problem 1(a)--(c) or the separate POVM question.

Files:

- `solution_packet.pdf`: compact status note and derivation.
- `source_paper.pdf`: arXiv:1108.2169.
- `supporting_paper_2501.02602.pdf`: decisive later source.
- Attempt record:
  `runs/fa_banach_001/attempts/1108.2169_probabilistic_tight_coupling_identification.md`.


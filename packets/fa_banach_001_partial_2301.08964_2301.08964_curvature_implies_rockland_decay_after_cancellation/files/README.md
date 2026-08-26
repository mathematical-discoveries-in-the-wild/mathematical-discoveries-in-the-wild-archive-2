# Partial solution: curvature implies Rockland decay after cancellation

Source: Cardona--Delgado--Ruzhansky, arXiv:2301.08964, Remark 1.9.

Status: substantial partial theorem, likely valid, pending human review.

## Result

If a compactly supported finite measure on a graded group satisfies the
Govindan Sheri--Hickman--Wright curvature assumption, subtracting a compactly
supported smooth function with the same mass produces a mean-zero measure
which satisfies the positive- and negative-order Rockland Fourier conditions,
for the measure and its reflection. The reverse implication is not proved.

The proof has three independent components: translation Holder regularity
gives a fractional Rockland derivative; a dyadic spectral root lemma passes
from an alternating convolution power to the original transform; and a
heat-kernel cancellation estimate supplies the negative Rockland power.

## Files

- `main.tex`: self-contained proof, including exact convolution-order audit.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv:2301.08964.
- `supporting_paper_2305.04700.pdf`: the source of the curvature assumption.
- `figures/open_problem_crop.png`: source question crop.
- `verification.md`: independent source, proof, compilation, and rendering audit.
- `tmp/`: build intermediates and rendered QA pages.

## Classification

This is not a full solution of the equivalence problem. It proves the useful
direction after the necessary mass correction. The converse and weak `(1,1)`
endpoint remain open.

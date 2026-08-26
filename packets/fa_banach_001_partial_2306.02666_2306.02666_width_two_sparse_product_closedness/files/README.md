# 2306.02666: exact hidden-width-two sparse-product closedness

- Status: `candidate_partial_likely_valid`
- Model: `GPT5.6`
- Source: Quoc-Tung Le, Elisa Riccietti, and Remi Gribonval, *Does a sparse
  ReLU network training problem always admit an optimum?*, arXiv:2306.02666v2
- Target: Section 3.3's open efficient-decision problem and Question 3.2
- Scope: two factors and exactly two hidden components

## Result

For row supports `S1,S2` and column supports `T1,T2`, let `L` be the set of
matrices

`u1 v1^T + u2 v2^T`

with `supp(ui) subset Si` and `supp(vi) subset Ti`. The packet proves that `L`
is nonclosed exactly when the two rectangles overlap and at least one of three
explicit combinatorial degenerations occurs:

1. one rectangle has both an exclusive row and an exclusive column;
2. the rectangles have two common rows and exclusive columns on both sides;
3. the transpose of case 2.

Thus closedness is decidable in linear time after reading the four supports.
Cases 2 and 3 are genuine false negatives for the paper's local-LU detector.

For independent Bernoulli row/column masks, the packet also gives an exact
finite multinomial formula for the probability that the width-two sparse
matrix-product image is nonclosed. By the source's Theorem 3.1, every such mask
is potentially ill-posed for a suitable finite regression problem. The formula
is an exact evaluation of this matrix-product certificate and remains only a
lower bound for all possible ReLU ill-posedness mechanisms.

## Evidence and verification

- `main.tex` and `solution_packet.pdf`: self-contained theorem and proof.
- `source_paper.pdf`: local copy of arXiv:2306.02666v2.
- `figures/open_problem_crop.png`: source page 7, Section 3.3 and Question 3.2.
- `code/verify_width_two.py`: exhaustive small-pattern and probability checks.
- `verification.md`: claim, proof, computation, novelty, and reviewer audit.
- `attempts/2306.02666_width_two_closedness_upgrade/attempts.md`: three focused
  attempts, including the required probability upgrade and unrestricted-width
  obstruction audit.

## Limitations and review recommendation

The unrestricted hidden-width problem remains open, and closedness of the
linear product image is not sufficient in general for all ReLU realization
sets to be closed. Recommended for expert review as a substantial, fully
proved partial result. The block-rank decomposition lemma and the bounded
novelty claim deserve the closest scrutiny.

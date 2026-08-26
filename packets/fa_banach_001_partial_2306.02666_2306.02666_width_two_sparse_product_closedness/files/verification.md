# Verification report

Status: `candidate_partial_likely_valid`

## Claim-to-source check

- Source: arXiv:2306.02666v2, Section 3.3, page 7.
- The source asks for more efficient algorithms deciding closedness of the
  sparse matrix-product image and, in Question 3.2, for probabilities of bad
  random supports.
- The source's Lemma B.8 gives only a sufficient local-LU detector and
  explicitly allows false negatives.
- The packet proves an exact decision rule only for two factors and hidden
  width two. It does not claim a solution for unrestricted width or for all
  ReLU realization-set obstructions.

## Proof audit

1. Each factorization is exactly a sum of two rank-one coordinate-rectangle
   cones.
2. The three nonclosedness cases have explicit sequences in the image and a
   coordinate-submatrix obstruction showing the limit is outside the image.
3. Negating the three cases leaves only disjoint supports, cross-nested
   rectangles, or a one-dimensional common row/column case.
4. In the cross-nested case the image is exactly a set cut out by support
   equations, one total-rank-at-most-two condition, and two block-rank-at-most-
   one conditions. This determinantal set is closed.
5. The Bernoulli formula is the multinomial probability of the same necessary
   and sufficient Boolean event.

## Computational sanity check

Command:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2306.02666_width_two_sparse_product_closedness/code/verify_width_two.py
```

The script exhaustively checks all `m,n <= 4` support patterns against the
closed-case partition and checks the multinomial formula against direct
weighted enumeration for `m,n <= 3` at 27 parameter/dimension choices. This is
not a proof; it checks the combinatorial case split and probability bookkeeping.

## Novelty audit

A bounded search on 2026-08-11 used the exact source title, `closedness sparse
ReLU sparsity pattern`, `rank-one supports closedness`, `sum of two rank-one
cones`, and arXiv:2112.00386. The source paper and its cited fixed-support
sparse-matrix-factorization paper were inspected. No exact width-two converse
classification or the two additional degeneration types was found. Novelty
confidence is moderate, because the result is elementary enough to exist under
different terminology.

## Reviewer focus

The most important human checks are the sufficiency direction of the block
decomposition lemma, the assertion that the three nonclosed cases exhaust all
non-cross-nested patterns, and whether the exact theorem is already folklore in
algebraic statistics or matrix-factorization geometry.

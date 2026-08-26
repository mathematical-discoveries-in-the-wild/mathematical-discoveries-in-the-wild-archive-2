# Verification record

## Mathematical checks

1. For a rank-one matrix `uv^T`, scalar factorization proves
   `gamma_2(uv^T) <= ||u||_infinity ||v||_infinity`, while domination of the
   maximum entry proves the reverse inequality.
2. For `A_n=1_n 1_n^T` and `S_i=<1_n,epsilon_i>`, direct multiplication gives
   `[<A_n epsilon_i,epsilon_j>]=ss^T`, hence its Schur norm is
   `max_i |S_i|^2`.
3. Direct optimization gives `||A_n||_{infinity -> 1}=n^2`, attained at the
   all-ones sign vector.
4. The moment-generating-function estimate
   `(cosh lambda)^n <= exp(n lambda^2/2)` gives
   `P(|S_i|>=t)<=2 exp(-t^2/(2n))`.  The theorem follows by a union bound.
5. Integrating the union-bound tail above `2n log(2K)` gives the stated
   expectation bound.

The verifier performs an exact integer check of the sampled-matrix identity
and prints seeded Monte Carlo ratios for several dimensions.

Command:

```sh
conda run --no-capture-output -n sandbox python code/verify_rank_one_sampling.py
```

The numerical output is only a sanity check.  The self-contained rank-one
identity and Chernoff argument in the packet are the proof.

## Source and novelty checks

- Original source: Thomas Sinclair and Naveen Vivek, *Remarks on the
  Grothendieck norm*, arXiv:2210.03868 (2022), Question 3.7 on PDF page 10.
- The local registry, attempt index, and solution index contained no result
  for this arXiv id or exact question before promotion.
- A bounded external search through 2026-08-13 used the exact question
  phrase, paper title and authors, arXiv id, and combinations of `random
  signs`, `Schur norm`, and `Grothendieck norm`.  It found the source paper and
  bibliographic mirrors, but no explicit answer or the rank-one obstruction.
- This was a bounded search, not an exhaustive priority determination.
  Mathematical confidence is high; novelty confidence is low-to-moderate
  because the counterexample is elementary.

## Artifact and PDF checks

- The original PDF was downloaded from arXiv and archived as
  `source_paper.pdf`.
- PDF page 10 was rendered at 180 dpi.  The full-width crop contains the
  complete Question 3.7 and was visually inspected for readability.
- The solution packet was compiled with all build artifacts under
  `tmp/build/`; each final page was rendered and visually inspected.
- The final LaTeX log was checked for undefined references, missing
  citations, overfull boxes, and fatal warnings.

## Human review recommendation

Likely valid as a full negative answer to Question 3.7.  Verify first the
rank-one Schur-norm identity and the normalization
`||1_n 1_n^T||_{infinity -> 1}=n^2`; the probability and expectation bounds
then follow immediately from the standard self-contained Chernoff estimate.

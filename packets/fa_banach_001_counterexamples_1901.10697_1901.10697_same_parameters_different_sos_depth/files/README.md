# Counterexample: ETF SOS Depth Is Not Determined by `(N,r)`

Status: `candidate_full_counterexample_likely_valid`.

Source: Afonso S. Bandeira and Dmitriy Kunisky,
*Sum-of-Squares Optimization and the Sparsity Structure of Equiangular Tight
Frames*, arXiv:1901.10697 (2019).

## Source question

Question 4.1 on PDF page 12 asks for the largest even degree `d` such that a
real ETF Gram matrix belongs to the generalized elliptope `E_d^N`, and asks:

> Does the answer depend only on `N` and `r`?

## Result

No. Two explicit strongly regular graphs with parameters `(26,10,3,4)` give
Seidel matrices `S_c,S_n` and ETF Gram matrices

`X_c=I+S_c/5`, `X_n=I+S_n/5`.

Both are Gram matrices of real ETFs with exactly `(N,r)=(26,13)`. Yet:

- `X_c` is the uniform average of 130 sign outer products, so
  `X_c in C^26=E_26^26` and its largest hierarchy degree is 26;
- `X_n` is not in `C^26=E_26^26`. Every sign vector that could occur in a cut
  decomposition must lie in the `+5` eigenspace of `S_n`. There are exactly
  14 such sign lines. Their outer products are affinely independent, and the
  unique affine representation of `X_n` has weights
  `-3/10,1/10,...,1/10`. The negative coefficient rules out a convex
  representation, so the largest degree for `X_n` is at most 24.

Therefore the largest generalized-elliptope degree is not determined by the
frame parameters `N` and `r`.

## Exact verification

`code/verify_counterexample.py` embeds the two graph6 strings and uses exact
integer/SymPy rational arithmetic after graph6 decoding. It:

1. checks both SRG parameter sets and `S^2=25I`;
2. exhausts the sign vectors in each 13-dimensional `+5` eigenspace via
   `2^13` pivot-coordinate assignments;
3. verifies the 130-term cut decomposition exactly;
4. verifies completeness, affine independence, and all 326 rational equations
   in the 14-line noncut certificate.

`code/exact_certificate.json` is the deterministic verifier output.

Run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/1901.10697_same_parameters_different_sos_depth/code/verify_counterexample.py
```

## Files

- `main.tex`, `solution_packet.pdf`: theorem, proof intuition, formal proof,
  scope, and references.
- `source_paper.pdf`: arXiv:1901.10697.
- `figures/open_problem_crop.png`: source Question 4.1.
- `code/verify_counterexample.py`: exact finite verifier.
- `code/exact_certificate.json`: exact certificate summary.
- `verification_report.md`: mathematical, provenance, code, and rendering QA.

Human review should focus on the kernel-support reduction for cut
decompositions and the exact exhaustiveness of the pivot-coordinate sign
enumeration.


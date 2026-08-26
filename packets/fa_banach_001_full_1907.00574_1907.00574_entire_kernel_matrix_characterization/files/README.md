# Entire-kernel characterization on Gaussian Fock space

Status: `candidate_full_likely_valid` for the literal open problem.

Source: Guangfu Cao, Ji Li, Minxing Shen, Brett D. Wick, and Lixin Yan,
*A Boundedness Criterion for Singular Integral Operators of convolution type
on the Fock Space*, arXiv:1907.00574, page 13.

## Result

If

```text
K(z,w) = sum_(alpha,beta) a_(alpha,beta)
         z^alpha w^beta / sqrt(alpha! beta!),
```

then its Gaussian Fock integral operator is bounded exactly when the matrix
`A=(a_(alpha,beta))` is bounded on `ell^2(N_0^n)`, and the two norms are equal.
An equivalent criterion uses only finite collections of kernel values and the
Fock reproducing kernel.

The packet also gives an explicit entire kernel whose rows, columns, Fock
slices, and coarse pointwise growth all satisfy the natural necessary tests,
while its block norms diverge.  This shows why coupled matrix control is
essential.

## Files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: official arXiv source PDF.
- `figures/source_question_crop.png`: exact source-page crop.
- `code/verify_kernel_matrix.py`: deterministic finite-dimensional checks.
- `verification.md`: reproducibility and QA record.

## Scope

This closes the all-entire-kernels question exactly as written.  It does not
claim a local `T(1)` theorem for a separately specified Fock
Calderón--Zygmund class.  The coefficient characterization is elementary
RKHS theory and may be folklore, so novelty confidence is low.


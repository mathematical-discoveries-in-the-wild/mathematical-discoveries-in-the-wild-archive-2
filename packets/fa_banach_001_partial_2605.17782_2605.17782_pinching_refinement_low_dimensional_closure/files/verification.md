# Verification record

## Formal checks

The packet contains three independent proof mechanisms.

1. **Closed paths.** In an eigenbasis of \(A\), pinching deletes exactly the \(B\)-edges crossing distinct eigenspaces. If a diagonal unitary makes \(B\) entrywise nonnegative, every deleted path has nonnegative weight. In two dimensions the off-diagonal transitions occur in conjugate pairs, so this condition is automatic.
2. **Rank-one collapse.** Marking and cyclically rotating an \(A\) gives a uniform average over the \(\binom{n+m-1}{m}\) weak compositions of \(m\) into \(n\) parts. For \(A=a|v\rangle\langle v|\), every term is a product of scalar moments \(\langle v,B^r v\rangle\geq\langle v,Bv\rangle^r\).
3. **Compression moments.** Diagonalizing \(PBP\) and applying scalar Jensen in the spectral measure of \(B\) gives \(\operatorname{Tr}(PB^mP)\geq\operatorname{Tr}((PBP)^m)\). This proves \(n=0,1\).
4. **First three-cycle corner.** For \((n,m)=(2,3)\), cyclicity gives the mean of \(\operatorname{Tr}(A^2B^3)\) and \(\operatorname{Tr}(ABAB^2)\). The first term is controlled by compression moments. After writing \(B=D^{1/2}CD^{1/2}\) with \(C\) a correlation matrix, the second term is bounded using \((CXCXC)_{kk}=\|C^{1/2}XC e_k\|^2\geq x_k^2\).

## Numerical checker

From the packet directory, run:

```bash
conda run --no-capture-output -n sandbox python code/check_pinching_subcases.py
```

The checker computes coefficients of \(\operatorname{Tr}(A+tB)^{n+m}\) by matrix-polynomial recurrence and compares them with the spectrally pinched value. It tests random complex \(2\times2\) matrices, rank-one \(A\) in dimension five, arbitrary dimension for \(n=0,1\), phase-balanced examples, the all-dimensional \((2,3)\) theorem, and the source's known \(m=2\) case.

Observed output on 11 August 2026:

```text
All pinching-subcase checks passed.
  minimum gap [2x2, 0<=n,m<=7]: -1.110223e-15
  minimum gap [dimension 5, n<=1, m<=8]: -2.664535e-15
  minimum gap [dimension 5, rank-one A, n<=6, m<=6]: -5.551115e-16
  minimum gap [phase-balanced dimension 4, n,m<=6]: 0.000000e+00
  minimum gap [dimensions 3--7, (n,m)=(2,3)]: 1.454698e-03
  minimum gap [source theorem, dimension 5, m=2, n<=9]: 6.537084e-03
```

The tiny negative values are below the checker's scale-sensitive tolerance and are consistent with floating-point roundoff at exact-equality cases.

## Full-conjecture attack

Before extracting the partial theorem, the search covered random real and complex PSD matrices in dimensions 3–5, ranks 1 through full, and total word degree up to 20. A targeted differentiable search for the \(m=3\) layer subsequently covered dimensions 3–5 and exponents through \(n=200\), again finding no negative gap beyond floating-point roundoff. These searches do not establish the unproved cases.

A proposed Jensen proof in the variable \(B\) was rejected: finite-difference/automatic-differentiation Hessian tests found negative directions for the full word-average coefficient. The compression argument in the packet avoids this error by applying scalar Jensen only to one-vector spectral measures.

## PDF build and audit

The PDF is built with:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
cp tmp/main.pdf solution_packet.pdf
```

All rendered pages are inspected after compilation. Temporary LaTeX and render artifacts stay under `tmp/` or `/tmp`.

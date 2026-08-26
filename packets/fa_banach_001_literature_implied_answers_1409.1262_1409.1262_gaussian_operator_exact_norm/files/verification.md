# Verification record

## Primary-source checks

- Source PDF, printed pp. 58–59: Remark 4.6 explicitly says the exact norm is
  known in the zero-pluriharmonic case and remains open in general.
- Source Lemma 2.3: checked the unitary
  `U f(z)=|det G| f(Gz) exp(-h(z))` and its inverse.
- Neretin, Chapter 5, equation (1.4): checked the block convention for
  `B[S]` and the placement of `B_t^T` in the upper-right block.
- Neretin, Chapter 5, Theorem 1.4: checked boundedness under the matrix-ball
  conditions.
- Neretin, Chapter 6, Theorems 1.3–1.4: checked the canonical invariants and
  the generalized eigenvalue pencil.
- Neretin, Chapter 6, Theorem 2.2: checked both determinant norm formulas and
  the explicit statement that the second formula holds for every bounded
  Gaussian operator.

## Algebra checks

- Direct conjugation gives
  `U^* exp(-tP) U f(w)=exp((h(G^-1w)-h(A_tG^-1w)))f(GA_tG^-1w)`.
- With `h(z)=z^T H z/2`, this exponent equals `w^T C_t w/2` for
  `C_t=G^-T(H-A_t^T H A_t)G^-1`.
- Setting `K=G^-T H G^-1` and `B_t=G A_t G^-1` gives the equivalent identity
  `C_t=K-B_t^T K B_t`.
- The reproducing kernel cross term is
  `(B_t w)^T conjugate(u)=w^T B_t^T conjugate(u)`, hence
  `S_t=[[C_t,B_t^T],[B_t,0]]` is the correct symmetric block matrix.
- Scalar normalization of Lebesgue measure changes the realization of the
  standard Fock space by a scalar unitary and does not change the operator or
  its norm.

## Limiting and special-case checks

- `h=0`: `C_t=0`; the formula reduces to norm one for a bounded pure linear
  composition operator.
- `B_t=0`: the operator is `f -> f(0) exp(w^T C_t w/2)` and the formula
  reduces to `det(I-C_t^*C_t)^(-1/4)`.
- Stable limit: `B_t -> 0`, `C_t -> K`, so the exact limit is
  `det(I-K^*K)^(-1/4)`.
- Strict convexity gives `||K||<1`, so this determinant is finite and equals
  one exactly when `K=0`.
- Independent numerical audit in dimension one: for three strict examples
  `(b,c)=(0.3,0.2),(0.55,-0.25),(0.2,0.6)`, the generalized-pencil formula
  agreed with the largest singular value of the 100-by-100 truncated Fock
  matrix to `4.5e-16` or better.

## Packaging checks

- `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`: passed.
- Final log scan: no warnings, overfull boxes, underfull boxes, or undefined
  references.
- Ghostscript null-device PDF parse: passed.
- Final packet: three letter-size pages.
- All three pages were rendered to PNG at 150 dpi and visually inspected;
  equations, boxes, headings, citations, and page breaks are clear and no
  clipping or overlap is present.

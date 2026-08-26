# The motivating cusp symbol is already locally Wiener

Status: **candidate substantial partial result; likely valid; human review recommended**

Source: Deyu Chen and Guixiang Hong, *The nonlinear estimates on quantum
Besov spaces*, arXiv:2601.11934v2 (2026), Theorem 1.4 and Remark 1.5 on PDF
page 6; the Wiener-space definition is on PDF page 23.

## Result

Let `m >= 1`. If `F in C^m(R)` and the top derivative `F^(m)` belongs to
`H^1_loc(R)`, then

`F in_loc W_0(R) cap W_m(R)`

for the Wiener spaces used in the source paper. In particular, for odd
`m=2k+1`,

`F(x)=|x|x^m`

satisfies the local Wiener hypothesis: `F^(m)(x)=(m+1)!|x|`, which is locally
`H^1`. Consequently, the displayed example in Remark 1.5 is already covered
by Theorem 1.4 for every `p,q,s` in that theorem with `ceil(s)=m`.

The proof is short. After multiplication by a smooth compact cutoff, both the
localized function and its `m`-th derivative lie in `H^1(R)`. Cauchy--Schwarz
and Plancherel give `H^1(R) -> {f : hat f in L^1(R)}`.

## Scope

This corrects and settles the paper's motivating cusp example and gives the
broader sufficient condition `F^(m) in H^1_loc`. It does **not** prove that
every locally `C^m` symbol is locally Wiener, nor does it replace the Wiener
hypothesis in Theorem 1.4 for arbitrary `C^m` symbols.

## Files

- `main.tex`, `solution_packet.pdf`: full proof packet.
- `source_paper.pdf`: arXiv:2601.11934v2.
- `figures/open_problem_crop.png`: source page 6, including Theorem 1.4 and
  Remark 1.5.
- `verification.md`: independent line-by-line proof audit and scope check.

The associated general-gap routes are retained in
`runs/fa_banach_001/attempts/2601.11934_general_bounded_input_gap_attempts.md`.


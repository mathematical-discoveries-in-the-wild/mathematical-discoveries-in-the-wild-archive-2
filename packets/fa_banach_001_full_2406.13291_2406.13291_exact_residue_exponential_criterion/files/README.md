# Exact residue criterion for completely alternating rational sequences

**Status:** candidate full solution, likely valid.

**Source:** Monojit Bhattacharjee and Rajkamal Nailwal, *A characterization of
completely alternating functions*, arXiv:2406.13291, Question 1.2 on source
PDF page 2 (published in *Journal of Mathematical Analysis and Applications*,
2025).

For

`r(x)=p(x)/product_i(x+b_i)`, `0<b_1<...<b_k`, `deg p<=k+1`,

write

`r(x)=beta+alpha*x+sum_i c_i/(x+b_i)`

and set `w(t)=sum_i c_i*t^{b_i}`.  The packet proves the exact classification:

`{r(n)}` is completely alternating if and only if `alpha>=0` and
`w(t)<=0` for every `0<t<1`.

If the source's additional strict-positivity convention is imposed, add only
`r(0)>0`.  When all data are rational, the exponential-polynomial sign test
reduces to polynomial nonpositivity on `[0,1]` and is exactly decidable by
Sturm sequences.

The proof takes the forward difference `d_n=r(n+1)-r(n)`.  Its unique signed
Hausdorff representing measure is

`alpha*delta_1 -(1-t)w(t)/t dt`.

Complete alternation of `r` is equivalent to complete monotonicity of `d`, so
uniqueness forces this signed measure to be positive, giving both necessity
and sufficiency.

## Contents

- `solution_packet.pdf`: expert-facing theorem and proof.
- `main.tex`: packet source.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: Question 1.2 and defining rational class.
- `tmp/`: build and rendering intermediates.

## Verification

The sign convention was checked from `nabla=I-E`: complete alternation of
`r` is equivalent to complete monotonicity of `Er-r`.  Endpoint atoms, the
degree-`k+1` term, integrability at zero, and the source's positivity convention
were checked separately.  The example

`r(x)=1-2/((x+1)(x+2)(x+3))`

has residue vector `(-1,2,-1)` and density polynomial
`w(t)=-t(1-t)^2`; it satisfies the exact criterion even though the source's
second partial-sum inequality fails.

## Novelty check

On 2026-08-11, the run indexes and exact-phrase/residue-keyword web searches
were checked.  They found the source and its published version, which still
state only sufficient general residue conditions, but no later exact
classification.  Novelty confidence is moderate: the proof is a short direct
completion of the source's signed-measure calculation and may be regarded as
an implicit observation, but the necessary-and-sufficient theorem was not
located or stated in the source.

## Human-review recommendation

Verify the uniqueness step for finite signed Hausdorff measures and confirm
that Question 1.2 is intended to allow the exact exponential-polynomial sign
criterion rather than demanding a finite list of inequalities purely in the
ordered zeros and poles.  Mathematically, the equivalence itself is complete.


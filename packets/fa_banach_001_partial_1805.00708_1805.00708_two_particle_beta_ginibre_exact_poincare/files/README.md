# Exact two-particle beta-Ginibre Poincare constant

Status: `candidate exact solved subcase, likely valid pending expert review`

Source: Djalil Chafai and Joseph Lehec, *On Poincare and logarithmic
Sobolev inequalities for a class of singular Gibbs measures*,
arXiv:1805.00708.

## Result

For the probability law on `C^2` with density proportional to

```text
exp(-a(|z1|^2+|z2|^2)) |z1-z2|^beta,   a>0, beta>=0,
```

the exact spectral gap is

```text
a(sqrt(beta^2+4)-beta),
```

and the optimal Poincare constant is

```text
(sqrt(beta^2+4)+beta)/(4a).
```

For the paper's two-particle normalization, `a=2`.  Thus at the classical
complex Ginibre value `beta=2`, the exact constant is `(1+sqrt(2))/4`.

## Method

The orthogonal center/difference coordinates factor the law into a planar
Gaussian and the radial measure `|v|^beta exp(-a|v|^2) dv`.  Fourier modes
in the polar angle and generalized Laguerre polynomials give the complete
relative spectrum

```text
4ak + 2a alpha_m,
alpha_m = (sqrt(beta^2+4m^2)-beta)/2.
```

The first nonconstant mode is `|m|=1, k=0`, giving the claimed gap.

## Scope

This fully resolves the Poincare constant for two particles and arbitrary
nonnegative repulsion exponent.  It is therefore a solved subcase of the
source's arbitrary-particle question.  It does not determine the constant for
three or more particles, and it does not determine the log-Sobolev constant.

## Files

- `main.tex`: self-contained proof.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: official arXiv PDF.
- `figures/open_problem_crop.png`: source question on PDF page 8.
- `code/verify_spectrum.py`: exact symbolic verification.
- `verification.md`: audit record.

## Novelty check

The run indexes and bounded arXiv/web searches for beta-Ginibre functional
inequalities, exact Poincare constants, two-particle planar Coulomb gases,
and the resulting closed formula found no prior statement of this result.
This is not exhaustive bibliographic certification.

## Human-review recommendation

Prioritize the Friedrichs boundary condition at the collision point and the
completeness of the Fourier-Laguerre decomposition.  The exact residual and
an independent extremizer Rayleigh quotient can be rerun with

```bash
conda run --no-capture-output -n sandbox python code/verify_spectrum.py
```

# Adjacent product-derivative dichotomy

Status: `substantial partial result, likely valid`.

Source target: Frederic Marbach, *A family of interpolation inequalities
involving products of low-order derivatives*, arXiv:2306.06668, Open Problem
1.10 on PDF page 4.

## Result

Fix an integer center order `j>=1`. If a mean-centered tuple uses only the
orders `j-1,j,j+1`, it consists of `a>=1` copies of each outer order and `b>=0`
copies of `j`; put `kappa=2a+b`.

For every finite `1<=q<infinity`,

```text
||D^j u||_{L^(q kappa)}
 <= (q kappa-1)^(a/kappa)
    ||(D^(j-1)u)^a (D^j u)^b (D^(j+1)u)^a||_{L^q}^{1/kappa}.
```

At `q=infinity`, no constant can make the corresponding inequality true.
Thus this entire adjacent-order subfamily is classified exactly by the
finite/infinite exponent dichotomy.

Two further boundary results are proved:

- for every symmetric pair `(j-d,j+d)`, the desired `q=1` estimate holds with
  constant one, by `d` integrations by parts;
- for the first fractional pair `(0,1)`, the estimate fails at `q=1`, while at
  `q=infinity` the standard homogeneous Holder seminorm satisfies
  `[u]_{W^(1/2,infinity)} <= 2 ||u u'||_infinity^(1/2)`.

## Proof mechanism

The finite-`q` adjacent theorem is one integration by parts followed by a
Holder split whose exponents close because `kappa=2a+b`. The endpoint failure
uses a smooth phase-plane bump with bounded `||f f''||_infinity` and
unbounded `||f'||_infinity^2`; separated finite differences impose the moment
conditions needed to lift the example to every center order `j`.

The fractional `q=1` counterexample is a smooth approximation to an interval
indicator: its `||u u'||_1` is fixed, while its critical `H^(1/2)` energy grows
logarithmically.

## Scope and provenance

This is not a full classification of Open Problem 1.10. Wider derivative gaps
for `q>1` and most noninteger mean orders remain open.

Kałamajska--Peszek, arXiv:1104.1967, contains the known finite-exponent base
case with one factor each of `f` and `f''`. The packet includes that paper and
does not claim the base inequality as new. Bounded local/arXiv/web searches
found no statement of the repeated-factor adjacent dichotomy, its
compactly-supported `q=infinity` obstruction, or their identification with
Marbach's open problem. Novelty is provisional pending specialist review.

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: arXiv:2306.06668.
- `supporting_paper_1104.1967.pdf`: prior nonlinear Gagliardo--Nirenberg paper.
- `figures/open_problem_crop_page4.png`: source Open Problem 1.10 and its three
  recorded examples.
- `code/verify_adjacent_product.py`: deterministic analytic/numerical sanity
  checks.
- `VERIFICATION.md`: proof and rendering audit.

## Reviewer focus

The central checks are the exact Holder exponent identity in Theorem A, the
uniform cutoff-strip bound in the phase-plane bump, the finite-difference
moment lift, and the logarithmic lower bound in the fractional `q=1`
counterexample.

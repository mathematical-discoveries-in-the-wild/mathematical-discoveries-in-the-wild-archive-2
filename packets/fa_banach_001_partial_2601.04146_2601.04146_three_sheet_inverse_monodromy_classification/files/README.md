# Three-sheet inverse monodromy classifies the quadratic Smirnov uniqueness condition

Status: `partial_result_likely_valid`

## Source gap

Emmanuel Fricain, Sophie Grivaux, Maëva Ostermann, and Dmitry Yakubovich,
“Embedding of Toeplitz operators with smooth symbols into strongly continuous
semigroups,” arXiv:2601.04146 (2026), Theorem 6.7 and the paragraph immediately
after it on PDF page 30.

For a component `Omega` with `|wind_F(Omega)|=2`, Theorem 6.7 assumes that

`u + zeta v + zeta^2 w = 0` a.e. on the relevant boundary

forces `u=v=w=0` for `u,v,w in E^1(Omega)`. The authors state that they do not
know a geometric condition implying this analytic uniqueness property.

## Result

A bounded finite branched-cover continuation of the reciprocal inverse gives
a sharp answer. If the continuation has sheet degree `d`, then a boundary
polynomial relation of degree at most `r` with `E^1(Omega)` coefficients is
unique exactly when `d>r` (under full boundary compatibility for the converse).
In particular, three inverse sheets imply the quadratic condition in Theorem
6.7(1), while one or two sheets produce an explicit nonzero relation from the
elementary symmetric functions of the sheets.

This yields a concrete analytic-geometric criterion: a connected bounded
inverse continuation with at least three sheets. It also explains sharply the
paper’s cube-root success and square-root failure.

## Proof intuition

Lift the proposed relation to the connected inverse covering. Boundary
uniqueness first makes it an analytic identity on one sheet, and the identity
theorem propagates it to every sheet. Over a regular value, one polynomial of
degree at most `r` then has `d` distinct roots. It must be the zero polynomial
when `d>r`.

Conversely, when `d<=r`, the monic polynomial whose roots are the sheet values
has bounded holomorphic symmetric coefficients on `Omega` and annihilates the
boundary trace `zeta`. This supplies the forbidden nonzero relation.

## Explicit family

For every integer `m>=3`, the packet gives a piecewise analytic `C^{1,1}`
symbol whose image is a clockwise outer circle and a clockwise unit circle,
internally tangent at `1`. The unit disk has winding number `-2`, and on its
boundary the reciprocal inverse is the selected branch of `lambda^(1/m)`.
The continuation is `pi(x)=x^m`, `Psi(x)=x`, so the quadratic uniqueness
condition holds for every `m>=3`. The `m=3` member recovers the source’s
example; `m>=4` supplies a new infinite family.

## Verification

- The collar argument uses $E^1\subset\mathcal N$, stability of the
  Nevanlinna class under restriction and bounded multiplication, and standard
  Privalov boundary uniqueness.
- A finite proper map makes the elementary symmetric fiber functions
  holomorphic; boundedness of `Psi` makes them bounded and removes branch-value
  singularities.
- Generic sheet separation is explicit in the hypothesis.
- `code/verify_family.py` checks junction values and first derivatives,
  representative winding numbers, and the three-root Vandermonde determinant
  for `m=3,...,20`. It prints a successful result. These checks are not a proof.
- Current verdict: `likely valid`, confidence 91/100.

## Bounded novelty search

On 9 August 2026, the run’s registry, solution, attempt, and proof-gap indexes
were searched for arXiv:2601.04146, the theorem’s boundary relation, inverse
monodromy, and finite-sheet variants. The adjacent prior attempt for
arXiv:2502.03303 concerns hypercyclicity questions and is not a duplicate.
Official-arXiv web searches used the exact source title with “monodromy,”
“reciprocal inverse monodromy commutant,” “Smirnov quadratic relation,” and the
displayed three-term relation. They found the source paper but no paper stating
this criterion or classification. This is a bounded search, not a guarantee of
novelty.

## Scope and human review recommendation

This is conservatively classified as a substantial partial result because the
condition adds bounded finite analytic continuation data; a reviewer should
decide whether finite inverse-cover degree counts as the “geometric condition”
requested by the source. Within that natural continuation class, the result is
a full sharp classification.

Review first the Nevanlinna-class collar step used to seed the lifted identity,
the descent of the symmetric coefficients through branch values, and the
semantic strength of calling sheet degree geometric.

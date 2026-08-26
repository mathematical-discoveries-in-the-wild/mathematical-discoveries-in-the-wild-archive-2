# Non-even near-ball branch for the Lp-Christoffel-Minkowski equation

Status: candidate partial result, likely valid. No global non-even uniqueness
claim is made.

## Source question

Theorem 1.4 of arXiv:2411.17896 proves small-data uniqueness for even data
and even classical solutions of

`h^(1-p) s_j(h,.) = g`,

and the authors explicitly ask whether the evenness assumption can be
removed.

## Result

For `n >= 3`, `1 <= j <= n-2`, `0 <= p < 1`, and `0 < alpha < 1`:

- the equation has a unique full (not parity-restricted) solution branch in
  a `C^(2,alpha)` neighborhood of the unit ball for arbitrary data `g`
  sufficiently `C^alpha`-close to 1;
- uniqueness on that branch already holds among every classical support
  function sufficiently `C^0`-close to 1;
- if `g` is even, the local solution is automatically even;
- the local conclusion also covers `(p,j)=(0,1)`, which the source excludes
  only from its global non-collapsing theorem.

The key calculation is that the full-space linearization has spherical
harmonic eigenvalues

`mu_k = j+1-p - j k(k+n-2)/(n-1)`.

The degree-one (translation/odd) eigenvalue is `1-p > 0`, and every degree
at least two has negative eigenvalue in the stated range. Thus evenness is
not needed locally.

## Limitation

The source's open problem is global among all classical solutions for small
data. This packet does not show that an arbitrary non-even solution with
`g` close to 1 must itself be close to the ball. The missing ingredient is
a non-symmetric `C^0` non-collapsing/compactness estimate; the source's
estimate uses central symmetry essentially.

## Files

- `solution_packet.pdf`: self-contained proof and review notes.
- `main.tex`: editable source.
- `verification.md`: proof audit.
- `source_paper.pdf`: source paper.
- `figures/open_question_crop.png`: source theorem and open question.

Human review should focus on the centered `p=1` area-measure inverse used to
upgrade `C^0`-local to `C^(2,beta)`-local uniqueness, especially the target
space's zero first-moment condition and uniqueness up to translations.

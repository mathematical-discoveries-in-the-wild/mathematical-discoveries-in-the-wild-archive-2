# Verification report

## Claim checked

For a real Banach space `E` and `f in PCLSC(E)`, the Fitzpatrick extension of
the convex subdifferential satisfies

```text
(partial f)^F = partial(f*).
```

The packet is intended as a simple alternative proof of Theorem 4.8 in
arXiv:1711.06165, thereby answering its Problem 4.10.

## Line-by-line audit

1. For `(s,s*) in G(partial f)`, subgradient equality gives
   `f(s)+f*(s*)=<s,s*>`.
2. Applying Fenchel--Young separately to `(s,x*)` and `(x,s*)`, then using
   that equality, gives
   `phi_{partial f}(x,x*) <= f(x)+f*(x*)` for every `(x,x*)`.
3. Convex conjugation reverses pointwise inequalities. Under the standard
   product pairing between `E x E*` and `E* x E**`, the conjugate of the
   separated function is
   `f*(y*)+f**(y**)`. Thus
   `phi_{partial f}*(y*,y**) >= f*(y*)+f**(y**)`.
4. Fenchel--Young for `f*` gives the further lower bound
   `f*(y*)+f**(y**) >= <y*,y**>`.
5. Membership in the Fitzpatrick extension means that the first and last
   quantities are equal. Both intervening inequalities are therefore
   equalities. Equality in Fenchel--Young is equivalent to
   `y** in partial(f*)(y*)`. This proves graph inclusion.
6. By Theorem 4.3 of the survey, `partial f` is closed, monotone, and
   quasidense. Theorem 4.6 therefore makes its Fitzpatrick extension
   maximally monotone. The graph of `partial(f*)` is monotone. A maximally
   monotone graph cannot be properly contained in another monotone graph, so
   the inclusion is equality.

No reflexivity, attainment, or differentiability assumption is used.
Extended-real cases are harmless: membership in the extension forces the
displayed conjugate to be finite.

## Circularity audit

The source survey cites Stephen Simons, *“Densities” and maximal
monotonicity*, arXiv:1407.1100, Section 11, for the maximal monotonicity of the
Fitzpatrick extension. Its theorem labelled `AFMAXthm` is proved through the
marker-function characterization of the extension, not through the identity
`(partial f)^F = partial(f*)`. The present use of maximality is therefore
noncircular.

## Bounded novelty check

Searches used the exact wording “Is there a simple direct proof,” the formula
variants `(partial f)^F = partial(f*)`, and the terms “Fitzpatrick extension”
plus “subdifferential.” They recovered the source survey, arXiv:1407.1100,
and Stephen Simons's later *A stand-alone analysis of quasidensity*
(arXiv:1907.07278), but no identical proof. This is evidence only, not a
certified exhaustive literature review.

## Verdict

`full_solution_likely_valid`. The argument is complete and noncircular,
subject to a human judgment that “simple direct proof” may use the two general
theorems stated just before the problem.

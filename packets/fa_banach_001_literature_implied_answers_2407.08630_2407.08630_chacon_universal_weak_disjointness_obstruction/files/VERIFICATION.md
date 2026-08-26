# Verification Report

Status: `literature_implied_answer (full negative resolution)`

## 1. Source question

Austin's concluding paragraph asks whether every weakly mixing transformation
can appear, up to isomorphism, as the first transformation in a nonconvergent
example of the double averages. The preceding paper treats bounded measurable
observables and discusses convergence of the function averages; its main
examples even have divergent integrals.

The open-problem crop was copied from the previously verified packet for the
same source PDF.

## 2. Supporting theorem

Lesigne--Rittaud--de La Rue, Definition 1, says that systems `(X,C,mu,C)` and
`(Y,D,nu,T)` are weakly disjoint when, for every `f in L2(mu)` and `g in
L2(nu)`, there are sets `A subset X`, `B subset Y` with full respective
measure such that

```text
1/N sum_{n<N} f(C^n x) g(T^n y)
```

converges for every `(x,y) in A x B`.

The same article defines a system to be universal when it is weakly disjoint
from every dynamical system. In Section 4.2 it records that the Chacon system
is weakly mixing and states Proposition 4.2: the Chacon system is universal.

## 3. Diagonal quantifier check

Let an arbitrary probability-preserving `T` act on the same Lebesgue
probability space as `C`. Apply universality with this second system and the
given `f,g`. The definition supplies full-measure `A` and `B`. Since both sets
now lie in the same space,

```text
mu(A intersect B) = 1.
```

For every `x in A intersect B`, the pair `(x,x)` belongs to the full rectangle
`A x B`, so the desired same-point average converges. No assertion about the
product measure of the diagonal is used.

This is the decisive point: ordinary product-almost-everywhere convergence
would not control a null diagonal, whereas weak disjointness supplies an
entire full rectangle.

## 4. Norm and integral convergence

If `|f| <= M_f` and `|g| <= M_g`, then every average has absolute value at
most `M_f M_g`. Its pointwise limit has the same bound. Dominated convergence
therefore yields convergence in `L^p` for every finite `p >= 1`.

For the integrated averages, finite linearity of the integral gives

```text
1/N sum_{n<N} integral f(C^n x)g(T^n x)dmu(x)
 = integral B_N(x)dmu(x).
```

The `L^1` convergence just proved forces convergence of the right-hand side.

## 5. Isomorphism check

Weak disjointness is a metric-isomorphism invariant (also stated in the
supporting paper). Alternatively, transporting the observables and the second
transformation through an isomorphism reduces any copy of the Chacon system to
the model above. Hence the obstruction applies "up to isomorphism," exactly as
Austin phrases the question.

## 6. Scope and literature status

The argument rules out divergence for two bounded observables `f,g`, hence
also Austin's more special same-observable scalar averages. It rules out
pointwise, finite-`L^p`, and integrated divergence.

The supporting article was published in 2003, so its authors could not have
identified their theorem as an answer to Austin's 2024 question. A bounded
search found no later paper explicitly making this connection. The correct
classification is therefore `literature_implied_answer`, not a new
counterexample and not `literature_already_answered`.

## 7. Reviewer focus

The only genuinely new identification to audit is the diagonal substitution
from a full rectangle. The remainder consists of the published Proposition
4.2 and standard dominated convergence.


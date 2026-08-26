# Verification report

Verdict: candidate full negative answer to Problem 3.9, likely valid, requiring expert review.

## Structural audit

1. **Ambient algebra.** Work on the circle `T=R/Z` with Lebesgue measure.
   The algebra `S(0,1)` is `L^0(T)` modulo null sets, and `AD(0,1)` is a
   regular unital star-subalgebra containing all idempotents.
2. **The digit series.** With binary digits `b_n in {0,1}`, the series
   `h=sum (3/4)^n b_n` converges uniformly, so it defines a bounded real
   measurable function. Its support is one modulo null sets.
3. **Necessary translation behavior of `AD`.** The countable `C^1`-piece
   representation of an approximately differentiable function shows that
   `(f(t+s)-f(t))/s` converges in measure as `s -> 0`. For a finite collection
   of pieces, translation-continuity of measurable sets keeps almost every
   point in the same piece, where the ordinary `C^1` difference quotient
   converges uniformly; the omitted pieces have arbitrarily small measure.
4. **Large digit quotient.** On `A_n={b_n=0}`, addition of `2^-n` changes
   exactly the `n`th digit and no later digit. Hence the difference quotient
   of `h` is exactly `(3/2)^n` on `A_n`.
5. **Localization survives.** For any measurable `E` of positive measure,
   the Rademacher functions `r_n=1-2b_n` form an orthonormal sequence in
   `L^2`, so `int_E r_n -> 0` and `|E cap A_n| -> |E|/2`. Translation
   continuity gives `|E cap (E-2^-n) cap A_n| -> |E|/2`. On this set the
   difference quotient of `chi_E h` is `(3/2)^n`. The quotient sequence is
   therefore not tight in measure, contradicting item 3 if `chi_E h` were in
   `AD`.
6. **Weak transcendence.** Ber--Kudaybergenov--Sukochev prove that `AD` is
   integrally closed. Thus, if a nonzero localization `chi_E h` were integral
   over `AD`, it would belong to `AD`, contrary to item 5. Hence `h` is weakly
   transcendental over `AD`.
7. **Derivation extension.** Proposition 3.7 of
   Ber--Chilin--Sukochev applies because `AD` is regular and contains every
   idempotent. With the prescribed value `delta(h)=0`, it gives a derivation
   on `AD[h]` extending the approximate derivative. Since `h` is not in `AD`,
   this algebra is strictly larger.
8. **Dyadic cocycle.** If `r=m/2^N`, write `t=(j+u)/2^N`. Translation by
   `r` permutes `j` and leaves the tail coordinate `u` unchanged. Therefore
   `alpha_r(h)-h` depends only on `j`, takes at most `2^N` values, belongs to
   `AD`, and has approximate derivative zero.
9. **Translation invariance.** The two derivations `delta alpha_r` and
   `alpha_r delta` agree on `AD` because the approximate derivative is
   translation invariant. They agree on `h` by items 7--8, and hence agree on
   the generated algebra `AD[h]`.
10. **Exact conclusion.** The strictly larger dyadic-translation-invariant
    algebra `AD[h]` admits a translation-invariant derivation extending
    `d/dt`; this negates maximality in Problem 3.9.

## Adversarial checks

- The proof uses ordinary rotations by dyadic rationals, not the binary
  odometer. The finite-prefix claim follows directly from the decomposition
  `t=(j+u)/2^N`.
- A single divergent sequence of pointwise quotients would not rule out
  approximate differentiability. The proof instead obtains divergence on a
  set whose measure tends to half of every chosen positive-measure
  localization and invokes convergence in measure for all `AD` functions.
- The coefficient `3/4` is essential only through `2q>1`; any `q in (1/2,1)`
  works. Choosing `3/4` makes all finite checks rational.
- The extension theorem permits the prescribed value zero because its support
  is dominated by the support of `h`.
- No topology or density of simple functions is imposed on the enlarged
  algebra. Thus there is no conflict with Theorem 3.2 of the source paper.
- The construction gives a star-subalgebra because `h` is real and `AD` is a
  star-subalgebra.

## Computational check

`code/verifier.py` uses exact rational arithmetic. For binary depths through
12 it checks that adding `2^-n` on `b_n=0` changes the truncated digit series
by exactly `(3/4)^n`. It also checks, for every dyadic rotation with denominator
through `2^7`, that the translated-series increment is independent of all
digits after the denominator depth. This is a sanity check only; the proof is
the exact binary-prefix argument.

Command:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2002.00590_dyadic_digit_AD_nonmaximal/code/verifier.py
```

## Literature and novelty audit

- No hit in `registry_index.tsv`, `solutions/index.tsv`, `attempts/index.tsv`,
  or `proof_gaps/index.tsv` for arXiv:2002.00590 or the core problem terms.
- Searched the exact Problem 3.9 sentence, the source arXiv id/title, and
  combinations of `AD(0,1)`, maximal subalgebra, translation-invariant
  derivation, dyadic translations, weak transcendence, and digit series.
- Checked the 2023 journal publication metadata and searched later citation
  variants.
- Checked the metadata and searchable text of the 2023 paper *Isomorphism
  between the algebra of measurable functions and its subalgebra of
  approximately differentiable functions*. It concerns algebraic
  isomorphisms and derivations on `S(0,1)` but no explicit answer to Problem
  3.9 was found.
- Located and checked the exact statement of Proposition 3.7 in the 2006
  extension paper and the integral-closure/unique-extension argument in
  arXiv:1906.00243.

Novelty confidence: moderate and provisional.

## Reviewer focus

The decisive analytic point is the implication `AD => translation difference
quotients converge in measure`. The decisive algebraic point is that
integral closure turns the localized non-`AD` result into weak transcendence,
exactly matching Proposition 3.7. The final group-action check should be made
with the source convention `alpha_r f(t)=f({t-r})`; the sign changes no part of
the finite-prefix argument.

## Packet QA

The final four-page PDF compiled without warnings or substantive layout
issues. Every page was rendered to PNG and visually inspected. The source crop
shows the complete Problem 3.9 and its immediately preceding scope paragraph
at readable review scale; no proof text, formula, citation, or source statement
is clipped.

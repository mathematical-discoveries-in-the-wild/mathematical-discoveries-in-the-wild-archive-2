# Verification report

Verdict: `candidate_full_solution_likely_valid`.

## Exact target

Ferenczi, arXiv:2005.07672v2, Question 6.2 on PDF page 22:

> Does there exist a largest operator ideal U with H = Space(U)?

Here `H` is the space ideal of separable spaces isomorphic to a Hilbert
space, finite or infinite dimensional.

## Dependency audit

1. **Ferenczi's construction.** Proposition 4.4 and its proof give: if
   `Y` is infinite codimensional in the real or complex shift space `X_S`,
   an infinite-dimensional complemented subspace of `X_S^m` cannot embed in
   `Y^n`. The same paper constructs `T_t = I - tS + K_t` with
   `Y_t = Im(T_t)` infinite codimensional and proves
   `T_1 + T_{-1} = 2I + K_1 + K_{-1}` Fredholm.
2. **Absence of Hilbert subspaces.** Gowers--Maurey, *Banach spaces with
   small spaces of operators*, arXiv:math/9407209, Section 5.2, states that
   for every proper set of spreads `S`, `X(S)` has no unconditional basic
   sequence. This applies to the shift space from their Section 4.2.
   Therefore `X_S` contains no `ell_2`; finite powers of `X_S`, and finite
   powers of their subspaces `Y_t`, also contain no `ell_2`.
3. **Direct-sum decomposition.** Gonzalez, *On essentially incomparable
   Banach spaces*, Math. Z. 215 (1994), proves that if `E` and `F` are
   essentially incomparable, every complemented subspace of `E direct_sum F`
   is isomorphic to the direct sum of a complemented subspace of `E` and a
   complemented subspace of `F`.
4. **Semi-Fredholm perturbation.** Strictly singular perturbations preserve
   upper semi-Fredholm operators. Applied to the restriction of the
   decomposition isomorphism, this makes its `Y_t`-coordinate upper
   semi-Fredholm after the Hilbert coordinate is removed.

## Internal proof checks

- A non-strictly-singular map between `ell_2` and `X_S^m` would fix a copy of
  `ell_2` inside `X_S^m`; hence all cross operators are strictly singular and
  therefore inessential.
- If `I_Z` factors through a space `W`, then `Z` is isomorphic to a
  complemented subspace of `W`. Thus membership of `I_Z` in both factorization
  ideals gives precisely the two complemented embeddings used in the proof.
- A finite power of `ell_2 direct_sum X` is isomorphic to
  `ell_2 direct_sum X^m`, so the decomposition theorem applies to every power
  appearing in `Opp`.
- Once the exotic summand is finite dimensional, the full common
  complemented subspace is Hilbertian. Conversely every separable Hilbert
  identity factors through the `ell_2` summand. Hence `Space(J_t)=H` exactly.
- Every operator ideal contains the finite-rank operators. A Fredholm member
  `F:X->X` has a parametrix `R` with `RF=I_X-Q`, `Q` finite rank; ideality and
  linearity therefore imply `I_X` belongs to the ideal.

## Bounded novelty check

Performed 2026-08-09.

- Searched the run registry and cheap source indexes for arXiv `2005.07672`,
  `largest operator ideal`, `Hilbert space ideal`, `Space(U)`, and close
  variants. No prior packet or answer was found.
- Searched the indexed web/arXiv corpus for the exact phrases `largest
  operator ideal` with `Hilbert`, `Does there exist a largest operator ideal`
  with `Hilbert spaces`, `space ideal H` with `largest`, and the source title
  with `Hilbert question`.
- Results found the source paper, its 2023 publication record, and later work
  citing its solution of Pietsch's proper-ideal problem, but no paper claiming
  to answer Question 6.2.

This is a bounded search, not a proof of novelty. Novelty confidence is
moderate; mathematical-validity confidence is high enough for promotion as a
candidate full solution requiring expert review.

## Human-review recommendation

Review as a likely full negative answer. In order of importance, verify:

1. the exact formulation and field scope of Gonzalez's decomposition theorem;
2. the upper semi-Fredholm perturbation step in Lemma 3;
3. that the `X_S` used in Ferenczi's real and complex constructions is covered
   by Gowers--Maurey's no-unconditional-basic-sequence statement.

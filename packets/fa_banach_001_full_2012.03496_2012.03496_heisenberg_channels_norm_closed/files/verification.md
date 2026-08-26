# Verification report

Status: `candidate_full_likely_valid`

## Source audit

The source PDF was checked at the following locations:

| location | input |
|---|---|
| printed p. 46, Corollary 2.3.12 | every Heisenberg channel is the adjoint of a unique Schrödinger channel |
| printed p. 47, paragraph and footnote 33 | the adjoint correspondence is an isometry |
| printed p. 47, Proposition 2.3.13(i) | `Q_S(H,G)` is operator-norm closed |
| printed p. 48, first paragraph | asks whether `Q_H(G,H)` is closed in the full bounded-map space |

The local evidence files are:

- `source_paper.pdf`
- `figures/open_problem_crop.png`
- `figures/source_duality_closedness_crop.png`

## Logical audit

Let `J(T)=T*`. The source gives a surjective isometry

```text
J : Q_S(H,G) -> Q_H(G,H).
```

The ambient bounded-operator space containing `Q_S(H,G)` is Banach, and the
source proves `Q_S(H,G)` norm closed. Thus `Q_S(H,G)` is complete. Its
isometric image `Q_H(G,H)` is complete in the metric induced from
`B(B(G),B(H))`. A complete subset of a metric space is closed.

The equivalent sequence audit is:

1. Assume `S_n=T_n*` converges in operator norm to a bounded map `S`.
2. `||T_n-T_m||=||S_n-S_m||`, so `(T_n)` is Cauchy.
3. Let `T_n -> T`; source Proposition 2.3.13(i) gives `T in Q_S(H,G)`.
4. `||T_n*-T*||=||T_n-T|| -> 0`, while `T_n*=S_n -> S`.
5. Uniqueness of norm limits gives `S=T* in Q_H(G,H)`.

This proof uses the norm topology only. The source's warning that weak-star
operator convergence need not preserve normality is therefore orthogonal to
the argument.

## Computational status

No computational experiment was used or is appropriate. The verification is
an exact functional-analytic type and completeness check.

## Limitations

- The theorem answers operator-norm closure only; it makes no new claim about
  closure in weaker topologies or compactness.
- The statement is kept in the source's separable-Hilbert-space scope.
- Novelty is not independently certified. The bounded search found no explicit
  later answer, but the result is an immediate corollary of adjacent source
  statements and should be checked by a functional analyst before promotion.


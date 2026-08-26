# Counterexample: power-pullback subalgebras of H-infinity

- **Source:** Behera--Maurya--Muthukumar, *Automorphisms of subalgebras of bounded analytic functions*, arXiv:2412.03245.
- **Target:** the concluding conjecture that every automorphism of every subalgebra of `H^infinity(D)` is induced by a disc automorphism.
- **Status:** `candidate_counterexample_likely_valid`.
- **Model:** `GPT5.6`.

## Result

The conjecture is false even for closed unital subalgebras and isometric
automorphisms.  For every integer `m>=2`,

```text
A_m = {g(z^m): g in H^infinity(D)}
```

is a closed unital subalgebra isometrically isomorphic to `H^infinity(D)`.
For any nonzero `a in D`, conjugating composition by the Möbius automorphism
`tau_a` through that isomorphism gives

```text
T(g(z^m)) = g(tau_a(z^m)).
```

This is an isometric algebra automorphism of `A_m`, but it cannot be
composition by any analytic self-map of the original disc.  Such a symbol
would have to satisfy `phi(z)^m=tau_a(z^m)`; the right side has `m` distinct
simple zeros, while all zero multiplicities of an `m`-th power are divisible
by `m`.

## Files

- `main.tex` — full counterexample proof and novelty bounds.
- `solution_packet.pdf` — rendered counterexample packet.
- `source_paper.pdf` — source paper compiled locally from the downloaded arXiv source bundle.
- `figures/open_problem_crop.png` — the concluding conjecture on source page 16.
- `VERIFICATION.md` — mathematical and artifact QA.

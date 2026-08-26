# Verification report

## Verdict

`candidate_full_solution_likely_valid`

The argument is complete modulo human verification of the source theorem
identification and the written inequalities. No unproved mathematical
dependency remains in the packet.

## Source identification

- Source: S. Astashkin, F. Sukochev, and D. Zanin, *On uniqueness of
  distribution of a random variable whose independent copies span a subspace
  in L_p*, Studia Math. 230 (2015), no. 1, 41--57; arXiv:1406.4950;
  DOI 10.4064/sm8089-1-2016.
- Target: Conjecture 2, source PDF page 3.
- Source tools used in the proof: Proposition 6 (the two-term Hardy-envelope
  generator criterion) and Theorem 9 (the strict-index characterization for
  the canonical envelope).

## Line-by-line mathematical audit

1. Put `m(t)=1/M^{-1}(t)` and let `h=f*` be the decreasing rearrangement of
   the generator assumed by the uniqueness hypothesis. Proposition 6 gives
   `T_p h \asymp m`.
2. Since `h` is decreasing, `h(t) <= (t^{-1}\int_0^t h^p)^{1/p}`; hence
   `h \lesssim m` pointwise.
3. If `m \lesssim h` near zero, the head of `T_p m` is bounded by that of
   `T_p h`. The near-zero part of its tail is bounded similarly. The remaining
   fixed tail is absorbed by `Q(t)=t m(t)^2`, which is decreasing because `M`
   is 2-concave. Thus `T_p m \asymp m`, and Theorem 9 gives the conjectured
   strict indices.
4. If the strict indices fail, step 3 implies that `m/h` is unbounded in every
   neighborhood of zero. Continuity points `t_n` can therefore be chosen with
   `t_n < t_{n-1}/2`, `m(t_n) >= 2m(t_{n-1})`, and
   `h(t_n) <= 2^{-n-2}m(t_n)/n`. Continuity gives a positive left interval on
   which `h <= 2^{-n-1}m(t_n)/n`.
5. Set `a_n=2^{-n}m(t_n)` and let `u=a_n` on `[t_{n+1},t_n)`. The growth
   condition makes `a_n` nondecreasing in `n`, so `u` is decreasing.
6. Define `P(t)=t m(t)^p` and `Q(t)=t m(t)^2`. Exact p-convexity makes `P`
   increasing, while exact 2-concavity makes `Q` decreasing.
7. `u` lies in `L_p`, because
   `\int u^p <= \sum 2^{-np}P(t_n) <= P(t_1)\sum 2^{-np}`.
8. For `t in [t_{n+1},t_n)`, the head estimate is
   `\int_0^t u^p <= \sum_{k>=n+1}2^{-kp}P(t_k)+t a_n^p
   \lesssim P(t)+t m(t)^p \lesssim t m(t)^p`.
9. On the same interval, the tail estimate is
   `\int_t^1u^2 <= \sum_{k<n}2^{-2k}Q(t_k)+2^{-2n}Q(t_n)
   \lesssim Q(t)=t m(t)^2`.
10. For `t>=t_1`, the total p-mass is absorbed by the increasing function
    `P`, and the tail vanishes. Therefore `T_pu \lesssim m` on `(0,1]`.
11. The function `g=h+u` is decreasing and belongs to `L_p`. Minkowski's
    inequality in the two Hardy terms gives `T_pg <= T_ph+T_pu \lesssim m`,
    while positivity gives `T_pg >= T_ph \gtrsim m`.
12. On the positive-length intervals chosen in step 4, `u/h >= 2n`; hence
    `g/h` is not bounded near zero. This avoids relying on values at the jump
    points of the staircase.
13. The explicit two-copy sign symmetrization of `g` has mean zero and
    decreasing rearrangement exactly `g`. Proposition 6 therefore supplies a
    second generator whose rearrangement is not equivalent near zero to `h`,
    contradicting uniqueness.

## Computational sanity check

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/1406.4950_uniqueness_conjecture_staircase_perturbation/code/check_staircase_bounds.py
```

The script tests finite staircase truncations for 12 power envelopes
`m(t)=t^{-1/q}` with `1 <= p < q < 2`, three geometric meshes, and 4000
sample points per case. It checks monotonicity, finite `L_p` mass, and a finite
uniform sampled bound for `T_pu/m`. This is a regression/sanity check only;
the symbolic monotonicity argument in the proof is the proof.

## Bounded novelty screen (2026-08-09)

Searched the run's registry/solution/attempt/proof-gap indexes for the arXiv id,
title, and the terms `uniqueness distribution`, `independent copies`, `Orlicz`,
`p-convex`, and `2-concave`; no duplicate result was found. External searches
used the exact source title, `Conjecture 2`, author names, and combinations of
the same core terms on arXiv and general scholarly web search.

Two especially relevant later sources were inspected. The 2022 paper by the
same three authors develops further sufficient uniqueness theorems and calls
the global uniqueness question a remaining open question. Astashkin's 2024
survey again poses a necessary-and-sufficient uniqueness problem as Problem 1.
No paper claiming the converse in source Conjecture 2, and no staircase
perturbation proof of it, was found within these bounds. The screen is bounded,
not a proof of novelty; the 2024 survey uses a quasi-equivalence formulation
that is broader than the exact pointwise near-zero equivalence in Conjecture 2.

## Human reviewer checklist

- Confirm that the source's phrase “equivalence near 0” applies to decreasing
  rearrangements exactly as used here.
- Check the monotonicity directions of `P` and `Q` from the source definitions
  of p-convexity and 2-concavity.
- Check the head and tail sums for arbitrary `t`, not only at `t_n`.
- Check the continuity-point selection and positive-measure domination
  intervals.
- Check the symmetrization and the final use of Proposition 6.
- Independently repeat a citation search before any public novelty claim.


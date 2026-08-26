# Verification report

Result: **candidate full result; no gap found in bounded audit**.

## Formal-hypothesis audit

- `Omega = ell_2` is Hausdorff and first countable in its usual Hilbert norm.
- `X = ell_2 direct_sum_2 ell_2` is Banach (indeed Hilbert).
- `I(x,y)=Ax+By` is bounded, injective, and dense.
- The induced `Omega` topology is strictly weaker: unit vectors `(0,e_k)`
  map to vectors of norm `2^{-k}`.
- `c_n(x,y)=x_n` is continuous and `c_n(phi_m)=delta_nm`.
- The annihilator of `(phi_n)` is zero, so the system is complete minimal and
  the displayed biorthogonal system is unique.
- `U=(a,0)` belongs to `X` because `a_n=2^{-n}` is square summable.

## Proof-pressure checks

1. **Scalar rearrangements use every term.** The crossing algorithm always
   consumes the next unused term of the selected sign. Both one-sided
   harmonic sums diverge, so neither sign family can be left with a first
   unused term forever. Overshoots tend to zero.
2. **Countable interleaving converges globally.** Low coordinates are beyond
   their local convergence thresholds after finitely many stages. High
   coordinate errors are uniformly dominated by
   `C(|x_j|+2^{-j})`, an `ell_2` sequence. This controls intermediate partial
   sums, not merely stage endpoints.
3. **Finite deletion.** Delete finitely many terms from a convergent
   rearrangement of the full family. The remaining order still converges and
   its sum is reduced by exactly the finite deleted sum. Hence every cofinite
   subfamily has full sum range.
4. **Universal natural order exhausts labels.** Forcing the least unused
   initial label at every stage guarantees that every label is eventually
   used. The extra approximation block is finite and uses only remaining
   labels.
5. **Embedding injectivity.** On an infinite support `S_j`, the equation
   `Ax=By` makes every coordinate of `y` equal to the same number
   `gamma_j x_j`; square summability forces `x_j=0`.
6. **Completeness.** An annihilator `(p,z)` would imply
   `sum |<v_n,z>| <= ||a||_2 ||p||_2`. Any nonzero coordinate of `z` sees a
   full harmonic subfamily `e_j/m`, forcing divergence.
7. **Ordinary universality.** The perturbation `A a^(N)` converges to `Aa`,
   so a subsequence of universal `w`-partial sums converging to `f-Aa` gives
   the target `f`.
8. **Rearrangement universality.** `sum a_n e_n` is unconditionally
   convergent. Therefore the same permutation that sends `sum w_n` to
   `f-Aa` sends the full Fourier series to `f`.

## Computational sanity check

Command:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2306.11156_complete_minimal_hilbert_doubly_universal_element/code/check_algebra.py
```

The script checks the exact diagonal lifting identity on 16,000 labeled
finite terms, finite biorthogonality matrices up to size 128, the closed form
square norm of `a`, and the forced-label exhaustion invariant for a finite
scheduling model. It does not verify the infinite-dimensional convergence
arguments and is not used as proof.

## Novelty bounds

Searched on 11 August 2026: the four cheap run indexes; the locally parsed
arXiv corpus; and current arXiv-domain web results for the exact question,
title, id, and close core phrases. No later answer was found. This is bounded,
not exhaustive, so novelty is still pending specialist review.

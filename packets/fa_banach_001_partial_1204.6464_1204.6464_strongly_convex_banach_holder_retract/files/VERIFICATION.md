# Verification report

Verdict: `candidate_partial_likely_valid`

## Formal audit

1. **Invariant-mean barycenter.** Strong convexity implies reflexivity. The
   scalar left invariant mean therefore defines `Lx` in the weakly closed
   convex hull of the orbit, hence in `C`. Duality gives
   `||Lx-Ly||<=k||x-y||`.
2. **First variance estimate.** Left invariance makes the barycenter of
   `(T_{st}x)_t` equal to `Lx`. Applying strong convexity relative to
   `T_sLx` kills the linear term and gives
   `||T_sLx-Lx||^2+cQ(x)<=k^2Q(x)`.
3. **Second variance estimate.** Applying the same inequality to the orbit of
   `Lx`, with barycenter `L^2x` and reference point `Lx`, gives
   `E(Lx)>=||L^2x-Lx||^2+cQ(Lx)`. Hence
   `Q(Lx)<=((k^2-c)/c)Q(x)`.
4. **Geometric increments.** With `rho=(k^2-c)/c<1`, the preceding bounds
   give `||L^{m+1}x-L^m x||<=C rho^{(m-1)/2}` uniformly in `x`.
5. **Hölder limit.** Since `L` is `k`-Lipschitz, balancing the geometric tail
   against `k^n||x-y||` proves that the uniform limit `R` is Hölder. If
   `gamma=sqrt(rho)`, one may take exponent
   `alpha=log(1/gamma)/(log(k)+log(1/gamma))`; for `k=1`, the limit is
   nonexpansive.
6. **Fixedness.** The mean-square residual of `L^m x` tends to zero. Passing
   to the uniform limit gives `mu_t||T_tRx-Rx||^2=0`. For fixed `s`, left
   invariance and the `k`-Lipschitz property force
   `||T_sRx-Rx||^2<=2k^2E(R)+2E(R)=0`.
7. **Retraction.** A common fixed point is unchanged by `L`; hence `R` is the
   identity on the common fixed-point set.
8. **Lp constant.** For `1<p<=2`, the Ball--Carlen--Lieb inequality makes
   `x -> ||x||_p^2` strongly convex with Bregman coefficient `p-1`. Thus
   `c=p-1`, and a nontrivial `k>=1` range exists exactly when `p>3/2`.

## Computational regression

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/1204.6464_strongly_convex_banach_holder_retract/code/check_lp_convexity.py
```

The script tests the midpoint Ball--Carlen--Lieb inequality on randomized
finite-dimensional `ell_p` vectors for several `p` in `(3/2,2]`, and checks
that every sampled `k<sqrt(2(p-1))` gives `0<=rho<1`. It is a regression for
signs and constants, not a substitute for the cited sharp inequality or the
proof.

Result: 100,000/100,000 midpoint cases and 25/25 threshold cases passed; the
minimum normalized floating-point slack was `-4.386e-16`.

## Scope audit

- The packet proves a subcase, not the unrestricted uniformly convex problem.
- The semigroup is taken discrete and left amenable; the single-map corollary
  uses the amenable power semigroup `N`.
- For the exact source problem, impose its Goebel--Kirk condition as well as
  the packet's strong-convexity threshold. The new theorem itself does not
  need the Goebel--Kirk inequality.
- The argument does not establish a Lipschitz retraction when `k>1`.
- The route stops when `k^2>=2c`; no claim is made that this threshold is
  sharp.

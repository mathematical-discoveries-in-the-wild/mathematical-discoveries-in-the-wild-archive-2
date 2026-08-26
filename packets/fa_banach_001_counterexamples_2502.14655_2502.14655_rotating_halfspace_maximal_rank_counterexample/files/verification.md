# Verification report

## Claim checked

For every `1 <= p < infinity`, the kernels

`rho_t(z)=2 |B_t|^{-1} 1_{|z|<t} 1_{z dot v_t>0}`,

with `v_t=(cos(log(1/t)),sin(log(1/t)))`, satisfy condition (A) of source
Theorem 1.1 and yield coercive BBM energies along `t_k=e^{-k}`, but the family
`(rho_{t_k})` is not of maximal rank.

## Analytic audit

1. `rho_t` is nonnegative, locally integrable, supported in `B_t`, and has
   total mass one.
2. The weighted kernel bound in condition (A) is at most one for every radius.
3. Support collapse and unit mass give weak-star convergence to `delta_0`.
4. For every `u`, the function
   `A_u(z)=||u(.+z)-u||_p^p/|z|^p` is even. Splitting the disk into the two
   half-spaces proves the exact identity `F^rho=F^kappa`.
5. The source's Theorem 1.2 applies to the normalized radial disk kernels
   `kappa_t`; exact equality transfers the entire coercivity implication,
   including the `p=1` BV endpoint.
6. The sequence `(cos k,sin k)` has dense tails because `1/(2*pi)` is
   irrational. For any fixed cone `C_tau(w)`, `tau<1`, its angular radius is
   strictly less than `pi/2`. Infinitely many normals lie close enough to
   `-w` that their positive half-space misses the whole cone. Hence its mass is
   exactly zero on a subsequence and its liminf is zero.

No numerical check is needed; all equalities are exact.

## Review focus

- Confirm that the source allows nonsymmetric kernels (it assumes only
  nonnegative measurable/local-integrable kernels).
- Confirm that maximal rank is tested on the raw `rho_t`, not its even part.
- The result does not address necessity under an added even-kernel hypothesis.

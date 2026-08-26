# Frozen stability does not control the coupled parabolic system

Status: `candidate_partial_likely_valid`.

Source: Alexander Dobrick and Jochen Glueck, *Convergence to equilibrium for
linear parabolic systems coupled by matrix-valued potentials*, arXiv:2208.10324.
The concluding remarks on source PDF page 16 say that checking boundedness for
potentials not dissipative in an `ell^p` norm is unclear in general.

## Result

For every prescribed frozen decay parameter `a>0` and PDE growth parameter
`lambda>0`, the packet constructs a smooth real `3 x 3` potential on
`(0,pi)` such that every matrix `V(x)` has the single eigenvalue `-a` and the
frozen matrix semigroups are uniformly exponentially stable, while the
Neumann system

`U_t = U_xx + V(x)U`

has the exact growing solution

`U(t,x)=exp(lambda*t)*(1,cos(x),cos(2x))`.

Thus pointwise spectral stability, even with a uniform frozen-semigroup bound,
cannot by itself provide the boundedness test sought in the source.  This is a
complete obstruction theorem for that natural criterion, but not a full
characterization of arbitrary non-dissipative potentials.

## Verification

Run:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2208.10324_pointwise_hurwitz_potential_pde_instability/code/verify_construction.py
```

The script checks symbolically that the rank-one perturbation is nilpotent,
that its action on the chosen eigenfunction is exact, and that the displayed
special matrix at `x=pi/2` is correct.  The proof in `main.tex` is independent
of the script.

Human review should focus on the rank-one functional `eta`, the nonvanishing
denominator, and the scope statement: this answers a sharp natural subproblem
of the source's broad boundedness direction, not the whole program.

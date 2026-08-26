# Verification report

Verdict: `candidate full counterexample, likely valid`.

## Claim audited

Conditional positive definiteness of `U_K^{sigma^{n-2}}` does not imply that
the uniform measure globally minimizes `I_K`.  The failure occurs for `n=3`
on every `S^{d-1}`, `d>=3`, even when the averaged pair kernel is strictly
conditionally positive definite and uniquely minimized by `sigma`.

## Critical checks

### 1. Symmetry and rotational invariance

The quantities `u=<x,y>`, `v=<y,z>`, and `t=<z,x>` are permuted by every
permutation of `(x,y,z)` and unchanged by simultaneous rotations.  Both the
cubic base kernel and the lifted pair-kernel sum are therefore continuous,
symmetric, and rotationally invariant.

### 2. Vanishing averaged potential of the base kernel

Normalized surface measure satisfies `integral zz^T dsigma(z)=I/d`.  Thus

- `integral <y,z><z,x> dsigma(z)=<x,y>/d`;
- `integral <y,z>^2 dsigma(z)=1/d`;
- `integral <z,x>^2 dsigma(z)=1/d`.

Substitution cancels every term in `U_{H_d}^sigma(x,y)`.

### 3. Strict conditional positive definiteness

For a zero-mass signed measure `nu`, the centered constant disappears and

`I_G(nu)=sum_{k>=1} ||integral x^(tensor k)dnu(x)||^2/k!`.

Every term is nonnegative.  Equality makes all polynomial moments vanish;
polynomials are dense in the continuous functions on the sphere, so `nu=0`.
Hence `G` is strictly conditionally positive definite.

### 4. Unique pair-energy minimizer

The centered kernel has zero `sigma`-potential.  For every probability measure
`mu`, expansion with `nu=mu-sigma` gives `I_G(mu)=I_G(nu)>=0`, with equality
only at `mu=sigma`.

### 5. Exact global energy comparison

Both pieces have zero energy at `sigma`.  At any Dirac mass, the base term is
`-(d-1)(d-2)/d^2`, while the lifted term is `3(e-c_d)`.  The packet's explicit
coefficient makes the resulting Dirac energy exactly
`-(d-1)(d-2)/(2d^2)<0`.

### 6. Compatibility with the source theorem

Along every direction `mu != sigma`, the linear term at `sigma` vanishes and
the quadratic coefficient is a positive multiple of `I_G(mu)`.  Therefore
`sigma` is a strict local minimizer in the source's directional sense, even
though it is not global.  There is no conflict with Theorem 5.3(ii).

## Scope limitation

The packet disproves only the conjectured converse/global equivalence.  The
source's implication from global minimization to conditional positive
definiteness remains valid, as do its results under conditional
three-positive-definiteness of the full kernel.

## Recommended expert checks

1. Recompute the three spherical second-moment identities in the averaged
   cubic kernel.
2. Check the tensor-moment proof of strictness for the exponential dot-product
   kernel.
3. Confirm that the chosen coefficient gives the stated half-gap at a Dirac
   mass.

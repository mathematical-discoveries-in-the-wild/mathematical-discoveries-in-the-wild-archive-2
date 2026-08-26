# Verification report

Verdict: candidate partial result, likely valid; no full solution claimed.

## Linearization audit

For `A(h)=nabla^2 h+hI`, the normalized elementary symmetric function
satisfies

`D s_j(I)[B] = (j/(n-1)) tr(B)`.

Hence

`D[h^(1-p)s_j(h)]_(h=1) w`

equals

`(j/(n-1)) Delta w + (j+1-p)w`.

On degree-`k` spherical harmonics, `-Delta` has eigenvalue
`k(k+n-2)`. The resulting multiplier is:

- positive for `k=0`;
- `1-p>0` for `k=1`;
- at most `j+1-p-2jn/(n-1)<0` for `k>=2`, since
  `(n-1)(j+1)-2jn = n-1-j(n+1) <= -2`.

Thus the derivative has no kernel for every `0<=p<1` and
`1<=j<=n-2`, including `(p,j)=(0,1)`.

## C0-local upgrade audit

1. Uniformly `C^0`-near support functions have uniformly bounded Lipschitz
   constants, so interpolation gives convergence in every `C^beta`,
   `0<beta<1`.
2. Therefore `f=s_j(h)=g h^(p-1)` is `C^beta`-close to 1.
3. At `p=1`, the derivative of `h -> s_j(h)` is
   `(j/(n-1))(Delta+(n-1))`; its kernel consists exactly of degree-one
   harmonics.
4. Restricting to zero-degree-one support functions and zero-first-moment
   densities makes this derivative an isomorphism. Every area-measure
   density has zero first moment.
5. The inverse function theorem provides a centered support function near
   1 with density `f`. Classical uniqueness for the `j`-th area measure
   identifies the original body up to translation. Its translation vector
   is small because the original support function is `C^0`-near 1.
6. The original solution is therefore in the full nonlinear inverse-function
   neighborhood and equals the local branch solution.

## Scope checks

- Reflection preserves the equation when `g` is even; local uniqueness then
  forces the branch solution to be even.
- The proof does not provide a global `C^0` bound for arbitrary non-even
  solutions.
- The literal intrinsic-volume Brunn-Minkowski queue signal is not claimed:
  it is answered negatively by Theorem 1.1 of the source paper.

## Literature check

Local run indexes and bounded arXiv/web searches on 2026-08-13 used the exact
paper title, the exact non-evenness question, and near-isotropic/non-symmetric
Lp-Christoffel-Minkowski terms. They found the source and Li Chen's
constant-data uniqueness result (arXiv:1905.11043), but no later answer to
the stated non-even small-data problem.

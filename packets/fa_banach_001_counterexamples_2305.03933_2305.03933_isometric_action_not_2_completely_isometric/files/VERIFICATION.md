# Verification

## Algebra checks

1. \(C_jC_k=0\) and \(R_jR_k=0\), so both \(B_C\) and \(B_R\) are unital,
   commutative, three-dimensional operator algebras.
2. Matrix transpose reverses products in general, but is an algebra
   homomorphism on the commutative algebra \(B_C\).
3. Transpose preserves the Hilbert-space operator norm, so
   \(\theta:B_C\to B_R\) is isometric.
4. The direct-sum swap
   \(\alpha(b,c)=(\theta^{-1}(c),\theta(b))\) is an isometric algebra
   automorphism with \(\alpha^2=\mathrm{id}\).  It therefore generates a
   \(\mathbb Z_2\)-action on the unital, nondegenerately represented algebra
   \(A\subset B(\ell_2^3\oplus_2\ell_2^3)\).

## Matrix-norm check

For \(\xi=(\xi_1,\xi_2)\in\ell_2^3\oplus_2\ell_2^3\), write
\(\xi_1=(z_0,z_1,z_2)\).  The column block matrix sends \(\xi\) to
\((C_1\xi_1,C_2\xi_1)\), whose norm is \(\sqrt2|z_0|\); hence its norm is
\(\sqrt2\).  The transposed row block matrix sends \(\xi\) to
\((R_1\xi_1,R_2\xi_1)\), whose norm is
\((|z_1|^2+|z_2|^2)^{1/2}\); hence its norm is \(1\).  The direct-sum matrix
norm is the maximum of the two component norms.  Therefore \(\alpha^{(2)}\)
is not isometric.

## Literature and duplicate screen

Cheap indexes were searched for arXiv:2305.03933, isometric versus
\(p\)-completely isometric actions, unique \(L^p\)-operator matrix norms, and
row/column \(p\)-operator spaces.  No existing run packet was found.  Focused
primary-source searches did not locate a later answer to the exact remark.

## Scope audit

- The counterexample is exact at \(p=2\).
- It refutes only the auxiliary sentence that an isometric action might
  automatically be \(p\)-completely isometric.
- The main relaxed crossed-product theorem and the range \(p\ne2\) remain
  open in this packet.


# Verification Report

## Verdict

candidate partial result - likely valid

The proof is a short reduction to two theorems explicitly available in the
local source corpus. No numerical or symbolic computation is involved.

## Exact-Question Audit

On PDF page 22, immediately before Corollary 4.9, Dimant and Lassalle write
that they do not know whether their lifting result remains true when
\(n=cd(E,F)=cd(E)\).

Corollary 4.9 assumes that \(\mathcal K(E)\) is an \(M\)-ideal in
\(\mathcal L(E)\), that \(F\) has property \((M)\), and that
\(n=cd(E,F)<cd(E)\). The packet keeps the first hypothesis, takes \(F\) to
be nonzero finite-dimensional (hence automatically property \((M)\)), and
proves the equality endpoint.

## Critical-Degree Audit

For every nonzero \(F\), scalar multiplication by a fixed \(y\in F\) gives
\(cd(E,F)\le cd(E)\).

If \(F\) is finite-dimensional and \(k<cd(E)\), choose a finite basis of
\(F^*\). Each scalar coordinate of an \(F\)-valued \(k\)-homogeneous
polynomial is weakly continuous on bounded sets. Coordinate convergence in
finite dimension is norm convergence, so the vector polynomial is weakly
continuous on bounded sets. Hence \(cd(E,F)\ge cd(E)\), proving equality.

## Scalar-to-Vector Lifting Audit

Fix \(P\in\mathcal P(^nE,F)\) with norm at most one, \(u\in E\), \(v\in F\)
with \(\|v\|\le\|u\|^n\), and a bounded weakly null net \(x_\alpha\).
Let \(L=\limsup\|v+P(x_\alpha)\|\).

A subnet converges in norm value to \(L\). For each member choose a norm-one
functional \(f_\alpha\) satisfying
\[
f_\alpha(v+P(x_\alpha))=\|v+P(x_\alpha)\|;
\]
this is valid over both the real and complex fields by Hahn--Banach.
Compactness of \(B_{F^*}\) in norm gives a further subnet with
\(f_\alpha\to f\) in norm. Since the vectors \(v+P(x_\alpha)\) are bounded,
\[
f(v+P(x_\alpha))\longrightarrow L.
\]

The scalar polynomial \(f\circ P\) has norm at most one and
\(|f(v)|\le\|v\|\le\|u\|^n\). Scalar \(n\)-polynomial property \((M)\) gives
\[
L\le\limsup\|u+x_\alpha\|^n
\]
on the selected subnet, and that limsup is at most the original one. Thus
\((E,F)\) has vector \(n\)-polynomial property \((M)\).

## Dependency Audit

1. From \(\mathcal K(E)\) being an \(M\)-ideal in \(\mathcal L(E)\), the
   source's cited HWW theorem gives property \((M)\) of \(E\) and the compact
   approximation net required by vector Theorem 4.7.
2. Scalar Proposition 3.10 of arXiv:1005.1260 states that if
   \(n=cd(E)\) and \(E\) has property \((M)\), then \(E\) has scalar
   \(n\)-polynomial property \((M)\).
3. Vector Theorem 4.7 of arXiv:1102.3850 says that, at
   \(n=cd(E,F)\), its compact approximation hypotheses plus vector
   \(n\)-polynomial property \((M)\) imply the desired \(M\)-ideal.

All hypotheses line up after the two lemmas above.

## Edge Cases

- \(F=\{0\}\) is excluded only to keep critical degree meaningful; the
  \(M\)-ideal conclusion is then trivial.
- The proof works for real and complex scalars.
- The existence and finiteness of \(cd(E)\) are assumed, exactly as needed to
  state the endpoint.
- Arbitrary nets, not merely sequences, are handled by standard subnet
  realization of a bounded real limsup and compactness of the
  finite-dimensional dual ball.

## Upgrade Audit

The same proof extends whenever the selected norming functionals have a
norm-convergent subnet. Requiring this for all bounded nets in \(F^*\) forces
finite dimensionality, so it gives no general infinite-dimensional upgrade.

Weak-star compactness alone is insufficient: even if
\(f_\alpha\to f\) weak-star, the diagonal pairing
\((f_\alpha-f)(P(x_\alpha))\) need not vanish. Approximation of \(F\) by
compact operators likewise does not uniformly approximate the range of an
arbitrary critical-degree polynomial. No claim beyond finite-dimensional
ranges is made.

## Literature Audit

The bounded local and external searches are recorded in README.md and
main.tex. They did not reveal this exact finite-dimensional endpoint.
Novelty remains subject to specialist review.

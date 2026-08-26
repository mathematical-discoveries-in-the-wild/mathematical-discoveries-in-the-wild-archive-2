# Verification report

Verdict: candidate substantial partial result, likely valid.

## 1. Compact-support estimate

For supp(f) contained in U^m, supp(f^{*n}) is contained in U^{mn}. Hence

    ||f^{*n}||_{p,omega}
      <= s(mn)||f^{*n}||_p
      <= s(mn)||f^{*(n-1)}||_1 ||f||_p.

Condition (S) gives s(mn)^(1/n) -> 1. The remaining factors converge to
r_1(f) and 1. The reverse inequality follows from the continuous algebra
embedding Lp(G,omega) into L1(G). No commutativity is used.

## 2. Spectrum, not only radius

If f=f* is compactly supported, then P(f) is compactly supported for every
polynomial P with zero constant term. Radius equality for all P(f), spectral
mapping, and polynomial convexity of the compact real set sigma_1(f) force
sigma_{p,omega}(f)=sigma_1(f). The nonunital case is harmless because 0 lies
in the L1 spectrum and zero-constant polynomials still separate every point
outside a compact subset of the real line containing 0.

## 3. Discrete central extension

A central function on a discrete group is constant on conjugacy classes. A
nonzero constant on an infinite class is incompatible with weighted lp
membership because omega>=1. Thus central elements admit finite-support
central truncations. These commute with their tails, so spectral radius is
subadditive and the compact-core equality passes to the limit. Applying the
same result to polynomials gives spectrum equality for self-adjoint central
elements.

## 4. Finite direct factor

For G=H x F and omega_H(h)=omega(h,e), submultiplicativity gives uniformly in
t in F

    omega_H(h)/omega(e,t^{-1}) <= omega(h,t)
      <= omega_H(h) omega(e,t).

Therefore Lp(G,omega) and the finite direct sum of copies of
B=Lp(H,omega_H) have the same elements and equivalent norms. The e-coordinate
term in the convolution inequality on G shows that omega_H satisfies (LPAlg)
up to an inessential constant. Condition (S) restricts from G to H.

Since H is abelian, the source theorem makes B symmetric. Convolution on the
direct product identifies the algebra with B tensor C[F]. Finite-group
Fourier decomposition gives C[F] as a finite direct sum of full matrix
algebras, so the result is a finite direct sum of M_d(B). Symmetry of Banach
star algebras is stable under finite matrix amplification and finite direct
sums.

## 5. Completion barrier

The Fendler--Grochenig--Leinert/Hulanicki lemma used in the source assumes
r_A(a)=r_B(a) for every a in A. It does not allow replacement by an arbitrary
dense core. This was checked directly in Lemma 3.1 of the supporting 2006
paper. The packet therefore does not infer the general conjecture from the
compact-core theorem.

## Recommended expert checks

1. Confirm the polynomial separation formulation for the nonunital spectra.
2. Confirm normalization of Haar measure on the finite factor only changes
   the (LPAlg) convolution inequality by a scalar constant.
3. Confirm use of the standard Leptin--Wichmann matrix-stability theorem for
   nonunital Banach star algebras via unitization.
4. Assess novelty of the finite-direct-factor subcase against specialist
   weighted-algebra literature.


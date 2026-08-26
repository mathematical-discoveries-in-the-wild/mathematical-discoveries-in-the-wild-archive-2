# Verification audit

## Exact source match

Source PDF page 15 states Theorem 3.5 for `m=1`: a nontrivial,
Glaeser-stable, proper, consistent M-bundle whose associated Gr-bundle has a
section itself has a manifold section. The next sentence conjectures the same
theorem for `m>=2` and says the current pasting process does not prove it.

The source's main manifold-extension problem is answered by its own Theorem
3.4 and is therefore a same-paper extraction false positive. The packet
addresses the genuinely open higher-order conjecture instead.

## Proof obligations

### 1. Affine fixed-coordinate fibers

At each point of the circle, the standard-coordinate family is affine in the
two parameters `b,c`. Its jets have one fixed tangent plane and no nonlinear
terms of degrees `2,...,m-2`.

After centering at the point, write a height as

```text
f(u)=f_(m-1)(u)+f_m(u)+o(|u|^m).
```

For a new graph coordinate system,

```text
y=A u+a f(u),   v=c^T u+gamma f(u),
```

where tangent compatibility is invertibility of `A`. With `B=A^{-1}`, the
claimed inverse is

```text
u=B y-Ba[f_(m-1)(By)+f_m(By)]+o(|y|^m).
```

The first omitted substitution has degree `(m-2)+(m-1)=2m-3`, which is
strictly larger than `m` for `m>=4`. Substitution into `v` gives a fixed
linear term plus a linear transformation of the two varying homogeneous
pieces. Hence the realization image is affine.

### 2. Properness, consistency, and tangent selection

Every model height vanishes on the circle, so every jet is proper. All jets
have horizontal tangent, making the Gr-fiber the singleton horizontal plane.
For other coordinates, the fibers are defined as all realizations of the same
geometric jets. Re-realization in any compatible coordinate system therefore
stays in the prescribed fiber, which is exactly consistency.

### 3. Glaeser stability

Given an arbitrary allowed jet at `t_0`, use the single local height

```text
(b_0+theta-t_0) sigma^(m-1)/(m-1)! + c_0 sigma^m/m!.
```

At a neighboring base point `s`, rewrite the coefficient as

```text
(b_0+s-t_0)+(theta-s).
```

Thus every neighboring Taylor jet lies in its prescribed fiber. In any fixed
compatible Q-coordinates the same local surface is a `C^m` graph. Its Taylor
jets satisfy the Glaeser finite-point inequalities, so the initially chosen
jet survives refinement. Since it was arbitrary, all nonempty fixed-Q fibers
are stable; incompatible Q-fibers are identically empty.

### 4. Nonexistence of a manifold section

A section would have horizontal tangent along the circle and hence a unique
local height germ on the sheet containing the circle. On overlaps these germs
agree. Their `(m-1)`-st radial derivative defines a periodic `C^1` function
`b(t)`. Membership in the affine jet family forces the next mixed derivative,
and therefore `b'(t)`, to equal one. Its integral around the circle is both
zero by periodicity and `2*pi`, a contradiction.

## Computational checks

`code/check_periodic_jet.py` performs deterministic exact-rational tests of:

1. the inverse residual through total degree `m`;
2. the transformed-height formula through total degree `m`;
3. the inequality `2m-3>m` over a wide range of orders; and
4. the local identity
   `partial_theta partial_sigma^(m-1) Phi(t,0)=1`.

The checker is corroborative and does not replace the general calculation.

## Novelty and scope

Four cheap run indexes had no hit for the arXiv ID, title, or M-bundle
keywords. Bounded exact-title, exact-conjecture, and higher-jet arXiv searches
found the source but no later resolution through 11 August 2026. Novelty
confidence is moderate because the counterexample is elementary once the
correct jet order is chosen.

The construction works for every `m>=4`, which suffices to refute the source's
universal `m>=2` conjecture. It does not settle `m=2` or `m=3`. Human review
should focus on the coordinate-realization lemma, the Glaeser-stability
quantifiers for a fixed Q, and the patching of local height germs used to
define the global periodic coefficient.

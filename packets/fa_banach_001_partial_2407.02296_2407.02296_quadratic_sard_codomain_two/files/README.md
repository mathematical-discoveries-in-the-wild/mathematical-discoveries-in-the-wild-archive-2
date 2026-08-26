# Global Quadratic Sard Property in Target Dimension Two

Status: candidate_partial_result_likely_valid.

Source: Antonio Lerario, Luca Rizzi, and Daniele Tiberio, *Sard properties
for polynomial maps in infinite dimension*, arXiv:2407.02296, Remark 3.

## Result

Let f:H -> R^2 be a quadratic map in the source class P_2^2(H). Write

~~~text
f_j(x) = c_j + 2<a_j,x> + <A_j x,x>,  j=1,2.
~~~

The source's weak continuity assumption on Df forces the self-adjoint
Hessians A_1,A_2 to be compact. The packet proves, without any commutativity
or operator-pencil hypothesis, that every such map has the global Sard
property:

~~~text
Lebesgue_2(f(Crit(f))) = 0.
~~~

Thus the source's quadratic expectation is settled completely when the
codomain is R^2. The result includes noncommuting Hessians and pencils that
are singular in uncountably many projective directions.

## Mechanism

For a critical point x, choose a projective multiplier lambda with
D(lambda dot f)(x)=0. On every bounded ball the multiplier incidence set is
compact in the weak topology. If x,z have nearby multipliers lambda,mu,
the exact quadratic Taylor formula gives

~~~text
(lambda+mu) dot (f(z)-f(x))
  = <(A_lambda-A_mu)(z-x),z-x>.
~~~

Thus the corresponding critical values lie in a strip whose normal thickness
is proportional to the multiplier-arc length.

The new point is that a singular multiplier need not be exceptional. Only
multiplier directions whose stationary fiber has a nonconstant image matter,
and those directions are countable. In an affine chart, write
`B_t=A_2-tA_1` and `K_t=ker(B_t)`. If the quadratic part varies on `K_t`,
vectors belonging to distinct kernels yield a biorthogonal system
`(A_1 h_t,k_t)`. If the quadratic part vanishes but the linear part varies,
the stationary gradients yield a second biorthogonal system `(g_t,v_t)`.
Every biorthogonal system in a separable Hilbert space is countable.

Away from those active directions, every multiplier has a unique stationary
value even when it has many stationary points. Compactness of the incidence
set makes this value uniformly continuous. The resulting strip cover has
total area tending to zero, while small arcs covering the countable active set
contribute arbitrarily small area.

## Scope and novelty

This proves the full codomain-two case of the source's expectation that every
quadratic map into every finite-dimensional codomain has the Sard property.
It makes no claim in codomain dimension greater than two. The biorthogonality
argument is intrinsically planar: for two distinct projective multipliers the
relevant mixed pairing is forced to vanish, whereas in higher target
dimension it need only lie in the intersection of two hyperplanes.

Bounded searches on 2026-08-09 used the source title and authors together with
the phrases quadratic Sard Hilbert, compact self-adjoint pencil, active
stationary fiber, and critical values quadratic map. They found the source
paper and general infinite-dimensional Sard literature, but no matching
statement of the unrestricted target-dimension-two theorem. Novelty confidence
is moderate pending expert review.

## Files

- main.tex: self-contained proof packet.
- solution_packet.pdf: rendered review copy.
- source_paper.pdf: original arXiv source.
- figures/open_problem_crop.png: source Remark 3 on PDF page 3.
- code/check_slab_identity.py: finite-dimensional numerical identity check.
- VERIFICATION.md: proof and render audit.

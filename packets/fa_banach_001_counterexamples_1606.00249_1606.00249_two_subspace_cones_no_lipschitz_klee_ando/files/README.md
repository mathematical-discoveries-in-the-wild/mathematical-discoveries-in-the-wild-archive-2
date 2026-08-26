# Two closed subspace-cones refute both Lipschitz Klee-Ando extensions

Status: candidate counterexample, likely valid; full negative answer to Problem
1.5 of arXiv:1606.00249, subject to human review.

## Source question

Miek Messerschmidt, *Strong Klee-Ando Theorems through an Open Mapping
Theorem for cone-valued multi-functions*, arXiv:1606.00249v2 (2018), Problem
1.5 on page 3:

> Do Corollaries 5.5 and 5.6 remain true when, in their statements, the word
> "continuous" is replaced by the word "Lipschitz"?

Corollary 5.5 is the coadditivity theorem; Corollary 5.6 is the conormality
theorem. The source defines a cone only by closure under addition and
nonnegative scalar multiplication, so a linear subspace is a cone.

## Result

The answer is **no for both corollaries**, witnessed by the same Banach space
and the same pair of closed cones.

Let

```text
q : E -> Y
```

be a quotient map with no Lipschitz right inverse, let `X = E direct_sum Y`,
and put

```text
M = E direct_sum {0},        N = graph(q).
```

Then `M` and `N` are closed linear subspaces of `X`, hence closed cones, and
`M + N = X`.

- A Lipschitz conormal decomposition into `M` and `N`, restricted to points
  `(0,y)`, would give a Lipschitz right inverse of `q`.
- A Lipschitz coadditive selector for translates of `M` and `N`, restricted
  to the pair `(0,(0,y))`, would also give a Lipschitz right inverse of `q`.

For a concrete obstruction take the quotient

```text
q : ell_infinity -> ell_infinity / c_0.
```

It has no uniformly continuous right inverse, hence no Lipschitz right
inverse; this is Kalton's classical example, recorded with proof route in
Proposition 2.5 of arXiv:1909.10417.

The contradiction does not use positive homogeneity or the norm bound in the
conclusions. Thus the counterexample is stronger than the exact requested
failure.

## Proof intuition

The graph of a quotient map stores the lifting problem geometrically. A
decomposition of `(0,y)` into the horizontal subspace and the graph must choose
an element `e` with `q(e)=y`. Likewise, an intersection point between a
horizontal translate and a graph translate chooses such an `e`, up to sign.
Therefore a regular selector for either cone problem would be a regular
section of the original quotient.

## Scope

This settles Problem 1.5 exactly as stated, for both Corollaries 5.5 and 5.6,
because those results allow arbitrary collections of closed cones. It does
**not** settle the separate stronger Conjecture 1.6, which asks for a single
closed generating cone in an ordered Banach space with no Lipschitz positive
and negative parts.

## Verification and novelty check

Checked on 2026-08-09:

- the cheap run indexes for `1606.00249`, `Strong Klee-Ando`, `coadditivity`,
  `conormality`, and `Lipschitz`;
- the full source around Problem 1.5 and Corollaries 5.5--5.6;
- exact-phrase and close-variant web searches for the problem, the Lipschitz
  decomposition property, quotient right inverses, and Klee-Ando Lipschitz
  selections;
- the 2019 survey *On the Lipschitz decomposition problem in ordered Banach
  spaces and its connections to other branches of mathematics*;
- arXiv:1909.10417, especially Proposition 2.5 and Corollary 5.9.

The search found the source question, the later survey retaining the
single-cone problem, and quotient maps with no uniformly continuous right
inverse. It did not find the two-subspace graph reduction or a paper claiming
a negative answer to both source corollaries. Novelty confidence is bounded,
not exhaustive.

Recommended human review: verify the two one-line restrictions to `(0,y)` and
check that the source's use of "cone" indeed permits non-proper cones (it does,
by the definition on page 4). No computational claim is involved.

## Files

- `main.tex`: self-contained formal packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv:1606.00249v2.
- `supporting_paper_1909.10417.pdf`: quotient-map obstruction.
- `figures/open_problem_crop.png`: page-3 crop containing Problem 1.5.


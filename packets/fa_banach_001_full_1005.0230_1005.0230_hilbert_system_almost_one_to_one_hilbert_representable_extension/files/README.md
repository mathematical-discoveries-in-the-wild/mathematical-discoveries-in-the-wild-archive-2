# Problem 8.1(c): Hilbert-representable almost one-to-one extensions

Status: `candidate_full_solution_likely_valid`

Source: Eli Glasner and Benjamin Weiss, *On Hilbert dynamical systems*,
arXiv:1005.0230, Problem 8.1(c), source PDF page 13.

## Result

Every metrizable recurrent-transitive Hilbert system is an almost one-to-one
factor of a Hilbert-representable system.  This gives a complete affirmative
answer to the explicitly stated option (c) of Problem 8.1.

The proof does not settle options (a) or (b), nor Problem 8.2.

## Main mechanism

The source's Theorem 3.1 constructs an almost one-to-one extension
`X/K -> Y`, where `X` is Hilbert-representable and `K` is a compact subgroup
of the uniform Ellis group of `X`.  The new step is:

> A quotient of a weakly compact unitary system by a compact group of
> commuting unitaries is Hilbert-representable.

For the realification of the Hilbert space, assign to `x` all Haar-averaged
symmetric tensor moments

`M_n(x) = integral_K (k x)^(tensor n) dk`.

Their weighted direct sum is weakly continuous and equivariant.  Equality of
all moments gives equality of the two Haar orbit measures by the real
Stone-Weierstrass theorem, hence equality of the `K`-orbits.  Thus the moment
map embeds `X/K` into a weakly compact subset of a Hilbert direct sum.

The packet also proves that the compact subgroup from Theorem 3.1 lifts
strongly and continuously to commuting unitaries on a cyclic Hilbert
realization of `X`.

## Files

- `solution_packet.pdf`: human-readable proof packet.
- `main.tex`: packet source.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source page 13 showing Problem 8.1.
- `VERIFICATION.md`: proof and packaging audit.

## Novelty scope

Bounded searches on 9 August 2026 used the exact question, title, arXiv id,
"factor of a Hilbert-representable system", "almost 1-1" together with
Hilbert representability, compact-group quotients, and symmetric tensor
moments.  They found the source, later surveys repeating the question, and
arXiv:1602.05097, which proves factor closure only for a special
pro-oligomorphic Hilbert compactification.  No general answer to option (c) or
the compact-group quotient lemma was found.  This is not a definitive priority
claim.

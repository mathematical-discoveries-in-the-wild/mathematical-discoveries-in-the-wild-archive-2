# Full solution packet: bounded orbit = weak-* compact invariant core

Status: `candidate_full_solution_likely_valid`; novelty requires human review.

## Source question

Choiti Bandyopadhyay, *Common Fixed Points of Semihypergroup
Representations*, arXiv:2404.18261, Remark 3.6, asks whether the existence of
a bounded orbit in Theorem 3.5 can be replaced by an equivalent, more
conventional condition on the representation.

## Result

For every separately weak-* continuous affine semihypergroup action on a dual
Banach space, the following are equivalent:

1. some orbit is norm bounded;
2. some orbit is relatively weak-* compact;
3. the action has a nonempty weak-* compact convex invariant subset.

Thus condition 3 is an exact conventional replacement for the bounded-orbit
hypothesis, and Theorem 3.5 remains equivalent after this substitution.  The
proof is elementary but genuinely uses the semihypergroup action axiom: the
image of an orbit point under a coefficient map is a probability barycenter of
orbit points.  Banach--Alaoglu and uniform boundedness supply the two compactness
implications.

The packet also proves sharpness.  For the discrete semihypergroup coming from
the amenable group `Z`, the affine equicontinuous action on `R` given by
`pi(n,x)=x+n` has no common fixed point and no bounded orbit.  Hence the orbit
hypothesis cannot simply be deleted.

## Novelty note

The closed-convex-orbit-hull construction is standard in affine fixed-point
theory and appears in the semigroup precursor cited by the source.  A bounded
search found no explicit statement of the three-way equivalence for
semihypergroup actions or its use as the answer to Remark 3.6.  The mathematical
resolution is full; priority/novelty should not be claimed without expert
review.

## Files

- `solution_packet.pdf`: review-ready theorem and proof.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: arXiv source PDF.
- `tmp/`: compilation and rendering intermediates.

## Human review focus

Check only the barycentric invariance step for the weak-* closed convex hull;
all remaining implications are direct applications of Banach--Alaoglu and the
uniform boundedness principle.


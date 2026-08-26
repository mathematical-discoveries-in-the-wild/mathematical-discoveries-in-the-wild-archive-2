# Partial Result: Bochner Lp Preserves Weak-Star Sequential Density in the RNP Regime

Status: candidate_substantial_partial_likely_valid_needs_human_review

Run: fa_banach_001  
Agent: agent_lane_17  
Target: Saurabh Dwivedi, *A study on coreflexive Banach spaces*,
arXiv:2604.14068, Question 3.13.

## Exact target

Question 3.13 asks whether `L^p(mu,X)` is weak-star sequentially dense in its
bidual whenever `X` is weak-star sequentially dense in `X**`. It explicitly
says the question remains open even when both `X*` and `X**` have the
Radon-Nikodym property.

## New partial result

For every probability space and `1<p<infinity`, the answer is affirmative
under exactly those two RNP assumptions. No coreflexivity assumption is
needed.

The proof has two ingredients:

1. The infimum of the sup norms of weak-star sequential lifts defines a Banach
   norm on `X**`. By the open mapping theorem, there is one constant `K_X`
   such that every `x**` has a lifting sequence bounded by `K_X||x**||`.
2. Under RNP duality,

       Lp(mu,X)*  = Lq(mu,X*)
       Lp(mu,X)** = Lp(mu,X**).

   Write any `f` in the latter space as a series of simple increments with
   summable Lp norms. Lift every finite-range increment with the uniform
   constant and diagonalize over the summable series. Two dominated-
   convergence arguments prove weak-star convergence against every
   `Lq(mu,X*)` test.

The packet also gives a quantitative coordinate proof for purely atomic
probability spaces without RNP assumptions. That atomic clause is an instance
of the source's preceding ell_p-sum proposition and is not claimed as the new
result; it records how the uniform-lifting lemma repairs the domination needed
by the naive coordinate diagonal.

## Scope

For a non-atomic measure without the RNP identifications, the bidual may have
singular elements that are not `X**`-valued functions. Eight focused routes
were checked; none turns the hypothesis on `X**` into sequential lifts for
that singular part. The fully general question remains open.

## Files

- `main.tex`: theorem, complete proof, upgrade audit, and references.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: 14-page target PDF.
- `figures/open_problem_crop.png`: page 13 with Questions 3.11--3.13.
- `verification.md`: proof, source, artifact, and novelty audit.
- `runs/fa_banach_001/attempts/2604.14068_bochner_sequential_density_upgrade_attempts.md`:
  eight-route development and stopping obstruction.

## Novelty bound

The four run indexes contained no matching result. A bounded arXiv search for
coreflexive Banach spaces returned only the source. OpenAlex and Crossref
searches for the weak-star/Bochner formulation returned no direct match, and
OpenAlex listed zero citing works for the 2026 published source on 2026-08-11.
This is not an exhaustive literature certification.

## Review focus

Review the completeness of the sequential approximation norm first, then the
counting-measure dominated convergence used to combine all simple increments.
Once those two points are accepted, the RNP representation turns the theorem
into a direct proof of the explicitly highlighted subcase.

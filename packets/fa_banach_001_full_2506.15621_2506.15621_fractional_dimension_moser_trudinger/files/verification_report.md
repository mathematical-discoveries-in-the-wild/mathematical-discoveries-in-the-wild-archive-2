# Verification Report

Candidate: arXiv:2506.15621, question on a finer Moser–Trudinger inequality for non-integer CD(K,N) dimension.

## Claim checked

The natural real-dimensional inequality holds under a small-volume N-isoperimetric bound and a positive Cheeger bound. Consequently it holds for the infinite-volume CD(K,N) spaces in the positive geometric regime of the source's main theorem.

## Verdict

candidate_full_likely_valid_human_review_needed

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Exact source target | valid | Official source PDF page 18 explicitly asks for a finer non-integer-dimensional version. |
| Fractional truncation | valid | With k=ceil(p-1) and q=p/(p-1), qk>=p but q(k-1)<p. Thus the proposed truncation is minimal for L^p control at small values. |
| Integer consistency | valid | If p=n is integer, k=n-1 and the polynomial is the source's sum from j=0 to n-2. |
| Rearrangement | valid | The source's coarea and Hölder proof yields integral |v'|^p I^p <= integral lip(u)^p. Nothing in that calculation requires integer p. |
| Poincaré estimate | valid | The two profile bounds give the global linear estimate I(s)>=bar(h)s with bar(h)=min{h,c s_0^(-1/p)}, hence ||u||_p <= p||lip(u)||_p/bar(h). |
| Large-volume integral | valid | v is uniformly bounded for s>=s_0; the exponential remainder is O(v^(qk)), and qk>=p permits domination by a constant times v^p. |
| Energy split | valid | The two profile bounds imply e_0+e_1<=1 on the disjoint intervals (0,s_0) and (s_0,infinity). |
| Tail value | valid | Weighted Hölder gives (c v(s_0))^p <= D e_1 with D=(c/h)^p (p-1)^(p-1)/s_0. |
| Logarithmic change | valid | t=log(s_0/s) turns the small-volume weighted energy exactly into integral |w'|^p=e_0 and the measure into s_0 exp(-t)dt. |
| Algebraic endpoint bound | valid | If rho is the small-volume energy, maximizing (rho^(1/p)x+a)^q-x^q over x>=0 gives (a^p/(1-rho))^(1/(p-1)). |
| One-dimensional Moser lemma | valid | The standard lemma and proof use only Hölder duality for p and q, so p need not be integer. |
| Endpoint | valid | The tail estimate supplies a^p<=D(1-e_0), making the algebraic loss uniformly bounded and proving alpha=c^q. |
| CD corollary | valid with source hypothesis | The source's small-isoperimetric theorem is stated for the real curvature-dimension parameter and supplies c,s_0; the positive Cheeger constant supplies h. |
| Scope | valid | No sharp profile-liminf constant or assertion for geometrically degenerate CD spaces is claimed. |

## Endpoint algebra audit

For 0<rho<1 and q=p/(p-1), differentiating

    f(x)=(rho^(1/p)x+a)^q-x^q

shows the maximum occurs at

    x=rho^((p-1)/p)*a/(1-rho).

Substitution gives

    max f = a^q/(1-rho)^(q-1)
          = (a^p/(1-rho))^(1/(p-1)).

This is the exact estimate used in the shifted Moser lemma.

## Adversarial stress tests

- Merely replacing the integer n by a real p without changing the polynomial is not enough; the ceiling rule is derived from the integrability threshold.
- The proof includes variation of the boundary value v(s_0); it is not silently set to zero.
- The endpoint is not obtained from the false bound (A+B)^q<=A^q+B^q. The exact optimization controls the cross term.
- When e_0 approaches one, the tail estimate forces a to zero at the correct rate.
- When e_0 is zero, w is constant and the shifted lemma is immediate; when e_0 is one, a=0 and the classical lemma applies.
- The result concerns a real local Sobolev exponent and curvature-dimension parameter, not a fractional-order Sobolev seminorm.

## Deep upgrade audit

Attempt 1 used only v(s)<=B+c^(-1)log(s_0/s)^(1/q), proving the strict subcritical range alpha<c^q. Attempt 2 split the energy and controlled B from the tail, revealing the exact shifted Moser lemma and upgrading the result to the endpoint alpha=c^q. A further sharpness audit showed that the theorem should be stated using a uniform profile coefficient c, rather than claiming the largest constant from a bare liminf without additional regularity.

## Novelty check

On 2026-08-11, the exact source question, CD(K,N) Moser–Trudinger inequalities, fractional-dimensional weighted Sobolev inequalities, real-dimensional radial measures, and isoperimetric-profile proofs were checked against the run registry, solution, attempt, and proof-gap indexes and by bounded web/arXiv search. Known papers establish weighted one-dimensional fractional-dimension inequalities, but no direct CD(K,N) answer or the stated profile theorem was located. This is a bounded check, not a guarantee of novelty.

## Artifact verification

- source_paper.pdf is the official arXiv PDF and has 32 pages under PDF parsing.
- figures/open_problem_crop.png is rendered from source PDF page 18 and includes the definition, non-integer question, and geometric context.
- solution_packet.pdf has 4 pages; every page was rendered at 1.5x and visually inspected, with no clipping, overlap, or illegible content.
- The final LaTeX log has no undefined references, overfull/underfull boxes, or package warnings.
- The proof is exact and has no numerical component.

Confidence: 94/100.

Recommended action: specialist review by an analyst working on rearrangements, metric-measure Sobolev inequalities, or curvature-dimension spaces.

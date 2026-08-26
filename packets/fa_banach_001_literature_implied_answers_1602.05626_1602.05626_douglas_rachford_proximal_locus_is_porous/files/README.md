# The exceptional Douglas--Rachford locus is porous

Status: **literature-implied answer (full scope); likely valid; pending human review**.

Bauschke--Schaad--Wang, arXiv:1602.05626, Remark 3.3(ii), asks whether the
closed nowhere-dense set `D` of pairs of symmetric maximally monotone linear
relations whose Douglas--Rachford operator is proximal is porous.

The answer is affirmative. In reflected-resolvent coordinates,

```text
(A,B) -> (R_A,R_B),
```

the parameter space is the square of the operator-norm unit ball in the real
symmetric matrices, and `D` is exactly the commuting-pair locus. It is cut out
by the nonzero degree-four polynomial

```text
F(R,S) = ||RS-SR||_F^2.
```

Corollary 1.7 of Glazyrin--Karasev--Polyanskii, arXiv:2112.05382v5,
quantitatively avoids the zero set of any nonzero degree-`d` real polynomial
inside a Euclidean ball. A controlled radial contraction first moves every
commuting pair into the interior of the contraction ball; the corollary then
produces a proportional hole which remains inside the parameter space. The
packet records an explicit porosity constant `1/(64n)` in the source metric.

This is classified as a literature-implied answer because the supporting
paper does not mention Douglas--Rachford operators or the 2016 question. The
identification and boundary argument are supplied in the packet.

Files:

- `solution_packet.pdf`: compact proof and provenance note.
- `source_paper.pdf`: arXiv:1602.05626v1.
- `supporting_paper_2112.05382.pdf`: arXiv:2112.05382v5.

Search bounds: exact arXiv-id/title and `Douglas--Rachford`/`porous` searches
over the run indexes and parsed local corpus, plus exact-phrase and close-term
web searches restricted to arXiv/primary sources. No later paper explicitly
answering Remark 3.3(ii) was found. The supporting theorem was found by the
structural keyword search for polynomial zero sets and porosity.

Primary review focus: confirm the reflected-resolvent parametrization at
singular boundary points and the two norm-comparison inequalities used to
transfer the explicit hole back to the source metric.


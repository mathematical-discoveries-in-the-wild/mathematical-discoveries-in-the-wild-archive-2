# Verification report

Status: `literature_implied_answer (partial subcase); likely valid; human review requested`

## Source checks

- arXiv:2206.09224v2, PDF page 5, Remark 1.6 explicitly says the
  arbitrary-domain analogue remains open.
- The same paper's Proposition 3.1 is local on arbitrary planar domains. Its
  proof on PDF pages 8--9 identifies the index of a regular graph point with
  the local degree of `grad v` and concludes from Corollary 5(i) that every
  regular point is elliptic.
- If `grad v` is injective on a neighborhood, the graph normal
  `N=eta o grad v` is not repeated there because `eta` is injective. Thus each
  graph point is regular in precisely the paper's definition.
- In the Pogorelov classification used by the source, an elliptic point has a
  neighborhood whose tangent plane meets the surface only at that point. For a
  graph, the affine tilt is therefore nonzero on a punctured disk and has one
  sign because that disk is connected.
- arXiv:2506.03906v2, PDF page 13, Corollary 5.2 states Ball's theorem with
  exactly the required assumptions: convex domain, `C^1` potential, locally
  injective gradient, and one local supporting hyperplane.

## Proof-obligation audit

1. **Local finite curvature:** a nonnegative distribution is a Radon measure;
   its mass is finite on every relatively compact graph patch. This is enough
   for Pakzad Proposition 3.1.
2. **Strict local extremum:** ellipticity excludes every other intersection
   with the tangent plane. Continuity and connectedness of a punctured planar
   ball make the sign constant, hence the extremum strict.
3. **Ball propagation:** apply Corollary 5.2 to `v` for a minimum and to `-v`
   for a maximum. Local injectivity is unchanged by the sign.
4. **Global sign:** overlapping nonempty open balls cannot support strict
   convexity of `v` on one and strict concavity on the other. Path-connectedness
   of a connected planar domain propagates a single sign.
5. **Global strictness on convex Omega:** local convexity yields convexity on
   line segments. Any non-strict equality would force affinity on a segment,
   contradicting local strict convexity at an interior point.
6. **Alexandrov identification:** convex mollifications converge locally
   uniformly, hence their Monge--Ampere measures converge weakly. The very weak
   determinant converges distributionally from its `curl curl` definition.
   The two limits coincide. In dimension two, changing `v` to `-v` leaves the
   determinant unchanged.

No computational claim is used.

## Novelty and provenance

The cheap run indexes were searched for the target id/title and the main
Monge--Ampere, arbitrary-domain, degree, and gradient-fiber terms. A bounded
web/arXiv search for exact and close variants found Ball (1980) and the recent
restatement/proof in arXiv:2506.03906, but no paper explicitly applying them
to the open remark in arXiv:2206.09224. The result is therefore classified as
an agent-identified literature implication, not a new mathematical theorem.

The full problem remains unresolved because the added local-injectivity
hypothesis is not derived from `Det D^2 v >= 0`. Eight materially different
upgrade attempts are recorded in the linked attempt file.

## Artifact checks

- Original and supporting PDFs were downloaded from arXiv.
- Three evidence crops were rendered from PDF pages 5, 9, and 13 and inspected
  visually for legibility and correct scope.
- `solution_packet.pdf` is compiled from `main.tex`; all pages are rendered and
  visually inspected after compilation.

## Human-review recommendation

Likely valid as a partial, literature-implied subcase. Review should focus on
the exact localization of the Pogorelov elliptic-point definition and on the
measure-limit paragraph. No claim is made that the local-injectivity hypothesis
follows from the source assumptions.

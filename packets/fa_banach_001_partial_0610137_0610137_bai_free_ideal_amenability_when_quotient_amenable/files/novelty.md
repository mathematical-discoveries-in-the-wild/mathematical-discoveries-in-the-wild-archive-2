# Novelty and literature-status check

Status: bounded search; exhaustive priority is not claimed.

## Sources checked

- The lightweight run indexes (`registry_index.tsv`, `solutions/index.tsv`,
  `attempts/index.tsv`, and `proof_gaps/index.tsv`) were searched for arXiv
  `0610137`, the exact title, “ideal amenability”, “bounded approximate
  identity”, and three-space terminology.  No prior run result for this
  question was found.
- The source paper and its reference trail were inspected around Theorem 5.4
  and PDF page 13.
- Bounded exact-title and close-keyword web searches were made for later
  work on ideal amenability of extensions, ideals without a bounded
  approximate identity, and three-space results.
- A. Ranjbari and A. Rejali, “Ideal Amenability of Fréchet Algebras,”
  U.P.B. Sci. Bull. A 79(4) (2017), 51--60, was inspected from the primary
  journal PDF, especially Theorem 4.1 on printed pages 57--58.

## Finding

The 2017 theorem states an unrestricted result which, because Banach spaces
are quasinormable, would specialize to the source question.  Its proof does
not establish the necessary conclusion: it evaluates a functional in
`(I intersect J)*` outside its domain, and after the repair that yields
vanishing on `I`, the induced coefficient module is
`(J/closure(IJ+JI))*`, not necessarily the dual of a closed ideal of `A/I`.
A separate proof-gap packet records the exact issue.

No checked source was found stating the BAI-free theorem under the hypothesis
that the quotient is amenable, or the exact closed-sum/essential-intersection
criterion proved in this packet.  These claims should therefore be treated
as candidate new partial results with moderate novelty confidence, not as an
exhaustive priority assertion.

## Scope

The unrestricted question is not declared solved.  The packet proves a
strictly stronger quotient hypothesis and a structural criterion which
recovers the original BAI theorem.  A future valid proof of the 2017 theorem,
or an earlier unnoticed extension theorem, could lower the novelty claim.

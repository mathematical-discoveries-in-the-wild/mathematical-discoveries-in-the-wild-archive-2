# Verification report

Verdict: `candidate_partial_likely_valid` for Open Problems 3 and 3' of
arXiv:1511.07105, under the stated residual finite-dimensionality hypothesis.

## Proof audit

- If `pi` has dimension `d`, the character `det(pi)` occurs in
  `pi^(tensor d)`, so tensor closure puts `det(pi)` and all of its positive
  powers in the sub-semidual.
- For every finite subset of the discrete group, recurrence in a compact torus
  approximates the inverse determinant character by positive powers.  The
  resulting net is Fell-convergent, and Fell closedness puts `det(pi)^(-1)` in
  the sub-semidual.
- The canonical identity
  `bar(pi) = Lambda^(d-1)(pi) tensor det(pi)^(-1)` then proves that the
  finite-dimensional part of every sub-semidual is conjugation-closed.
- If `A_S=C*(G)/I_S` is RFD, `I_S` is the intersection of kernels of all
  finite-dimensional representations factoring through `A_S`.
- The finite-dimensional family is closed under conjugation.  The kernel
  intersection is therefore invariant under the full group algebra's
  inversion anti-automorphism `vartheta(u_g)=u_(g^-1)`.
- Inversion consequently descends to `A_S`, so every representation factoring
  through `A_S` has its conjugate factoring through `A_S`.  The support axiom
  for a sub-semidual then puts the conjugate back in `S`.
- Applying the theorem to `G_d` gives the RFD-qualified locally compact
  Eberlein result.  In the point-separating case, Theorem 7.1 of the source
  gives `B_r(G) subset B`, hence `A(G) subset B`.

## Upgrade attempts and obstruction audit

1. The first route tried to use a bounded unitary antipode on the quotient
   compact quantum group to settle the problem without hypotheses.
2. A deeper audit showed that descent of that bounded anti-automorphism to an
   arbitrary exotic completion is equivalent to invariance of `I_S` under
   inversion, which is the desired conclusion.  Invoking it would be circular.
3. Determinant recurrence and exterior-power duality produced the unconditional
   finite-dimensional theorem.
4. Intersecting finite-dimensional kernels upgraded that theorem to the full
   RFD-quotient result.
5. Finite-dimensional one-sided tensor-semigroup counterexample attempts are
   ruled out by the theorem itself.
6. Infinite-dimensional one-sided tensor families remain a possible route, but
   no rigorous weak-containment separation after discretization was obtained.

## Novelty check

A bounded primary-source search covered the exact phrases `sub-semidual` and
`Must B be conjugation-closed?`, the source title and authors, and the terms
`exotic group C*-algebra`, `comultiplication`, `antipode`, and `inversion`.
Sources checked included arXiv:1511.07105, arXiv:1211.4982, Woronowicz's primary
compact-quantum-group paper, and primary papers on exotic group completions.
No later paper explicitly resolving Open Problem 3 and no explicit RFD theorem
matching this packet were found.  Novelty confidence is moderate.

## Packet and visual checks

- `latexmk` completed with resolved references and no logged warnings,
  overfull boxes, or underfull boxes.
- The final packet contains four A4 pages.
- Every page was rendered at 150 DPI and inspected at original resolution.
  The source crop is readable; the determinant and RFD proofs, antipode audit,
  references, margins, and page numbers are clean, with nothing clipped.
- Text extraction confirms the finite-dimensional theorem, the RFD upgrade,
  the limitations, and the human-review focus.

## SHA-256

```text
14dc383c7ba1d87fbe964eee407da1eb1e8fc01ea83048167af0739f1b7fd6b1  solution_packet.pdf
0313c1c6ba1ac7cefecf15443e5c847efb9490a45e03790a5f5776bd3a966a22  source_paper.pdf
1ff4055a1387be54b717f73219dd29e676f863c46a468a9c36ad4e8786fcca1d  supporting_paper_woronowicz_compact_quantum_groups.pdf
0d28bc6c1e4eabb6c0ae68c158a257ab3129c3d8677153ae622401f2e1247c9c  figures/open_problem_crop.png
```

## Human-review recommendation

Check two points first: that pointwise recurrence of determinant characters is
indeed Fell convergence in the one-dimensional stratum, and that RFD gives the
exact preimage kernel equality used to descend inversion.  Then confirm the
source's Theorem 7.1 implication used in the locally compact corollary.

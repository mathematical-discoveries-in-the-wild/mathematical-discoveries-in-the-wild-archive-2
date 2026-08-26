# Counterexample Packet: The Fixed-Point Converse Fails

Run: `fa_banach_001`

Status: `candidate_counterexample_likely_valid`

## Source Problem

- Ali Jabbari, Ali Ebadian, and Madjid Eshaghi Gordji, *A Weak Form of
  Amenability of Topological Semigroups and its Applications in Ergodic and
  Fixed Point Theories*, arXiv:2005.08089; Collectanea Mathematica 74 (2023),
  149-171.
- Remark 5.3 on source page 18 asks whether the fixed-point condition in
  Corollary 5.2(ii) implies `phi`-amenability of `S`.
- `source_paper.pdf` is the original arXiv paper.
- `figures/corollary_5_2_crop.png` and `figures/open_problem_crop.png` show the
  complete referenced condition and Remark 5.3.

## Claimed Contribution

The converse is false, even for a four-element discrete semigroup and a
nontrivial character.  Let

`S = C_2 x R_2`,

where `R_2={0,1}` is the right-zero semigroup (`ij=j`), and define

`(eps,i)(delta,j)=(eps+delta mod 2,j)`,  `phi(eps,i)=(-1)^eps`.

Then `P(phi)={0} x R_2` is a two-element right-zero semigroup.  Every
continuous affine action of `P(phi)` on a nonempty compact convex set has a
common fixed point: take a fixed point of either action map and use
`p p_0=p_0`.

Nevertheless, `S` is not right `phi`-amenable, hence is not `phi`-amenable.
Right `phi`-amenability would produce a functional `m` on `C(S)` satisfying

`m(phi)=1`,  `m(R_s f)=phi(s)m(f)`.

For the two kernel idempotents `p_i=(0,i)`, let `u_i` indicate the second
coordinate `i`.  Right translation by `p_i` annihilates
`phi u_(1-i)`.  Invariance therefore gives
`m(phi u_0)=m(phi u_1)=0`, contradicting
`phi=phi u_0+phi u_1` and `m(phi)=1`.

The packet proves the needed invariant-functional consequence directly from
the source definition, so the contradiction does not depend on accepting a
separate mean-characterization theorem.

## Scope

This completely answers the literal two-sided wording of Remark 5.3.  The
source defines `phi`-amenable to mean both left and right `phi`-amenable, while
Corollary 5.2(ii) is one-sided.  The example exploits precisely that mismatch.
It does not answer the repaired one-sided question asking whether condition
(ii) implies *left* `phi`-amenability.

For completeness, the same mechanism gives a two-element counterexample if
the trivial character is allowed: take `S=R_2` and `phi=1`.

## Verification Status

Verdict: `likely valid`, pending human review.

The proof is finite-dimensional and exact.  The verifier script checks all
associativity and character identities and independently proves inconsistency
of the normalized invariant-functional linear system over the rationals.
Human review should focus on the left/right module orientation and the literal
meaning of `phi`-amenable in Remark 5.3.

## Novelty Check

The run indexes were searched for arXiv:2005.08089, the title, Remark 5.3,
`P(phi)`, fixed-point converses, right-zero semigroups, and character
amenability.  No duplicate result, attempt, or proof-gap packet was found.

Bounded web/arXiv searches on 2026-08-09 used the exact Remark 5.3 wording,
the title and DOI, the source authors, `P(phi)`, `right zero`, and
`character amenable`.  They found the source/preprint and bibliographic pages,
but no later solution, correction, or matching counterexample.  SciRate's
arXiv record displayed zero discussion/citation links.  This is not an
exhaustive novelty claim.

## Files

- `main.tex`: full counterexample proof and scope analysis.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: original source paper.
- `figures/`: real source-page crops for Corollary 5.2 and Remark 5.3.
- `verification.md`: adversarial proof check.
- `code/verify_finite_semigroup.py`: exact finite verifier.
- `tmp/`: LaTeX intermediates and rendered QA pages.

## Human Review Recommendation

Send to a specialist in semigroup amenability.  The construction is
elementary; the key editorial question is whether Remark 5.3 intended the
defined two-sided notion or the repaired left-sided notion suggested by its
fixed-point context.

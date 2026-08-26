# Verification report

## Claim checked

Problem 10.8 has an affirmative answer for finitely generated virtually
abelian groups with no nonzero homomorphism to the reals: the explicit sets
`F_N=B_N T` have right-translation Wasserstein defect `O_g(1/N)`.

## Source check

- Theorem 10.4, Example 10.7, and Problem 10.8 were checked in the ingested
  official arXiv source and the local 36-page source rendering.
- The question asks for a genuine finite set rather than the multiset allowed
  by rational approximation; it is not answered later in the source.
- The crop includes the motivation, full hypotheses, and complete formula.

## Adversarial step check

| Step | Verdict | Reason |
| --- | --- | --- |
| Normal lattice subgroup | valid | A finitely generated virtually abelian group has a finite-index torsion-free abelian subgroup after removing torsion; its normal core remains finite index and free abelian. |
| Transfer cancellation | valid | The cocycle identity makes the sum of coset displacements a homomorphism `Gamma -> A`; a nonzero value would survive under a real linear functional. |
| Layer formula | valid | Right multiplication sends `a t` to `(a+c_t(g)) sigma_g(t)`; relabelling the finite layers gives the displayed defect exactly. |
| Layer collapse | valid | Each shifted-box difference has mass zero and `l1` norm `O(1/N)`; pairing identical lattice coordinates across two layers has fixed cost. |
| Augmentation square | valid | For `R[Z^d]`, mass and first moment are precisely the augmentation and the class in `I/I^2`; their vanishing places the kernel in `I^2`. |
| Second-difference estimate | valid | Pairing a signed first difference with its translate costs a fixed word length times the `l1` boundary size `O(1/N)`. |
| Finite-set conclusion | valid | The triangle inequality reduces every pair `g,f` to the two one-sided defects. |

No amenability property is used beyond the source's ambient problem; virtually
abelian groups are amenable automatically.  The theorem correctly preserves
the no-real-characters hypothesis.

## Upgrade attempts

The recovery reread the eight routes in
`attempts/2509.10686_uniform_finite_transport_upgrade.md`.  The direct
deduplication, ordinary Folner boundary, layer-cake, virtually nilpotent, and
general tiling routes all retain the exact gaps recorded there.  None supports
an honest upgrade beyond the packaged virtually abelian theorem.

## Novelty bound

On 21 August 2026, searches covered all four run indexes, the exact title and
arXiv id, exact phrases from Problem 10.8, and primary searches combining
uniform finite subsets with Wasserstein or Arens--Eells almost invariance.
No later exact answer or statement of this partial theorem was found.  This is
a bounded search and should not replace an expert bibliography check.

## Verdict

Likely valid substantial partial result; send to an expert.  The unrestricted
amenable-group problem remains open in this packet.

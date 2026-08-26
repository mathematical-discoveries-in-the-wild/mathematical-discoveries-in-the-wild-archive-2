# Verification report

## Verdict

Likely valid full positive solution to Remark 4.11(v) / Problem 5 of arXiv:2508.20061v3. Human review is recommended before dissemination.

## Claim audited

For Thompson's group `F`, its commutator subgroup `F'=[F,F]` is framenable in the sense of Definition 3.1 of the source paper.

## Adversarial checks

1. **The index set must be countably infinite.** The source explicitly defines “countable” to mean countably infinite. The set of interior dyadic rationals is countably infinite, and transitivity makes a section of the orbit map a countably infinite subset `S` of `F'`.

2. **No repetitions in the selected orbit.** Exactly one representative is selected for each orbit point. Hence `s -> s(x_0)` is bijective from `S` to the dyadic set, and `{pi_s delta_{x_0}:s in S}` is exactly the standard orthonormal basis, not merely a total family with uncontrolled multiplicities.

3. **Bessel and total conditions.** Because the selected family is an orthonormal basis, its coefficient sum equals the squared norm. It is therefore a Parseval frame and, a fortiori, a weak frame.

4. **Almost invariance is in the same representation.** For each `g in F'`, the standard endpoint-germ theorem says that `g` is the identity on some interval `[0,epsilon_g]`. Consequently `pi_g delta_{2^{-n}}=delta_{2^{-n}}` for all sufficiently large `n`. Thus one sequence of unit vectors is pointwise almost invariant for every group element, which is exactly `1_{F'} prec pi` for a countable discrete group.

5. **Transitivity really holds for `F'`.** Cannon--Floyd--Parry identify `F'` with the subgroup trivial near both endpoints and establish the relevant transitivity on interior dyadic points (Theorem 4.1 and Lemma 4.2). An elementary reduction is also recorded in the packet: start with an element of `F` mapping one dyadic point to another and correct its two endpoint slopes by elements supported on the two sides of the target point; the corrected element fixes the target and lies in `F'`.

6. **The action defines a unitary representation.** Each group element permutes the dyadic set, so its linear action on the standard basis extends to a unitary on `ell^2(D)`.

7. **No contradiction with source Remark 4.10.** That remark shows failure of the Bessel property for the orbit indexed by the whole group `F`: infinitely many stabilizer elements repeat a nonzero coefficient. Definition 3.1 permits a countably infinite subset. A transversal removes all repetitions and gives an orthonormal basis. The packet uses `F'` because its endpoint-triviality supplies almost invariant delta vectors.

8. **No hidden amenability claim.** A weak frame over a proper subset does not invoke the source's amenability characterization, which requires a weak frame vector over the whole group. The argument proves framenability only and does not address whether `F` or `F'` is amenable.

## Literature and novelty check

On 11 August 2026 the run indexes and bounded web/arXiv searches were checked for arXiv:2508.20061, “framenable”, “commutator subgroup”, “Thompson”, and direct variants of “`[F,F]` is framenable”. The arXiv source (v3, December 2025) still states the problem, and the 2026 journal landing page reported no citing papers. No later direct answer was found. This supports, but cannot guarantee, novelty.

## Recommended verifier focus

Confirm the cited Thompson-group facts in Cannon--Floyd--Parry, especially the passage from transitivity of `F` to transitivity of `F'`. After that, the proof is a direct verification of Definition 3.1.

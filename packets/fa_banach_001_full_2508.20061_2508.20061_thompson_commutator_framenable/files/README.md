# 2508.20061 — the commutator subgroup of Thompson's group F is framenable

Status: candidate full result, likely valid, human review needed.

Model: GPT5.6.

Source: Dorin Ervin Dutkay, Catalin Georgescu, and Gabriel Picioroaga, *Frame Vector Group Representations and Amenability Properties*, arXiv:2508.20061v3, Remark 4.11(v) on source PDF page 21.

## Result

The paper's Problem 5 has a positive answer: the commutator subgroup `F'=[F,F]` is framenable.

The proof uses the permutation representation of `F'` on the countably infinite set

    D = Z[1/2] intersect (0,1)

of interior dyadic rationals. Two standard facts about Thompson's group are decisive:

- `F'` acts transitively on `D`;
- every element of `F'` is the identity on a neighborhood of 0 (and of 1).

Fix `x_0` in `D` and select one group element for each point of the orbit of `x_0`. The corresponding translates of `delta_{x_0}` are exactly the standard orthonormal basis of `ell^2(D)`, so they form a weak frame over a countably infinite subset of `F'`. On the other hand, the vectors `delta_{2^{-n}}` are eventually fixed by every element of `F'`, hence are almost invariant. Thus the same representation satisfies both requirements in the source's definition of framenability.

The packet first proves a general transitive-action criterion, then applies it to `F'`. It also explains why this does not conflict with Remark 4.10 of the source: that remark sums over the whole group and therefore repeats stabilizer orbits infinitely often, whereas framenability permits a sparse subset and the proof uses one representative per orbit point.

## Files

- `main.tex`: theorem, proof intuition, full proof, scope, and novelty check.
- `solution_packet.pdf`: compiled human-review packet.
- `verification_report.md`: adversarial proof audit.
- `source_paper.pdf`: official arXiv PDF.
- `figures/open_problem_crop.png`: source PDF page 21 crop containing Remark 4.11(v).
- `code/crop_source.py`: reproducible crop script.

## Human review recommendation

Review as a likely valid full positive solution. The highest-value check is simply that the standard Thompson-group facts are being invoked with `F'`, not merely `F`; Cannon--Floyd--Parry, Theorem 4.1 and Lemma 4.2, supply exactly these facts. The representation-theoretic step is elementary and is fully written out.

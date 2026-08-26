# Candidate counterexamples to Questions 5.3 and 5.4 via the counit

Status: **candidate full counterexamples as stated, likely valid, needs expert review**

Source: Benjamin Anderson-Sackaney, *On Ideals of L1-algebras of Compact
Quantum Groups*, arXiv:2111.13247, Questions 5.3 and 5.4 on PDF page 30.

## Result

Both questions have negative answers as written.

Take any noncoamenable compact quantum group, concretely the compact dual of
the nonamenable free group `F_2`, and let `epsilon^u` be its universal counit.
The counit is a norm-one convolution idempotent and its left multiplier on
`L^infinity(G)` is the identity. Therefore:

- the corresponding compact quasi-subgroup is all of `L^infinity(G)`;
- its preannihilator `J^1(N)` is the zero ideal;
- the zero ideal has the constant-zero bounded right approximate identity;
- `epsilon^u` is not in the reduced measure algebra, since otherwise the
  counit would descend to the reduced C*-algebra and the compact quantum
  group would be coamenable.

This disproves Question 5.3. It also disproves Question 5.4, because the
annihilator of the counit's multiplier range is the same zero ideal, which
has a brai although the quantum group is not coamenable.

## Scope warning

These are exact edge-case counterexamples. They do not address repaired
versions requiring a proper compact quasi-subgroup, a nonzero ideal, or a
proper multiplier range (such as the source's earlier intrinsic-group
hypothesis).

## Files

- `solution_packet.pdf`: source screenshot, theorem, proof, verification, and
  novelty bounds.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: official arXiv PDF.
- `figures/questions_5_3_5_4_crop.png`: both source questions.
- `VERIFICATION.md`: proof audit and reviewer checklist.

No computational code is included because the counterexample is formal and
structural.

## Human-review priority

Confirm that the source permits the whole algebra as a compact
quasi-subgroup and uses the standard convention under which the zero ideal
has a brai. Then verify the standard equivalence between descent of the
universal counit and coamenability for compact quantum groups.

## Novelty status

A bounded search on 11 August 2026 covered the run indexes, exact question
wording, the source title and arXiv id, the published version, the author's
thesis, contractive-idempotent/counit combinations, and later citations. No
explicit statement of this edge-case counterexample was found. This is
provisional novelty evidence only.

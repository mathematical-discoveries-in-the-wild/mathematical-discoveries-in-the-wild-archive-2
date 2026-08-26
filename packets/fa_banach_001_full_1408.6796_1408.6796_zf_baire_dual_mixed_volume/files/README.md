# Choice-free dual mixed volume characterization

**Status:** candidate full result, likely valid; pending human review.

**Source question:** C. H. Jiménez and I. Villanueva,
*Characterization of dual mixed volumes via polymeasures*,
[arXiv:1408.6796](https://arxiv.org/abs/1408.6796), Question 3.5,
PDF page 12.

## Result

The consistency question has an affirmative answer, simultaneously in every
dimension `n >= 2`.

Let `D_n` say that every separately radially additive, rotation-invariant
real functional of `n` star bodies in `R^n` which vanishes whenever two
arguments intersect only at the origin is a scalar multiple of the dual mixed
volume. Then

```text
Con(ZF)  =>  Con(ZF + "D_n holds for every n >= 2").
```

Indeed, Shelah proved that `ZFC` is equiconsistent with
`ZF + DC + "every set of reals has the Baire property"`. Since ZF and ZFC are
themselves equiconsistent, this is relative to `Con(ZF)`. In any such model,
every additive section on the Polish group
`C(S^{n-1})` is Baire measurable and therefore continuous by the Pettis
argument. The star-body functional consequently becomes positively
homogeneous and separately bounded. The bounded branch of Theorem 3.4 in the
source paper then gives the required scalar multiple of dual mixed volume.

Thus the inaccessible cardinal used in the familiar Solovay-model route is
not needed: the all-sets-Baire-property model has exactly the regularity the
argument requires.

## Files

- `main.tex` / `solution_packet.pdf`: precise statement and proof.
- `source_paper.pdf`: local copy of arXiv:1408.6796.
- `figures/open_question.png`: exact source excerpt.
- `references/shelah_1984_inaccessible_away.pdf`: decisive supporting
  consistency theorem (Conclusion 7.17).
- `verification.md`: mathematical, literature, and artifact audit.
- `../../../attempts/1408.6796_solovay_baire_automatic_continuity.md`:
  six-step proof, upgrade, and adversarial audit.

## Scope and review focus

This is a relative-consistency answer, not a proof of the characterization in
bare ZF and not an independence theorem. Recommended review focus:

1. transfer of the all-sets-Baire-property axiom from the reals to arbitrary
   Polish spaces via the Baire-isomorphism theorem;
2. formal availability under `DC` of the compact-metric analytic ingredients
   in the bounded branch of the source theorem;
3. the equiconsistency statement in Shelah (1984), Conclusion 7.17.

Bounded exact-title, exact-question, phrase, author, and citation searches on
2026-08-11 located the two source papers and later unrelated dual-volume work,
but no subsequent resolution. Novelty confidence is moderate: the proof is
short once the Polish-group automatic-continuity step is isolated.

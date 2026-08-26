# A unit-norm full-spark frame that is not 1-splittable

Status: **candidate full counterexample, likely valid, novelty uncertain;
send to human review**.

Source question: Xuemei Chen, Christian Kummerle, and Rongrong Wang,
*Sparse Recovery for Overcomplete Frames: Sensing Matrices and Recovery
Guarantees*, arXiv:2408.16166. Immediately after Definition 3.5, the authors
conjecture that all full-spark frames are splittable for a sufficiently small
positive constant.

## Result

The conjecture is false already for sparsity `s=1` in `R^2`. Consider the
unit-norm frame with columns

```text
a = (-7/25, -24/25),  b = (1,0),  c = (20/29, -21/29).
```

Every two columns are independent. Two exact witness pairs force respectively

```text
beta >= 391/2065  and  beta <= 23/175,
```

but `391/2065 - 23/175 = 598/10325 > 0`. Hence no positive `beta` makes the
frame 1-splittable. All best one-term approximants used in the witnesses are
unique, so the result is unaffected by the general nonuniqueness of best
atomic sparse approximations.

## Files

- `solution_packet.pdf`: self-contained exact proof.
- `main.tex`: source of the proof packet.
- `problem.md`: exact formulation and scope.
- `solution.md`: plain-text proof companion.
- `verification.md`: adversarial checklist and exact values.
- `references.md`: source and bounded novelty audit.
- `computations/verify_exact.py`: exact rational verification using only the
  Python standard library.
- `computations/verify_exact_output.txt`: recorded successful verification.
- `source_paper.pdf`: source paper containing the conjecture.

The numerical search script in `attempts/` was used for discovery only. No
floating-point computation is used in the proof.

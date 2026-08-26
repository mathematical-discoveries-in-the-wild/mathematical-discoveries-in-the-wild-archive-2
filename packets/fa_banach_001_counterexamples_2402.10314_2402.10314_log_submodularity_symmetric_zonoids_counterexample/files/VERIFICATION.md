# Verification report

Status: `candidate_counterexample_likely_valid`

## Claim checked

The conjecture following equation (44) in arXiv:2402.10314v3 is false as
stated.

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Source transcription | valid | Page 27 conjectures equation (44) for `A,B,C` symmetric zonoids and `mu` any log-concave measure. |
| Measure class | valid | `mu` is normalized two-dimensional area on a convex parallelogram. A uniform measure on a convex body is log-concave. |
| Set class | valid | `A,B,C` are centered rectangles with nonempty interior, hence symmetric zonotopes and symmetric zonoids. |
| Minkowski sums | valid | Their coordinate half-widths are `(1,1)`, `(2,11/10)`, `(11/10,2)`, and `(21/10,21/10)`. |
| Coordinate change | valid | `(u,v) -> (u+v,u-v)` has constant Jacobian magnitude `2`, which cancels from every normalized-area ratio. |
| Exact measures | valid | The four probabilities are `19/80`, `11/40`, `11/40`, and `41/80`. |
| Violation | valid | The left side minus the right side is `59/1280`, strictly positive. |
| Density robustness | valid but optional | The example is already full-dimensional and absolutely continuous. Approximate-identity convolution gives a smooth positive log-concave counterexample because the four rectangle boundaries are continuity sets and the violation is strict. |

## Exact computation

For a centered rectangle `R(s,t)=[-s,s] x [-t,t]`, its preimage in the
`(u,v)` coordinates is

```text
|u+v| <= s,  |u-v| <= t,  |u| <= 4,  |v| <= delta.
```

The support rectangle in `(u,v)` coordinates has area `16*delta`.

- If `s=t=q`, then the first two constraints become
  `|u|+|v|<=q`. Its area is `4*q*delta-2*delta^2`, so the probability is
  `q/4-delta/8`.
- For `(s,t)=(2,11/10)`, the constraint `|u+v|<=2` is redundant because
  `|u-v|<=11/10` and `|v|<=1/10` imply `|u+v|<=13/10`. Thus the probability
  is `(11/10)/4=11/40`. The swapped rectangle is identical by symmetry.

Substitution of `delta=1/10`, `q=1`, and `q=21/10` yields the table above.

## Computational sanity check

Run:

```bash
python code/check_exact_measures.py
```

The script uses `fractions.Fraction`, reproduces all four probabilities, and
checks the exact defect `59/1280`. It is a transcription check; the proof is
the area computation above.

## Novelty check

The local lightweight indexes and bounded web queries described in the README
found no prior counterexample or later resolution. The official arXiv record
lists v3, revised 2026-02-26, as current, and that version still prints the
conjecture. Novelty is plausible but not certified.

## Reviewer focus

Confirm that the phrase "any log-concave measure" is intended literally. The
example uses neither singularity nor lower-dimensional test bodies: the
measure has a full-dimensional density and every test set is a rectangle with
nonempty interior.

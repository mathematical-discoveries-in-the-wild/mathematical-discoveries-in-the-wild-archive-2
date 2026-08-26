# Verification report

## Claim checked

The universal lower-ratio existence assertion in Remark 2 of arXiv:2407.05062
is false for both the single-operator requirement (75) and its averaged
version (82).

## Verdict

Valid; candidate full counterexample; confidence 99/100.

## Source audit

- PDF pages 23--25 give the ratio setup and Eqs. (74), (75), (81), and (82).
- PDF page 29, Remark 2, conjectures existence for any prescribed positive
  `alpha_1` or `alpha_2`.
- Eq. (10) permits `Phi(X)=X^2-X^3` and expressly imposes no positivity,
  linearity, or normalization constraint on `Phi`.

## Proof audit

| Step | Status | Reason |
| --- | --- | --- |
| Scalar specialization | valid | `C` is a Hilbert space and real scalars are self-adjoint operators. |
| Source-admissible map | valid | Use the two allowed coefficients `a_2=1` and `a_3=-1`, with `V=1`. |
| Continuous target | valid | `f(x)=1` is continuous on `[0,1]`. |
| Sigmoid brackets | valid | `1 +/- delta sigma(x)` satisfy the stated error bounds for sufficiently small positive `delta` and remain strictly positive. |
| Vanishing numerator | valid | `Phi(f(A))=Phi(1)=1-1=0`. |
| Invertible denominator | irrelevant to rescue | Any admissible scalar denominator is nonzero, but zero divided by it remains zero. |
| Contradiction | valid | `0 >= alpha_2` is false for every `alpha_2>0`. |
| Averaged formula | valid | `k=1`, weight one, reduces Eq. (82) to the same calculation. |

## Computational audit

Command:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2407.05062_zero_numerator_refutes_positive_lower_ratio/code/verify_counterexample.py
```

The script uses exact rational arithmetic and confirms the contradiction for
representative positive and negative nonzero denominators.  This is a sanity
check, not a premise of the proof.

## Novelty audit

Search date: 2026-08-11.

Searched the run registry/solution/attempt/proof-gap indexes for the arXiv id,
title, and ratio-approximation terms.  Also searched current web/arXiv results
for the exact title, `ratio type approximation`, the conjecture language, the
author, and arXiv:2407.05062.  The searches found the source paper and mirrors,
but no later paper explicitly resolving Remark 2.  Search absence is not proof
of novelty.

## Scope and reviewer focus

The packet refutes only the lower-ratio half, which is sufficient to disprove
the universal existence conjecture.  It does not claim the upper-ratio half is
false.  A reviewer should check whether the author intended, but omitted, a
uniform strict-positivity condition on `Phi(f(A))`.  Such a condition would be
a substantive repair, not part of the printed conjecture.

Human review recommendation: **send to human**.

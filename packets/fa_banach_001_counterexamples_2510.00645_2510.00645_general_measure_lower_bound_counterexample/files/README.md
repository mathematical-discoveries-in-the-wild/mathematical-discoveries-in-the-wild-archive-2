# Counterexample to the direct general-measure lower bound

Source: Andreas Malliaris and Francisco Marín Sola, *Quantitative improvements of functional inequalities under concavity properties*, arXiv:2510.00645 (2025).

Status: candidate counterexample, likely valid; scoped negative answer to the lower-bound half of Question 6.1.

## Result

The direct same-form extension of Theorem 3.4 to arbitrary positive Borel measures is false, already with the original choice `psi=log` and the affine function `N(t)=t`.

The packet gives two versions:

- an exact three-atom example `mu=delta_1+delta_2+6 delta_3`; and
- a stronger example in which `mu` has a smooth compactly supported density made from three narrow translated bumps.

For the smooth example, with `f(t)=2^(1-t)` and `h=5/2`, one has `u=V/2` and `Phi(h)=2`, but

```text
int N f dmu
  < (u/Phi(h)) int_[0,Phi^{-1}((V/u)Phi(h))] N dmu.
```

Thus the failure is not caused by ambiguity at an atom. The natural fractional-atom repair also fails in the discrete prototype by the exact gap `1/4`.

## Scope

This disproves the natural extension retaining the conclusion of Theorem 3.4 with the distribution function of a general measure. It does not rule out a differently normalized, measure-regularity-dependent, or otherwise modified inequality. The corresponding upper-bound questions in Question 6.1 remain open.

## Files

- `main.tex`: complete proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: Question 6.1 and its discrete-measure discussion on source PDF page 17.
- `code/verify_counterexample.py`: exact arithmetic checks for the atomic example, fractional-atom repair, and smooth-error margin.

## Human review recommendation

Accept as a scoped counterexample to the direct lower-bound extension in Question 6.1. Check chiefly that the same-form formula is the intended interpretation of “Theorem 3.4 ... for general measures”; the algebra and smooth-bump estimates are elementary and exact.

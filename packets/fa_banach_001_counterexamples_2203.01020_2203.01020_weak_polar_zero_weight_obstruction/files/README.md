# Counterexample Packet: Zero Weights Break the Weak-Polar Implication

Run: `fa_banach_001`

Source: Pekka Koskela and Khanh Nguyen, *Existence and uniqueness of
limits at infinity for homogeneous Sobolev functions*, arXiv:2203.01020;
Journal of Functional Analysis 285 (2023), 110154.

Status: `candidate_full_counterexample_and_corrected_result_likely_valid`.

## Result

The implication `R_p(h,O)<infinity => mathcal R_p(O)<infinity` and
Theorem 1.3(I) are false under the printed definition of a weak polar
coordinate system.  On `X=R^2`, with `p=2`, take a singleton radial family
consisting of the positive x-axis and let

```text
h(x)=0 on the ray, and h(x)=exp(|x|) off the ray.
```

The weak-polar inequality is then vacuous, while

```text
R_2(h,0)=(3*pi/2)e^{-2}<infinity,
mathcal R_2(0)=sum_j 1/(3*pi)=infinity.
```

The ray family also has 2-modulus zero, directly contradicting property 4
in Theorem 1.3(I).

The packet proves a sharp repair.  If the coordinate weight is positive for
line-almost every point of the radial family (integrated over directions),
then the requested simple direct proof works and gives

```text
mathcal R_p(O) <= C^{p/(p-1)} R_p(h,O),  p>1,
mathcal R_1(O) <= C R_1(h,O).
```

It uses only annular crossing length, the weak-polar inequality tested with
`indicator/h`, and Holder's inequality.

## Files

- `main.tex`, `solution_packet.pdf`: counterexample and corrected theorem.
- `source_paper.pdf`: source arXiv PDF.
- `figures/theorem_and_direct_proof_request_crop.png`: Theorem 1.3 and the
  request for a simple direct proof on source page 3.
- `figures/weak_polar_zero_weight_definition_crop.png`: source page 5,
  explicitly allowing coordinate weights that are not strictly positive.
- `code/crop_source_passages.py`: reproducible crop script.
- `code/verify_zero_weight_counterexample.py`: exact-formula sanity check.
- `VERIFICATION.md`: proof audit and build record.
- `tmp/`: build and render intermediates.

## Human review recommendation

Accept as a complete counterexample to the statements as printed and as a
complete repair under radial almost-everywhere positivity.  The key review
point is interpretive: confirm that no positivity convention beyond the
displayed weak-polar definition is intended.  The paper explicitly says that
strict positivity has not been assumed, which strongly supports the literal
reading used here.

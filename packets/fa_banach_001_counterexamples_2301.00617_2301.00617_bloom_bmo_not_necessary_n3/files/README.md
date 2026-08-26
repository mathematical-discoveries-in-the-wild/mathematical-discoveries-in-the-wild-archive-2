# Bloom's triplet weighted-BMO condition is not necessary in dimension three

Status: `counterexample_likely_valid_novelty_overlap_unresolved`

Source: Tuomas P. Hytönen, *Some remarks on convex body domination*,
arXiv:2301.00617, Remark 7.11 (source PDF page 19).

## Result

The weighted-BMO condition

```text
u_ij in BMO_{sqrt(lambda_i/lambda_k)} for every i,j,k
```

is not necessary for `W=U^* Lambda U` to be a matrix `A_2` weight once the
matrix size is at least three. A 3-by-3 example is given with globally simple
scalar-`A_2` eigenvalues and a globally real-analytic unitary diagonalizer.

For `0<a<1`, let `s(x)=(1+x^2)^(a/2)`,

```text
Lambda = diag(s^-1, 2s^-1, 4s),
U      = diag(rotation by angle x, 1).
```

Then `W=U^* Lambda U` is pointwise comparable to
`D=diag(s^-1,s^-1,4s)`, hence is matrix `A_2`. But `u_11=cos x` fails
`BMO_{sqrt(lambda_1/lambda_3)}=BMO_{1/(2s)}` on intervals escaping to
infinity.

The packet also proves a general block-cluster theorem: rotations within a
block of mutually comparable eigenweights preserve matrix `A_2` without any
regularity condition on the rotation.

## Scope and novelty warning

This disproves higher-dimensional necessity of Bloom's particular triplet
condition. It does not classify every unitary diagonalizer `U` for which
`U^* Lambda U` is matrix `A_2`.

A bounded literature audit found no exact construction, but a highly relevant
March 2026 paper by Morten Nielsen and Hrvoje Šikić, *Matrix weights on compact
and non-compact domains*, J. Math. Anal. Appl. 555(2), 130069, could not be
checked at theorem level because the publisher full text was inaccessible.
No novelty or priority claim is made until a human compares that paper.

## Files

- `solution_packet.pdf`: expert-facing statement and proof.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: Remark 7.11 from source page 19.
- `supporting_papers/nielsen_sikic_2021_muckenhoupt_matrix_weights.pdf`:
  decisive source for the exact weighted-BMO convention and multivariate
  statement of Bloom's sufficient condition.
- `code/crop_open_problem.py`: reproducible source crop.
- `code/verify_counterexample.py`: numerical/symbolic sanity checks.
- `verification.md`: build, visual inspection, and scope record.

## Human-review recommendation

First verify the Loewner-comparability lemma and the one-period weighted-BMO
calculation. Then compare the exact example and block theorem against the 2026
Nielsen--Šikić paper before assigning novelty.


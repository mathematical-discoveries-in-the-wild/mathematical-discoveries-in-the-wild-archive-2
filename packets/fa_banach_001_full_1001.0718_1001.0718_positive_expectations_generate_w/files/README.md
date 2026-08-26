# Positive Expectations Generate W

Source: R. G. Douglas and P. W. Nowak, *Invariant expectations and
vanishing of bounded cohomology for exact groups*, arXiv:1001.0718;
Journal of Topology and Analysis 3 (2011), 89--107.

Status: candidate full affirmative solution to Question 5.2, likely valid.

## Result

Every `Xi in W` has an algebraic representation

```text
Xi = c M - c' M'
```

with `M,M' in M_+` and `c,c'>=0`. Thus the answer to Question 5.2 is yes.

The key is a common-slack repair of the pointwise Jordan decomposition of a
finite-support approximant. If its positive and negative masses are the
functions `A` and `B`, then `A-B` is scalar. Adding `R-A` to both parts at
the identity group coordinate makes their total masses the scalars `R` and
`R-c` without changing their difference. Uniform boundedness and weak-*
compactness then pass the decomposition to every element of `W`.

The proof uses only the definitions of `W` and `M_+`; group exactness and
invariance of expectations are not required.

## Files

- `main.tex`: exact statement and proof.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: original source PDF.
- `figures/open_problem_crop.png`: page-17 crop containing Question 5.2.
- `code/verify_finite_decomposition.py`: 500 randomized finite checks.
- `verification.md`: reproducibility, checksum, and visual-QA record.

## Human Review Recommendation

Check that the source's embedding of `ell_u(G)` is isometric, that weak-*
convergence supplies the uniform norm bound, and that positivity on the
restricted module is weak-* closed. These are the only functional-analytic
passage points beyond the elementary finite-support decomposition.

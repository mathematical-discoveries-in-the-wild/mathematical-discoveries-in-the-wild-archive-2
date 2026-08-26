# Analytic-Eigenfield Criterion for Injectivity

Source: J. A. Ball, V. Bolotnikov, and S. ter Horst, *Abstract
interpolation in vector-valued de Branges--Rovnyak spaces*,
arXiv:1804.08492; Integral Equations and Operator Theory 70 (2011),
227--263.

Status: candidate full solution, likely valid.

## Result

For the source's admissible data, put
`X_0 = closure(Ran(P^(1/2)))`. The multiplier `M_{Sigma_12}` on
vector-valued holomorphic functions is injective if and only if the only
holomorphic function `G:D -> X_0` satisfying

```text
T^* P^(1/2) G(z) = z P^(1/2) G(z)     (z in D)
```

is `G=0`.

This is a necessary-and-sufficient condition expressed solely in the original
`P,T` data, including when `P` is degenerate. It follows by sharpening the
source's Lemma 4.7: its colligation-dependent growth condition on
`B_2^* g_{n+1}` is equivalent to unit-disk Taylor growth of `g_{n+1}` because
the colligation state operator is contractive.

A weighted-shift family shows strict improvement over the paper's sufficient
hyperrange condition (4.32). With `w_n=1/(n+1)`, that condition fails while
the criterion proves injectivity because every possible eigenfield has forced
coefficients of size at least `n!`.

## Files

- `main.tex`: theorem, proof, weighted-shift corollary, scope, and novelty check.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: original source PDF.
- `figures/open_problem_crop.png`: page-16 crop containing the open question.
- `code/verify_weighted_shifts.py`: reusable arithmetic consistency check.
- `verification.md`: commands, checks, checksum, and visual-QA record.

## Human Review Recommendation

Check the extraction of the recurrence identities from the converse half of
Lemma 4.7 and the root-growth equivalence using `||A||<=1`. The weighted-shift
example is secondary; the pencil criterion itself is the claimed full answer.

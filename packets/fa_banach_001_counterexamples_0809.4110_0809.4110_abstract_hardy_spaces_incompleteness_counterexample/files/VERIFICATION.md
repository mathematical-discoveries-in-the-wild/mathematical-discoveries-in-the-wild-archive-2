# Verification report

Verdict: `likely valid; candidate counterexample pending human review`

## Formal checks

1. `(0,1)` with Euclidean distance and Lebesgue measure is a space of homogeneous type.
2. Each selected rank-one operator `B_{Q_n}` has `L^2 -> L^2` norm one; every other `B_Q` is zero.
3. The source normalization gives the maximal atom/molecule `a_n=n^2 r_n`, and the molecular annular conditions add no further outputs because `B_{Q_n}` only reads `f` on `Q_n`.
4. The Paley-Zygmund estimate gives a uniform lower probability bound whenever a finite Rademacher coefficient vector has nonzero `ell_2` norm. Hence almost-everywhere convergence forces `ell_2`-Cauchy coefficients.
5. The reverse inclusion uses the standard almost-sure convergence of square-summable Rademacher series.
6. The resulting atomic gauge is a norm, not merely a seminorm, because Rademacher coefficients are unique in `L^2`.
7. The Cauchy sequence `sum_{n<=N} r_n` would require the nonexistent `ell_2` coefficient vector `(1,1,...)` as its limit.

## Computational sanity check

Command:

```text
conda run --no-capture-output -n sandbox python runs/fa_banach_001/solutions/counterexamples/0809.4110_abstract_hardy_spaces_incompleteness_counterexample/code/finite_rademacher_check.py
```

The script verifies exact orthogonality on the finite dyadic model through eight Rademacher coordinates, checks the fourth-moment bound for all coefficient vectors in `{-1,0,1}^6`, and displays the weighted tail decay of the proposed Cauchy sequence. These finite checks do not prove the infinite-dimensional statement.

## Literature check

Search date: 2026-08-09. Search bounds and terms are recorded in `README.md` and `main.tex`. No later explicit resolution was found.

## Primary human-review focus

- Confirm that Remark 2.6 asks the unqualified completeness question under only uniform `L^beta` boundedness of `(B_Q)`.
- Confirm the fourth-moment/Paley-Zygmund implication from convergence in probability to `ell_2`-Cauchy coefficient vectors.
- Confirm that repeated appearances and arbitrary orderings of atoms are covered by the coefficient-vector argument.

# An explicit category-(c) normalizable frame

Status: `candidate_counterexample_likely_valid`

Source: Pu-Ting Yu, *Frame-normalizable Sequences*, arXiv:2308.13071,
*Advances in Computational Mathematics* 50 (2024), Paper 89,
<https://doi.org/10.1007/s10444-024-10182-z>.

Target: Conjecture 3.14 on page 9 of the source PDF.

## Result

Conjecture 3.14 says that no normalizable frame can belong to category (c) of
Theorem 3.13.  The packet gives an explicit counterexample in
`H = ell^2(N)`.

Partition the standard basis into infinite sets `E_k`, set
`a_k=r_k=2^{-k}`, and pair each `p in E_k` bijectively with a coordinate in
`E_k^c`.  The two unit vectors

```text
u_{k,p}^{+/-}
  = sqrt(1-a_k/2)e_p +/- sqrt(a_k/2)e_{sigma_k(p)}
```

form a block whose exact frame operator is

```text
S_k = a_k I + (2-2a_k) P_{E_k}.
```

The union of these unit-vector blocks has optimal frame bounds `2` and `3`.
After scaling block `k` by `r_k`, the resulting sequence is still a frame,
with optimal bounds `1/7` and `11/28`, and its normalization is the preceding
unit-vector frame.

For `delta_k=(3/2)r_k`, the `k`-th norm band is exactly the scaled block
`r_k U_k`.  Its optimal bounds are

```text
A_k = 2^{-3k},
B_k = 4^{-k}(2-2^{-k}).
```

Thus every norm band is a frame, `(A_k)` is summable, and `B_k -> 0`.  This is
precisely category (c), so the construction disproves Conjecture 3.14.

## Files

- `solution_packet.pdf`: review-ready statement and complete proof.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: local copy of the source paper.
- `figures/category_c_theorem_crop.png`: Theorem 3.13(c), source page 8.
- `figures/open_problem_crop.png`: Conjecture 3.14, source page 9.
- `code/crop_source_pages.py`: reproducible source-figure generation.
- `verification.md`: proof audit, build checks, and reviewer focus.

## Scope and novelty

This is a full negative answer to Conjecture 3.14.  It does not classify all
normalizable frames or answer the paper's other questions.

The run indexes were searched for the arXiv id, exact title, and the
category-(c) conjecture.  Bounded web searches on 2026-08-09 used the exact
conjecture sentence, the title with “category (c),” and the title/author with
“conjecture.”  They located the arXiv paper, journal publication, an author
thesis, and unrelated later references, but no resolution or this
construction.  Novelty remains subject to expert literature review.

## Human-review recommendation

High priority.  The proof is elementary and fully diagonal.  A reviewer need
only check the two-vector cancellation identity, the three diagonal frame
operators, and that the chosen norm bands isolate exactly one scale.


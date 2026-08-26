# The MSS-type restricted-invertibility theorem is algorithmic

Status: `literature_implied_answer_partial_subcase`

Source: Naor--Youssef, arXiv:1601.00948, the algorithmic question in the
introduction (source PDF page 8) and Theorem 11.

Answer: Xie, arXiv:2005.01070, Corollary 1.2 and the deterministic algorithm
following Theorem 1.1.

## Identification

The source asks whether four of its restricted-invertibility theorems can be
made algorithmic.  One of them, Theorem 11 (the MSS-type variant), asserts
that for `R=rank(A)` there is a `k`-column submatrix with

```text
||(A_S)^(-1)||
 <= sqrt(m)/(sqrt(R)-sqrt(k))
    * sqrt((1/R) sum_{i=1}^R sigma_i(A)^(-2)).
```

Xie's Corollary 1.2 gives, deterministically,

```text
||(A_S)^(-1)||
 <= sqrt(m)/(sqrt(R)-sqrt(k-1))
    * sqrt((1/R) sum_{i=1}^R sigma_i(A)^(-2)).
```

This is slightly stronger because `sqrt(k-1)<sqrt(k)`.  The proof supplies a
deterministic polynomial-time selection algorithm, with the stated running
time `O(k(m-k/2)n^(theta+1))`.

## Scope

This answers the algorithmic question for Theorem 11 only.  It does not by
itself algorithmize the source's tail-singular-value Theorem 6, its Schatten
corollary, or its max-distance full-column-rank theorem.  It also does not
settle the separate open question asking for the RMS dual-column parameter
together with the optimal `1/sqrt(epsilon)` dependence.

## Files

- `main.tex`: compact theorem-to-theorem identification.
- `solution_packet.pdf`: compiled status note.
- `source_paper.pdf`: official arXiv:1601.00948 PDF.
- `answer_paper_2005.01070.pdf`: official later paper.
- `verification_report.md`: algebraic, scope, source, build, and visual checks.


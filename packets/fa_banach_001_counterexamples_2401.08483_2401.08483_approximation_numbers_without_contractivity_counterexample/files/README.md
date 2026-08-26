# Counterexample: contractivity cannot be removed from the truncation theorem

Status: `counterexample_likely_valid`

Source: Deepesh K. P., *Approximation results on s-numbers of operators*,
arXiv:2401.08483v2 (2024), Section 4 on PDF pages 13--14; published in
*Palestine Journal of Mathematics* 14(3) (2025), 308--318. The source asks
whether Theorem 4 remains valid when the norm restrictions on the truncation
operators are removed.

## Claimed contribution

The answer is no, even on the Hilbert space `ell_2`, even when both truncation
operators have finite rank, and even when both converge strongly to the
identity.

Let `R_m` be the orthogonal projection onto the first `m` coordinates and set

```text
T   = I,
P_n = R_(2n),
Q_n = R_n + 2(R_(2n)-R_n).
```

Then `P_n` and `Q_n` are finite rank, `P_n -> I` and `Q_n -> I` strongly,
and `T_n = Q_n T P_n = Q_n`. Nevertheless, for every fixed `k` and all
`n >= k`,

```text
a_k(T_n) = 2,        while        a_k(T) = 1.
```

Thus the approximation numbers do not converge. Here
`||P_n|| ||Q_n|| = 2`, so the example lies exactly outside the contractive
hypothesis of the source theorem.

## Proof mechanism

The strong convergence is just a tail estimate: `Q_n-I` changes only
coordinates beyond `n`, so its value on any fixed `ell_2` vector tends to
zero. For the approximation numbers, `Q_n` acts as `2I` on the `n`-dimensional
block spanned by coordinates `n+1,...,2n`. Every operator of rank less than
`k <= n` has a nonzero kernel vector on that block, forcing its distance from
`Q_n` to be at least `2`. The zero approximant gives the matching upper bound.
The same kernel argument gives `a_k(I)=1`.

## Verification

The proof is exact and uses no computational or external theorem dependency.
The verifier report checks the source match, strong convergence, finite-rank
factorization, and both approximation-number calculations independently.

Verifier focus: confirm that the source question is read literally as removal
of the displayed condition `||P_n|| ||Q_n|| <= 1`. Under that reading, the
counterexample satisfies stronger truncation assumptions than the theorem
requires.

## Novelty and scope

A bounded search on 9 August 2026 covered the four lightweight run indexes,
the exact arXiv id and title, the exact norm-restriction sentence, and close
queries combining approximation numbers, truncations, contractivity, and
counterexamples. The arXiv v2 source and the 2025 journal version were checked;
the journal version still prints the question as open. No later exact answer
or matching counterexample was found. This supports, but cannot certify,
novelty.

The packet answers only the first question in the source's concluding section.
It does not address the separate program of two-sided convergence for other
`s`-numbers, nor does it characterize weaker norm hypotheses that might still
imply convergence.

Human review recommendation: accept after a short operator-theory check. The
argument is elementary; the main semantic audit is the scope of "the norm
restrictions ... are removed."

## Files

- `source_paper.pdf`: arXiv:2401.08483v2.
- `figures/open_problem_crop.png` and
  `figures/open_problem_crop_continuation.png`: source PDF pages 13--14.
- `main.tex` and `solution_packet.pdf`: full counterexample packet.
- `VERIFICATION.md`: explicit verifier report.

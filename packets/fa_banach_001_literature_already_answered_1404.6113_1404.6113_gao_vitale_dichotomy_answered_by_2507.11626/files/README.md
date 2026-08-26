# Gao--Vitale intrinsic-volume dichotomy: answered negatively

The open-problem signal in arXiv:1404.6113 is Remark 2.1 (source PDF page 12).
It repeats Gao and Vitale's conjecture that, for every convex GB-compact set
`K` in a separable Hilbert space, the decreasing sequence
`m_k=(k+1)V_{k+1}(K)/V_k(K)` either has a positive limit or is
`O(k^{-1/2})`.

This is no longer open. Dospolova, Germanskov, and Zaporozhets,
*On Steiner entire function* (arXiv:2507.11626), restate the same assertion as
Conjecture 3.5 and disprove it immediately afterward on PDF page 9. Their
Theorem 3.4 connects the logarithmic decay of `m_k` to the order `rho(K)` of
the Steiner entire function, while Theorem 3.1 realizes every order in
`[0,1]`. Choosing a realized order `rho(K)` strictly between `2/3` and `1`
supplies a convex GB-compact counterexample whose `m_k` tends to zero but more
slowly than `k^{-1/2}` along a subsequence.

Files:

- `solution_packet.pdf`: compact identification note.
- `source/1404.6113.pdf`: source paper containing the repeated conjecture.
- `source/2507.11626.pdf`: later paper explicitly disproving it.

Status: literature already answered; exact negative answer, not a new result.

# arXiv:1904.05239 — singular-commutator block counterexample

Status: `candidate_counterexample_likely_valid`

The source asks whether the commutator-kernel exclusion in its near-identity
matrix rearrangement theorem is necessary and asks for other simple sufficient
conditions beyond commutativity.

The packet proves that every pair with a common orthogonal reducing
decomposition into blocks of dimension at most two satisfies every word
inequality.  Applying this to

```text
A = diag(2,1,4),
B = [[2,1,0],[1,2,0],[0,0,4]]
```

gives positive definite, noncommuting `3 x 3` matrices with
`ker(AB-BA)=span(e_3)`.  Nevertheless, every rearrangement inequality holds,
both globally and for `(I+epsilon A,I+epsilon B)` for every `epsilon>0`.
Moreover, the top eigenspace of every `mA+nB` lies in the commutator kernel.

Files:

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: official arXiv v2 source.
- `figures/open_problem_crop.png`: readable full-width source page 3.
- `code/verify_example.py`: exact arithmetic and random-word sanity checks.
- `VERIFICATION.md`: proof, source, literature, and rendering audit.

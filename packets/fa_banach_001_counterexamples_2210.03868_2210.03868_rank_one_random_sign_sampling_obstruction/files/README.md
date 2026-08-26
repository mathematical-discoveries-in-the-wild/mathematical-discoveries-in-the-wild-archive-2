# Polynomial random-sign sampling can miss the Grothendieck scale

Status: candidate full negative answer to Question 3.7, likely valid, awaiting
specialist review.

Sinclair and Vivek ask in Question 3.7 of arXiv:2210.03868 whether the Schur
norm of the `K x K` matrix

`[<A epsilon_i, epsilon_j>]`

formed from `K=O(n)` independent uniform sign vectors approximates
`||A||_{infinity -> 1}` with high probability.

The answer is no.  For the positive semidefinite rank-one matrix
`A_n = 1_n 1_n^T`, if `S_i` is the coordinate sum of `epsilon_i`, then the
sampled matrix is `ss^T`.  Therefore its Schur norm is exactly
`max_i |S_i|^2`, whereas `||A_n||_{infinity -> 1}=n^2`.  With probability at
least `1-delta`, their ratio is at most

`2 log(2K/delta)/n`.

In particular, it tends to zero for `K=O(n)`.  More strongly, it tends to
zero in probability whenever `K=exp(o(n))`, and its expectation is at most
`2(log(2K)+1)/n`.

Contents:

- `main.tex` and `solution_packet.pdf`: source question, theorem, and proof.
- `source_paper.pdf`: arXiv:2210.03868.
- `figures/open_problem_crop.png`: readable crop of Question 3.7 on PDF page
  10.
- `code/verify_rank_one_sampling.py`: exact finite identity check and seeded
  Monte Carlo sanity table.
- `VERIFICATION.md`: mathematical, source, novelty, and artifact QA record.

The claim answers only Question 3.7.  It does not address the separate
noncommutative questions later in the source paper.

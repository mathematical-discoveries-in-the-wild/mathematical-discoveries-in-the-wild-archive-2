# An explicit counterexample to the all-vector LIL conjecture

Status: `counterexample_likely_valid`

Source target: Cheng--Fang--Zhu, *Random weighted shifts*,
arXiv:1811.05761, Conjecture 7.17 (PDF page 48).

For independent weights taking the values `e` and `e^{-1}` with equal
probability, and the deterministic vector

`x = sum_{k>=1} k^{-3/5} e_k`,

exponentially many disjoint length-`n` blocks are available in the tail of
`x`.  Almost surely, for every sufficiently large `n`, one of the first
`ceil(e^n)` such blocks consists entirely of weights equal to `e`.  Its
single contribution forces

`log ||T^n x||^2 >= (4/5)n - O(log n)`.

Consequently the normalized logarithm tends to positive infinity along all
sufficiently large integers, contradicting the conjectured LIL limsup `1`.
The packet contains the exact proof and a deterministic numerical audit of
the summable failure bound and growth estimate.

Files:

- `solution_packet.pdf`: source statement, theorem, proof, and scope.
- `main.tex`: packet source.
- `source_paper.pdf`: official arXiv PDF.
- `figures/open_problem_crop.png`: source page containing Lemma 7.15 and
  Conjecture 7.17.
- `code/verify_counterexample.py`: numerical transcription checks.

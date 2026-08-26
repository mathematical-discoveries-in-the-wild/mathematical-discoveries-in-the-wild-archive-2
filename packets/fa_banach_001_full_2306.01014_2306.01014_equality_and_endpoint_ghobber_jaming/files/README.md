# Equality and endpoint Functional Ghobber–Jaming principles

Status: `candidate_full_solution_likely_valid`

This packet answers both Questions 2.10 and 2.11 of arXiv:2306.01014.

Main results:

- For every `1 < p < infinity`, under the strict hypothesis of the source
  theorem, equality in its displayed Functional Ghobber–Jaming inequality
  occurs only for `x=0`. Thus there are no nonzero extremizers, for any
  admissible subsets or pair of p-orthonormal bases.
- At `p=1` and `p=infinity`, every change between p-orthonormal bases is a
  generalized permutation. A finite uncertainty estimate exists exactly when
  the two proposed support sets are disjoint after this permutation. In that
  case sharp endpoint estimates and all equality cases are explicit; if the
  sets overlap, a coordinate vector has both tails zero and no estimate is
  possible.

The endpoint result also explains why a literal Hölder-limit of the source's
coherence/cardinality hypothesis becomes trivial: the coherence is always one.

Files:

- `main.tex`: full proof and scope discussion.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: arXiv:2306.01014.
- `code/verify_fgj.py`: randomized finite-dimensional consistency checks.
- `tmp/`: build and page-render intermediates.


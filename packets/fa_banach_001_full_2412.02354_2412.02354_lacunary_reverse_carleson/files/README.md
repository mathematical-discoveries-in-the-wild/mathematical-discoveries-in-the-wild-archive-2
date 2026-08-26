# Candidate full solution: the missing Besov reverse-Carleson range

Source: Evgueni Doubtsov, Anton Tselishchev, and Ioann Vasilyev,
“Reverse Carleson measures for spaces of analytic functions,”
arXiv:2412.02354.

Status: `candidate_full_likely_valid`.

Problem 8.1 asks whether reverse Carleson measures fail to exist for
`HB_0^{p,q}` when `0<p<1` and `p<q<2`. The packet gives an affirmative
answer. In fact, it proves the stronger statement that for every finite
right-hand exponent `s`, every angular exponent `a`, and every fine index
`q<2`, no finite measure can dominate either `HB_0^{a,q}` or
`HF_0^{a,q}` through an `L^s(mu)` norm.

The proof uses normalized lacunary polynomials. Their Hardy norms remain
bounded, their mixed analytic norms grow as `N^(1/q-1/2)`, and averaging
rotations against an arbitrary finite measure supplies a rotation with
bounded `L^s(mu)` norm.

Main review files:

- `solution_packet.pdf`
- `main.tex`
- `verification.md`
- `figures/open_problem_crop.png`
- `source_paper.pdf`

Ledger record:
`runs/fa_banach_001/ledger/results/2412.02354_lacunary_reverse_carleson.json`.

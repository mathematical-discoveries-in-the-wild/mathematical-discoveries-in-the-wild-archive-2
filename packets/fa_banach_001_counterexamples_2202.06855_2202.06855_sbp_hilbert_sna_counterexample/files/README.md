# arXiv:2202.06855 — small-ball Hilbert SNA counterexample

Status: `candidate_counterexample_likely_valid`

Question 4.3 asks whether every Banach subspace of `SNA(M)` is separable and
isomorphically polyhedral whenever `M` has the small ball property.

This packet gives a negative answer. A construction of Behrends--Kadets
produces a dense `G_delta` subset `M` of `ell_2` with the small ball property.
Baire category implies `M-M=ell_2`. Consequently every Hilbert functional,
restricted to `M`, strongly attains its Lipschitz norm on a chord of `M`.
This embeds a closed isometric copy of `ell_2` into `SNA(M)`, and `ell_2` is
not isomorphically polyhedral.

Files:

- `main.tex`: self-contained theorem and proof.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: compiled archived source paper.
- `behrends_kadets_2001.pdf`: primary source for the dense small-ball construction.
- `figures/open_problem_page.png`: source page containing Question 4.3.
- `verification.md`: proof, literature, and artifact audit.

The construction answers the printed question, which does not require `M` to
be complete. It leaves open the stronger complete-metric variant.

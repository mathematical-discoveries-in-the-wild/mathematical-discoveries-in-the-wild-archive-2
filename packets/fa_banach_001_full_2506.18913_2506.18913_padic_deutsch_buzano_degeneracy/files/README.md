# Full-solution packet: degeneration of p-adic Deutsch and Buzano bounds

Status: **candidate full negative resolution; likely valid; human review required**

Source: K. Mahesh Krishna, *p-adic Ghobber-Jaming Uncertainty Principle*,
arXiv:2506.18913, Questions 3.7 and 3.9.

## Result

Under the definitions in the source, every pair of p-adic orthonormal bases
has coherence exactly one.  Thus the overlap term in Deutsch's lower bound
always collapses to zero.

More precisely, over `Q_p` the source's entropy satisfies the sharp universal
bounds

`0 <= S_tau(x)+S_omega(x) <= 4(n-1) log(p)/p^2`.

Both endpoints occur already when the bases coincide.  The classical upper
bound `2 log n` is false: over `Q_2` in dimension eight, equal canonical bases
and `x=(1,2,...,2)` give entropy sum `7 log 2 > 6 log 2`.

The optimal universal p-adic Buzano substitute is just the product of the two
Cauchy--Schwarz bounds.  Its constant one is sharp even when the outside
vectors are orthogonal, so it cannot generate a nontrivial Deutsch lower
bound.

## Files

- `main.tex`: self-contained proof and sharp examples.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_questions_page.jpg`: source page 10 crop containing both
  questions.
- `code/verify_entropy_bounds.py`: exact arithmetic regression audit.
- `verification.md`: source, proof, novelty, and rendering audit.

Ledger: `runs/fa_banach_001/ledger/results/2506.18913_padic_deutsch_buzano_degeneracy.json`.

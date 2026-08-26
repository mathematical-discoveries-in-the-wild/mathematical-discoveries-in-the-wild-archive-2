# PPT characterization of fermionic radial channels

Status: candidate full solution of the PPT-characterization subproblem; likely
valid; human review recommended.

The final section of arXiv:2402.15440 asks for a characterization of which
fermionic radial quantum channels are PPT. This packet gives the complete
answer for every even Clifford dimension `n=2k`: the partial transpose of the
normalized Choi state has `n+1` explicitly computed eigenvalues, expressed by
a signed Krawtchouk transform of the radial symbol. Their multiplicities are
the binomial coefficients, so PPT is exactly a finite list of `n+1` linear
inequalities.

For the fermionic Ornstein--Uhlenbeck channel with symbol `phi(r)=t^r`, the
formula collapses to elementary trigonometry and gives the exact threshold

`t <= tan(pi/(4n))`.

Equivalently, at semigroup time `s` with `t=e^{-s}`, PPT begins exactly at
`s=log(cot(pi/(4n)))`. The packet also gives the exact Choi negativity and a
rigorous entanglement-breaking sufficient region. The source's
entanglement-breaking characterization and unassisted capacity questions
remain open.

Files:

- `solution_packet.pdf`: reviewable proof packet.
- `main.tex`: packet source.
- `source_paper.pdf`: local rendering of the official arXiv v6 source.
- `figures/open_problem_crop.png`: exact open-question passage on PDF page 36.
- `code/verify_spectrum.py`: explicit matrix/Krawtchouk spectrum check.
- `verification.md`: mathematical, computational, and presentation checks.


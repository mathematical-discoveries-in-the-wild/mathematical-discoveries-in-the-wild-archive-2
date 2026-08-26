# The 2-Kazhdan question for integral special linear groups

Status: `literature_implied_answer (complete for n>=3)`

Source question: Marcus De Chiffre, Lev Glebsky, Alexander Lubotzky, and
Andreas Thom, *Stability, cohomology vanishing, and non-approximable groups*,
arXiv:1711.10238, Question 4.6 on source PDF page 24:

> Is `SL_n(Z)` 2-Kazhdan (at least for large `n`)?

The later literature gives a complete answer for `n>=3`:

- `SL_3(Z)` is **not** 2-Kazhdan. Brück--Hughes--Kielak--Mizerka,
  arXiv:2410.22310, Theorem 1.1, construct a finite-dimensional orthogonal
  representation `pi_3` with `H^2(SL_3(Z),pi_3) != 0`.
- `SL_n(Z)` **is** 2-Kazhdan for every `n>=4`. Bader--Sauer,
  arXiv:2308.06517, Theorem A gives property `(T_{n-2})`, hence degree-two
  vanishing for every unitary representation without invariant vectors.
  Their Theorem C and formula (1) give `H^2(SL_n(Z),C)=0` for `n>=4`.
  Splitting an arbitrary unitary representation into its invariant part and
  orthogonal complement, and using the finite-type cochain complex, yields
  `H^2(SL_n(Z),V)=0` for every unitary `V`.

Thus the source's large-`n` clause has an affirmative answer, with the sharp
transition (among `n>=3`) between `n=3` and `n=4`.

This is an agent-identified implication, not new mathematics. The supporting
papers discuss higher property T and cite the source framework, but do not
present this exact two-line classification as an answer to Question 4.6.

Other questions in arXiv:1711.10238--amenable Frobenius approximability,
closure under central quotients or semidirect products by `Z`, and universal
`C*`-coefficient vanishing--are outside this packet and remain unclaimed.

Files:

- `solution_packet.pdf`: compact status and identification note.
- `source_paper.pdf`: arXiv:1711.10238.
- `supporting_paper_2308.06517.pdf`: Bader--Sauer.
- `supporting_paper_2410.22310.pdf`: Brück--Hughes--Kielak--Mizerka.
- `VERIFICATION.md`: source locations and implication audit.
- Ledger: `runs/fa_banach_001/ledger/results/1711.10238_sln_2_kazhdan_classification.json`.

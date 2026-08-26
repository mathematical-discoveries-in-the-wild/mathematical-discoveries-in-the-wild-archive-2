# Candidate full answer: dense yes, closed no

Status: **candidate full answer in the source's intended setting, pending
expert review**.

This packet addresses Problem 3 in Szymon Głab, Pedro L. Kaufmann, and
Leonardo Pellegrini, *Large structures made of nowhere Lp functions*
(arXiv:1207.3818), printed page 17.

For `0<p<infinity`, let `G_p` be the set of `Lp` functions that are not
essentially bounded on any nonempty open set. The packet proves:

- under the factorial dense-partition construction of the source and
  `dens(Lp)<=continuum`—in particular in its separable setting and on
  `[0,1]`—`G_p union {0}` contains a dense free algebra;
- on every measure space, every `Lp`-closed pointwise subalgebra is contained
  in `L-infinity`, so `G_p union {0}` contains no nonzero closed subalgebra.

Thus the sharp answer is: **dense yes; closed no**.

Files:

- `solution_packet.pdf` — expert-facing proof packet
- `main.tex` — LaTeX source
- `source_paper.pdf` — original arXiv paper
- `figures/open_problem_crop.png` — exact printed-page-17 crop
- `verification.md` — proof-audit report
- `code/check_dominance.py` — finite leading-rate sanity checks (not proof)

Highest-value review points:

1. the unique leading-exponential term after bounded perturbations;
2. the quasi-Banach Baire argument for `0<p<1`;
3. the match between the explicit density-cardinal condition and the
   cardinal/separability convention used in the source.

Ledger record:
`runs/fa_banach_001/ledger/results/1207.3818_dense_free_algebra_closed_algebra_dichotomy.json`.

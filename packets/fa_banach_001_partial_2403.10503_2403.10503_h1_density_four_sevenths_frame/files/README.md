# First-Hermite rectangular frame at density 4/7

Status: `candidate_substantial_partial_likely_valid`

This packet proves, by the Lyubarskii--Nes rational Zak-matrix criterion and
an outward-rounded interval certificate, that

\[
\mathcal G(h_1,a\mathbb Z\times b\mathbb Z)
\quad\text{is a frame whenever}\quad ab=4/7.
\]

It is a new solved hyperbola inside the still-open region
`1/2 < ab < 1` of the first-Hermite frame-set conjecture. The full
conjecture remains open. The source paper is Faulhuber--Shafkulovska--Zlotnikov,
arXiv:2403.10503; the rational rank theorem used in the proof is
Lyubarskii--Nes, arXiv:1108.2684.

Key files:

- `solution_packet.pdf`: reviewer-facing proof packet.
- `main.tex`: source of the packet.
- `code/verify_certificate.py`: exact exponent-gap checks and rigorous
  interval proof on 1024 rational boxes.
- `verification.md`: reproduced output and audit notes.
- `source_paper.pdf`: source/open-problem paper.
- `supporting_rational_rank_criterion.pdf`: decisive supporting paper.
- `figures/`: full-width source excerpts of the conjecture and open-status
  statement.

Verifier command from the repository root:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2403.10503_h1_density_four_sevenths_frame/code/verify_certificate.py
```

Human review should focus on the rational rank-criterion transcription, the
two centered coefficient matrices, the all-monomial reverse-triangle bound,
and the interval/tail implementation.


# Periodic-profile MCF counterexample and correction

Status: `candidate_counterexample_likely_valid`

This packet addresses the open generability program stated after Example 5.8
of arXiv:1212.1430 by auditing its basic periodic construction.  It proves an
exact signed Fourier cross-spectrum formula for every bounded periodic
profile in the `p=2` simple-wave class and gives two rigorous counterexamples
to the published Lemma 4.1:

- a real two-phase square wave makes the stated formula twice the defining
  MCF pairing;
- a positive-frequency complex exponential has zero negative-direction
  pairing although the source formula assigns it nonzero mass.

Thus no scalar normalization repairs the result.  The full characterization
of all generated MCFs remains open, but the corrected theorem identifies
signed cross-spectral compatibility that any such characterization must
retain.

Files:

- `solution_packet.pdf` -- expert-facing theorem and counterexamples
- `source_paper.pdf` -- arXiv:1212.1430v3
- `main.tex` -- packet source
- `figures/open_problem.png` -- source p. 38 generability statement
- `figures/oscillation_lemma.png` -- source p. 28 Lemma 4.1
- `code/fourier_verifier.py` -- finite Fourier sanity check
- `verification.md` -- mathematical and artifact audit

Attempt:
`runs/fa_banach_001/attempts/1212.1430_periodic_profile_mcf_attempt.md`

Ledger:
`runs/fa_banach_001/ledger/results/1212.1430_periodic_profile_oscillation_lemma_counterexample.json`

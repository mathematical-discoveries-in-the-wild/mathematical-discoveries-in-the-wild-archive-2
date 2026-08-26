# Full dimension-two resolution of the generalized Busemann intersection question

Status: `candidate substantial partial result; likely valid`.

Question 1 of arXiv:2208.03882 is resolved affirmatively for `n=2` and
every real `0<p<2`. For `0<p<1`, angle doubling and a quarter-turn identify
the normalized spherical Fourier operator with the sharp one-dimensional
Hardy-Littlewood-Sobolev operator. Lieb's sharp theorem gives the exact
constant and identifies equality cases as centered ellipses. For `1<p<2`,
the identity `I_(2-p) I_p = Id` turns the upper HLS bound into the requested
reverse inequality. At `p=1`, Parseval gives equality for every body, exactly
as the source notes.

The higher-dimensional conjecture remains open. A later stochastic theorem
settles only the `0<p<1`, `n/p` integral subfamily; the present circle
argument fills the entire continuum in dimension two.

Files:

- `solution_packet.pdf`: review-ready proof packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: original arXiv PDF.
- `figures/open_question_crop.png`: genuine crop from source PDF page 3.
- `code/axisym_search.py`: independent higher-dimensional counterexample search.
- `code/verification_output.txt`: corrected-phase numerical output.
- `VERIFIER_REPORT.md`: proof, scope, novelty, and rendering audit.
- Ledger: `runs/fa_banach_001/ledger/results/2208.03882_dimension_two_hls_full_resolution.json`.

# Interval-length rigidity boundary for arXiv:1702.07323

Status: candidate substantial partial result, likely valid.

The source asks whether every open finite-measure spectral set on the real
line induces a number-rigid projection DPP.  This packet gives an exact
linear-rigidity classification for the separated interval sets

`S = union_n (3n, 3n + ell_n)`.

- `ell_n = 2^-n` gives a genuine number-rigid open set with infinitely many
  components.
- `ell_n = n^-p`, `p>1`, gives an explicit open finite-measure process that is
  not linearly number rigid.
- The latter is not claimed to be nonlinearly non-rigid; the packet records
  the failed Palm/deletion-tolerance upgrade and explains the obstruction.

Files:

- `solution_packet.pdf`: compiled proof packet.
- `source_paper.pdf`: official arXiv:1702.07323 PDF.
- `source_question_page.png`: full rendered source PDF page 3.
- `supporting_papers/2409.18519.pdf`: decisive linear-rigidity criterion.
- `supporting_papers/2407.14168.pdf`: later special infinite-union results.
- `code/check_interval_lengths.py`: finite-truncation sanity checks.
- `verification.md`: proof and rendering checks.

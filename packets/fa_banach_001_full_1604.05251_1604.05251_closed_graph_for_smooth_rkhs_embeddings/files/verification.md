# Verification

Verified on 2026-08-11.

- Rebuilt the 55-page source paper from the locally archived arXiv sources. The only source-build changes were compatibility edits in a temporary copy: an unused unavailable package was disabled and obsolete glossary-style hooks were replaced by current defaults. The mathematical source was unchanged.
- Located the question on rebuilt PDF page 9 and extracted `figures/open_problem_crop.png` from that page.
- Compiled `main.tex` with `latexmk -pdf -interaction=nonstopmode -halt-on-error`.
- Final artifact: `solution_packet.pdf`, A4, 3 pages, 274112 bytes.
- The final log contains no LaTeX errors, fatal errors, undefined references, or overfull boxes.
- Rendered and inspected all three pages after the final standards-compliance edit. No clipping, overlap, illegible formula, or bad page break remains.
- Extracted the final PDF text with Ghostscript and confirmed the closed-graph conclusion and the scope disclaimer concerning the separately corrected MMD theorem.

## Mathematical audit

- `C^m(Ω)` and `C^m_0(Ω)` are Fréchet for every finite `m` and for `m=∞` under the exact source topologies.
- RKHS-norm convergence implies pointwise convergence without any continuity hypothesis on `K`.
- Target convergence implies pointwise convergence because the zeroth-order seminorm is present.
- These two facts make the graph of the everywhere-defined canonical inclusion closed, so the Fréchet closed graph theorem applies.
- The quantitative derivative estimates are consequences of continuity and are not used circularly in the proof.

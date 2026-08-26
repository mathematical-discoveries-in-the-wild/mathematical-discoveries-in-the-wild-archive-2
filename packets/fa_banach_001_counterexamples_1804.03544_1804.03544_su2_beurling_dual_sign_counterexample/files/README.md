# SU(2) Beurling-ultradistribution sign counterexample

Status: `candidate_full_counterexample_likely_valid_needs_human_review`

## Result

The positive exponential in the second clause of source Conjecture 4.5.5 is
false.  The Dirac mass at the identity belongs to the asserted Beurling dual
(the source explicitly includes all ordinary distributions), but

    delta_e_hat(l) = I_(2l+1)

and the two extremal sub-Laplacian eigenvalues equal `l`.  Therefore the
proposed Hilbert--Schmidt norm is at least

    sqrt(2) exp(B l^(1/(2s))),

which is unbounded for every `B>0`.

The packet also proves the exact correction: use a negative exponential in
the Beurling clause.  The first, Roumieu-dual clause is correct.

## Files

- `main.tex` / `solution_packet.pdf`: self-contained proof and correction.
- `source_paper.pdf`: locally compiled 163-page arXiv source thesis.
- `Full_Tex.tex` / `Full_Tex.tex.gz`: archived arXiv source and gzip payload.
- `source_evidence_pages_147_149.pdf`: the source definitions and conjecture.
- `VERIFICATION.md`: proof audit and reproduction notes.
- `code/check_su2_blocks.py`: exact spectrum/sign checker.
- `rendered/`: latest RGB render of every final packet page.

The local source required two purely TeX-compatibility edits for TeX Live
2026 (a obsolete justification option and one `bm` expression); these do not
touch the mathematical target.  The exact archived gzip is retained.

## Reproduction

Run the checker:

    conda run --no-capture-output -n sandbox python \
      runs/fa_banach_001/solutions/counterexamples/1804.03544_su2_beurling_dual_sign_counterexample/code/check_su2_blocks.py

Compile from the packet directory:

    latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp/pdfs main.tex


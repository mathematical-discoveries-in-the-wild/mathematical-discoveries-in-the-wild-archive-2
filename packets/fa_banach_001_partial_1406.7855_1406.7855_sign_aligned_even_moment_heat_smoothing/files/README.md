# Sharp heat smoothing for sign-aligned Walsh spectra

Status: candidate_partial_result_likely_valid

For every even integer \(p=2m\) and for \(p=\infty\), this packet proves
the Mendel--Naor heat-smoothing estimate with the sharp rate \(e^{-kt}\)
for real tail functions whose Walsh coefficients can all be made
nonnegative by a cube translation and an overall sign.

The result allows arbitrarily wide Fourier support above degree \(k\).
The proof is a \(2m\)-fold moment expansion: after symmetrization, the
generator inserts the average of \(2m\) Fourier degrees, and sign alignment
prevents cancellation.

Novelty confidence is moderate. Targeted searches found later work on
narrow spectra and holomorphic settings, but no matching sign-aligned
even-moment statement. The general scalar conjecture remains open.

Human review should focus on the zero-symmetric-difference expansion, the
symmetrization of the distinguished generator factor, and the exact role
of the translation character.

Files:

- solution_packet.pdf: self-contained proof and source context;
- source_paper.pdf: locally rendered exact arXiv source;
- figures/source_conjecture_page.png: source page containing Conjecture 1.1;
- code/verify_even_moment.py: finite-cube numerical sanity check;
- the run attempt log records eight focused upgrade attempts.


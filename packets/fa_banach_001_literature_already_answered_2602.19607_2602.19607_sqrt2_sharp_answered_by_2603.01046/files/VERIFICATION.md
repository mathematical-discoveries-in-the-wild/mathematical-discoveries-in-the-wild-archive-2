# Verification record

## Mathematical cross-check

- Confirmed from the source TeX and compiled PDF that arXiv:2602.19607 asks whether `sqrt(2)` is optimal simultaneously in the eigenvalue and symmetric-norm corollaries.
- Confirmed from the source TeX and compiled PDF of arXiv:2603.01046 that Question 2.2 reproduces the same question, Theorem 2.5 answers it affirmatively for every `n >= 3`, and Remark 2.6 explicitly covers the eigenvalue inequality at `j=0`.
- Recomputed the rank-one formula, tetrahedral tight-frame identity, spectra of `S^T S` and `S S^T`, and the exact quotient `sqrt(2)` independently.
- Compared the numerical-search extremizer with Zhang's matrices: they agree up to global sign, vector signs, and relabelling, all of which leave the relevant symmetric moduli and quotient unchanged.

## Novelty check

A bounded search on 2026-08-11 used the exact title, `operator symmetric modulus`, `best possible`, and `sqrt(2)`. It found arXiv:2603.01046, submitted 1 March 2026, whose abstract explicitly says that it answers Bourin--Lee questions. Direct source inspection established an exact match. No originality claim is made for the construction.

## PDF verification

- Source and supporting PDFs were compiled locally from the cached arXiv TeX sources.
- Question and theorem crops were rendered from those PDFs and visually inspected.
- `solution_packet.pdf` was compiled with `latexmk`, rendered page by page, and visually inspected.
- The final log was checked for overfull boxes and unresolved references.

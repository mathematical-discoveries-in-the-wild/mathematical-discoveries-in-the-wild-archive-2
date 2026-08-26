# Orthogonal semilattice crossed product is not the l1 quotient

**Status:** candidate full counterexample to the stronger equality speculation
in Remark 27 of arXiv:2601.14907; the preceding general faithfulness question
remains open.

Take the orthogonal semilattice `S={0,e_n}` and let it act identically on the
coordinate ideals of `A=c_0`.  Then `Null=0` and the convolution algebra is
pointwise `ell^1`, but every integrated covariant representation sees only the
coefficient sum in `c_0`.  The identity representation attains the sup norm,
so the universal crossed product is `c_0`, not the Banach quotient `ell^1`.

Contents:

- `solution_packet.pdf`: review-ready proof packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_question_crop.png`: actual page-13 source crop.
- `code/verify_orthogonal_semilattice.py`: finite-truncation sanity checks.
- `verification.md`: commands and expected output.
- `main.tex`: packet source; build artifacts remain in `tmp/`.

Related unresolved work is recorded at
`attempts/2601.14907_maximal_seminorm_faithfulness_attempt.md`.


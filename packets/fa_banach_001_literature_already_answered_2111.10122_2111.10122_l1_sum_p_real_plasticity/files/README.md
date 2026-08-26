# The finite-p `ell_1`-sum subcase is already answered

Status: `literature_already_answered (ell_1 direct-sum_p R subcase,
1<p<infinity)`.

Source/open-problem paper: Rainis Haller, Nikita Leo, and Olesia Zavarzina,
*Two new examples of Banach spaces with a plastic unit ball*, arXiv:2111.10122;
Acta et Commentationes Universitatis Tartuensis de Mathematica 26 (2022),
89--101.  Its introduction (PDF page 1) asks whether every Banach-space unit
ball is plastic, and Theorem 3 proves the particular case
`ell_1 direct-sum_2 R`.

Exact later answer: Nikita Leo, *Banachi ruumi ühikkera plastilisus*
(*Plasticity of the Unit Ball of a Banach Space*), Master's thesis, University
of Tartu, 2024.  Chapter 2, Theorem 2.1 (printed page 14; PDF page 14) proves
that `B_(ell_1 direct-sum_p R)` is plastic for every `1<p<infinity`.

## Identification

The relation is explicit, not merely inferred.  At the start of Chapter 2 the
thesis cites the Haller--Leo--Zavarzina paper, says that the article is
restricted to `p=2`, and says the chapter generalizes it by allowing arbitrary
real `p>1`.  Theorem 2.1 then states the exact all-finite-`p` conclusion.

This is the same strengthening independently reached during the direct attack:
the source's Euclidean proof extends after replacing its two quadratic distance
identities by monotonicity of the corresponding scalar `p`-distance profiles.
Because the 2024 thesis already contains the theorem and proof, this is not a
new run result.

## Scope

- Answered in the thesis: `ell_1 direct-sum_p R` for every `1<p<infinity`.
- The endpoint `p=1` is already isometric to `ell_1` and follows from the
  classical plasticity theorem for `ell_1`.
- Not answered by this identification: `p=infinity` or the source's full
  question for arbitrary Banach spaces.

## Files and retrieval note

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered note.
- `source_paper.pdf`: arXiv:2111.10122.
- `supporting_thesis_metadata.md`: stable repository metadata, exact theorem
  location, and official PDF link.

The official thesis PDF was inspected through the University of Tartu DSpace
record.  Repeated direct file transfers from the DSpace bitstream endpoint
stalled in this environment, so the packet records the stable item and PDF
links rather than pretending a local supporting copy succeeded.

Human review recommendation: accept as exact later-literature resolution of
the finite-`p` subcase and retain it for duplicate memory; do not count it as a
new proof.

# Counterexample: arXiv:1011.5400

This packet gives an explicit 11-diagram dependence in `D_5(0,6)` when
`n=2`, contradicting the linear-independence clause of Theorem 3.5 as
printed.

The relation has a short hand proof: after imposing three adjacent
opposite-color pairs, its tensor coefficient reduces to a pigeonhole identity
for three elements of a two-point set. An exhaustive coordinate checker tests
all `4^6=4096` coordinates. A separate exact symbolic enumeration gives the
full degree-six determinant

`N^33 (N-2)^26 (N-4)^2`, where `N=2n`,

and rank 31 at `N=4`.

Files:

- `solution_packet.pdf`: self-contained counterexample proof.
- `source_paper.pdf`: archived arXiv:1011.5400 PDF.
- `source_theorem_crop.png`: real screenshot of source Theorem 3.5.
- `main.tex`: packet source.
- `code/check_relation.py`: exhaustive direct tensor-coordinate audit.
- `code/gram_small.py`: exact diagram enumeration and determinant audit.
- `code/crop_source.py`: reproducible source crop.
- `VERIFICATION.md`: audit trail, visual QA, and hashes.

The spanning statement and the cases `n>=3` are not decided here.

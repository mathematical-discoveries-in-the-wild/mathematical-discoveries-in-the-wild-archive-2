# No unconditional basis at the critical first-difference Besov endpoint

Status: `candidate partial result; likely valid`.

For the open parameter range

`0 < p < q <= 1`, `s = d(1/p - 1)`, `s < 1/p`,

this packet proves that `B^s_{p,q,1}(I^d)` cannot possess an unconditional
Schauder basis. Its Banach envelope is canonically `L1(I^d)`: the source
embedding supplies one norm inequality, while a sharp dyadic-atom estimate
at critical scaling supplies the other. A hypothetical unconditional basis
would pass through the envelope and give an unconditional basis of `L1`,
contrary to the classical nonexistence theorem.

The existence of a conditional Schauder basis remains open. The envelope
argument cannot exclude it because `L1` has conditional bases. Focused
upgrade attempts against smooth wavelets, spline systems, the approximation
property, and alternative block constructions did not close this gap.

Files:

- `solution_packet.pdf`: review-ready proof packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: original arXiv PDF.
- `figures/open_question_crop.png`: genuine crop from source PDF page 2.
- `VERIFIER_REPORT.md`: proof and scope audit.
- Ledger: `runs/fa_banach_001/ledger/results/2002.12917_critical_besov_no_unconditional_basis.json`.

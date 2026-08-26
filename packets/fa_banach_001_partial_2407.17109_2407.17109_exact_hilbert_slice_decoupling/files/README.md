# Exact Hilbert-slice quantum/classical decoupling

This packet records a candidate new exact refinement adjacent to arXiv:2407.17109v2.

## Result

For every finite frequency family and every `1 <= q <= infinity`,

`D^Q_{2,q} = D^C_{2,q}`.

The unitary map `U = F_sigma F_W` identifies Hilbert--Schmidt operators with
`L^2` functions, preserves every localization constraint, and preserves the
norm of each term and its sum.  For `N` pairwise disjoint positive-measure
pieces, the common sharp constant is `1` for `q <= 2` and
`N^(1/2 - 1/q)` for `q >= 2`.

The paper's queued “natural question” is answered by the paper itself.  This
packet instead strengthens the paper's adjacent `p=q=2` optimality remark.

## Files

- `main.tex`: complete definitions, theorems, proofs, sharpness, and limits.
- `solution_packet.pdf`: compiled proof packet.
- `source_paper.pdf`: official arXiv v2 PDF.
- `figures/open_problem_crop.png`: source page-2 theorem and optimality remark.
- `tmp/`: compilation and page-render QA artifacts.

## Review recommendation

Check the normalization `F_sigma^2=I`, the support identity
`F_sigma(U T)=F_W(T)`, and novelty against the published paper and standard
decoupling references.  The mathematical proof is short and exact; the main
remaining uncertainty is literature priority.

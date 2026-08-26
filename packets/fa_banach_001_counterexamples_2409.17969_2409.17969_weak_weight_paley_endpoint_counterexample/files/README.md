# Weak-weight Paley: endpoint counterexample and interior theorem

This packet answers the literal all-exponent question in Remark 5.2(1) of
arXiv:2409.17969 negatively.  On every rank-one noncompact symmetric space,
the Plancherel-critical weight `u(lambda)=(1+|lambda|)^(-n)` has finite weak
`L^1` norm, but normalized shrinking approximate identities force the proposed
`p=q=1` Paley integral to grow like `log R`.

The same packet proves a positive upgrade for every `1<p<2` and strict
interior `p<q<p'`.  Real interpolation sharpens the source's restriction and
Hausdorff-Young bounds to a Lorentz `L^{p',p}` estimate, which pairs exactly
with the weak weight through Lorentz Holder.  The edge lines `q=p,p'` remain
open for `1<p<2`.

Status: `candidate_counterexample_likely_valid`, pending human review.

Files:

- `main.tex`: counterexample, interior theorem, and scope boundary.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: official arXiv source PDF.
- `figures/open_problem_crop.png`: exact question on source PDF page 27.
- `code/verify_exponents.py`: deterministic exponent and critical-weight
  checks.
- `VERIFICATION.md`: proof, literature, build, visual-QA, and hash record.


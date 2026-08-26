# Full result: exact transfer criteria without the full-preimage sigma hypothesis

Status: `candidate_full_solution_likely_valid` (pending expert review)

Source: D. Dhara, P. Pattanayak, R. Rattan, and S. Sarkar,
“k-quasi n-power posinormal Weighted Composition and Cauchy Dual of
Moore-Penrose inverse of Lambert Operators,” arXiv:2507.06511, Section 6,
physical PDF page 15.

The source's first future-work direction asks to relax
`T^{-k}(Sigma)=Sigma`. This packet removes that assumption for the ordinary
and weighted composition results, including the adjoints. For
`W=M_pi C_phi`, define the transfer operator `P_j=(C_phi^*)^j`, orbit weight
`pi_j`, and `q_j=P_j(|pi_j|^2)`. The packet proves exact scalar
necessary-and-sufficient conditions for `W` in both regimes `k>=n` and `k<n`.
The harder second regime follows from a sharp weighted transfer lemma whose
optimal constant is `||P_r(|b|^2/q)||_infinity`. It also reduces the condition
for `W^*` to an exact one-step transfer inequality on `L^2(supp q_k)`.

No invertibility, full-preimage sigma-algebra, or real/nonnegative weight is
required. The unweighted formulas follow by taking `pi=1`. A three-point
noninvertible example shows that the theorem applies strictly beyond the
source hypothesis and computes optimal constants.

Files:

- `solution_packet.pdf`: review-ready proof packet.
- `main.tex`: self-contained proof source.
- `source_paper.pdf`: exact source PDF compiled from the stored arXiv source.
- `figures/open_problem_crop.png`: rendered source-page evidence.
- `code/verifier.py`: independent weighted finite-matrix verifier.
- `VERIFIER_REPORT.md`: command, checked claims, and recorded verdict.

Novelty check: bounded run-index and arXiv searches on 2026-08-11 using the
exact future-work sentence, title/id, author combinations, and core operator
terms found no later resolution or transfer characterization. This does not
guarantee priority.

Human-review recommendation: inspect the extended-quotient/truncation step in
the sharp transfer lemma and the closure identity
`closure Ran(W*^k)=L^2(supp q_k)`. The finite verifier checks both regimes and
sharp constants in 920 cases, 43 systems being noninjective.

# Counterexample packet: the domain hypothesis cannot be dropped from Theorem 5.2

status: candidate_counterexample_likely_valid

source_arxiv: 2204.00146

source_result: Theorem 5.2 and the final future-work paragraph in Section 5 of Arora--Gluck, *Criteria for eventual domination of operator semigroups and resolvents*.

scope: full counterexample to the literal domain-free extension of the four-way equivalence in Theorem 5.2; not a complete characterization of every possible relation between resolvent and Cesaro positivity.

## Result

On (E=L^2(0,1)), let (u=mathbf 1), let

\[
Pf=\left(\int_0^1 f(s)\,ds\right)\mathbf 1,
\qquad A=P-I.
\]

Then (A) generates a bounded positive uniformly continuous semigroup, (s(A)=0) is a simple pole, and the associated spectral projection is (P). The Cesaro means are strongly positive with respect to (mathbf 1) for every positive averaging time; (P) is strongly positive; and the individual strong maximum principle holds at (0). Nevertheless, the individual strong anti-maximum principle fails. A single witness is

\[
f(x)=x^{-1/4}\in L^2(0,1)_+.
\]

Indeed, at (mu=-1/2),

\[
R(\mu,A)f=2f-\frac{16}{3}\mathbf 1,
\]

which is positive near (0). More strongly, the same (f) violates anti-maximum negativity for every (mu\in(-1,0)). Since (operatorname{dom}(A)=L^2(0,1)\not\subset L^\infty(0,1)=E_u), this gives the requested sharp boundary example.

## Literature audit

The same rank-one generator appears on PDF page 3 of Arora--Gluck, arXiv:2203.05680v2. That passage displays the correct resolvent formula but then asserts the operator inequality (R(\mu,A)\preceq-P) for every (mu\in(-1,0)). The witness above disproves even (R(-1/2,A)f\le0). This packet therefore records a correction to that auxiliary example. It does **not** challenge Theorem 1.2 of that paper, whose additional domination assumption is not satisfied here.

## Evidence

- `source_paper.pdf`: arXiv:2204.00146v3.
- `supporting_paper_2203.05680.pdf`: arXiv:2203.05680v2, containing the audited rank-one passage.
- `figures/open_problem_crop.png`: source page 18, including the future-work paragraph.
- `figures/literature_audit_crop.png`: supporting-paper page 3, including the displayed claim under audit.
- `main.tex`: self-contained formal proof and scope discussion.
- `VERIFICATION.md`: independent algebra, order, quantifier, source, and render checks.
- `solution_packet.pdf`: compiled review packet.

## Novelty check

A bounded search on 2026-08-09 covered the run's registry, solution, attempt, and proof-gap indexes; the local full-source corpus; arXiv searches for the exact source id and title; the phrases `rank-one projection`, `A=P-I`, `Cesaro means`, `anti-maximum principle`, `dom(A)`, and `E_u`; and searches for an erratum or correction to arXiv:2203.05680. No prior run result, later correction, or exact published statement of the conclusion in this packet was found. The construction itself is not new: it is the construction printed in arXiv:2203.05680. The candidate novelty is the corrected sign/order analysis and its consequence for the domain-free extension of source Theorem 5.2. Novelty confidence is therefore **medium**, while mathematical-validity confidence is **high pending human review**.

## Human review recommendation

Verify the order calculation at (mu=-1/2), the quantifier strengthening for all (mu\in(-1,0)), and the interpretation of source Theorem 5.2 without its domain hypothesis. The broad future-work program remains open: this example does not separate Cesaro positivity from right-hand resolvent positivity, since both hold; it separates them jointly from the anti-maximum conclusion.

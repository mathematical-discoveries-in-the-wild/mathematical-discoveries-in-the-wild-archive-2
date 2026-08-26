# Verifier report

Date: 2026-08-13

Verdict: `likely valid`, suitable for human scope review as a candidate counterexample to the literal displayed Conjecture 2 of arXiv:1901.07496v2.

## Proof audit

- For repeated vectors (x_1=\cdots=x_n=x\neq0), the cotype-(r) left side is exactly (n^{1/r}\|x\|).
- The Rademacher square mean is exactly (\sqrt n\|x\|), because (\mathbb E|\sum_j\varepsilon_j|^2=n).
- Therefore a cotype-(r) constant would dominate (n^{1/r-1/2}) for every (n), impossible when (r<2).
- For every discrete group, the trivial isometric representation on the one-dimensional conjugate-exponent space has constant coefficient (1), so the source-defined (B_p(\Gamma)) is nonzero.
- With (p=3), the displayed conjugate exponent is (q=3/2<2), giving an explicit counterexample even for the trivial group.

No hidden infinite-dimensionality, amenability, or representation-theoretic assumption is used.

## Scope audit

Daws's cited paper was inspected directly. Section 8.3, after Proposition 8.8 (journal page 74; PDF page 28), conjectures cotype `max(p,p')`, not an unrestricted conjugate exponent. It also announces a convention swap relative to Runde. Hence:

- the source conjecture is false literally and without an exponent range;
- the elementary example does not refute Daws's original corrected conjecture;
- the source's Conjecture 1 remains open.

## Render audit

The final three-page PDF was rendered at 150 dpi and inspected page by page. The source crop is readable and contains the coefficient-space definition, Proposition 1, the cotype transition, and the full displayed Conjecture 2. There is no clipping, overlap, overfull box, undefined reference, or undefined citation. The LaTeX log contains one harmless underfull bibliography line.

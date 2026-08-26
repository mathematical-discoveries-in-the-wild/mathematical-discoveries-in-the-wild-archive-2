# Verification report

## Claim audit

- The current source is arXiv:2408.00422v2, revised 8 November 2025 and published in 2026.
- Section 6.2 says that the epsilon-scaling for general \(L^p\) graphons was not determined; the conclusion repeats the point.
- The source defines \(L^p\) graphons for \(p\geq1\) on \((0,1)^2\), hence every such kernel lies in \(L^1\).
- Nonnegativity is made explicit in the packet, because it is required for the energy and the monotone truncation argument.
- The displayed statement of Theorem 6.2 in the current PDF says \(\epsilon\to\infty\), an apparent typographical error: the section heading, Lemma 6.2, proof, conclusion, and every surrounding statement use the intended sharp-interface limit \(\epsilon\to0\).

## Proof audit

1. **Product convergence:** the source's narrow-product lemma applies to every bounded continuous \(q_R(\lambda,\mu)\).
2. **Testing against the kernel:** the averaged \(q_R\) converge weak-star in \(L^\infty((0,1)^2)\), and \(W\in L^1\) is an admissible test function.
3. **Dirichlet liminf:** \(D^W\geq D^W_R\); pass to the limit for fixed \(R\), then use monotone convergence as \(R\uparrow\infty\).
4. **Potential liminf:** the identical argument with \(\Phi_R=\min(\Phi,R)\) handles the unbounded quartic potential.
5. **Binary characterization:** \(V(\nu)=0\) if and only if \(\nu_x\) is supported on \(\{-1,1\}\) for almost every \(x\).
6. **Finite binary energy:** \(D^W(\nu)\leq4\lVert W\rVert_1\) on the binary class.
7. **Identification with TV:** on \(\{-1,1\}^2\), \(|\lambda-\mu|^2=2|\lambda-\mu|\), exactly matching the source normalization.
8. **Recovery:** the constant sequence has zero potential and the required limiting Dirichlet coefficient.
9. **Coefficient trichotomy:** the finite-coefficient case follows from eventual lower bounds on \(a_\epsilon\); the divergent case follows from lower semicontinuity whenever \(D^W(\nu)>0\), with a constant recovery sequence when \(D^W(\nu)=0\).

## Adversarial checks

- Narrow convergence does not make \(D^W\) globally continuous when second moments escape. The proof claims only lower semicontinuity and explicitly uses truncation.
- The theorem allows \(D^W=+\infty\) away from the binary class. Gamma convergence is an extended-valued theory, so this is not an obstruction.
- If \(W\) changes sign, the truncation monotonicity and energy lower bound fail; signed kernels are excluded.
- If \(W\notin L^1\), binary Dirichlet energies can be infinite and the \(L^1\)-testing step fails; nonintegrable kernels are excluded.

## Novelty audit

Bounded searches through 2026-08-13 covered the run indexes, current arXiv v2 text and references, exact-title citations, and arXiv/general scholarly queries combining graphon Ginzburg--Landau, \(L^1/L^p\), unbounded kernels, Gamma convergence, and epsilon scaling. No later resolution was located. Specialist priority review is recommended because the conclusion is short and directly contradicts the source's scaling heuristic.

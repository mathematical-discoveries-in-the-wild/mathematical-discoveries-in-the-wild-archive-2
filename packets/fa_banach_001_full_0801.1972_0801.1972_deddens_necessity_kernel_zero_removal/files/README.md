# Necessity in Deddens's analytic-Toeplitz intertwining conjecture

Status: `candidate_full_proof_likely_valid`

Source: Paul S. Bourdon and Joel H. Shapiro, *Intertwining relations and
extended eigenvalues for analytic Toeplitz operators*, arXiv:0801.1972.

Source location: introduction, PDF page 3. The paper states that necessity
remains open in Deddens's conjecture: if

```text
X T_phi = T_psi X  with X nonzero,
```

must the complex conjugate of `psi(D)` be contained in the point spectrum of
`T_phi^*`?

## Result

The packet proves the necessity statement in full. Reparametrize the Hardy
kernel analytically by

```text
k_zeta(w)=1/(1-zeta w)
```

and set `F(zeta)=X^* k_zeta`. The adjoint intertwining relation gives the
analytic eigenfield identity

```text
T_phi^* F(zeta)=conj(psi(conj(zeta))) F(zeta).
```

The field is not identically zero because the reproducing kernels span a
dense subspace. At a zero `zeta_0`, factor
`F(zeta)=(zeta-zeta_0)^m G(zeta)` at its first nonzero Taylor coefficient.
After cancelling off the zero and taking the limit, `G(zeta_0)` is a nonzero
eigenvector with the previously missing eigenvalue. This works at every zero,
so the entire conjugate image lies in the point spectrum.

## Packet contents

- `main.tex`: complete proof.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: arXiv source paper.
- `figures/source_page_03.png`: source statement that necessity remains open.
- `verification.md`: convention, analyticity, zero-removal, and literature audit.

Human review recommendation: **review as a full proof of the necessity half
of Deddens's conjecture**. The decisive check is the elementary
Banach-valued analytic zero-removal lemma.

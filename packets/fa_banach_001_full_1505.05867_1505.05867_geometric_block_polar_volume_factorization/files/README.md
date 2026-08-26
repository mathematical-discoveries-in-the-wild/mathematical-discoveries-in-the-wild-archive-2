# Geometric block-polar proof of the mixed-ball volume factorization

Status: `candidate full solution (likely valid; human review requested)`.

## Source problem

Henning Kempka and Jan Vybíral, *Volumes of unit balls of mixed sequence
spaces*, arXiv:1505.05867. In the closing remarks (source PDF page 13), the
authors ask whether

\[
\operatorname{vol}(B_{p,q}^{m,n})
=\operatorname{vol}(B_q^{mn})
 \left(\frac{\operatorname{vol}(B_p^m)}
 {\operatorname{vol}(B_q^m)}\right)^n
\]

has a geometric or combinatorial interpretation yielding a non-analytic proof.

## Result

Yes. More generally, for any two bounded star bodies `K,L` in `R^m`, the
`l_q`-sums of `n` copies satisfy

\[
\frac{\operatorname{vol}(\mathcal B_q^{(n)}(K))}
 {\operatorname{vol}(\mathcal B_q^{(n)}(L))}
=\left(\frac{\operatorname{vol}(K)}{\operatorname{vol}(L)}\right)^n.
\]

The proof is a block-shell argument. The volume of the gauge shell of `K` at
radius `r` is `m vol(K) r^{m-1} dr`. The admissible block radii
`(r_1,...,r_n)` occupy the same `l_q`-ball for every inner body. Replacing `L`
by `K` therefore multiplies each of the `n` independent shell measures by
`vol(K)/vol(L)`. No gamma integral is evaluated.

Equivalently, match the normalized cone measures on the boundaries of `L` and
`K`, extend that matching homogeneously along rays, and apply it independently
to all `n` blocks. The resulting a.e. geometric transport preserves every
block radius, maps the `L`-mixed ball onto the `K`-mixed ball, and scales
Lebesgue volume by `(vol(K)/vol(L))^n`.

Taking `K=B_p^m` and `L=B_q^m` gives the displayed source identity because
`mathcal B_q^{(n)}(B_p^m)=B_{p,q}^{m,n}` and
`mathcal B_q^{(n)}(B_q^m)=B_q^{mn}`.

## Scope and literature check

- This completely answers the paper's second closing question.
- The first closing question, asking for weak-Lorentz-ball volumes, was later
  answered by Doležalová--Vybíral, arXiv:1906.04997, and is not claimed here.
- A bounded search on 11 August 2026 covered the exact question, title and
  formula; citations of the source; mixed-ball volume-ratio and block-polar
  terms; and later mixed-norm volume papers. No later source giving this exact
  geometric shell proof was found. This supports but does not prove novelty.

## Files

- `main.tex`, `solution_packet.pdf`: complete proof packet.
- `source_paper.pdf`: arXiv:1505.05867.
- `figures/source_page-13.png`: rendered source evidence.
- `proof.md`: standalone formal proof.
- `verification.md`: proof audit and novelty-search bounds.
- Ledger: `runs/fa_banach_001/ledger/results/1505.05867_geometric_block_polar_volume_factorization.json`.

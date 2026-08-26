# Sharp Hyers--Ulam constants for max products

Status: `substantial_partial`, likely valid, pending human review.

The source survey asks whether the optimal affine Hyers--Ulam constant \(H(E)\) equals the Jung constant \(J(E)\) for every real Banach space. This packet proves a max-product propagation theorem:

\[
J\!\left((\prod_i X_i)_\infty\right)=\sup_iJ(X_i),
\qquad
H\!\left((\prod_i X_i)_\infty\right)\geq\sup_iH(X_i).
\]

Consequently, if \(\sup_iH(X_i)=\sup_iJ(X_i)\)—in particular, if every factor satisfies \(H(X_i)=J(X_i)\)—then the product also satisfies the exact equality \(H=J\).

This gives exact constants for broad non-Hilbert classes, including arbitrary max products of Hilbert spaces and every \(c_0\oplus_\infty Y\), for which \(H=J=2\). A concrete new-looking finite-dimensional case is
\(H(\ell_2^2\oplus_\infty\mathbb R)=J(\ell_2^2\oplus_\infty\mathbb R)=2/\sqrt3\).

The full arbitrary-space conjecture remains open. Five focused upgrade attempts are recorded in `runs/fa_banach_001/attempts/0201098_linf_product_hyers_ulam_jung_upgrade.md`; the obstruction is that non-max sums have Jung-extremal configurations coupling coordinates, while the lift only transfers coordinatewise bad nearisometries.

Contents:

- `main.tex` / `solution_packet.pdf`: theorem, proof, examples, limitations, and novelty audit.
- `source_paper.pdf`: Väisälä's survey, arXiv:math/0201098.
- `supporting_huuskonen_vaisala_2002.pdf`: known factor equalities for Hilbert spaces.
- `figures/source_question.png`: crop of the exact question on printed page 4.
- `verification_report.md`: mathematical, novelty, source, and rendered-PDF checks.

Ledger: `runs/fa_banach_001/ledger/results/0201098_linf_product_hyers_ulam_jung_constants.json`.

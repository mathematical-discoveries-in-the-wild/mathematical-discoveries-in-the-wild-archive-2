# Sharp Sobolev extension constant for planar sectors

Status: `literature_implied_answer` (full answer to the wedge asymptotic)

Original source: Vladimir Lotoreichik, *Lower bounds on the norms of extension
operators for Lipschitz domains*, arXiv:1306.1524, Remark 4.6 on PDF page 15.

Answer source: Rafik Zeraoulia, *Sharp \(W^{1,2}\) Extension Constants for
Planar Sectors*, Zenodo DOI
[`10.5281/zenodo.20534573`](https://doi.org/10.5281/zenodo.20534573),
Theorem 1 on PDF page 2 (4 June 2026).

## Identification

The source asks for the exact asymptotics of the least full-plane extension
norm \(\mathcal E(\Omega_{\pi-\theta})\) as \(\theta\downarrow0\).
Zeraoulia's Theorem 1 computes the sharp constant for every planar sector of
opening \(0<\varphi<2\pi\):

\[
  C_{\rm full}(\varphi)
  =\left(1+\max\left\{\frac{\varphi}{2\pi-\varphi},
  \frac{2\pi-\varphi}{\varphi}\right\}\right)^{1/2}
  =\left(\frac{2\pi}{\min\{\varphi,2\pi-\varphi\}}\right)^{1/2}.
\]

For the convex wedges of the source, \(0<\varphi\le\pi\), this becomes
\(\mathcal E(\Omega_\varphi)=\sqrt{2\pi/\varphi}\). Hence

\[
 \mathcal E(\Omega_{\pi-\theta})
 =\sqrt2+\frac{\sqrt2}{2\pi}\theta
  +\frac{3\sqrt2}{8\pi^2}\theta^2+O(\theta^3).
\]

The later paper does not cite arXiv:1306.1524, so the relation requires direct
identification and belongs in `literature_implied_answers`.

## Independent proof check

The proof was independently reconstructed before the supporting paper was
located. The upper bound is the angular reflection-dilation
\(u(r,\eta)\mapsto u(r,\varphi(2\pi-\eta)/(2\pi-\varphi))\).
Its exterior squared norm is exactly a weighted sum with coefficients
\((2\pi-\varphi)/\varphi\) and its reciprocal. For the lower bound,
logarithmic polar coordinates turn Dirichlet energy into strip energy;
slow symmetric and antisymmetric boundary traces force the two reciprocal
ratios. Dilation toward the vertex makes the \(L^2\) term negligible. This
matches Sections 3--5 of the supporting paper and checks the norm convention.

## Files

- `source_paper.pdf`: arXiv:1306.1524.
- `supporting_paper_zenodo_20534573.pdf`: the exact-answer paper.
- `main.tex`, `solution_packet.pdf`: compact identification note.

# Exact weighted Sobolev constant via a flat cone

Status: **candidate full result, likely valid; human review requested**

Source paper: T. H. Giang, N. M. Tri, and D. A. Tuan, *On some Sobolev
and Pólya--Szegö type inequalities with weights and applications*,
arXiv:2412.15490.

Source question: Remark 3, source PDF page 10, asks for the exact value of
the best constant (C_{2\alpha,6}) in
\[
 C_{2\alpha,6}
 \left(\int_{\mathbb R^3}|x|^{2\alpha}|u|^6\right)^{1/6}
 \leq
 \left(\int_{\mathbb R^3}
 (|\nabla_xu|^2+|x|^{2\alpha}|u_y|^2)\right)^{1/2}.
\]

## Result

For every \(\alpha>0\),
\[
 \boxed{C_{2\alpha,6}=C_{\mathrm{Euc},3}
 =\sqrt3\left(\frac{\pi}{2}\right)^{2/3}.}
\]
Thus the sharp constant is independent of \(\alpha\).

## Proof map

1. In cylindrical coordinates set
   \(\rho=r^{\alpha+1}/(\alpha+1)\),
   \(\varphi=(\alpha+1)\theta\), and \(z=y\).
2. This is an exact isometry of both terms in the quotient onto the ordinary
   Sobolev quotient on the flat cone
   \(C_{2\pi(\alpha+1)}\times\mathbb R\).
3. Remove the singular axis by a logarithmic cutoff of vanishing energy.
4. Every compact subset away from the axis embeds isometrically in a smooth
   complete Cartan--Hadamard 3-manifold obtained by rounding the cone tip with
   a convex surface-of-revolution profile.
5. Kleiner's sharp three-dimensional Cartan--Hadamard isoperimetric theorem,
   followed by the standard coarea rearrangement argument, gives the
   Euclidean sharp Sobolev lower bound.
6. Conversely, arbitrarily large Euclidean balls occur far from the cone
   axis, so truncated Aubin--Talenti bubbles give the Euclidean upper bound.

## Packet contents

- `solution_packet.pdf`: complete proof and review packet.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: local render from the ingested arXiv source.
- `figures/open_problem_crop.png`: source Remark 3 and its surrounding
  normalization.
- `VERIFICATION.md`: adversarial verification report.
- `tmp/`: build and rendered-page intermediates.

## Novelty check

Bounded searches through 9 August 2026 used the arXiv id, exact paper title,
the exact open-question phrase, `C_{2 alpha,6}`, `weighted Sobolev best
constant`, `Grushin sharp Sobolev constant`, and the source authors. They
found the source/prepublication record and general Cartan--Hadamard Sobolev
literature, but no later paper identifying this weighted quotient with the
flat angle-excess cone or giving the stated exact constant. This is not a
comprehensive priority search.

## Human review recommendation

**Send to human.** Check especially the exact change-of-variables identities,
the smooth Cartan--Hadamard completion of each compact cone exterior, and the
logarithmic zero-capacity cutoff at the singular axis.


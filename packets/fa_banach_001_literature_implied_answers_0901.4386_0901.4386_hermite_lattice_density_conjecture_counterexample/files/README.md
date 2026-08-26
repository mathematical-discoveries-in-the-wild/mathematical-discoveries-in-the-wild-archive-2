# Literature-Implied Counterexample: the Hermite lattice-density conjecture

## Source question

- Source: L. D. Abreu, *Sampling and interpolation in Bargmann--Fock spaces of polyanalytic functions*, arXiv:0901.4386.
- Location: the displayed conjecture in the Overview and the discussion in “Further questions.”
- Claim tested: if a lattice \(\Lambda\subset\mathbb R^2\) makes \(G(h_n,\Lambda)\) a Gabor frame, then \(D(\Lambda)>n\). The surrounding paragraph uses the shifted form \(G(h_{n-1},\Lambda)\) with threshold \(n\).

## Full answer

The conjecture is false, even for a square lattice.

Faulhuber--Shafkulovska--Zlotnikov (2025), Proposition 3.8, prove that
\[
  G\!\left(h_9,\frac1{\sqrt3}\mathbb Z^2\right)
\]
is a Gabor frame for \(L^2(\mathbb R)\).  In the source paper's convention,
\(D(A\mathbb Z^2)=|\det A|^{-1}\).  For \(A=3^{-1/2}I_2\),
\[
  D\!\left(\frac1{\sqrt3}\mathbb Z^2\right)
  =\left|\det(3^{-1/2}I_2)\right|^{-1}=3.
\]
Thus the frame exists although \(3\not>9\).

This also defeats the intended shifted reading: write \(h_9=h_{n-1}\) with
\(n=10\); then the proposed necessary inequality would be \(D(\Lambda)>10\),
again contradicted by \(D(\Lambda)=3\).

## Status and scope

`literature_implied_counterexample (full negative answer to the lattice Hermite-density conjecture)`.

This is not an original theorem.  It is the direct implication of a later
published frame theorem and the source paper's explicit definition of lattice
density.  It does not classify the full frame set of \(h_9\), and it does not
settle the source paper's broader questions about Haar-window superframes or
vector-valued coherent states.

The run already contained a packet for arXiv:0804.4613 recording critical
square-lattice frames of density \(n+1\) for \(n\ge4\).  Proposition 3.8 is
strictly more decisive for the literal conjecture in arXiv:0901.4386: its
density is only \(3\) while the Hermite order is \(9\).

## Files

- `main.tex`: proof note.
- `solution_packet.pdf`: rendered proof note.
- `source_paper.pdf`: source paper.
- `supporting_paper_faulhuber_shafkulovska_zlotnikov_2025.pdf`: later theorem.
- `VERIFICATION.md`: exact source/support checks.


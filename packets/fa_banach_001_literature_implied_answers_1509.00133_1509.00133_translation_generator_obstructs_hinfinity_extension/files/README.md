# A translation-generator obstruction to the proposed strip calculus

**Status:** `literature_implied_answer (full negative answer to the universal
extension question, under the standard functional-calculus interpretation)`

## Source question

Gordon Blower and Ian Doust, *Operational calculus and integral transforms for
groups with finite propagation speed*, arXiv:1509.00133, Remark 4.2 on printed
page 11, ask whether their homomorphism

\[
  \Phi_A:\mathcal A\longrightarrow\mathcal L(E)
\]

extends to a bounded algebra homomorphism on
`H^infinity(Sigma_{omega_0})`. The full source page is preserved in
`figures/open_problem_page.png`.

## Identification

There is no such extension in general. Let `1<q<infinity`, `q != 2`, and let
`A` be the Fourier-multiplier operator with symbol `xi` on `L^q(R)`. Then

\[
 \cos(tA)=\tfrac12(S_t+S_{-t}),
\]

where `S_t` is translation, so the cosine family is contractive. Proposition
6.2 of the source therefore supplies the Mehler--Fock operational calculus
with strip width `omega_0=1/2`.

On the other hand, Cowling--Doust--McIntosh--Yagi, Example 5.2 and Lemma 5.3,
construct the sectorial multiplier `T` with symbol `exp(xi)` on `L^q(R)` and
prove that it has no bounded `H^infinity` calculus on any positive sector.
Here `A=log T`. If the proposed extension for `A` were a bounded strip
functional calculus, then for every bounded holomorphic `m` on the sector
`S_{1/2}`, the function `b(z)=m(exp z)` would lie in
`H^infinity(Sigma_{1/2})`, and

\[
  m(T)=b(A)
\]

would be bounded with the required uniform norm estimate. This would give
`T` a bounded sectorial calculus, contradicting Lemma 5.3.

The contradiction is not merely existential: the supporting paper uses
Gaussian interpolation of arbitrary bounded sequences on the integers and de
Leeuw restriction to show that such a calculus would make every bounded
sequence a Fourier multiplier on `L^q(T)`, which forces `q=2`.

## Scope and interpretation

This is a counterexample to an automatic extension theorem for arbitrary
Banach spaces and arbitrary cosine generators satisfying the source growth
bound. It does not rule out extensions for Hilbert spaces or for individual
operators with an independently known bounded strip calculus.

The conclusion uses the standard operator-theoretic meaning of “functional
calculus map” already encoded by the source notation `Phi_A(psi)=psi(A)`: an
extension must agree with the holomorphic/resolvent calculus. If “bounded
algebra homomorphism” were instead meant as a purely abstract homomorphism
with no compatibility or convergence requirement, the source question would
not specify a functional calculus and the argument would not address such
pathological extensions.

## Provenance and novelty

This is not claimed as a new theorem. The decisive obstruction is Lemma 5.3
of the 1996 supporting paper, which the 2017 source itself cites in its earlier
discussion of bad strip multipliers. The contribution here is the direct
identification of that obstruction with Remark 4.2 through the logarithmic
translation generator and the source's Mehler--Fock example.

The bounded search used the exact source title and arXiv id, the quoted
extension sentence, and combinations of “finite propagation speed”,
“bounded H-infinity calculus”, and “cosine family”. No later paper explicitly
advertising a resolution of Remark 4.2 was found.

## Files

- `main.tex` and `solution_packet.pdf`: compact status note and proof.
- `source_paper.pdf`: arXiv:1509.00133.
- `supporting_paper_cowling_doust_mcintosh_yagi_1996.pdf`: the decisive
  supporting result.
- `figures/open_problem_page.png`: rendered source page containing Remark 4.2.


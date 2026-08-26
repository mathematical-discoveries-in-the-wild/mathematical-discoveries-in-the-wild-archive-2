# Counterexample to the mixed-norm tensor identity in arXiv:2405.09378

Status: `candidate_counterexample_likely_valid`

Source: Gianluca Giacchi, *Boundedness of metaplectic operators within
$L^p$ spaces, applications to pseudodifferential calculus, and time-frequency
representations*, arXiv:2405.09378; J. Fourier Anal. Appl. 30 (2024), 69.

The source's final remark proposes a mixed-norm research program based on the
claimed identity

\[
\|\mathfrak T_M(f\otimes g)\|_{L^{p,q}}=\|f\|_p\|g\|_q.
\]

The packet gives an exact Gaussian counterexample.  In dimension one, take
$P_{12}=0$, $Q_{12}=1$, $p=1$, $q=2$, and
$f=g=e^{-\pi x^2}$.  The quotient of the left-hand side by the asserted
right-hand side is $2^{-1/4}$, not $1$.  More generally, for $P_{12}=0$ the
quotient is

\[
\det(I+Q_{12}^TQ_{12})^{1/(2q)-1/(2p)}.
\]

The broad program of characterizing all mixed norms of metaplectic Wigner
distributions remains open; this packet disproves only its explicit advertised
input and supplies the exact correction for the lower-shear subfamily.

- Review packet: `solution_packet.pdf`
- Original source: `source_paper.pdf`
- Source evidence: `figures/open_problem_crop.png`
- Proof-development note:
  `runs/fa_banach_001/attempts/2405.09378_mixed_norm_tensor_identity_counterexample.md`
- Ledger:
  `runs/fa_banach_001/ledger/results/2405.09378_mixed_norm_tensor_identity.json`

Human review should verify the mixed-norm order and the one-line Gaussian
completion of squares.  Both conventions are transcribed explicitly in the
packet.


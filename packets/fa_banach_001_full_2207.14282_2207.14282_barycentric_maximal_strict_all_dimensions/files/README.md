# Barycentric maximal Rényi strictness in all finite dimensions

Source: M. Mosonyi, G. Bunth, and P. Vrana, *Geometric relative entropies
and barycentric Rényi divergences*, arXiv:2207.14282v5; Linear Algebra and
its Applications 699 (2024), 159--276.

Status: candidate full proof of the conjecture in Section 6.4, likely valid.

## Result

For every finite-dimensional complex Hilbert space, every pair of
noncommuting positive definite operators rho,sigma, and every alpha in
(0,1),

'D_alpha^{bary,max}(rho||sigma) < D_alpha^{max}(rho||sigma)'.

The source proves only the two-dimensional case.  Its directional
derivative formula extends dimension-freely because the scalar kernel
'Lambda_alpha-1' is conditionally negative definite.  A finite Schoenberg
embedding turns the derivative into a sum of double-commutator Dirichlet
forms.  Each is nonpositive, and simultaneous equality is equivalent to
commutation of rho and sigma.

## Files

- main.tex: theorem and complete proof.
- solution_packet.pdf: rendered review packet.
- code/verify_cnd_derivative.py: scalar-kernel, embedding, trace, and
  randomized derivative checks.
- verification.md: proof, literature, build, checksum, and visual-QA
  record.

The environment's external-usage limit prevented downloading a duplicate
source PDF; the exact conjecture and derivative formula were checked against
the repository's local parsed arXiv v5 source.


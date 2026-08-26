# Verification audit

## Source match

The source page image records Question 3.9 verbatim. The notation in the proof
packet uses \(A=L(\Gamma)\), with
\(\mathcal N\subseteq\mathcal M\subseteq A\), exactly as in the source.

## Proof obligations

1. **Expectation composition.** For nested tracial von Neumann subalgebras,
   \(E_{\mathcal N}E_{\mathcal M}=E_{\mathcal N}\). This follows from the
   uniqueness of the trace-preserving expectation (or orthogonal projections
   in \(L^2\)).
2. **Pimsner--Popa domination.** If
   \(\lambda=[\mathcal M:\mathcal N]^{-1}>0\), then
   \(E_{\mathcal N}(y)\geq\lambda y\) for \(y\in\mathcal M_+\). Applying this
   to \(y=E_{\mathcal M}(x)\) gives the key ambient inequality.
3. **Limit passage.** EM convergence is pointwise \(L^2\)-convergence of
   conditional expectations. The positive cone is closed in \(L^2\), so the
   operator inequality survives the limit.
4. **Finite-dimensionality.** The limit inequality implies every nonzero
   projection in \(\mathcal P\) has trace at least \(\lambda\). A diffuse or
   infinite atomic finite von Neumann algebra has arbitrarily small nonzero
   projections, hence \(\mathcal P\) is finite-dimensional.
5. **Finite-dimensional escape.** The packet proves directly, using the i.c.c.
   condition and finite Fourier approximation, that every finite-dimensional
   subalgebra of \(L(\Gamma)\) has conjugates converging to \(\mathbb C\).
6. **Orbit-closure contradiction.** A closed invariant orbit closure containing
   \(\mathcal P\) contains the closure of the orbit of \(\mathcal P\), hence
   contains \(\mathbb C\), contradicting confinement of \(\mathcal M\).

## Computational sanity check

`code/check_matrix_obstruction.py` verifies with exact rational arithmetic, for
dimensions 2 through 12, that scalar expectation on \(M_d\) dominates
\(d^{-1}\operatorname{id}\) on the extremal diagonal positive rays while
erasing a nonzero traceless diagonal direction. This is not evidence for the
theorem; it guards against the invalid stronger inference rejected in the
upgrade log.

## Novelty and limitations

Cheap run indexes and exact-phrase searches through 11 August 2026 found no
statement of the compact-orbit theorem. The June 2026 follow-up arXiv:2606.09673
emphasizes that EM subalgebra spaces and URAs may be noncompact, which is
consistent with the obstruction isolated here, but it does not state this
finite-index descent result. Novelty confidence is moderate: the proof is short
and may be unindexed folklore. Expert review should focus on the limit passage
and the finite-dimensional escape lemma.

# Verification Report

Candidate: arXiv:2209.10690, Theorem 1.4 and the principal-symbol reading of
Section 3 open problem 2.

## Verdict

Likely valid candidate counterexample. Confidence: 96/100.

| Step | Status | Notes |
| --- | --- | --- |
| Choose a bump eigenfunction target | valid | A proper open arc has complement with nonempty interior, so a nonzero real `C_c^infty` bump disjoint from the sensor exists and can be normalized. |
| Householder identities | valid | With `w=(h-f)/||h-f||` and real unit vectors, `U=I-2P_w` is unitary, self-adjoint, and swaps `h` and `f`. |
| Pseudodifferential class | valid | `P_w` has smooth rank-one kernel. Expanding `UAU-A` gives only compositions of an elliptic pseudodifferential operator with smoothing finite-rank operators; every term is smoothing. |
| Positivity and ellipticity | valid | Unitary conjugation preserves self-adjoint positivity, invertibility, and spectrum. A smoothing perturbation preserves order, ellipticity, and the principal symbol. |
| Eigenfunction equation | valid | `Ef=UAUf=UAh=Uh=f`. |
| Spectral-inequality contradiction | valid | The normalized `f` is in the spectral subspace at threshold one, while its `L^2(omega)` norm is zero. |

## Adversarial checks

- The source theorem quantifies over every nonempty open sensor; hence choosing
  a proper open arc is enough to refute it.
- The construction works on the complex Hilbert space by complex-linearly
  extending the real Householder reflection.
- `U=I+smoothing` preserves every Sobolev space, so the conjugated operator has
  the expected domain and remains an elliptic operator of order `nu`.
- No asymptotic estimate is used in the contradiction; it occurs at a single
  eigenvalue.
- The construction does not establish nonnegativity of the global
  representation-theoretic symbol assumed in arXiv:2209.12092. No claim about
  that stronger theorem is made.

## Human review recommendation

Send to a microlocal-analysis reviewer. The main review issue is interpretive:
whether the source intended a stronger complete-symbol hypothesis than it
stated. Under the principal-symbol language explicitly used in the proof, the
counterexample is complete.


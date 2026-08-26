# Verification audit

## Source locations

- Source question: arXiv:1703.04883v1, Chapter 5, Section 5.1, Question 1, printed page 163, arXiv PDF page 179.
- The theorem being tested: Theorem 1.38, parsed source `kap_01.tex` lines 844--884. It states, under metrizability of `(D(q),tau_q)`, that any two of (i) closedness, (ii) closed kernel plus continuity of the quotient embedding, and (iii) Hilbert completeness imply the third.
- Supporting theorem: Dierolf (1975), Theorem 4, printed page 76 (supporting PDF page 5). Every topological vector space is a quotient of a complete Hausdorff topological vector space.

## Counterexample checks

Let `H_0=c_00` with the inherited `ell_2` norm, choose Dierolf's quotient map `pi:Z->H_0`, put `L=ker pi`, and define `q(z)=||pi(z)||_2^2`.

1. `Z` is complete and Hausdorff by Dierolf's theorem.
2. `L` is closed because `Z/L` is homeomorphic to the Hausdorff space `H_0`.
3. `q` is a quadratic form, finite on all of `Z`, so `D(q)=Z`, and `ker q=L`.
4. `q^(1/2)=||pi(.)||_2` is continuous for the topology of `Z`. Hence adjoining the form seminorm does not refine the topology: `tau_q=tau_Z`.
5. Since `Z` is complete, `(D(q),tau_q)` is complete. Thus `q` is closed: assertion (i).
6. Under the quotient identification, both `(D(q)/L,q)` and `(Z/L,tau_Z/L)` are `H_0` with its `ell_2` norm topology. The canonical embedding is a topological isomorphism: assertion (ii).
7. `H_0` is incomplete. For example, the truncations of `(1/n)_{n>=1}` are Cauchy in `ell_2` but their limit has infinite support. Thus assertion (iii) fails.
8. The form topology cannot be metrizable: otherwise a quotient of the complete metrizable topological vector space `Z` by the closed subspace `L` would be complete, contradicting item 7.

This verifies a counterexample to `(i)+(ii) => (iii)`, which is enough to answer the source question negatively.

## Literature search

A bounded search through 2026-08-13 covered the run's four cheap indexes; exact wording of the source question; combinations of `Energy forms`, `Theorem 1.38`, `Dierolf`, `complete quotient`, and `quadratic form`; Dierolf's EuDML/GDZ record; and standard discussions of incomplete quotients of complete nonmetrizable spaces. No source explicitly recording this quadratic-form application was found. No originality or priority claim is made.

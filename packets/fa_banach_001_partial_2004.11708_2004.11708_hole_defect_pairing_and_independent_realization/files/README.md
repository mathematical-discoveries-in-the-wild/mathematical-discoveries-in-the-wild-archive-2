# arXiv:2004.11708 — hole-defect pairing and independent realization

Status: candidate partial result.

The source’s final remark asks which holes of an operator spectrum can be filled by restricting to a closed invariant subspace. This packet proves two complementary statements:

- For every bounded operator `T`, invariant subspace `M`, and `lambda` in the resolvent of `T`, there is a canonical Banach-space isomorphism
  `ker(T_quotient-lambda) ~= M/(T|M-lambda)M`.
  The common finite defect, or infinitude, is constant on each component of the resolvent. A filled hole is therefore exactly an open eigenvalue region of the quotient operator, paired pointwise with the residual defect of the restriction.
- For any finite family of pairwise disjoint circular holes, one fixed nonnormal operator on a separable Hilbert space has invariant subspaces realizing every prescribed fill/no-fill pattern. The same construction realizes any prescribed finite or infinite defect multiplicity independently in every hole.

The packet does not classify the realizable profiles for an arbitrary prescribed operator; that is the unresolved scope of the broad source question.

Files:

- `solution_packet.pdf`: theorem statements, complete proofs, scope, and literature context.
- `source_paper.pdf`: official arXiv PDF for 2004.11708.
- `supporting_barnes_2007.pdf`: supporting restriction/quotient spectral and Fredholm literature.
- `main.tex`: packet source.
- `attempts.md`: upgrade-attempt record.
- `verification.md`: proof and rendering checks.

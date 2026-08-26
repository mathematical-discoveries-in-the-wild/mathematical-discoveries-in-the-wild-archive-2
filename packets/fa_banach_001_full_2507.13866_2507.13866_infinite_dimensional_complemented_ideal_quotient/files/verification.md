# Verification record

## Mathematical audit

- A free ultrafilter on each infinite block exists in ZFC (via the ultrafilter
  lemma), and its complement is a proper maximal ideal containing `Fin`.
- For a maximal ideal `M=P(N)\\U`, the level-set definition gives
  `c_{0,M}=ker(phi_U)`, where `phi_U` is scalar ultralimit.
- For `I=intersection_n M_n` and `J=M_0`, this gives
  `c_{0,I}=intersection_n ker(phi_n)` and `c_{0,J}=ker(phi_0)`.
- An infinite selector containing one point from every block lies in every
  `M_n`, so `Fin` is strictly contained in `I`.
- The block `A_1` lies in `J` but not in `M_1`, so `I` is strictly contained
  in `J`.
- The map `Lx=(phi_n(x))_{n>=1}` is contractive on `c_{0,J}`.
- The block-constant map `R` is an isometric right inverse, belongs to
  `ker(phi_0)`, and yields the projection `P=Id-RL` with norm at most two.
- The lower quotient-norm bound follows because `L` annihilates `c_{0,I}`;
  the reverse bound uses the representative `RLx`. Hence the induced quotient
  map is an onto linear isometry to `ell_infinity`.

No computational check is needed; all identities are exact.

## Bounded novelty search

Checked through 2026-08-11:

- the run registry, solution, attempt, and proof-gap indexes;
- current arXiv:2507.13866v2, revised 2026-03-18;
- exact title, exact question phrase, authors, `I-null sequence`, relative
  complementation, ultrafilter-kernel, and infinite-dimensional quotient
  searches.

The current source still states the question. No later paper or independent
answer was found. Novelty confidence is moderate: bounded search does not
establish priority.

## Human review focus

Check whether Remark 6.7 tacitly intended a regularity restriction on the
ideals that is absent from the printed statement. Under the paper's stated
definition—proper ideals containing `Fin`—the construction is a complete
answer.

Verdict: `candidate_full_solution`, likely valid.

# Power-congruence norm identity: complete classification

Status: `candidate_full_solution_likely_valid_pending_human_review`

For a unital `C*`-algebra, `a > 0` invertible, and `p > 0`, the identity

`||(a^(p/2) x^p a^(p/2))^(1/p) a^(-1)|| = ||x||`

holds for every positive invertible `x` if and only if

`p = 2` or `a` is central.

The key reduction sets `c=a^p`, `q=2/p` and turns the norm identity into

`z <= t c  iff  z^q <= t^q c^q`.

For `q != 1`, Nagy's local-monotonicity characterization then forces
centrality. The `p=2` case holds for every `a` by a direct square-norm
calculation.

## Important provenance limitation

The problem environment occurs in the raw arXiv TeX for arXiv:2403.07341
*after* `\end{document}`. It is absent from the rendered 25-page paper. This
packet therefore solves an orphaned drafting remnant, not a problem visible in
the published PDF. See `source_problem_excerpt.txt` for the exact raw text.

## Files

- `main.tex`, `solution_packet.pdf`: theorem, proof, provenance, novelty scope,
  and review notes.
- `source_paper.pdf`: rendered arXiv target (which does not contain the raw
  problem).
- `supporting_nagy_2019.pdf`: primary source for the centrality theorem.
- `source_problem_excerpt.txt`, `figures/raw_source_problem.png`: exact raw
  source evidence for the unrendered problem.
- `verify_examples.py`: floating-point sanity checks, explicitly not a proof.
- `references.md`, `verification_report.md`: evidence and QA records.

## Human review

- [ ] A human expert has independently checked the proof, provenance decision,
  and novelty status.

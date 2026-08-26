# Full candidate: a tripartite Werner state PPT-entangled across every cut

Status: `full_solution_likely_valid` (awaiting specialist review).

For every local dimension `d>=3`, this packet constructs a
`U tensor U tensor U`-invariant state that is PPT and entangled across each of
the three bipartitions `A|BC`, `B|AC`, and `C|AB`, answering the open question
in Remark 5.5 of arXiv:2301.03849 affirmatively.

In the Eggeling--Werner coordinates the example is simply

```text
(r_plus,r_minus,r_1,r_2,r_3) = (3/4,1/32,0,0,3/16),  r_0=7/32.
```

It is cyclically invariant, so all three cuts are equivalent.  The exact
one-cut PPT inequalities have positive slack, while the exact one-cut
biseparability inequality fails by `45/1024`.

Files:

- `solution_packet.pdf`: review-ready proof packet.
- `main.tex`: LaTeX source.
- `proof_intuition.md`: proof mechanism in plain language.
- `VERIFICATION.md`: exact and direct-matrix audit record.
- `NOVELTY.md`: bounded literature-search record.
- `source_paper.pdf`: arXiv:2301.03849.
- `supporting_eggeling_werner_quant-ph_0010096.pdf`: the decisive coordinate
  characterization used in the proof.
- `figures/open_problem_crop.png`: source question on PDF page 25.
- `code/verify_candidate.py`: exact rational checks and direct matrices for
  dimensions 3, 4, and 5.

Primary verifier focus: confirm the Eggeling--Werner criterion transcription
and the cyclic-permutation transfer among the three cuts.

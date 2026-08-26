# Counterexample packet: finite paths defeat componentwise cardinality

Status: `candidate_counterexample_likely_valid`

Source: Florent P. Baudier, Bruno M. Braga, Ilijas Farah, Alessandro Vignati,
and Rufus Willett, *Coarse equivalence versus bijective coarse equivalence of
expander graphs*, arXiv:2307.11529, the paragraph after Theorem 1.2 on printed
pages 3--4.

## Result

The expander hypothesis in Theorem 1.2 cannot be replaced by the assumption
that the components are merely finite connected graphs.  A coarse disjoint
union of finite paths already gives a counterexample.

Let `P_n={0,...,4n-1}` with its path metric and put the components farther and
farther apart.  On each component, the map `f` compresses the first `2n`
vertices two-to-one into the first `n` vertices, then expands the remaining
part with discrete slope `3/2`.  It has a uniform 2-Lipschitz coarse inverse,
and both compositions are within distance 1 of the identity.  It also maps
every component into itself, so the exact component-cardinality condition in
Theorem 1.2(2) holds.

Nevertheless, no bijection is a bounded distance from `f`.  If the distance
bound were `C`, then on every sufficiently large component the first `2n`
domain vertices would have to inject into the `C`-neighborhood of the first
`n` target vertices, which has at most `n+floor(C)` vertices.  Taking
`n>floor(C)` is impossible.

## Files

- `main.tex`: self-contained statement, proof, verification, and novelty audit.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop_page3.png` and
  `figures/open_problem_crop_page4.png`: the complete two-page source evidence.
- `code/check_finite_path_counterexample.py`: exhaustive finite checks of the
  floor formulas and constants; not part of the proof.
- `code/make_open_problem_crops.py`: reproducible source-crop generator.
- `verification.md`: algebraic, computational, and visual QA record.

## Verification

Run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2307.11529_finite_paths_bijective_coarse_counterexample/code/check_finite_path_counterexample.py
```

The script checks all components `n=1,...,2000`: both component maps have
adjacent increments at most 2, both composition errors are at most 1, and the
image is 1-dense.  It also checks the final counting deficit for integer
closeness bounds through 500.

Human review should focus on the interpretation of the source's phrase
"the conclusion of Theorem 1.2 can fail" and on the last counting argument.

## Novelty status

On 2026-08-09, the run's four cheap indexes, exact source phrase, core keyword
searches, the latest arXiv source page, and the source paper's OpenAlex citation
record were checked.  OpenAlex listed two citing works as of its 2026-07-23
update; both concern operator algebras of expanders and neither addresses the
finite-connected-graph question.  No prior answer or this finite-path example
was found within those bounds.  Novelty is plausible, not certified.

Ledger:
`runs/fa_banach_001/ledger/results/2307.11529_finite_paths_bijective_coarse_counterexample.json`

# Verification report

Status: `candidate_counterexample_likely_valid`

## Exact algebraic audit

1. The cross-component metric is constant on component pairs, tends to
   infinity off the diagonal, and dominates each component diameter in the
   only nontrivial triangle configuration.
2. Both component maps are monotone with adjacent increments at most 2, so
   the global maps are 2-Lipschitz.
3. Direct residue-class calculations give both composition errors at most 1.
4. The source component/cardinality condition holds with every component
   retained and the identity component matching.
5. For any proposed closeness bound `C`, the first `2n` vertices of a large
   component would have to inject into at most `n+floor(C)` vertices.  Taking
   `n>floor(C)` is the decisive contradiction.

## Computational sanity check

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2307.11529_finite_paths_bijective_coarse_counterexample/code/check_finite_path_counterexample.py
```

Output:

```text
checked components n=1,...,2000
max adjacent f-step: 2
max adjacent g-step: 2
max |g(f(k))-k|: 1
max |f(g(j))-j|: 1
image of each component is 1-dense
counting obstruction checked for closeness bounds C=0,...,500
```

The computation is not used as proof.

## Source evidence

The question spans printed pages 3--4 of `source_paper.pdf`.  Both pages were
rendered at 180 dpi and cropped at full text width by
`code/make_open_problem_crops.py`.  The final crops were visually inspected
for complete, readable text.

## Novelty audit

Bounded on 2026-08-09 to the run indexes, exact phrase and core keyword
web/arXiv searches, the current arXiv source page, and the two works in the
OpenAlex citation record (record update 2026-07-23).  No answer to the exact
finite-connected-component question was found.  Novelty is plausible, not
certified.

## Human verifier focus

- Confirm the interpretation of the source's question.
- Check the metric and the two floor-formula compositions.
- Check that excluding all bounded-distance bijections is stronger than the
  required exclusion of bounded-distance bijective coarse equivalences.

## PDF QA

`solution_packet.pdf` was compiled twice with `latexmk` into `tmp/`; the final
log has no overfull/underfull box, undefined-reference, or warning hits.  The
five final pages were rendered at 150 dpi and inspected individually.  The
source crops are readable and complete across printed pages 3--4; equations,
proof endings, headings, citations, and page numbers are unclipped, with no
overlap or missing glyphs.

# Verification report

Status: `candidate_counterexample_likely_valid`

## Exact proof audit

1. For `q=2m`, the family consists of `m` copies of `z` and `m` copies of
   `1-z`; hence it has no common zero and every input has coefficient norm 1.
2. The product vanishes only at 0 and 1.  At either point the sum of the
   moduli of all inputs is `m`, so the source parameter is exactly `delta=m`.
3. Evaluating an arbitrary Bezout identity at 0 makes the `m` coefficients
   paired with `1-z` sum to 1.  Their constant terms therefore cannot all
   have modulus below `1/m`, and coefficient norm dominates the constant term.
4. Thus every solution satisfies `max_i ||R_i|| >= 1/m`, even if no degree
   restriction is imposed.
5. If the source constant depended only on maximal degree, degree 1 would
   supply one fixed `C`, forcing `max_i ||R_i|| <= C/m^2`.  Choosing an integer
   `m>C` gives the contradiction.
6. The lower bound is attained by `R_i=1/m` for all `i`, so the exact optimum
   on this family is `1/m=q/(2 delta^2)`.

## Computational sanity check

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2310.12734_many_polynomial_bezout_delta_counterexample/code/check_duplication_counterexample.py
```

Expected output:

```text
checked exact duplicated families for m=1,...,10000
delta=m, q=2m, and optimal max coefficient norm=1/m
identity verified exactly with every R_i=1/m
optimal norm equals q/(2*delta^2), so linear q-dependence is necessary
```

The computation uses exact rational arithmetic and is not part of the proof.

## Source evidence

The complete printed page 26 of `source_paper.pdf` was rendered at 170 dpi as
`figures/source_open_problem_page26.png`.  It includes the whole statement and
was visually inspected for readability and completeness.

## Literature audit

On 2026-08-09, exact-phrase and core-keyword web searches, the current arXiv
record, and author/citation search pages were checked after the direct proof
attempt.  No later answer or occurrence of this counterexample was found.
This supports plausible novelty only; it does not certify priority.

## Human verifier focus

- Confirm that the source constant is required to be independent of `q`.
- Check that the source's preceding coefficient normalization, if intended in
  Section 10.4, is satisfied exactly by the example.
- Check the evaluation-at-zero lower bound and the quantifier `m>C`.

## PDF QA

`solution_packet.pdf` was compiled twice by `latexmk`; the final log has no
overfull/underfull box, undefined-reference, or substantive warning hits.  All
four final pages were rendered at 150 dpi and visually inspected individually.
The source statement on page 2 is complete and readable; equations, proof
endings, references, and page numbers are unclipped, with no overlap or missing
glyphs.

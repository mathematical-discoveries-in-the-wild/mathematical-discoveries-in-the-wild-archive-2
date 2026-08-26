# Verification

## Mathematical checks

- Source target: Open Problem 3.1 after Theorem 3.5 in arXiv:2112.13900, source PDF page 20.
- Maximal monotonicity: `A` is represented as the subdifferential of a proper lower-semicontinuous convex function.
- Positive homogeneity: checked separately for positive scalars and for scalar zero under the source's inclusion-based definition.
- All ambient, operator, nesting, (H3), and (H4) hypotheses except boundedness are checked explicitly.
- Failure: `0 in Ax` only at `x=0`, which is contained in `G_2` and excluded from `G_1\G_2`.
- Scope: the example is not quasibounded, so the proposed quasibounded replacement remains open.

## Computational audit

Command:

`conda run --no-capture-output -n sandbox python code/verify_counterexample.py`

Result:

```text
PASS: monotonicity samples, (H3), (H4), and absence of annular zeros
```

## Literature and artifact checks

- Cheap run indexes contained no prior artifact for arXiv:2112.13900 or this exact question.
- Bounded web/arXiv searches through 2026-08-12 found the source publication and surrounding strong-quasibounded degree literature, but no later explicit answer or this counterexample.
- The packet compiled with `latexmk` without warnings, overfull boxes, or unresolved references. All three pages were rendered with Poppler at 120 dpi and visually inspected; no clipping, overlap, illegible text, or malformed figures were found.

## SHA-256 hashes

```text
883f67a4490d4233b798feb7582c4b1a8cc9cd0b41daba1bd1a147b60b28e996  source_paper.pdf
fef3173420c9ed3bc09168bf674adc1071a170cd21dbaa3887b757a568147e9c  figures/theorem_3_5_crop.png
ecb57373475fabbe4dc34fdfb99ad79feff73dde1236f5e06a5336abefaac2de  figures/open_problem_crop.png
5df5dab70bdeb5d32385b9bd448681ed685930b736cf198518a7ecf1b2d77267  code/verify_counterexample.py
1e7a07ba1c0f668f05b0041bdb717917234547187330807e3a6bc9131a34fa12  solution_packet.pdf
```

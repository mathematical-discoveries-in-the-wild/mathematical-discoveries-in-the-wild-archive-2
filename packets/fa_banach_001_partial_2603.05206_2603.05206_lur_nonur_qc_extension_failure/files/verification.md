# Verification record

Status: `candidate_partial_likely_valid`.

## Mathematical audit

- The source question was checked in the PDF on page 2.
- The planar input was compared line by line with the proof of Theorem 3.2
  in the source TeX.  The packet uses only the nested half-plane sublevels,
  the two low-value points, and boundedness of the levels after restriction
  to a compact square.
- The explicit point on each cutting line is proved to lie inside the
  corresponding `ell_p^2` ball by an exponential estimate.
- The LUR proof for the `ell_2` sum is included rather than assumed.
- Non-uniform rotundity is witnessed by an explicit fixed-separation chord
  sequence.
- The coordinate supremum is checked for a common Lipschitz constant and
  convex non-strict sublevels.
- The half-plane continuation lemma is stated and proved.
- The final contradiction uses values separated by a quantity tending to
  one at points whose distance tends to zero.

## Computational audit

Run:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2603.05206_lur_nonur_qc_extension_failure/code/verify_geometry.py
```

The script checks the first twenty blocks using log-space arithmetic.  It
verifies the line formula, strict interior inequality, outside-point margin,
and fixed chord separation.  These checks are supporting evidence only; the
packet contains analytic proofs of the inequalities.

## Build and rendering audit

`main.tex` was compiled with `latexmk` into `tmp/`, and the final PDF was
rendered page by page with Poppler.  All pages were visually inspected.  The
build log was checked for undefined references, missing files, and overfull
boxes.


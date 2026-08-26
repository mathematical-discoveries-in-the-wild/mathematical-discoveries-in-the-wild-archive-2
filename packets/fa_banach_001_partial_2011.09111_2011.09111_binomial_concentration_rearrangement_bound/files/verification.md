# Verification record

Status: `PASS (analytic proof with independent finite checks)`

Date: 2026-08-11

## Mathematical checks

- Re-derived the Doob representation
  `g-Eg = (1/2) sum c_i(epsilon_<i) epsilon_i` and checked that averaging over
  future bits preserves `|c_i| <= a_i`.
- Checked the backward induction: symmetric averaging of an even convex
  function is again even convex, and its value is nondecreasing in the
  amplitude.
- Checked the normalization
  `E |(1/2) sum 4B epsilon_i| = 4 beta_m B`.
- Derived the closed formula
  `beta_m = m 2^(-m) binom(m-1,floor((m-1)/2))` directly from the binomial
  sum and verified its parity plateaus and monotonicity.
- Rechecked the subset-to-container proof, including the identity
  `(1-alpha)|f_(Q\E)-f_Q| = alpha|f_E-f_Q|`.
- Verified that a false cube with `m` long directions occupies fraction
  `2^(m-n)` of its circumscribed cube.
- Checked the source theorem and lemma numbering in the final arXiv PDF:
  Lemma 3.5 (bisection factor 2), Lemma 3.6 (partition), Lemma 3.7
  (adjacent-cube means), and Lemma 3.9 (source comparison).

## Executable verifier

Command:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2011.09111_binomial_concentration_rearrangement_bound/code/verify_binomial_bound.py
```

Output:

```text
PASS: beta formula/monotonicity checked through m=200
PASS: exact Lipschitz-cube LP optima agree for m=1,2,3
PASS: hybrid constants for n=2,...,12 match the packet
PASS: binomial comparison improves the source term for m>=2
```

The small linear programs enumerate every absolute-value sign pattern and
optimize over all real 1-Lipschitz functions on the discrete cube. They are
independent evidence, not part of the analytic proof.

## PDF build and visual QA

Build command:

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
```

- `solution_packet.pdf`: 4 letter-size pages, 274869 bytes.
- No unresolved references, LaTeX warnings, overfull boxes, or underfull boxes
  in the final log.
- All four pages were rendered at 1.75x with PyMuPDF and visually inspected.
  Equations, theorem boxes, bibliography, and page breaks are readable and no
  content is clipped.
- The source crop was rendered at 2.5x from source PDF page 3. It shows the
  complete open-question sentence at full readable text width.

SHA-256:

```text
solution_packet.pdf  a16caffe90c1d9f1d11d2d05f6154e3c9506d0b398fe7c0d5a821a50dde4c4fa
source_paper.pdf     ccb0dcf48c3d7b96f59acc2bc4f02a6839f4eb2ac741b2a7341f8435fe4cb273
```

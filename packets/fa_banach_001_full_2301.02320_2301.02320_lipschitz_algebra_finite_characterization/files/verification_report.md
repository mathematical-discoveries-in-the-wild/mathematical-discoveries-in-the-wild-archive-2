# Verification report

## Mathematical audit

- Checked that every infinite compact metric space has an accumulation point
  and a subsequence whose radii decrease by a factor at least 3.
- Verified the reverse-triangle estimate
  `d(x_n,x_m) >= (2/3) d(x_n,o)` and the resulting Hölder bound
  `(3/2)^alpha` for both alternating functions.
- Checked that `d^alpha` is a metric for `0 < alpha <= 1`, so the real McShane
  extension theorem applies without increasing the seminorm.
- Checked the forced-zero-tail proof: joint non-degeneracy is used only to
  exclude a common zero at the accumulation point, and product equality then
  forces exact vanishing on the tail.
- Expanded the non-openness factorization at even and odd indices separately.
  The residual terms tend to zero after division by `rho_n`; the two limiting
  bounds force both base values to vanish when `epsilon < 1/2`.
- Verified the finite converse for both properties using the coordinate
  algebra and finite-dimensional norm equivalence.
- Audited the standard sum/max norm conventions, big Hölder orders, and the
  explicit exclusion of little-Lipschitz and nonmetrizable variants.

## Executable check

Command:

```text
python code/verify_alternating_obstruction.py
```

Result:

```text
PASS: alternating Hölder obstruction verified (alpha=0.1:max=1.04137974, alpha=0.25:max=1.10668192, alpha=0.5:max=1.22474487, alpha=0.75:max=1.35540301, alpha=1:max=1.50000000)
```

The script checks 80-level explicit shrinking-sequence models for five Hölder
orders, exact alternating base quotients, zero products on the model sequence,
and the scalar contraction coefficient used in the non-openness proof.  This
is a sanity check only; the proof is symbolic.

## Build and visual QA

Commands:

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
cp tmp/main.pdf solution_packet.pdf
pdftoppm -png -r 150 solution_packet.pdf tmp/rendered/page
```

- The final packet has 4 letter-size pages.
- The final LaTeX log has no unresolved references, warnings, underfull boxes,
  or overfull boxes.
- Every rendered page was inspected at original resolution on 2026-08-11.
- Page 1: title/status, exact source question, evidence image, definitions, and
  displayed norm are readable and unclipped.
- Page 2: proof intuition, classification theorem, alternating lemma, geometric
  estimate, McShane step, and start of the obstruction proof are readable and
  unclipped.
- Page 3: forced-zero proof, full non-openness calculation, and finite converse
  are readable and unclipped.
- Page 4: scope, verification, novelty, review recommendation, and both
  references are readable and unclipped.

## SHA-256

```text
919ba6b1302e28f3d585edff9bfc5d903947e43d5284afd44c02769e98a4a516  solution_packet.pdf
56bc2ef022bce3cc539b57c80c0d9c45cf7598aa6c0c08a42061dd4269834f8b  source_paper.pdf
92a45bd983c97ed3b1026c44fa8d92353be5c9d5f8a2e4f86c81a0663a4a3e8b  figures/open_problem_crop.png
```

## Verdict

`candidate_full_solution_likely_valid`.  The theorem completely answers the
standard compact-metric big-Lipschitz reading of Question 1 and strengthens it
to all big Hölder orders and a characterization of open multiplication.


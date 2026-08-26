# Verification report

Status: full counterexample and exact two-dimensional classification; proof
complete; ready for human mathematical review.

## Mathematical audit

- The semi-skew question was checked in the official arXiv v4 PDF, Remark
  10.2 on pages 20--21. Definition 8.1 is on page 18.
- For the two-dimensional semi-skew matrix, G maps each coordinate axis onto
  the other. The polar of a full linear subspace is its orthogonal
  complement, so both axes satisfy the fixed-point equation directly.
- Any solution is a polar and hence closed, convex, and contains zero.
  Bipolarity is therefore applicable to GC and gives C^polar=GC.
- The invertible linear transformation rule for polars gives
  C^polar=G^T C. Combining the two identities yields invariance under
  G^{-1}G^T=diag(-r,-1/r).
- Even hyperbolic iterates, contraction inside the convex set, and closedness
  recover both coordinate projections of every point. Integer iterates give
  both signs and arbitrarily large magnitude on every occurring axis.
- Consequently only the zero subspace, either coordinate axis, or the whole
  plane can occur. The zero and whole plane fail by direct polarity; the
  axes succeed.

## Independent exact checks

Command:

~~~text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/1708.09741_semiskew_axis_fixed_points/code/verify_axis_solutions.py
~~~

Observed result:

~~~text
all symbolic axis and hyperbolic-invariance checks passed
~~~

The script uses exact SymPy algebra to check G^{-1}G^T, both axis swaps,
polar bases for the image subspaces, failure of the zero and full subspaces,
and representative positive and negative same-sign unequal weights. These
checks are sanity checks, not dependencies of the proof.

## Build and visual audit

- latexmk completed with no final warnings, undefined references, overfull
  boxes, or underfull boxes.
- The final packet has 3 letter-size pages.
- Every final page was rendered at 150 dpi to an RGB PNG (1275 by 1650) and
  visually inspected. No clipping, overlap, unreadable glyph, broken formula,
  or malformed page transition was found.
- The source evidence is a real crop from source page 20 and contains the
  exact semi-skew prove-or-disprove question.
- Extracted final PDF text contains no unresolved question-mark marker.
- The ledger JSON parses and records model GPT5.6.

## SHA-256

~~~text
14a892a121f7242d763138904f84266e4e86f20a6e2c8893d9514114561ed25b  solution_packet.pdf
dc12d4734d6d977295c0ca4358c49f82269209c27bca0d419d8378f325784fbf  source_paper.pdf
0e03cd56d811b837b136ea846a21ea514a2d4f934b922765f39ffe42fea73749  figures/open_question_page20.png
d8e206c25f13bfb206e98a15c7996dc3104e6c84263d58865e85d17a59a3a508  main.tex
e862a66ed375036d690bae73974c63c5c24a2d69afe977294857db66b1a470c0  code/verify_axis_solutions.py
~~~

## Human-review focus

Check the two identities C^polar=GC and C^polar=G^T C, including the use of
closed convex bipolarity; verify the projection limits under the even powers
of diag(-r,-1/r); and check that integer powers plus convex contraction
generate each full occurring axis. The result deliberately does not claim a
classification for arbitrary non-positive-definite G.

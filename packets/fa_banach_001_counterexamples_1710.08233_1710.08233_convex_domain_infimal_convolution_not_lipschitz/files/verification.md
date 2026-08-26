# Verification report

Status: `counterexample_likely_valid`.

## Mathematical audit

- The source definition allows extended-real functions and defines the domain
  as the finite locus.  The example uses exactly that convention.
- Both finite restrictions share the same closed unit disk, a compact convex
  set with nonempty interior and smooth boundary.
- `f(a)=1+a_2` is 1-Lipschitz and nonnegative on the disk; `g=0` is
  0-Lipschitz and nonnegative.
- Adding the indicator of a closed convex disk shows both extended functions
  are proper, lower semicontinuous, and convex.
- Compactness of every feasible lens gives exactness of the convolution.
- The scalar minimax identity
  `min_s max(s^2,(t-s)^2)=t^2/4` follows from
  `t<=|s|+|t-s|<=2 max(|s|,|t-s|)` and equality at `s=t/2`.
- This yields the exact horizontal-diameter formula and the divergent
  difference quotient.  No numerical step is used in the proof.
- The open-disk variant uses two points strictly inside the convolution domain
  and independently rules out global Lipschitzness there.

## Reusable checker

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/1710.08233_convex_domain_infimal_convolution_not_lipschitz/code/verify_counterexample.py
```

The checker uses exact rational arithmetic for 151 values of `t` and 1001
values of `s`, hence 151,151 scalar inequality checks, including exact equality
at `s=t/2`.  It also evaluates the closed- and open-disk difference quotients
for seven decreasing positive values of `epsilon`.  These checks are only
regression tests; the displayed inequalities in the proof are the proof.

## Packet evidence and rendering

- The source PDF is the arXiv PDF for `1710.08233` (26 pages).
- `figures/open_problem_crop.png` is a readable full-width crop of source PDF
  page 10 containing the conjecture and its immediate context.
- `solution_packet.pdf` was built with `latexmk`, rendered page by page, and
  visually inspected.  It has 3 pages; the final LaTeX log has no warning,
  overfull/underfull-box, or undefined-reference messages.

Final checker summary:

```text
exact scalar minimax inequalities passed: 151151
closed quotient at epsilon=1e-7: 3162.2776206399
open-interior quotient at epsilon=1e-7: 1309.8582225563
all disk-lens counterexample checks passed
```

SHA-256 values:

```text
solution_packet.pdf       12a55914f90f774e9a146947024547b7b1e8cba1b38c9d14935233f12d696eab
source_paper.pdf          9f25c972428838c72ccaa221c4ac5bb30122958855b4518c50443694b3bccd95
main.tex                  98168ed82260f6f5121b42d1f07d4bfee8e9dd4dc7ce648ede2b7f4b464a0b47
open_problem_crop.png     bec01f89ac1ed7c80f2f61e6400403fdf485c69615a1b82587ae8cd6a4ca89cb
verify_counterexample.py  55f2f95df731a3813662cdcc11ba91d319415248f6089a8d1bb071d5e8ff41d7
```

## Reviewer focus

The only interpretive issue is whether the source intended global Lipschitz
continuity on the essential domain, as written, or merely local Lipschitz
continuity on the interior of the Minkowski sum.  The example fully refutes
the former and deliberately does not claim to refute the latter.

# Verification report

## Mathematical checks

- `A_a=aI+i sqrt(1-a^2)P` is exactly unitary because `P=P*` and `P^2=I`.
- Its coefficient majorant is `a+sqrt(1-a^2)r`; solving at norm one gives
  `r=sqrt((1-a)/(1+a))`, which tends to zero.
- The example has degree at most one, so it belongs to every source
  degree-at-most-`d` class with `d>=1`, as well as the all-matrix class.
- In exact degree `d`, the class radius is the reciprocal `d`th root of the
  optimal `ell_1` coefficient-to-operator-norm constant.
- For `H_theta=Re(e^{-i theta}A)`, self-adjointness, homogeneous degree, and
  `||H_theta||<=||A||` are all preserved.
- The normalized phase identity is
  `average_theta |Re(e^{-i theta}z)|=(2/pi)|z|`; summing before integrating
  yields `K_d^C<=(pi/2)K_d^sa`.
- Taking infima over positive degrees is legitimate and gives the uniform
  factor `2/pi` because `(2/pi)^(1/d)>=2/pi`.
- The scalar Boolean example `f_a(x)=a+i sqrt(1-a^2)x_1` has supremum norm
  one and the same vanishing radius formula.
- Diagonal Pauli embedding preserves every complex Boolean coefficient,
  degree class, supremum/operator norm, and radius.
- Proposition 2.2 of the source is stated for arbitrary `A`; its coefficient
  scaling by `3^(-|s|)` gives the factor-three comparison with complex
  Boolean radii without a self-adjointness assumption.

No conditional lemma remains.

## Numerical checker

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2210.14468_general_matrix_quantum_boolean_radius/code/verify_general_matrix_radius.py
```

The checker tests 12 unitary examples (`n=1,2,3` and four values of `a`) and
uses 262,144 equally spaced phases for the phase-average sanity check.  Its
output is:

```text
unitary_cases=12
max_unitarity_error=1.110e-16
max_radius_formula_error=8.882e-16
classical_cases=4
max_classical_norm_error=1.110e-16
max_classical_radius_error=8.882e-16
phase_samples=262144
max_phase_average_error=3.807e-11
```

## Novelty check

- Searched `registry_index.tsv`, `solutions/index.tsv`, `attempts/index.tsv`,
  and `proof_gaps/index.tsv` for arXiv:2210.14468, the title, quantum Boolean
  radius, and close Bohnenblust--Hille terms.  No duplicate result was found.
- Bounded web and local-source searches through 2026-08-09 used the exact
  quoted source sentence, `quantum Boolean radius`, `general matrix`,
  `complex-valued Boolean cube`, the authors, and the arXiv id.
- The search found the source preprint and published article, the underlying
  real Boolean-radius article, and adjacent later quantum Boolean-analysis
  papers.  It found no direct later statement of the phase-collapse example
  or homogeneous `pi/2` coefficient comparison.

Novelty confidence is moderate because the search was bounded, not
exhaustive.

## Source evidence

- Source: arXiv:2210.14468v4, 20 pages.
- Exact location: Definition 5.3 and Remark 5.4, source PDF page 16.
- `figures/open_problem_crop.png` was rendered from `source_paper.pdf` at
  180 dpi, retains the full page width, and contains the full definition and
  deferred-problem sentence.

## PDF QA

- Final packet: 6 US-Letter pages, 416,957 bytes, PDF 1.7.
- Final SHA-256:
  `d4893b898e816fe27fa2c6096227fbbd93d7f5dbe711f82b55596afa9953578e`.
- `tmp/main.pdf` and `solution_packet.pdf` are byte-identical.
- The final LaTeX log has no warnings, overfull/underfull boxes, undefined
  references, or errors.
- Ghostscript text extraction contains both new theorem headings, both
  zero-radius conclusions, the factor-three comparison, and the references.
- All 6 pages were individually inspected at 150 dpi after the final source
  edit.  No clipping, overlap, broken glyphs, unreadable formula, or page-flow
  defect was found.
- The 180-dpi source crop was separately inspected and shows the complete
  Definition 5.3 and Remark 5.4 at readable width.

## Human-review recommendation

Review the intended meaning of `general A`, the unitary two-term example, and
the phase-average coefficient comparison.  If those agree with the source
formulation, the packet is ready for promotion as a full class-by-class
answer.

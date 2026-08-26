# Verification report

Verification date: 2026-08-11  
Agent: `agent_lane_00`  
Model: `GPT5.6`

## Mathematical checks

The committed verifier was run with:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2602.19599_sharp_involutory_dilations/code/verify_involutory_dilation.py
```

Recorded output:

```text
exact symbolic assertions: 82
floating singular-value/involution assertions: 2240
endpoint and real-scalar assertions: 204
largest norm-formula error: 2.665e-15
all involutory-dilation checks passed
```

The exact checks construct rational matrices directly and verify both
`S_A^2=I` and `K S_A K = 2 Q_A`, where `K=sqrt(2) H`.  They also verify the
characteristic polynomial and proposed larger eigenvalue of the scalar
Rayleigh matrix.  The floating checks independently compare the exact norm
formula with computed singular values for real and complex matrices of sizes
1 through 8 at seven scales.

The proof itself was additionally audited for:

- attainment of the upper Rayleigh bound by a norm-attaining vector of `A`;
- the complex lower bound from `i in W(A)` and the source's ellipse formula;
- preservation of norm and compression under complexification in the real
  `n>=2` lower bound;
- the real `n=1` orthogonal exception;
- dimensions, involutory identity, reality, and exact norm of the `4n`
  direct-sum construction.

## Source excerpts

`source_paper.pdf` is the current arXiv PDF downloaded on 2026-08-11.
Questions 3.2 and 3.4 were rendered from PDF pages 11 and 12 and cropped into
`figures/question_3_2.png` and `figures/question_3_4.png`.  Both excerpts
were visually checked against the source pages.

## Compilation and visual QA

- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
  completed successfully after two passes.
- The final log has no warnings, undefined references, overfull boxes, or
  underfull boxes.
- The packet has 3 letter-sized pages.
- All 3 pages were rendered at 150 dpi and visually inspected.  Equations,
  source excerpts, theorem statements, and page boundaries are legible and
  unclipped.

## Hashes

```text
7028feb27c54e7c730d4083a3cb6ec712fdf1236f93ddd588eb2348ed6858edc  solution_packet.pdf
d75a087742520a84cd86c052e205dc59ff926666e735609d5c88a148fb8b0b28  source_paper.pdf
5ea057cc2c971e90f43b85b23dc194cfb356d753319cfcabbe3e3df90cbe1d67  code/verify_involutory_dilation.py
```

Conclusion: candidate full resolution, likely valid; priority is not
asserted.

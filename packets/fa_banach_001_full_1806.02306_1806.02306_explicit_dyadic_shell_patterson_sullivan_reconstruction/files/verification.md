# Verification record

Status: proof assembled; packet build and final visual QA complete.

## Mathematical checks

- The dyadic radii satisfy `d_D(0,r_n)=n log 2` exactly.
- Same-shell and cross-shell separation estimates give a uniform separation
  constant.
- Absolute convergence for `s>1` reduces to the geometric series
  `sum_n 2^{-n(s-1)}`.
- The exact distance identity was reduced to the uniform Busemann asymptotic
  `exp(R_n-d(z,r_n zeta))=P_z(zeta)+O_K(2^{-n})`.
- The roots-of-unity filter was checked with the Fourier convention used in
  the packet.
- Alias errors have bounded norms, exponentially small low-frequency parts,
  and exponentially small tails in the shell-scale ratio. This yields the
  almost-orthogonality estimate and normalized Abel `L2` convergence.
- Boundary-kernel `L2` convergence implies the uniform unit-ball statement
  for bounded harmonic functions via their `L-infinity` boundary values.

## Numerical verification

Command:

```text
conda run --no-capture-output -n sandbox python code/dyadic_probe.py
```

The exact `z=0` Gram computation gives normalized `L2` alias errors

```text
s=1.250000   0.05902520
s=1.125000   0.04335371
s=1.062500   0.03131811
s=1.031250   0.02239859
s=1.015625   0.01593959
```

and `error/sqrt(s-1)` approaches about `0.128`. A 2048-angle check at
`z=0.47+0.31i` confirms uniform convergence of the Busemann weight. These are
sanity checks and are not used as proof.

## Novelty check

- Cheap run indexes: no prior result/attempt/claim for either arXiv id or the
  deterministic critical-density route.
- Full local source corpus: the exact sharpened phrase occurs only in
  arXiv:2101.09622.
- Exact-phrase and arXiv-focused web searches on 2026-08-13 found the two
  Bufetov--Qiu sources and no later solution or matching dyadic construction.
- Novelty confidence: moderate; mathematical confidence: high pending human
  review.

## Artifact QA

- Source PDFs: valid official arXiv PDFs, 66 and 58 pages.
- Source crops: rendered from source PDF pages 13 and 17 and visually checked
  for full-width readability and complete statements.
- LaTeX compiled to a six-page PDF with no warnings, overfull/underfull boxes,
  undefined references, or multiply defined labels.
- All six final pages were rendered at 150 dpi and visually inspected. No
  clipping, overlap, unreadable evidence, or margin defects were found.
- `solution_packet.pdf` SHA-256:
  `3bcc3bc8942fe8f29164e09a5561993d0a6b7925b0f3bb906e15721ef53715ca`.
- `source_paper.pdf` SHA-256:
  `fef04e899bf7ac2c5325a48552626f9ee2d97c12d18f1f51d7bc146eac596002`.
- `sharpened_question_source_2101.09622.pdf` SHA-256:
  `eedc6e41e32aafe09ca7f5156928c836cf07ffc95ba2d5cabd54dee736c61889`.

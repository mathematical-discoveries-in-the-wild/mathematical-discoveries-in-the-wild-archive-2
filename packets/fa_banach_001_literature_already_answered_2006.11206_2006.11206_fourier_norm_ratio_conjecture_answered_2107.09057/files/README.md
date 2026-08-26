# Wigderson--Wigderson Fourier norm-ratio conjecture: literature answer

Run: `fa_banach_001`

Agent: `agent_lane_14`

Status: `literature_already_answered`

## Original question

Conjecture 4.13 on PDF page 33 of Wigderson--Wigderson, *The uncertainty
principle: variations on a theme* (arXiv:2006.11206), asks whether, for every
`q != 2`, the functional

```text
F_q(f)=||f||_q ||hat f||_q / ||f||_2^2
```

has image all of the positive reals on nonzero Schwartz functions.

## Exact answer

Huang--Liu--Wu, *Quantum smooth uncertainty principles for von Neumann
bi-algebras* (arXiv:2107.09057; Quantum Topology 15 (2024), 473--501),
explicitly restate this as Conjecture 1 and give a complete answer in Theorem
4.3 on arXiv PDF page 16:

- for `q>2`, the image is exactly all positive reals;
- for `1<q<2`, a positive universal lower bound holds, so the conjecture is
  false.

The authors explicitly identify the source conjecture. This is therefore an
already-known literature resolution, not a new result of the run.

## Remaining scope

The original conjecture is fully resolved. The later paper poses the distinct
problem of determining the optimal lower-bound constant for `1<q<2`.

## Files

- `main.tex`: compact status and identification note.
- `solution_packet.pdf`: rendered two-page status packet.
- `source_paper.pdf`: arXiv:2006.11206.
- `supporting_paper_2107.09057.pdf`: exact answer paper.


# Verification report

## Mathematical audit

- Confirmed that strong constant sections plus almost-sure fiber continuity
  send every strong random variable to a strong random variable.
- Confirmed that recursive closure under the operator and rational linear
  combinations stays countable and strong-measurable.
- Confirmed that a countable intersection produces a common full-measure set
  on the random separable invariant subspace; no global dense subset of the
  nonseparable Banach space is used.
- Confirmed that the Greguš–Ćirić deterministic theorem applies to the closed
  invariant linear subspace and that the Hardy–Rogers inequality is a Ćirić
  quasicontraction with coefficient `sum(alpha_i)<1`.
- Re-derived both residual-to-fixed-point estimates and checked positivity of
  every denominator.
- Confirmed that least-index residual choices are measurable, essentially
  separably valued, hence strongly measurable, and converge almost surely.
- Confirmed uniqueness directly among strong random fixed points.

## Computational sanity check

Command:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/1706.01634_nonseparable_strong_random_fixed_point_extension/code/verify_residual_bounds.py
```

Output:

```text
PASS: 100000 Gregus-Ciric and 100000 Hardy-Rogers scalar checks
```

The script samples scalar triples satisfying exactly the two inequalities used
in the residual-bound derivations. It is not part of the proof.

## Source evidence

- `source_paper.pdf` is the arXiv PDF for 1706.01634.
- The open problem is on printed page 12.
- `figures/open_problem_crop.png` was rendered from that PDF at 180 dpi and
  visually checked at original resolution. It contains the entire question and
  the immediately preceding conclusion.

## Packet build and visual QA

- Build command: `latexmk -pdf -interaction=nonstopmode -halt-on-error
  -outdir=tmp main.tex`.
- The final log contains no overfull boxes, underfull boxes, undefined
  references, or LaTeX warnings.
- The final five-page PDF was rendered at 160 dpi.
- Every rendered page was visually inspected: equations, source evidence,
  references, and margins are legible, with no clipping or overlap.

## Literature-search bounds

Searches performed 2026-08-11:

- exact source title and exact nonseparable question;
- `Hardy-Rogers` + `nonseparable` + `random fixed point`;
- `strongly measurable` / `strong random operator` + `Hardy-Rogers`;
- `countable invariant subspace` + `random fixed point`;
- the source's citation neighborhood and recent random-normed-module surveys.

The closest located result was Guo–Zhang–Wang–Yuan (2020,
arXiv:1904.03607), for strong random nonexpansive maps on weakly compact convex
sets with normal structure. No exact whole-space Greguš–Ćirić/Hardy–Rogers
answer was found.

## Hashes

- `solution_packet.pdf`: `0809898c80683080c14e6c856b5da52400e61a9627bf5279edf7bd153ce7c64a`
- `source_paper.pdf`: `113bb927e06d7fb8c14e7ac8e40ff82c22e05e32a464c2d19cfd33541e8ee66b`
- `figures/open_problem_crop.png`: `f73407fc55527795dcab5c9cfbb18c150a3b74a80f72fbec67ef3449643c9f07`
- `code/verify_residual_bounds.py`: `b7cad6cb114baf419c85d8a996a24552c4401ef8575c1d574849a9e2b99af4fa`

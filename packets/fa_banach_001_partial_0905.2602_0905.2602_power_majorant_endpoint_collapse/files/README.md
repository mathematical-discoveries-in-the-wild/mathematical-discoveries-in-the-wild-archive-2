# Power majorants: Hölder cases and collapse to the Zygmund endpoint

**Status:** candidate substantial structural partial result, likely valid.

**Source:** Pavel Shvartsman, *The Whitney extension problem for Zygmund
spaces and Lipschitz selections in hyperbolic jet-spaces*, arXiv:0905.2602,
Problem 1.2 on source PDF page 3.

For `omega(t)=t^s` with `0<s<m`, the packet proves the norm-equivalent
identification

`C^k Lambda^m_{t^s}(R^n) = B^{k+s}_{infinity,infinity}(R^n)`.

Consequently:

- every noninteger `s` gives a positive finiteness result by the classical
  Hölder-space theorem;
- every integer `s=r<m` is exactly the classical endpoint
  `C^{k+r-1} Lambda^2_t`;
- in particular, the paper's `Z_m=Lambda^m_{t^{m-1}}` is
  `C^{m-2} Lambda^2_t`.

Thus all power-law cases either are already positive or collapse to the
paper's `m=2` endpoint branch.  The general-majorant problem and that endpoint
remain open.

## Contents

- `solution_packet.pdf`: theorem, proof, limitations, and upgrade obstruction.
- `main.tex`: packet source.
- `source_paper.pdf`: the original arXiv paper.
- `figures/open_problem_crop.png`: source Problem 1.2.
- `verification.md`: proof and literature checks.
- `tmp/`: LaTeX and rendering intermediates.

## Novelty and scope

The proof combines standard Besov finite-difference/lifting equivalences with
the known Hölder finiteness theorem.  The endpoint-collapse application is a
useful structural reduction, but the underlying equivalences are classical;
novelty confidence is therefore low.  No later full resolution of Problem 1.2
was found in bounded searches through 2026-08-11.

## Human-review recommendation

Check the inhomogeneous bounded-function convention in the Besov lifting
identity and confirm that the chosen formulation of the `C^{q,alpha}`
finiteness theorem has constants independent of the closed trace set.  The
integer parameter shift should then be immediate.


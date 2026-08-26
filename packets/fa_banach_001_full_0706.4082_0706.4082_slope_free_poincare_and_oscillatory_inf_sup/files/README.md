# Boundary slope is irrelevant for the channel Poincare constant

Status: `candidate full solution to source Remark B.2; likely valid; human review requested`

Source: Jon Wilkening, *Inf-sup estimates for the Stokes problem in a periodic channel*, arXiv:0706.4082, Remark B.2 on source p. 18. The packet also gives substantial progress on the distinct question in Remark 4.3.

## Result

For the periodic subgraph

```text
Omega_h={(x,y): x in R/(LZ), 0<y<h(x)},
0<h0<=h(x)<=h1,
```

the mean-zero Poincare constant has an explicit upper bound depending only on `L`, `h0`, and `h1`. It is completely independent of `M=||h'||_infinity`. This fully answers Remark B.2: the source's linear `M` factor is an artifact of flattening the upper boundary.

The proof anchors the function to its mean on the fixed rectangle `T x (0,h0)`, uses the rectangular Poincare inequality and an explicit trace estimate there, then controls the part above `h0` along vertical fibers.

## Further inf-sup result

For the smooth oscillatory graphs

```text
h_N(x)=h0+D(1-cos(Nx)),  N even,
```

an alternating pressure on the `N` upper teeth proves

```text
beta(Omega_N)^(-1) >= pi sqrt(DN/(14 zeta(3))) = c sqrt(M_N).
```

Thus the Stokes inf-sup inverse really can deteriorate with boundary oscillation, even though the mean-zero Poincare constant does not. This narrows the exponent gap in source Remark 4.3 to `[1/2,2]`; it does not settle whether the source's quadratic upper exponent is optimal.

## Files

- `main.tex`, `solution_packet.pdf`: source question, proof intuition, full slope-free theorem, oscillatory inf-sup lower bound, limitations, and novelty audit.
- `source_paper.pdf`: official arXiv PDF.
- `figures/open_problem_crop.png`: source p. 18, including Remark B.2.
- `verification.md`: mathematical and artifact audit.

Human-review focus: check the averaged horizontal trace identity, the passage from the base-rectangle mean to the whole-domain zero mean, and the Fourier normalization in the alternating-tooth inf-sup example.


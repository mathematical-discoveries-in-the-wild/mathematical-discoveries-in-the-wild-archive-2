# Verification

Status: passed.

## Mathematical checks

- `Q_j = I-u_j u_j^T` is a rank-`(t-1)` orthogonal projection.
- ETF tightness gives `sum Q_j = n(t-1)/t I_t`.
- An orthonormal generator of `u_j^perp` has maximal minors equal to the
  coordinates of its row wedge.
- That row wedge is `+/- *u_j`; Hodge star is an isometry.
- Independent signs preserve both ETF tightness and absolute inner products.
- `binom(t,t-1)=t` and `t-1>=2` for `t>=3`, exactly matching Definition 6.2.
- For regular simplices, `n=t+1>t=m` and the angle is `1/t`, so the family is
  nonorthogonal and nondegenerate.

## Automated check

Executed with the run's `sandbox` conda environment. The script checked the
simplex ETF, projection idempotence, fusion tightness, maximal-minor Plucker
vectors, Plucker equiangularity, and Plucker tightness for every
`3 <= t <= 12`. It passed with worst residual `4.716e-15`.

## Build and visual QA

- `pdflatex` completed twice with no warnings, overfull boxes, underfull boxes,
  undefined references, or errors in the final log.
- Final packet: 4 US-letter pages, 440012 bytes.
- All four pages were rendered at 120 dpi and visually inspected. Text,
  equations, theorem breaks, source crop, and margins are clean; nothing is
  clipped or overlapped.

## Final artifact hashes

```text
source_paper.pdf          fce8d21d26ca978237bcb111ec5296eb73dd7f07dc5bbbba761e6608b0fbaebf
open_question_crop.png    3f30834e73e84b1d0f6b382c871f40965c8f7fdf19a72018023e691ed3e76fd8
solution_packet.pdf       bc5e1e8d02e11ceb4f52da2330202af07b77f9756949c5539581f7efa5d60504
```

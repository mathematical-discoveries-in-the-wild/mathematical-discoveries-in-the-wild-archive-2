# Superball ranges for the three-dimensional covering-pessimum conjecture

Status: `partial_result`

Source: Yoav Kallus, *When is the ball a local pessimum for covering?*,
arXiv:1301.5895.

## Result

Write `B_p^3={x: sum |x_i|^p <= 1}`. The source's global conjecture is
verified for every superball with

- `1 <= p < 2`, using the body-centered cubic lattice; and
- `p >= 9`, using the cubic lattice.

For the BCC lattice, the exact `l_p` covering radius is
`(1/2)(1+2^{-p})^{1/p}`. Its corresponding density increases on `[1,2]`
and reaches the ball density `5 sqrt(5) pi/24` only at `p=2`. For `p>=9`,
the cubic covering density is at most `3^{1/3}`, already strictly below the
ball value.

The full conjecture and the superball interval `2<p<9` remain open in this
packet. Eight focused upgrade attempts are recorded in the attempt note.

## Files

- `main.tex`, `solution_packet.pdf`: statement, proof, and limitations.
- `verification.md`: proof audit.
- `code/verify_superball_ranges.py`: directed-interval scalar verification
  and independent cell/density checks.
- `source_paper.pdf` and `figures/source_conjecture.jpg`: source context.


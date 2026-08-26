# Distinct-symbol bilinear commutators

Status: candidate full split resolution in the standard real-symbol setting;
human review requested.

This packet answers the two final problems of arXiv:1707.01639:

- Problem A is affirmative for the intended homogeneous nonvanishing
  convolution kernels and real symbols. Boundedness of the summed commutator
  first forces `b1+b2` into BMO; subtracting its slot-2 commutator leaves a
  slot-difference operator whose median test forces `b1` into BMO, hence also
  `b2`.
- Problem B is false as printed. With `b1=0` and `b2(x)=x_1`, the inner
  commutator and hence the iterate vanish, although `b2` is not BMO.

Files:

- `main.tex`, `solution_packet.pdf`: theorem and proof.
- `source_target_1707.01639.pdf`: target paper.
- `VERIFICATION.md`: scope and artifact checks.

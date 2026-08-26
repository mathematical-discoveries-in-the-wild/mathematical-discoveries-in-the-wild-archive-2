# arXiv:1907.08812 — sharp multiplier exponent for a flat zero patch

Status: `candidate_substantial_partial_likely_valid`

The source asks whether its non-multiplier range can be sharpened to
`q <= (d-sigma)/(d-sigma-s)`. This packet proves the conjectured exponent in
the structured codimension-one case.

If `1/2 < s < 1`, `w in H^s(T^d)`, and the Sobolev trace of `w` vanishes on a
nonempty open patch of a rational affine hyperplane, then

```text
1/w is not in M_2^q for every 2 <= q <= 1/(1-s).
```

This equals the source's proposed exponent when `sigma=d-1`. The proof tests
the multiplier on shrinking normal slabs. Their Fourier coefficient norm has
the exact lower scaling `tau^(1-1/q)`, while localized fractional Poincare
gives an upper scaling `tau^s E(tau)` with `E(tau)->0`, including the endpoint.

Files:

- `main.tex`: self-contained partial-result packet.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: official arXiv source.
- `figures/open_problem_crop.png`: full-width source page 30.
- `VERIFICATION.md`: proof, scope, novelty, and rendering audit.

# Explicit dyadic-shell Patterson--Sullivan reconstruction

Status: **claimed full new solution; likely valid; pending human review**.

This packet answers the sharpened deterministic question (1.41) in
Bufetov--Qiu, arXiv:2101.09622, and supplies an explicit deterministic
configuration for the open-problem program in arXiv:1806.02306.

For hyperbolic radius `n log 2`, place the `2^n` equally spaced points

```text
r_n exp(2 pi i j / 2^n),   r_n=(2^n-1)/(2^n+1).
```

The resulting configuration is uniformly separated, has critical
hyperbolic counting growth, and reconstructs every bounded harmonic function
by the Patterson--Sullivan ratio. The convergence is uniform over the unit
ball of bounded harmonic functions and over base points in compact subsets of
the disk.

The proof turns the problem into convergence of boundary Poisson kernels.
Continuous angular averages are an approximate identity. The discrete-shell
quadrature errors live near dyadic Fourier frequencies and are almost
orthogonal across shells, so their normalized Abel average vanishes in
`L^2(T)`.

Files:

- `solution_packet.pdf`: review-ready proof packet.
- `source_paper.pdf`: arXiv:1806.02306v2.
- `sharpened_question_source_2101.09622.pdf`: arXiv:2101.09622v1.
- `figures/`: real source-page crops of the two deterministic questions.
- `code/dyadic_probe.py`: exact zero-basepoint Gram check and Busemann sanity
  check; verification only, not part of the proof.
- `verification.md`: build, rendering, and numerical verification record.

Primary review focus: the block-Fourier estimates in the alias lemma and the
interpretation of the source's informal phrase “critical upper density.”


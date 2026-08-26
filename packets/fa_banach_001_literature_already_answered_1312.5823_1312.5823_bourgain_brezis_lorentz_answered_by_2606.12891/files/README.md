# Bourgain--Brezis critical Lorentz estimate: answered by arXiv:2606.12891

Status: `literature_already_answered_affirmative`.

The introduction of Giga--Xiang, arXiv:1312.5823v1, points to Bourgain and
Brezis Open Problem 1 and says that the divergence-free, curl-in-`L1` case was
unknown. The precise cited question asks whether the periodic div--curl
solution on `T^3` obeys the endpoint `L^{3/2,1}` estimate.

Goodman--Hernandez--Spector, arXiv:2606.12891v1, explicitly identify that same
question and answer it affirmatively. Their Corollary 1.4 proves

```text
||Z||_{L^{3/2,1}(T^3)} <= C ||F||_{L^1(T^3)}
```

for every divergence-free mean-zero `F`, where
`Z = curl(-Delta_{T^3})^{-1}F`. The later authors know and state that this is
an answer to Bourgain--Brezis Open Question 1.

The supporting theorem settles the exact problem cited by arXiv:1312.5823. It
does not automatically settle every bounded-domain variant with arbitrary
boundary conditions, but the source paper does not state such a variant as a
separate numbered open problem.

The folder contains the original and supporting PDFs and a compact
human-facing `solution_packet.pdf`.

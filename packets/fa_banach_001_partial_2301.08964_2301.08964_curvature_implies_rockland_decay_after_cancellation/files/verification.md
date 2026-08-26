# Verification report

Status: analytic and source audit completed on 2026-08-21; compilation and
visual rendering checks are recorded below after the final rebuild.

## Independent source audit

- `source_paper.pdf`, arXiv:2301.08964: Remark 1.9 asks for the relation
  between the curvature assumption and the Rockland Fourier condition.
- `supporting_paper_2305.04700.pdf`, Definition 1.1: the alternating recursion
  starts with `sigma^(0)=sigma`, convolves by the reflection at odd steps and
  by `sigma` at even steps, and requires two-sided translation Holder control.
- With the packet's Fourier convention, the exact odd-step identity is
  `hat(sigma^(2m-1))=(A* A)^m`. The recovered draft had the factors reversed;
  `main.tex` was reconstructed with the corrected parity bookkeeping.

## Analytic audit

- The dyadic root lemma was rederived from the spectral projections of
  `T T*`; its summability threshold is exactly `t < s/(2q)`.
- CA for the reflected measure follows by inserting the original odd
  convolution density between the two compact measures.
- The low-frequency estimate was checked directly from the heat-semigroup
  representation: small times use total variation, large times use zero mass
  and heat-kernel translation decay.
- Under the packet convention
  `hat(mu * eta) = hat(eta) hat(mu)`, the negative-power representation uses
  `mu * p_t`. The three reversed occurrences in the recovered draft were
  corrected during the August 21 packet audit.
- The smooth mass correction preserves every positive-order estimate.
- The result is deliberately partial: it does not infer the converse from a
  one-sided operator estimate and does not claim weak `(1,1)`.

## Computation

No computation is used in the proof.

## Rendering audit

`main.tex` was force-rebuilt on 2026-08-21 to a four-page PDF. The log has no
LaTeX errors, undefined references, or overfull boxes. All four pages were
rendered at 120 dpi and visually inspected; the source crop and formulas are
readable, and there is no clipping, overlap, or malformed output.

## Protocol structure QA (2026-08-21)

An explicit `Proof intuition` section now precedes the three lemmas and the
one-way theorem. The packet was force-rebuilt to four pages; the final log has
no LaTeX errors, undefined references, or overfull boxes. Poppler renders of
all pages at 130 dpi were visually inspected. The source crop, noncommutative
order, new intuition, root lemma, theorem, and scope statement are readable
and unclipped. SHA-256 of the final `solution_packet.pdf`:
`efd7d995253f73de60fd8ee4d54e3c064b0d7e7ff8887e1b50629e746a9dcd29`.

# Verification

Status: `candidate_partial_resolution_likely_valid; input_orientation_and_two_sided_version_solved; literal_one_sided_T_endpoint_open`

## Mathematical checks

- The source formula was checked directly in Remark 1.4: it varies the first/output variable, while bad-input cancellation uses a second/input-variable difference.
- On each sufficiently remote shell, the tail region contains the shell uniformly after a fixed dimension-dependent dilation.
- Size bounds both terms of the kernel difference by the reciprocal shell volume scale.
- `L2^2 <= L-infinity * L1`, followed by multiplication by shell volume, gives a shell contribution `O(sqrt(omega(c 2^j)))`; every positive power is summable.
- The finite number of shells introduced by changing the dilation is controlled by size and only changes dimensional constants.
- The Cadilhac-Conde-Alonso-Parcet proof was audited at the diagonal and off-diagonal bad terms.  For `K in M' cap M_tilde`, commutation with `pi f pi` makes the key trace inequality valid; the trace restriction and assumed `L2(N) -> L2(N_tilde)` bound handle every other change of range algebra.
- A trace-preserving conditional expectation `E_M:M_tilde -> M` identifies the Hilbert adjoint restricted to `N` with the central-valued kernel `E_M(k(v,u)^*)`; operator-norm contractivity transfers the displayed output-tail estimate.
- Weak `(1,1)` for the adjoint and `L2` boundedness do not imply the missing weak endpoint for `T` by interpolation/duality, so the one-sided scope boundary is necessary.
- Eight materially distinct upgrade attempts, including a counterexample search, are recorded in `attempts/1702.06536_tail_decay_endpoint_upgrade.md`.

## Source and literature checks

- The official source PDF is included and its exact question appears in the packet.
- arXiv:2009.03827 proves a scalar-kernel semicommutative endpoint under summable annular `L2` regularity.
- arXiv:2105.05036 proves the annular `L2`-Hörmander endpoint by a decomposition avoiding pseudolocalization, and explicitly states arbitrary input-algebra and central-kernel extensions.
- arXiv:2512.06843 gives a later scalar/semicommutative `L2`-mean refinement; it does not remove the orientation issue or state the source's general commutant-valued range theorem.
- Exact-title, question-text, tail-decay, adjoint-orientation, and later-citation searches found no full resolution of the literal one-sided implication for `T`.

## Reproducibility and presentation

- `main.tex` is compiled twice with `pdflatex`.
- The final PDF is text-extracted and checked for theorem labels, references, and the source question.
- Every page is rasterized and visually inspected for clipping, overflow, missing glyphs, and unreadable source evidence.

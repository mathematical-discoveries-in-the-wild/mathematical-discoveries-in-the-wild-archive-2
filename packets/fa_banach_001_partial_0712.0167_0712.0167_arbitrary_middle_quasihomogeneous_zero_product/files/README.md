# A two-sided quasihomogeneous zero-product theorem

Status: `candidate_substantial_partial_likely_valid_human_review_needed`

Source: Trieu Le, *The zero-product problem for Toeplitz operators with
radial symbols*, arXiv:0712.0167, Problem 1.1 (PDF page 2).

## Result

Let `Omega` be any bounded Reinhardt domain. Suppose every symbol in a
finite Toeplitz product except one is bounded and separately
quasihomogeneous (it has a single character under the coordinate torus).
The exceptional symbol may lie at any position and may belong merely to
`L^2(Omega)`. If the product vanishes on analytic polynomials, then one of
the symbols is zero almost everywhere.

This simultaneously:

- extends Le's radial theorem from degree-zero, fully radial symbols to
  arbitrary torus characters with arbitrary radial amplitudes;
- moves from the unit ball to every bounded Reinhardt domain; and
- extends the known endpoint-arbitrary theorem to an arbitrary symbol in
  the interior of the product, with quasihomogeneous factors on both sides.

## Proof mechanism

A separately quasihomogeneous Toeplitz operator is a one-character weighted
shift on monomials. The weights are values of bounded multivariable Mellin
transforms. Taking a matrix coefficient of the zero product leaves the
product of a left Mellin factor, a right Mellin factor, and one fixed angular
Fourier-Mellin transform of the arbitrary symbol. On each common translate
of the positive integer lattice this product vanishes. The positive lattice
is a uniqueness set for bounded holomorphic functions on a product of right
half-planes, so the arbitrary symbol's Fourier-Mellin transform vanishes.
Varying the angular frequency recovers the full symbol.

## Limitations

The original problem remains open for two arbitrary bounded Bergman symbols.
Finite sums of torus characters on both sides of an arbitrary middle symbol
also create colliding angular terms not separated by this proof. Eight
focused upgrades and the exact obstruction are recorded in the packet and
attempt note.

## Files

- `solution_packet.pdf`: theorem, proof, literature boundary, and upgrade audit.
- `source_paper.pdf`: arXiv:0712.0167.
- `supporting_2009.01951.pdf`: March 2026 revision of the closest known theorem.
- `supporting_dong_zhou_2011.pdf`: two-factor separately-quasihomogeneous result.
- `figures/`: source-question and literature-boundary evidence crops.
- Attempt log: `runs/fa_banach_001/attempts/0712.0167_arbitrary_middle_quasihomogeneous_zero_product.md`.

Human review should focus on the weighted-shift index bookkeeping and the
passage from fixed-frequency Mellin uniqueness to vanishing of every torus
Fourier coefficient. No computational dependency is used.

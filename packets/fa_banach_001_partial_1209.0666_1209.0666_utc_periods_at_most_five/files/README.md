# arXiv:1209.0666 — the Universal Tiling Conjecture for `p <= 5`

Status: candidate substantial partial result, likely valid, human review requested.

The source's Conjecture 1.4, `UTC(p)`, asks whether every finite family of integer spectra `A_i/p` of one fixed `p`-point set `Γ` has a common tiling complement in `Z`.

This packet proves `UTC(p)` for every `p = 1, 2, 3, 4, 5`:

- for `p=2,3`, rigidity of vanishing sums of two or three unit vectors forces all normalized differences onto one complete residue scale;
- for `p=4`, the classification of `4 x 4` complex Hadamard matrices gives two cosets of a common order-two subgroup, and a fixed 2-adic scale on the quotient yields one common parity complement;
- for `p=5`, the order-five Hadamard classification forces every spectrum to be a coset of the unique subgroup of order five.

Consequently, a bounded measurable spectral set of measure one whose spectrum has integer period at most five tiles the line, with a tiling set contained in `(1/p)Z`.

The full conjecture for arbitrary `p` remains open. The order-six strategy is obstructed by the non-rigid and incompletely classified family of `6 x 6` complex Hadamard matrices.

Files:

- `solution_packet.pdf`: complete statement, proof, scope, and verification note.
- `source_paper.pdf`: official arXiv PDF for 1209.0666.
- `supporting_paper_1909.13145.pdf`: order-four Hadamard classification source.
- `supporting_paper_1201.0631.pdf`: order-five Hadamard classification source.
- `figures/open_problem_crop.png`: source Conjecture 1.4.
- `code/verify_low_period.py`: bounded finite-cyclic audit.
- `verification.md`: proof and artifact checks.

Ledger: `runs/fa_banach_001/ledger/results/1209.0666_utc_periods_at_most_five.json`.

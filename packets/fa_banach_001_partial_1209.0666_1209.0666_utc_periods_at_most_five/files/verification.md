# Verification

## Mathematical checks

- Source target: arXiv:1209.0666, Conjecture 1.4 (`UTC(p)`), source PDF page 2. The induced spectral-to-tile statement uses source Proposition 2.8 and the proof of Theorem 1.5.
- `p=2,3`: checked that orthogonality forces normalized within-spectrum differences to be nonzero modulo `p`; the gcd block complement then gives unique sums modulo `pg`.
- `p=4`: checked the dephased Hadamard normal form, existence of the finite cyclic character quotient, uniqueness of its order-two element, the congruence `e_i delta = q/2 (mod q)`, the resulting common 2-adic valuation, and the quotient parity complement.
- `p=5`: checked that dephased equivalence to `F_5` makes each row spectrum a coset of the unique order-five subgroup in the cyclic character quotient.
- Boundary: the proof does not claim `p >= 6`; the order-six Hadamard structure is non-rigid and incompletely classified.

## Computational audit

Command:

`conda run --no-capture-output -n sandbox python code/verify_low_period.py`

Result:

```text
p=2: column_sets=1101, nonempty_families=373, spectra=373
p=3: column_sets=6079, nonempty_families=553, spectra=553
p=4: column_sets=10061, nonempty_families=505, spectra=655
p=5: column_sets=8436, nonempty_families=96, spectra=96
PASS: 25677 primitive column sets, 1527 nonempty spectrum families, 1677 spectra
```

The script uses floating-point root-of-unity tests with tolerance `1e-8` and is a bounded audit, not a proof.

## Literature and artifact checks

- Bounded local-index and web/arXiv searches through 2026-08-12 found no explicit theorem proving `UTC(p)` for all `p <= 5`.
- arXiv:1909.13145 gives nearby size-two and size-three Fourier-Hadamard compatibility results and explicitly leaves the primitive-set/tiling-set relationship for future work.
- arXiv:1201.0631, Proposition 2.1, states the order-five Hadamard classification used in the proof.
- The packet compiled with `latexmk` without warnings, overfull boxes, or unresolved references. All four pages were rendered with Poppler at 120 dpi and visually inspected; no clipping, overlap, illegible text, or malformed figures were found.

## SHA-256 hashes

```text
9d63e21f4a897fe23aeda289f42e630516cd51be17a64a6ce26e422538e991f5  source_paper.pdf
d99524b024c6d138f22972a12ab5143206795edb1044e239e6e45f1363139496  supporting_paper_1909.13145.pdf
f76ba442a750e49c3e9ee625a87875d403a1d3ef424b47829c33b41d733ea8af  supporting_paper_1201.0631.pdf
4d6fa6faebaa058f65dda744b977ca31414341f3f61cd7bb84b42b1bf3700c1f  solution_packet.pdf
```

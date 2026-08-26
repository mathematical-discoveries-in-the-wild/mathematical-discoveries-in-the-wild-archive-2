# Spherical Hermite sums in dimensions at least three

**Status:** `candidate_partial_likely_valid`

This packet answers the open question in Remark 3.3 of Philippe Jaming and
Michael Speckbacher, *Convergence of Hermite expansions in modulation spaces*
(arXiv:2601.04893), completely in every dimension `d>=3`:

> The spherical Hermite partial sums converge in `M^p(R^d)` for every function
> if and only if `p=2`.

The source asks for all dimensions.  In `d=2`, the packet proves failure at
`p=1,infinity` and convergence at `p=2`, but leaves
`1<p<infinity`, `p!=2` open.  The packet is therefore filed as a substantial
partial result, although it gives a full classification for each `d>=3`.

The proof combines:

1. an elementary high-monomial limit from Bargmann-Fock norms to torus norms;
2. a Pell-equation construction that places the desired lattice ellipsoid
   exactly inside integer-radius Hermite spheres; and
3. de Leeuw transference plus Fefferman's ball multiplier theorem.

Files:

- `main.tex` and `solution_packet.pdf`: proof packet;
- `source_paper.pdf`: local source paper;
- `figures/open_problem_crop.png`: full-width crop of Remark 3.3 on source
  page 10;
- `code/verify_pell_and_gamma.py`: exact arithmetic checks and numerical Gamma
  moment convergence checks;
- `VERIFICATION.md`: verification record and reviewer focus.

Human-review priority: verify the Fock-to-torus limit lemma and the exact use of
de Leeuw's dilation theorem.  The Pell identity itself is exact and is checked
by the included script.

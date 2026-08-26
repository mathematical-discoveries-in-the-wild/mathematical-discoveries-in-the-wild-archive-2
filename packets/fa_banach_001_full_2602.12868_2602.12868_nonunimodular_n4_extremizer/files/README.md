# A sparse non-unimodular equality case in complex dimension four

**Status:** `candidate_full_solution_likely_valid` — full affirmative answer to
the explicit equality-case question on page 26 of arXiv:2602.12868.  This does
not prove Conjecture 1.2 for all four-row systems.

## Result

For the four rows

\[
  a_{\varepsilon,\delta}=(1,\varepsilon,\delta,0),
  \qquad (\varepsilon,\delta)\in\{\pm1\}^2,
\]

one has

\[
 \min_{x\in\mathbb T^4}
 \max_{\varepsilon,\delta\in\{\pm1\}}
 |\langle x,a_{\varepsilon,\delta}\rangle|=2=\sqrt4.
\]

Every row is non-unimodular because its fourth coordinate is zero.  Hence this
constructs exactly the kind of non-unimodular equality case whose existence the
source paper says is unknown for \(n=4\).

## Proof in one paragraph

After removing a common phase, the four correlations are
\(1+\varepsilon z+\delta w\), with \(|z|=|w|=1\).  If all four had modulus
strictly below 2, their squared-modulus expansions would imply
\(|\Re z|,|\Re w|,|\Re(z\bar w)|<1/2\).  These three quantities are the pairwise
real inner products of the three planar unit vectors \(1,z,w\).  But among
three unoriented lines in the plane, two have angle at most \(\pi/3\), so one
pairwise inner product has absolute value at least \(1/2\), a contradiction.
For \(\omega=e^{2\pi i/3}\), the phase vector \((1,\omega,\omega^2,1)\) gives
correlation moduli \(0,2,2,2\), proving equality.

## Contents

- `solution_packet.pdf`: rendered review packet.
- `main.tex`: packet source.
- `source_paper.pdf`: arXiv:2602.12868.
- `figures/open_problem_crop.png`: page-26 source passage.
- `code/verify_extremizer.py`: independent million-sample and global numerical
  checks; the proof itself is exact and computation-free.
- `tmp/`: LaTeX and rendering intermediates.

## Novelty check

On 2026-08-13, bounded searches for arXiv:2602.12868, its exact title, the
quoted phrase “non-unimodular vectors achieving equality,” and combinations of
“complex Spencer,” “dimension 4,” and “non-unimodular equality” found the source
preprint and mirrors only, with no follow-up solution or erratum.  Novelty is
therefore plausible but not certified; expert literature review is requested.

## Human review focus

Check the strict-inequality contradiction in the lower bound, the source inner
product convention, and whether this sparse Walsh configuration has appeared
under another formulation.  The main conjecture and the linked Banach–Mazur
distance conjectures remain open in dimension four.

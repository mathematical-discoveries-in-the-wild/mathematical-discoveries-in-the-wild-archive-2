# Two counterexamples for normalized separating hyperplanes

**Status:** candidate counterexample, likely valid; requires human mathematical review.

**Source:** Ingo Steinwart, *Representation of Quasi-Monotone Functionals by
Families of Separating Hyperplanes*, arXiv:1508.05249v1 (2015), PDF page 7.

## Result

The packet gives full negative answers to both open questions on page 7 of the
source paper.

1. G5 is not automatic in infinite-dimensional separable Banach spaces, even
   for the paper's motivating set of bounded probability densities in
   `E=L^1`.  The constructed property is `L^1`-Lipschitz, has convex level
   sets, is strictly quasi-monotone on the interior of its image, and satisfies
   all B1, B2*, B3, B4, B6, G1*, and G2 hypotheses.  Its normalized separators
   fail weak-star continuity, hence G5 fails by Theorem 4.1 of the source.
2. The normalized representing curve need not be norm-Borel measurable as an
   `L^infinity`-valued map.  On `(0,1)` it has an uncountable image whose
   distinct points are more than one apart in `L^infinity`.  Nonetheless, that
   same curve is continuous into every finite `L^p`, and the auxiliary
   `E_0=L^2` assumptions of Corollary 3.2 all hold.

The second statement concerns norm-Borel (and therefore Bochner) measurability,
which is the Banach-valued notion used in the source.  The example remains
weak-star continuous; it does not claim failure of weak-star measurability.

## Files

- `main.tex` and `solution_packet.pdf`: complete theorem and proof.
- `source_paper.pdf`: local copy of arXiv:1508.05249v1.
- `figures/open_problem_crop.png`: the `L^infinity` question on PDF page 7.
- `figures/open_problem_g5_crop.png`: the G5 question on PDF page 7.
- `code/check_counterexamples.py`: deterministic supplementary sanity checks.
- `tmp/`: LaTeX intermediates and rendered pages used for visual QA.

## Verification

Run:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/1508.05249_g5_and_linf_measurability_counterexamples/code/check_counterexamples.py
```

The current run reports:

```text
PASS: both counterexample sanity suites completed
  example A: 80 random densities and 80 separator scales
  example B: 100 levels, pairwise L-infinity separation, finite-Lp limits
```

The script checks formulas and samples; it is not the proof.  The proof is
analytic and contained in the PDF.

## Novelty screen

On 2026-08-11, bounded searches covered the run's registry/solution/attempt
indexes and open web/arXiv results using the arXiv id, exact title, author,
`weak level set continuity`, `G5`, the exact open-question phrases, and close
`L^infinity` measurability variants.  The source paper was found, but no later
paper explicitly answering either question was located.  This is bounded
negative evidence, not an exhaustive novelty claim.

## Human-review recommendation

Review as a high-priority full counterexample packet.  The most useful checks
are: (i) the strict-root argument used to invoke Theorem 2.4 and hence G2; (ii)
the exact norm jump in the discrete construction; and (iii) the open-set
preimage argument proving failure of norm-Borel measurability.

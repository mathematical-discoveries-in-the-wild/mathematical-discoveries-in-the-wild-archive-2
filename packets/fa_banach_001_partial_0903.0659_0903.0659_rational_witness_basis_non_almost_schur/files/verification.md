# Verification record

Status: `candidate_partial_likely_valid`  
Agent: `agent_lane_03`  
Model: `GPT5.6`  
Verified: 2026-08-11

## Mathematical checks

1. **Exact source scope.** Source PDF page 15 defines a basis for an
   increasing/decreasing filter class and asks for explicit bases both for
   almost-Schur filters and for the negation class. The packet claims only the
   negation half as solved.
2. **Canonical filters are proper and free.** Finite intersections of tail
   weak-neighborhood traces contain a trace with the union of tests, minimum
   tolerance, and maximum tail index. Admissibility makes every such trace
   nonempty; arbitrary tail indices make the generated filter free.
3. **Each canonical filter is bad.** Its defining rational unit sequence is
   weakly filter-null and has constant norm one.
4. **Normalization is safe.** A non-almost-Schur witness has norms bounded
   below by some `delta>0`; multiplication by `1/||x_n||<=1/delta` preserves
   scalar filter convergence to zero.
5. **Rational approximation is safe.** Finitely supported rational unit
   vectors are norm dense in the `ell_1` unit sphere. An error bounded by
   `1/n` is norm-null along every free filter, so the rationalized witness is
   still weakly filter-null.
6. **Domination direction.** Every finite weak-neighborhood trace of the
   rationalized witness belongs to the original filter, as does its
   intersection with a cofinite tail. Hence `W_u subset F`, which is exactly
   the direction required for a basis of the increasing negation class.
7. **CH obstruction.** `W_u` has base size at most continuum and no countable
   base (a countably based filter is Schur by source Corollary 4.5 and Theorem
   3.5). Under CH its character is `omega_1`. A recursion adding an enumerated
   base plus a genuinely new set at each countable stage gives a strict chain
   of countably based Schur filters with union `W_u`.

## Upgrade attempts

Six focused routes were recorded in
`runs/fa_banach_001/attempts/0903.0659_rational_witness_filter_basis.md`:
literature audit, rational witness compression, maximal extensions, Schur
dominators, block/diagonal subclasses, and simultaneous blockers. The last
four all leave a genuine positive-class extension problem. The packet is
therefore correctly classified as partial.

## Literature and duplicate audit

- Cheap run indexes searched by exact arXiv id, title terms, and core terms.
- Exact problem phrase, exact title/citations, `almost Schur filter`, and
  `basis of filters` searched through 2026-08-11.
- Later filter-convergence papers citing the source were found, but no answer
  to the basis request or matching rational witness construction.

This was a bounded novelty audit, not an exhaustive priority claim.

## Build and visual QA

Build command from the packet directory:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
cp tmp/main.pdf solution_packet.pdf
```

- Final PDF: 4 pages.
- Final LaTeX log: no warnings, undefined references, overfull boxes, or
  underfull boxes.
- All four pages were rendered at 150 dpi and inspected.
- Page 1: title, exact scope, definitions, intuition, and trace-filter
  definition are fully visible.
- Page 2: basis theorem and proof, exact criterion, and beginning of the CH
  obstruction are fully visible.
- Page 3: CH recursion, limitations, literature boundary, and source metadata
  are fully visible.
- Page 4: exact source crop is sharp, complete, and unclipped.

## Hashes

```text
solution_packet.pdf       c7981978da2c2c3bdd7b9284a7b57260c99aa8cc6b89b9c7beadfc675bcaa54b
source_paper.pdf          6750d725c76f4ad8ddb64355785c1eec2df343b9149efb51e8fe79ca7a9b3274
open_problem_crop.png     228a2e80d3c497cb65387baa30ec8d759de6834d888f76390b3d2ece55df602b
```

## Human-review recommendation

Check the direction `W_u subset F` after rationalization and the character
argument in the optional CH proposition. The main basis theorem itself is
elementary and independent of CH; only the chain obstruction uses CH.


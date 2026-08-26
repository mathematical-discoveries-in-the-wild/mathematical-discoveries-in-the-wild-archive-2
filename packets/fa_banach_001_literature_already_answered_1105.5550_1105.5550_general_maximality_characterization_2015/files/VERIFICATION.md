# Verification record

## Exact-source checks

- Original source PDF page 10 contains Proposition 18 and Remark 7, ending
  with the open request about maximality of `F+G`.
- Supporting PDF page 7 contains all four equivalent clauses of Theorem 2.
- The supporting paper cites the Bot--Grad paper as reference [2].

## Applicability check

- Proposition 18 makes `Q=F+G` monotone and gives convex lower-semicontinuous
  functions `Q(x,.)+delta_C`.
- The standard `+infinity/-infinity` extension has precisely those slices
  and preserves the associated operator, so Theorem 2 applies.
- The elementary step-function example in the packet satisfies every
  assumption of Proposition 18 but has a nonmaximal associated graph.

## Classification caution

The supporting paper supplies a general necessary-and-sufficient theorem
and cites the source, but does not explicitly say “this answers Remark 7.”
The literature-resolution classification is therefore an inference.

## Packet build and visual QA

- `latexmk` completed in two passes with no final warnings, underfull boxes,
  overfull boxes, or unresolved references.
- The three-page packet was rendered at 140 dpi and every page was inspected.
  Page 1 is unclipped; page 2 reproduces the complete source remark; page 3
  reproduces all four clauses of the later Theorem 2 at readable scale.
- Ghostscript text extraction confirms that the exact open-question wording,
  the necessary-and-sufficient status, and Theorem 2 are embedded.

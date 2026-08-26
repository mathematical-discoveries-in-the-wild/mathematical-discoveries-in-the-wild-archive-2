# Verification record

Status: `candidate_partial_likely_valid`.

## Mathematical audit

- The source theorem and open question were checked on source PDF page 13.
- For arbitrary `D:A -> J*`, restriction to `K=I intersect J` was checked to
  be an `I`-bimodule morphism.
- After subtracting an inner derivation, only `D0(i)|K=0` is used; the proof
  never assumes the stronger and generally unjustified statement
  `D0|K=0` as a `J*`-valued map.
- The pairing computation proving `D0(I^2)=0` was checked with both dual
  module actions.  Ideal amenability implies weak amenability, and the packet
  includes a proof that weak amenability forces `closure(I^2)=I`.
- The annihilator calculation was checked in both directions:
  `D0(ia)=0` annihilates `JI`, and `D0(ai)=0` annihilates `IJ`.
- `E=closure(IJ+JI)` was checked to be a closed `A`-submodule of `J`, and
  `J/E` was checked to be an `A/I`-bimodule.
- Under `E=I intersect J` and closedness of `I+J`, the natural map
  `J/(I intersect J) -> (I+J)/I` is a bounded Banach-module isomorphism by
  the open mapping theorem.
- The recovery of the BAI theorem includes explicit proofs of both
  `I intersect J=closure(IJ+JI)` and closedness of `I+J`.
- The trace-class example was checked directly: spatial implementation of
  derivations gives weak amenability; rank-one sandwiching gives topological
  simplicity; diagonal trace-norm estimates rule out a bounded approximate
  identity.

## Upgrade audit

Eight focused attempts were recorded in
`runs/fa_banach_001/attempts/0610137_bai_free_three_space_upgrade_attempts.md`.
Two produced the promoted theorems.  The remaining routes isolate the
uncontrolled residual module and explain why neither a full proof nor a
counterexample is claimed.

## Build and rendering audit

`main.tex` is compiled with `latexmk` into `tmp/`.  The final PDF is rendered
page by page with Poppler, visually inspected, and its log checked for
undefined references, missing files, and overfull boxes.

No computational verifier is needed: all arguments are analytic and are
included in the packet.

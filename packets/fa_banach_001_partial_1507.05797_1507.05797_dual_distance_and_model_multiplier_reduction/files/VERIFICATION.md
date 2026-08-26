# Verification record

## Source statement

- The locally cached single-file arXiv source was decompressed and compiled to
  `source_paper.pdf`.
- Compiled page 14 contains the question asking when a general Toeplitz kernel
  contains only bounded functions.
- Compiled page 19 contains Definition 5.7 and asks whether every nontrivial
  `H_p^+` Toeplitz kernel has a minimal function.
- Both complete pages were rendered at 180 dpi and visually inspected before
  inclusion in the packet.

## Proof checks

- The duality proof keeps the closure of `range T_{conj(g)}`; it does not assume
  the Toeplitz operator has closed range.
- The equality between evaluation norm and quotient distance follows from the
  standard isometric identification `K* = H^q/K^perp`.
- Set inclusion into `H_infinity` is upgraded to bounded inclusion only after a
  closed-graph argument.
- In the model-multiplier theorem, `K_min(w) subset K` is used before dividing
  by `w`; the exact representation then puts every quotient in `H^p`.
- The Smirnov intersection step proves that quotient constant, and a separate
  maximal-function argument proves `K=K_min((theta/z)w)`.
- No claim is made that every general-`p` Toeplitz kernel admits the exact
  multiplier representation.

## Literature scope

- arXiv:2001.10890 was checked for the extremal/intersection representation and
  scalar maximal-function result.
- arXiv:2004.09985 was checked as later general-`p` factorisation context.
- arXiv:2512.20406 was checked as the latest located model-multiplier and
  square-rigidity treatment; its exact Hayashi representation is in `H^2`.
- Exact-phrase and terminology searches did not locate a later full
  general-`p` answer.  The packet makes a cautious candidate-partial claim only.

## Build and render checks

- `source_paper.pdf` compiles to 26 pages and has SHA-256
  `070e54218c20832da82b0afd488596c6b34b970e61e0599241f7d7a51e794f21`.
- `solution_packet.pdf` compiles to 5 A4 pages and has SHA-256
  `d8703eceafa1dc661adca093eb6940d7fe8ae23e3fb3a1e38aee25a3be65f011`.
- The packet log contains no warnings, overfull boxes, undefined references, or
  multiply defined labels.
- Every packet page was rendered at 150 dpi and visually checked for clipping,
  legibility, equation layout, and source-screenshot readability.

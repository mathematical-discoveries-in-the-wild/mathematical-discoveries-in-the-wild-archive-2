# Verification record

## Exact source locations

- Compiled source PDF page 13 states that the critical model equation is open
  in odd dimensions at least three.
- The same page asks for endpoint divergence after multiplication by every
  nonnegative function tending to infinity.

## Answer-paper crosswalk

- Official arXiv:1510.06662 PDF page 3 explicitly identifies Martinazzi's
  question and states Theorem 1.1.
- The full-norm constraint in Hyder is stronger than Martinazzi's local
  derivative constraint, so divergence on Hyder's smaller class implies the
  requested divergence.
- Official PDF page 5 states Theorem 1.3 for every dimension, every finite
  measure open domain, `0<lambda<lambda_1`, and `b>0`.
- Hyder's model nonlinearity is exactly `lambda*u*exp(b*u^2)`; the packet does
  not generalize this to all critical nonlinearities.

## Residual-scope checks

- Parini--Ruf, arXiv:1607.07681, establishes a fractional
  Sobolev--Slobodeckij inequality and a blow-up threshold, but does not identify
  the exact optimal exponent.
- Sk, arXiv:2002.11747, Theorem 1.1 characterizes the unbounded-domain
  Slobodeckij/truncated-exponential inequality by a fractional Poincare
  inequality and states that the exact optimal Slobodeckij exponent remains
  unknown.  These are recorded as partial/variant answers only.

## Provenance caveat

The local answer-paper asset is a typeset theorem transcription because the
official answer PDF was available for line- and page-level inspection through
the arXiv browser but could not be persisted in the local workspace during
this run.  It links the official PDF and clearly identifies itself as a review
transcription rather than a facsimile.

## Build and render checks

- `source_paper.pdf` is the 18-page locally compiled source paper; SHA-256
  `c7ae75d1c9301803d3fdf0c41287949023511720399bf975a325d9d870a139ce`.
- `answer_paper_excerpt.pdf` is the one-page, explicitly labelled review
  transcription described above; SHA-256
  `acd9b2a1cb490a17612618ad18d2e5b0bb41d6ffdf9d9e3f77804830f3a7ed23`.
- `solution_packet.pdf` is four A4 pages; SHA-256
  `49b1949b8e115c35f92704c0d0a0118c4199c04e36ad4b587a519868fc71e9ac`.
- The packet and excerpt logs contain no warnings, overfull boxes, undefined
  references, or multiply defined labels.
- Every page of both output PDFs was rendered at 150 dpi and visually
  inspected.  Text, equations, table, source-page image, links, and margins are
  clear, correctly placed, and unclipped.

# Verification notes

## Mathematical checks

1. `xi*` is the uniformity of uniform convergence on bounded subsets of the
   locally convex space `V`, exactly as in Glasner--Megrelishvili,
   arXiv:1007.5303, Section 3.3.
2. Namioka--Phelps means every equicontinuous subset of `V*` is
   `(weak-star, xi*)`-fragmented.  Thus the hypothesis applies to the minimal
   compact subsystem `K`.
3. The distality-lifting step uses only fragmentation and minimality, and is
   the same mechanism as in the source's Theorem 3.1.
4. The invariant-measure packing argument is run separately for every strong
   dual seminorm `p_B`; no countability or metrizability of `xi*` is assumed.
5. Completeness is proved directly: a `xi*`-Cauchy net in an equicontinuous
   weak-star compact set has a weak-star convergent subnet, and taking scalar
   limits in the Cauchy inequalities gives uniform convergence on every
   bounded `B`.
6. The final radius set is weak-star closed because `p_B` is the supremum of
   weak-star continuous scalar functions, hence weak-star lower
   semicontinuous.
7. The proof does not assume affinity of the original maps.  Affinity is used
   only for the induced action on probability measures, exactly as in the
   standard invariant-measure argument.

## Novelty check

The run indexes were searched for the arXiv id, title, `Namioka--Phelps`,
`nonlinear Ryll--Nardzewski`, and fixed-point variants.  Bounded web/arXiv
searches used the exact source question and close phrases.  Later arXiv papers
in the local corpus citing the source (including arXiv:2006.15393 and
arXiv:2203.02368) were searched for an answer.  No later exact resolution was
found.  This is not exhaustive bibliographic certification.

## Artifact checks

- The source question was visually located on page 10 of `source_paper.pdf`.
- The final PDF was compiled with `pdflatex` and checked with `pdfinfo`.
- All final pages were rendered to PNG and visually inspected for clipping,
  overlap, broken glyphs, and margin defects.
- Temporary LaTeX files and rendered pages are confined to `tmp/`.


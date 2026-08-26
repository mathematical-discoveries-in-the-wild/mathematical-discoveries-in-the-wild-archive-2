# Verification

## Claim-to-source audit

- ArXiv draft: `source_arxiv_0004146.tex`, around lines 595--666, contains
  Proposition 2.6 and the sentence asking whether condition `(ii)` can be
  removed.
- Published source: `source_published_2003.pdf`, Proposition 3.4 and Remarks
  3.5 on pages 339--340, retains the same condition and question.
- Supporting identity: `supporting_proc17465_crossref.json` identifies DOI
  `10.1090/proc/17465`, Huang and Sukochev, Proceedings of the AMS 154 (2026),
  no. 2, pages 793--806, published online 2025-12-01.
- Supporting theorem: `supporting_proc17465_abstract.json` gives the complete
  abstract. It states the unrestricted Rademacher/disjoint-subsequence
  alternative for bounded sequences in order-continuous noncommutative
  quasi-Banach bimodules and explicitly says this answers Randrianantoanina's
  question.
- Assumption map: `E(M,tau)` is an order-continuous Banach `M`-bimodule and is
  continuously included in `L_1(M,tau)+M`, so the later theorem applies with
  `p=1`. Normalized sequences are bounded.
- Conclusion map: the Rademacher inequality is identical. Disjoint operator
  elements transfer to disjoint functions in `E` by the standard
  singular-value disjointification already used in the source's Proposition
  2.4.

## Mechanical checks

Run from this directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Then inspect the log for undefined references, citations, and overfull boxes;
render every page of `solution_packet.pdf` and inspect the page images.

Completed on 2026-08-11: `latexmk` converged with no undefined references,
citation warnings, or overfull boxes. Both pages were rendered at 150 dpi and
visually inspected. The final PDF SHA-256 is
`c76397ca0aab512b6bf88f25c4b7f154843c710e7abc21dd4aaaf9ec07635afb`.

## Search record

The cheap run indexes contained no prior entry for arXiv:math/0004146.
Primary-source and exact-title searches on 2026-08-11 located the 2003
publisher PDF and DOI `10.1090/proc/17465`. Crossref supplied the exact AMS
resource metadata; the DOI-indexed abstract supplied the complete theorem
statement and explicit answer attribution.

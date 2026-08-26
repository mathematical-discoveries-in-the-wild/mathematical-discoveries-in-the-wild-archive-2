# Bounded novelty search

Search date: 2026-08-13.

## Local indexes

Searched `registry_index.tsv`, `solutions/index.tsv`, `attempts/index.tsv`, and
`proof_gaps/index.tsv` for `2303.03527`, the paper title, weighted Hardy
criticality, `alpha+p`, and exterior domains.  No prior run result on this
paper or exact problem was found.

## External search

Focused web/arXiv searches included:

- `"Is" "critical" "exterior domain" "alpha+p" weighted p-Laplacian`
- `"-Delta_{alpha,p}" exterior domain critical alpha+p N`
- `"weighted p-Laplacian" "exterior ball" criticality distance boundary`
- the exact source title together with `citations critical exterior`
- `"Let Omega be" "C^{1,gamma}-exterior" "critical"`
- `site:arxiv.org "alpha+p" "exterior domain" "critical" "Hardy"`

The searches found the arXiv and 2025 Journal of Spectral Theory versions of
the source paper, talks based on it, a 2025 paper citing it for other Hardy
estimates, and the older paper *Optimal Lp Hardy-type inequalities*, which
constructs optimal weights for unweighted p-Laplacians on exterior-type
domains.  They did not locate an explicit statement that the distance-weighted
operator in the source problem is subcritical on every exterior ball for all
real \(\alpha\), nor a later paper explicitly answering Open Problem (3).

This was a bounded search, not an exhaustive MathSciNet/zbMATH review.

## Source-archive caveat

The current source document ends at line 1977 of the parsed arXiv source.  A
second, discarded draft begins afterward.  In that discarded material, a
footnote records that for \(N=p=2\), \(\alpha=0\), and the exterior unit disk,
the two solutions \(1\) and \(\log r\) imply subcriticality, and it says that a
similar argument should work generally.  That footnote is not in the final
paper PDF, which still asks Open Problem (3), but it is evidence of prior
author awareness of the planar seed.  Consequently:

- mathematical confidence in the packet theorem is high;
- novelty confidence is only moderate;
- the genuinely stronger content is the explicit proof for every
  \(N\ge2\), \(1<p<\infty\), and \(\alpha\in\mathbb R\), including both
  endpoint families.


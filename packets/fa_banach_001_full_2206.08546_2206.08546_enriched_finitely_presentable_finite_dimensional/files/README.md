# Enriched finitely presentable Banach spaces are finite-dimensional

This packet gives a candidate full answer to Remark 3.3 of arXiv:2206.08546.

## Result

For real or complex Banach spaces, enriched finite presentability in the
category of Banach spaces and contractions is equivalent to finite
dimensionality.

More strongly, a single fixed diagram detects the converse:

    c0 --S--> c0 --S--> ...

where S is the left shift. Its colimit in Ban is zero. If A is
infinite-dimensional, Josefson--Nissenzweig gives norm-one weak-star null
functionals phi_n. The contraction Jx=(phi_n(x)) maps A into c0 and has
norm(S^m J)=1 for every m. Thus the represented CMet diagram retains two
points, J and 0, at distance one even though both map to the unique point of
Ban(A,0).

## Artifacts

- solution_packet.pdf — complete seven-page-or-longer proof packet
- main.tex — packet source
- verification.md — logical, source, literature, and artifact audit
- source_paper.pdf — arXiv:2206.08546v3
- supporting_josefson_nissenzweig.pdf — arXiv:2003.06764
- figures/open_problem_page8.png — rendered source question
- figures/jn-01.png — rendered supporting theorem statement

The full result is new relative to the bounded search recorded in
verification.md; novelty is not certified exhaustively.

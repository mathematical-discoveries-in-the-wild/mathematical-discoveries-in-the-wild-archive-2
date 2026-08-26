# Nakano DSS classification: literature already answered

Status: `literature_already_answered`.

Original source: César Ruiz and Víctor M. Sánchez, *Nonlinear subsets of
function spaces and spaceability*, arXiv:1401.5906v5 (2014), PDF page 11,
“Open questions.”

Decisive later source: Francisco L. Hernández, César Ruiz, and Mauro Sanchiz,
*Disjointly strictly singular inclusions between variable Lebesgue spaces*,
arXiv:2406.14175 (2024), especially Theorem 4.8 on PDF pages 15–16 and
Theorem 6.3 on PDF page 21.

The 2014 source says that a characterization of disjointly strictly singular
(DSS) inclusion operators between Nakano function spaces is unknown.  The
2024 paper gives the complete characterization.  On an atomless finite
measure space, for exponents `q<p` almost everywhere, Theorem 4.8 proves that
`L^{p(.)} -> L^{q(.)}` is DSS if and only if

`integral_0^{mu(Omega)} a^{(pq/(p-q))^*(x)} dx < infinity`

for every `a>1`; it gives five other equivalent formulations, including
`L`-weak and `M`-weak compactness and a rearrangement limit criterion.  If
`p=q` on a positive-measure set, the inclusion is immediately non-DSS, so
this covers every finite-measure inclusion.  On atomless infinite measure
spaces, Theorem 6.3 proves that every inclusion that exists is non-DSS.

The supporting paper’s abstract and introduction explicitly advertise
“complete characterizations,” and César Ruiz is an author of both papers.
Thus this is a direct later resolution, not a new result of the run.

Scope limitation: this packet settles only the DSS-characterization question
in the source’s closing paragraph.  It does not claim to settle the separate,
more diffuse questions about algebrability or Nakano-space spaceability.

Local evidence:

- `source_paper.pdf`: arXiv:1401.5906v5, 12 pages.
- `supporting_paper_2406.14175.pdf`: decisive 2024 paper, 22 pages.
- `solution_packet.pdf`: compact identification note.
- Ledger: `runs/fa_banach_001/ledger/results/1401.5906_nakano_dss_classification_answered_2406.14175.json`.


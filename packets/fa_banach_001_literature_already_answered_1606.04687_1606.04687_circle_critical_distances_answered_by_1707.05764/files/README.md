# Literature status: critical directed distances from arXiv:1606.04687

- **Source paper:** H. Brezis, P. Mironescu, I. Shafrir, *Distances
  between homotopy classes of \(W^{s,p}(\mathbb S^N;\mathbb S^N)\)*,
  arXiv:1606.04687.
- **Primary answering paper:** I. Shafrir, *On the distance between homotopy
  classes in \(W^{1/p,p}(\mathbb S^1;\mathbb S^1)\)*,
  arXiv:1707.05764.
- **Additional recent answer:** R. L. Frank, P. Ivanisvili, *The distance
  between homotopy classes of Sobolev maps on spheres*, arXiv:2606.29382.
- **Model:** GPT5.6
- **Disposition:** `literature_already_answered` for the circle-critical
  problem, with a recorded additional first-order higher-dimensional answer.

## Exact identification

Open Problem 1 on page 5 of arXiv:1606.04687 asks whether the directed
distance is symmetric, or depends only on the absolute degree difference.
Open Problem 2 asks for a uniform lower bound of order
\(|d_1-d_2|^{1/p}\) in the critical space \(W^{N/p,p}\). The authors single
out \((N,p)=(1,2)\) and explicitly note that the then-known result did not
cover the direction \(0<d_2<d_1\).

Theorem 1.1 of arXiv:1707.05764 proves, for every \(1<p<\infty\) and all
integers \(d_1,d_2\),
\[
 \operatorname{Dist}_{W^{1/p,p}}(\mathcal E_{d_1},\mathcal E_{d_2})
 =\sigma_p(d_2-d_1),
\]
where \(\sigma_p(d)\) is the minimum critical energy in degree \(d\).
Because \(\sigma_p(-d)=\sigma_p(d)\), this gives symmetry and the requested
two-sided order in dimension one. Corollary 1.1 gives the exact highlighted
Hilbert-case formula
\[
 \operatorname{Dist}_{H^{1/2}}(\mathcal E_{d_1},\mathcal E_{d_2})
 =2\pi |d_1-d_2|^{1/2}.
\]

Theorem 1.1 of arXiv:2606.29382 separately gives the exact directed distance
in \(W^{1,N}(\mathbb S^N;\mathbb S^N)\) for every \(N\), thereby resolving
the other highlighted Hilbert case \((N,p)=(2,2)\) and proving symmetry in
the entire first-order critical family.

## Scope limitation

This packet does not claim that the source paper's global questions are now
settled for every critical fractional or higher-order space. In particular,
the general \(W^{N/p,p}\) problem outside the circle and first-order families,
and the source's separate \(W^{2,1}(\mathbb S^1;\mathbb S^1)\) question, are
not answered by the two supporting papers. Those remaining formulations are
broad research programs rather than viable sparse-queue targets for a bounded
single-paper attempt.

## Files

- `source_paper.pdf`: source/open-problem paper.
- `supporting_paper_1707.05764.pdf`: complete circle-critical answer.
- `supporting_paper_2606.29382.pdf`: first-order critical sphere answer.
- `main.tex` and `solution_packet.pdf`: compact status note.
- `source_1606.04687.tar.gz` and `source_metadata_1606.04687.json`: locally
  inspected source materials.

## Search note

The run's cheap indexes contained no exact record for arXiv:1606.04687.
Exact-title and exact-problem web searches found arXiv:1707.05764 and the
June 2026 arXiv:2606.29382. The statements above were checked directly in
the downloaded PDFs, not inferred from citation metadata.


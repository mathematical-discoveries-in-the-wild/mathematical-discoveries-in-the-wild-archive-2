# A universal compression obstruction for fast A-collection gluing

Status: candidate full negative answer in the constructional sense of Remark 3.6, likely valid, requiring expert review.

Source: Florent Baudier, *Quantitative nonlinear embeddings into Lebesgue sequence spaces*, arXiv:1210.0588. The target is Remark 3.6 on source PDF pp. 26--27, immediately after Lemma 3.3, Proposition 3.4, and Example 3.5.

## Result

Let a metric space contain an isometric geodesic ray, let (p\ge 1), and let

\[
 \Phi(x)=(\varphi_n(x)-\varphi_n(o))_{n\ge1}
\]

be the paper's gluing map into an \(\ell_p\)-sum. Suppose the coordinate maps take values in unit balls, satisfy

\[
 \|\varphi_n(x)-\varphi_n(y)\|\le b_n
 \quad\text{whenever }d(x,y)\le n,
 \qquad \sum_n b_n^p<\infty.
\]

Then, along the ray,

\[
 \|\Phi(\gamma(t))-\Phi(\gamma(0))\|
 =o\!\left(t^{1/(p+1)}\right).
\]

Consequently this particular gluing map has compression exponent at most (1/(p+1)).

For every adapted fast A-collection in the source, Lemma 3.3 gives normalized characteristic maps with (b_n^p\le 2\epsilon_n), while fastness means \(\sum_n\epsilon_n<\infty\). Thus the theorem applies. For (p=2), every Hilbert-valued embedding induced by the paper's construction has compression exponent at most (1/3), so no such A-collection can induce an embedding with compression (1/2).

The proof splits the coordinates at an integer (m). The first (m) coordinate differences cost at most (2^pm). In every later coordinate, divide a ray segment of length (t) into pieces of length at most (n), so the cost is at most \(\lceil t/n\rceil b_n\). If (E_m=\sum_{n>m}b_n^p\), this gives

\[
 \|\Phi(\gamma(t))-\Phi(\gamma(0))\|^p
 \le 2^pm+2^{p-1}\bigl(1+(t/m)^p\bigr)E_m.
\]

Taking (m\asymp\delta t^{p/(p+1)}\), first letting (t\to\infty), and then \(\delta\downarrow0\), proves the little-o bound.

## Scope

The negative answer concerns exactly the normalized-characteristic, unweighted \(\ell_p\)-sum gluing construction of Lemma 3.3 and Proposition 3.4, which is what the surrounding text calls "our embedding" and what Remark 3.6 naturally refers to as an A-collection "inducing" an embedding. It does **not** say that a tree itself has Hilbert compression at most (1/3); the source correctly notes that a tree's Hilbert compression is (1). It also does not rule out a materially different weighted or nonlinear construction merely using an A-collection as auxiliary data.

## Packet contents

- `solution_packet.pdf`: review-ready proof packet.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: arXiv source-question PDF.
- `figures/A_collection_definition_crop.png`: source definitions and Lemma 3.3.
- `figures/open_problem_crop_1.png` and `figures/open_problem_crop_2.png`: Proposition 3.4, Example 3.5, and the complete two-page Remark 3.6.
- `VERIFICATION.md`: structural proof audit, scope audit, and novelty record.
- `tmp/`: compilation and rendering intermediates.

## Novelty check

On 11 August 2026, bounded searches covered the four run indexes; the exact arXiv id, title, and question wording; title/citation variants; and combinations of adapted fast A-collections, radial dilation, normalized characteristic maps, trees, compression (1/2), and compression (1/3). No later paper explicitly answering Remark 3.6 and no matching universal gluing obstruction were located. Novelty is provisional.

## Human-review recommendation

First confirm that "an A-collection inducing an embedding" in Remark 3.6 means the construction immediately preceding it. Then verify the coordinate split, the ray-chain estimate, and the two-limit optimization. If a broader meaning of "inducing" was intended, reclassify the theorem as a sharp negative result for the paper's proposed mechanism rather than a full answer to every conceivable A-collection-based construction.


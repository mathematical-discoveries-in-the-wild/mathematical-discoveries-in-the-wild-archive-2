# Verification report

Verdict: `candidate_partial_likely_valid`

Model: `GPT5.6`

Date: 2026-08-09

## Claim-to-source check

- The source PDF is arXiv:2502.02186v3 by Rafał Latała and Marta Strzelecka.
- Source page 3, Conjecture 5 asks for the sharp absolute dependence on $p^*$ and $q$ in the Gaussian upper bound.
- Source page 5, equation (3) states the Bernoulli comparison used in the packet.
- The packet is correctly classified as partial: arbitrary dense supports remain open.

## Proof audit

1. **Forest split.** Rooting each bipartite tree and assigning each edge to its child partitions the support. In the row-child part every row has at most one edge; in the column-child part every column has at most one edge. Both claims remain true regardless of which bipartition contains the root.

2. **Degree-one norm identities.** If every row has degree at most one, grouping by columns gives
   $\|B\|_{p\to q}=\max_j\|(b_{ij})_i\|_q$ for $p\le q$. If every column has degree at most one, grouping by rows and Hölder gives
   $\|B\|_{p\to q}=\max_i\|(b_{ij})_j\|_{p^*}$. The endpoint conventions use maxima and are consistent.

3. **Arboricity extension.** The definition of arboricity supplies an edge partition into $a$ forests. Triangle inequality gives the factor $a$. No graph decomposition theorem beyond the definition is invoked.

4. **Gaussian parameter truncation.** Source equations (1) and (2) give the maximal column/row estimates with factors $\sqrt q$ and $\sqrt{p^*}$. When $r\ge\operatorname{Log}d$, the pointwise inequality $\|x\|_r\le d^{1/r}\|x\|_\infty\le e\|x\|_\infty$ replaces $\sqrt r$ by the desired dimension truncation. This covers $r=\infty$.

5. **Bernoulli functional.** Deleting entries preserves the arboricity upper bound and decreases every row and column norm. Hence every scalar chaos appearing after deletion is pointwise bounded by $a(R+C)$, so its $L_{\operatorname{Log}k}$ norm and the max-inf-sup functional are bounded by the same quantity.

6. **Endpoint cases.** For arbitrary support, the $\ell_1\to\ell_q$ norm is exactly the largest column $\ell_q$ norm and the $\ell_p\to\ell_\infty$ norm is exactly the largest row $\ell_{p^*}$ norm. Entry deletion cannot increase these norms, giving the factor-$3$ Bernoulli comparisons.

No circular use of either source conjecture was found. The Gaussian proof uses only inequalities that the source has already established.

## Computational sanity check

Command:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2502.02186_forest_support_random_operator_norms/code/verify_forest_bounds.py
```

Output:

```text
PASS: 500 random forest matrices, 10000 Bernoulli signings; rooted decompositions and spectral/endpoint bounds verified.
```

The script checks finite examples only and is not used as proof.

## Literature/novelty check

Cheap run indexes and archived claims had no hit for arXiv:2502.02186. Bounded primary arXiv searches combined the exact title or identifier with `forest support`, `support graph`, `star forest`, `Bernoulli`, and `bounded arboricity`; no prior statement of these subcases was found. Novelty confidence remains moderate because the deterministic forest lemma is elementary and could be folklore under other terminology.

## Remaining reviewer focus

- Confirm the intended source convention that the deletion set $I$ in equation (3) is a subset of matrix-entry pairs.
- Search beyond arXiv for the elementary forest/arboricity norm lemma under sparse-matrix or graph-norm terminology.
- Check that the source authors intend uniform absolute constants in Conjecture 5 exactly as rendered in v3.

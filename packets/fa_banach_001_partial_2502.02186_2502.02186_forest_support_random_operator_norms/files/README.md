# 2502.02186: bounded-arboricity random operator norms

- Status: `candidate_partial_likely_valid`
- Model: `GPT5.6`
- Source: Rafał Latała and Marta Strzelecka, *Operator $\ell_p\to\ell_q$ norms of Gaussian matrices*, arXiv:2502.02186v3
- Target: source Conjecture 5 (sharp dependence on $p,q$ for Gaussian matrices) and the Bernoulli conjecture on source page 5, equation (3)
- Packet: `runs/fa_banach_001/solutions/partial/2502.02186_forest_support_random_operator_norms/`

## Result

Let the bipartite support graph of a nonzero matrix $A$ have arboricity $a$. For every $1\le p\le2\le q\le\infty$,

\[
\mathbb E\| (a_{ij}g_{ij})\|_{p\to q}
\le Ca\left[
\sqrt{p^*\wedge\operatorname{Log}n}\max_i\|(a_{ij})_j\|_{p^*}
+\sqrt{q\wedge\operatorname{Log}m}\max_j\|(a_{ij})_i\|_q
+\mathbb E\max_{i,j}|a_{ij}g_{ij}|
\right].
\]

Thus the source's sharp-parameter Gaussian conjecture holds with an absolute constant on forest supports ($a=1$), and quantitatively with a linear arboricity loss in general.

For the source Bernoulli functional

\[
H_{p,q}(A)=\max_i\|(a_{ij})_j\|_{p^*}+\max_j\|(a_{ij})_i\|_q+\Phi_{p,q}(A),
\]

the packet proves, throughout $p\le q$,

\[
\frac{H_{p,q}(A)}{2(a+1)}
\le \mathbb E\|(a_{ij}\varepsilon_{ij})\|_{p\to q}
\le aH_{p,q}(A).
\]

In particular, the Bernoulli conjecture holds with absolute constants on forest supports. It also holds at $p=1$ or $q=\infty$ for arbitrary support, with factor at most $3$.

## Proof mechanism

Root each support-forest component. Split every edge according to whether its child endpoint is a row or a column vertex. One piece has row degree at most one and therefore has $\ell_p\to\ell_q$ norm equal to its largest column $\ell_q$ norm; the other has column degree at most one and norm equal to its largest row $\ell_{p^*}$ norm. This gives

\[
\max\{R_{p^*}(A),C_q(A)\}\le\|A\|_{p\to q}
\le a(R_{p^*}(A)+C_q(A)).
\]

The Gaussian result then follows from the source's endpoint maximal-row/maximal-column estimates and the elementary dimension truncation $\|x\|_r\le d^{1/r}\|x\|_\infty$. For Bernoulli matrices, row and column norms do not depend on the signs, and the same deterministic bound controls every deleted-edge chaos in $\Phi_{p,q}(A)$.

## Evidence and verification

- `source_paper.pdf`: local copy of arXiv:2502.02186v3.
- `figures/gaussian_conjecture_crop.png`: source page 3, Conjecture 5.
- `figures/bernoulli_conjecture_crop.png`: source page 5, equation (3).
- `code/verify_forest_bounds.py`: reproducible sanity check. It passed on 500 random bipartite forests and 10,000 Bernoulli signings.
- `verification.md`: claim-to-source, proof, endpoint, computation, and novelty audit.
- `main.tex` and `solution_packet.pdf`: complete proof and review packet.

Verification command:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2502.02186_forest_support_random_operator_norms/code/verify_forest_bounds.py
```

## Novelty and limitations

A bounded local-index and primary arXiv search on 2026-08-09 found no prior statement of these forest/arboricity subcases or the arbitrary-support Bernoulli endpoint observation. Novelty confidence is moderate because the rooted-forest norm decomposition is elementary and may be folklore.

The unrestricted conjectures remain open here. The constants in the broader sparse-support statements grow linearly with arboricity.

## Human review

Recommended for expert review as a fully proved partial result. The most important checks are the interpretation of the source deletion set $I$, the endpoint conventions, and whether the forest argument appears elsewhere under different terminology.

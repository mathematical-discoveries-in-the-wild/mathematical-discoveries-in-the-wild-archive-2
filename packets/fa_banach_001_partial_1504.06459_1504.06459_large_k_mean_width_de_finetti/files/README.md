# A de Finetti endpoint for the growing-`k` mean-width question

Status: `candidate_substantial_partial_likely_valid`

Source: Cécilia Lancien, *k-extendibility of high-dimensional bipartite
quantum states*, arXiv:1504.06459, Section 9.1 (PDF pages 17--18).

The source asks for the mean width of ordinary `k(d)`-extendible states on
`C^d tensor C^d` for general growing `k(d)`. It proves the fixed/small-`k`
asymptotic and a lower bound valid for every `k(d)`.

The packet proves the uniform endpoint estimate

`0 <= w(E_k)-w(Sep) <= C min(d^(-1), d/k)`.

Consequently,

`w(E_{k(d)}) / w(Sep) = 1 + O(d^(5/2)/k(d))`,

so `k(d) >> d^(5/2)` is a complete regime in which the `k(d)`-extendible
mean width is asymptotically the separable mean width. Combined with the
source's lower bound, `k(d)=o(d)` instead forces the ratio to diverge.

The proof is a short but apparently unstated synthesis of the quantitative
finite de Finetti trace-norm bound, Gaussian support-function duality, and the
known `d^(-3/2)` separable mean-width scale. Novelty confidence is modest:
bounded exact-phrase, author/title, citation, and theorem searches found no
statement of this endpoint corollary, but it is derived from known estimates.
The intermediate window `d lesssim k lesssim d^(5/2)` remains open.

Files:

- `solution_packet.pdf`: theorem, proof, phase endpoints, and upgrade audit.
- `source_paper.pdf`: Lancien's source paper.
- `supporting_paper_quant-ph_0602130.pdf`: quantitative finite de Finetti
  source of Christandl--König--Mitchison--Renner.
- `supporting_paper_quant-ph_0503221.pdf`: Aubrun--Szarek separable-width
  source.
- `figures/open_problem_crop.png`: real source-PDF crop of Section 9.1.
- `verification.md`: proof audit and reviewer priorities.

Human-review priority: verify the trace-distance convention/constants (which
do not affect the exponent), the normalization by `gamma(d^2)`, and the
division by the separable lower mean-width bound.

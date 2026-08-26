# Partial Result: Deterministic Rank-One Matrix RIP in n^(1+o(1)) Measurements

Status: candidate_substantial_partial_likely_valid_needs_human_review

Run: fa_banach_001  
Agent: agent_lane_17  
Target: Simon Foucart, *Linearly Embedding Sparse Vectors from ell_2 to ell_1
via Deterministic Dimension-Reducing Maps*, arXiv:2310.18565.

## Exact target

Section 6, page 14 of the source asks whether deterministic matrices can give

    (1-delta)||X||_F <= ||A(X)||_1 <= (1+delta)||X||_F

for all rank-r matrices with `m << n^2`, ideally using rank-one measurement
matrices. The source calls even the unrestricted deterministic case wide open.

## New partial result

For every fixed `delta in (0,1)` and over either the real or complex field,
the rank-one subcase has a deterministic polynomial-time construction using
rank-one measurement matrices and

    m <= n exp(C_delta (log log(n+2))^2) = n^(1+o(1)) = o(n^2).

The construction first extracts an explicit flat tight frame
`B: K^n -> K^M` from Indyk's recursive extractor embedding. It then retains
only coordinates `(j,k)` along a constant-degree explicit spectral expander
and uses measurements `A_(j,k)=b_j b_k^*`. For `X=uv^*`,

    |<A_(j,k),X>_F| = |b_j^*u| |b_k^*v|,

so expander mixing compares the measurement sum with
`||Bu||_1 ||Bv||_1`. Tightness controls the mixing error exactly in the
Frobenius norm.

The relative flatness can be made arbitrarily close to one, and the normalized
second singular value of the graph can be made arbitrarily small by fixing a
large enough degree. Rescaling gives any prescribed `delta`.

## Scope

This solves only `r=1`. Six materially different extension attempts were
audited. For `r>1`, entrywise absolute value destroys the separable outer-
product structure used by the expander mixing lemma; all checked elementary
extensions either lose `sqrt(r)`, need `M^2=n^(2+o(1))` measurements, or
require a presently unavailable low-rank absolute-value sampler.

## Files

- `main.tex`: full theorem, proof, limitations, and references.
- `solution_packet.pdf`: compiled human-review packet.
- `source_paper.pdf`: target paper.
- `source_indyk_eccc.pdf`: primary source for the explicit embedding.
- `figures/open_problem_crop.png`: source challenge on page 14.
- `figures/indyk_theorem_page_6.png` and
  `figures/indyk_corollary_page_7.png`: primary-source construction evidence.
- `code/verify_rank_one_expander.py`: deterministic finite regression check.
- `verification.md`: proof, artifact, and novelty audit.

## Verification command

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2310.18565_expander_tensor_rank_one_matrix_rip/code/verify_rank_one_expander.py
```

Expected final line:

```text
VERIFIED: tight frames, expander mixing, factorization, and rank-one RIP bounds
```

## Novelty bound and review focus

The four run indexes and bounded primary-source/arXiv phrase searches found
the target, Indyk's embedding, explicit expanders, randomized rank-one RIP,
and adjacent deterministic sparse-vector RIP work, but no statement of this
rank-one expander-sparsification. This is not an exhaustive literature
certification.

The main expert-review focus is the structural extraction in Lemma 1: every
recursive Indyk block map is a scalar tight frame because its dictionary is a
concatenation of orthonormal bases and its extractor graph repeats each input
coordinate with constant degree. The expander proof after that lemma is
elementary.

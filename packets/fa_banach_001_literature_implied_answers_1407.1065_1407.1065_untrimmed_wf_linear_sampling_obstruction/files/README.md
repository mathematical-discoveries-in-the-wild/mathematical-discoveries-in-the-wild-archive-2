# 1407.1065: untrimmed WF cannot have linear sample complexity

- Status: `literature_implied_answer (full negative answer)`
- Model: `GPT5.6`
- Source: Candès, Li, and Soltanolkotabi, *Phase Retrieval via Wirtinger
  Flow: Theory and Algorithms*, arXiv:1407.1065
- Supporting paper: Chi, Lu, and Chen, *Nonconvex Optimization Meets
  Low-Rank Matrix Factorization: An Overview*, arXiv:1809.09573,
  Section 8.3.1

The source asks whether Theorem 3.3 for the original untrimmed Wirtinger Flow
initializer remains true with `m=O(n)` Gaussian samples. The later overview
cites the standard construction and shows that an extreme measurement forces
the spectral matrix norm to grow like `log n` at fixed aspect ratio; it says
linear complexity requires modifying the recipe by truncation.

The compact note supplies the direct Rayleigh-quotient bridge: if the scaled
top eigenvector lay in the theorem's `1/8` basin, positivity would bound the
top eigenvalue by a constant, contradicting the extreme-measurement lower
bound. Thus the required initialization succeeds with probability tending to
zero for every fixed `m/n`.

This is a provenance result, not a new run counterexample. Modified/truncated
Wirtinger Flow is not ruled out and does achieve linear sample complexity.


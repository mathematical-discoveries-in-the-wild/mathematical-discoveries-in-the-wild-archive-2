# Symmetric-tensor leverage bounds for Z_p(X)

Status: candidate full solution to the first formulation of Problem 1 in
arXiv:1711.02214, pending expert review.

The packet proves the requested outer second-moment estimate for every random
vector, without centering. It also proves the stronger outer p-moment estimate
for all vectors with regular one-dimensional moment growth, including centered
log-concave vectors, and settles Problem 2 in the range q <= p.

Core estimate: for every integer k >= 1,

    E ||X||_{Z_{2k}(X)}^{2k}
      <= rank E[X^{tensor k}(X^{tensor k})*]
      <= binom(n+k-1,k).

The proof lifts to the symmetric tensor power and bounds the rank-one
supremum by an ordinary leverage score. See `solution_packet.pdf` for the full
proof, source screenshots, scope, novelty check, and reviewer guidance.

Verification:

    conda run --no-capture-output -n sandbox python code/verify_tensor_leverage.py

The companion development history is
`../../../attempts/1711.02214_symmetric_tensor_zp_upgrade_attempts.md`.

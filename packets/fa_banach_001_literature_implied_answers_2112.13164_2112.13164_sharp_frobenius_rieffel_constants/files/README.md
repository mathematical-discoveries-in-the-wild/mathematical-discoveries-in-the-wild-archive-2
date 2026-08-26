# Sharp Frobenius-Rieffel constants via the Pimsner-Popa index

Status: `literature_implied_answer (full problem)`.

Aguilar, Garcia, and Kim ask for the sharp lower equivalence constants between
the operator norm and Frobenius-Rieffel norms on arbitrary finite-dimensional
C*-algebras. Pimsner and Popa's 1986 Theorem 6.1 already computes the exact
finite-dimensional order index. Translating their multiplicity-and-trace
formula and adding the rank-one equality case gives the exact
Frobenius-Rieffel constant.

If

`A = direct_sum_k M_{d_k}`, `B = direct_sum_j M_{n_j}`,

`m_{kj}` is the multiplicity of the `j`th simple component of `B` in the
`k`th component of `A`, `q_k=v_k/d_k`,
`omega_j=sum_l q_l m_{lj}`, and `b_{kj}=min(m_{kj},n_j)`, then

`kappa_sharp = D^{-1/2}`,

where

`D=max_k sum_j b_{kj} omega_j/q_k`.

For `A=M_n`, this reduces to

`D=sum_j m_j min(m_j,n_j)`.

It also corrects one numerical guess in Table 1 of the source: for
`B^5_{2^2,1}={diag(A,A,lambda)}`, the sharp constant is `1/sqrt(5)`, not
`1/2`.

The supporting authors did not identify their theorem as an answer to the
Frobenius-Rieffel question. The implication and equality witness are recorded
in `solution_packet.pdf` for review.


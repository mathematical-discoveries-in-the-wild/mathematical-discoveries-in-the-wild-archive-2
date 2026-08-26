# Verification report

Verdict: `literature_implied_answer (full problem); likely valid`.

## Mathematical audit

1. Every unital inclusion of finite-dimensional C*-algebras is described,
   after unitary conjugacy, by a nonnegative integral multiplicity matrix
   `m_{kj}`.
2. With `q_k=v_k/d_k` and
   `omega_j=sum_l q_l m_{lj}`, the trace-preserving expectation sends a
   rank-one projection supported in ambient summand `k` to blocks
   `(q_k/omega_j) rho_j`, where `rho_j` is the reduced density matrix of the
   corresponding vector component.
3. `rank(rho_j) <= min(m_{kj},n_j)`. Trace divided by rank gives the lower
   bound `1/D`, and a weighted maximally entangled vector in each block attains
   equality simultaneously.
4. Therefore the squared sharp Frobenius-Rieffel constant is `1/D`.
5. Pimsner-Popa Theorem 6.1 gives the same `D` as the reciprocal of their
   finite-dimensional order constant. This establishes the claimed provenance
   identification.
6. For `B^5_{2^2,1}`, the unit vector
   `(sqrt(2/5),0,0,sqrt(2/5),sqrt(1/5))` has rank-one projection `p` with
   `P_B(p)=I_5/5`, proving that the source's guessed constant `1/2` is too
   large and that `1/sqrt(5)` is attained.

## Literature audit

- The source paper asks for the sharp constants immediately before Table 1,
  arXiv PDF page 14; the table is on page 15.
- Pimsner and Popa, Theorem 6.1, printed page 93 (packet supporting PDF page
  38), gives the exact finite-dimensional multiplicity-and-trace formula.
- Gao and Rouze (2022), formula (14), restate the `M_n` specialization as the
  Pimsner-Popa index.
- Aguilar, Garcia, Kim, and Latremoliere's March 2026 revision of
  arXiv:2301.05692 still says that the sharp Frobenius-Rieffel constants are
  unknown, confirming that the literature implication was not noticed there.

Novelty classification: not a new mathematical theorem; a previously
unrecorded direct identification, with an elementary equality witness.

## Render audit

Completed on 11 August 2026. The final three-page LaTeX build has no warnings,
undefined citations, overfull boxes, or underfull boxes. All three rendered
pages were inspected after the final formula corrections; equations, headings,
references, and the explicit `B^5_{2^2,1}` witness are legible and unclipped.


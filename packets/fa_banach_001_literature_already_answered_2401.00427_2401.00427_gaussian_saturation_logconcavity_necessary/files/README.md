# Gaussian saturation: the unrestricted conjecture is false

**Status:** literature already answered.

Section 3.2 of arXiv:2401.00427 proposes equation (3.5): centered
Gaussians should exhaust the inverse Brascamp--Lieb infimum for every datum
when the input functions are merely nonnegative, integrable, and even.

Two later papers determine the situation.

- Nakamura--Tsuji, arXiv:2409.13611, Theorem 1.3, prove Gaussian saturation
  for arbitrary symmetric quadratic kernels and positive exponents when the
  even inputs are also log-concave. Their Theorem 4.1 resolves the linked
  Kolesnikov--Werner exponential-kernel datum.
- Milman, arXiv:2501.11018, Section 1.1 (PDF page 5), proves that the
  log-concavity assumption cannot be dropped. His two-dimensional correlated
  Gaussian construction uses one interval indicator and the indicator of its
  complement, thereby refuting the unrestricted universal statement.

Thus the source conjecture is false as written, and the natural log-concave
repair is already a theorem in the literature.

Files:

- `solution_packet.pdf`: compact status and identification note.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: arXiv:2401.00427v2.
- `supporting_2409.13611.pdf`: positive log-concave theorem and the linked
  Kolesnikov--Werner result.
- `supporting_2501.11018.pdf`: later negative answer without log-concavity.


# No similarity between the trivial and sign weighted Bergman modules

Status: **candidate full negative solution, likely valid**.

For every `n >= 2` and every `lambda >= 1`, the trivial and sign reducing
submodules of the weighted Bergman/Hardy module `A^(lambda)(D^n)` are not
similar over the symmetric polynomial ring. Moreover, multiplication by the
Vandermonde is never onto, so the associated division problem has a negative
answer for all parameters.

The source paper, arXiv:2409.11101, asks the general similarity question in
Section 4.3 (PDF page 20), proves only `n=2`, `lambda=1,2`, and restates the
general division problem in Remark 4.22 (PDF page 21).

The proof compares the reproducing kernels of the symmetric module and the
Vandermonde-divided sign module on the full diagonal. Their norm ratio grows
exactly as `(1-|a|^2)^(-n(n-1)/2)`. Any hypothetical similarity is an
invertible multiplier, so its reciprocal would be a nonzero holomorphic
function on the diagonal bounded by a constant times
`(1-|a|^2)^(n(n-1)/2)`. Maximum modulus makes that impossible.

Files:

- `solution_packet.pdf`: review-ready proof packet.
- `source_paper.pdf`: the original arXiv paper.
- `figures/open_problem_crop.png`: exact general similarity question.
- `figures/division_question_crop.png`: Remark 4.22's division formulation.
- `code/verify_confluent_kernel.py`: exact symbolic checks of the determinant
  formula used in the proof.
- `verification.md`: audit record, novelty bounds, and hashes.

Human review should focus on the cyclic-multiplier reduction and the
normalization in the sign-kernel determinant. Both are written out explicitly
in the packet.


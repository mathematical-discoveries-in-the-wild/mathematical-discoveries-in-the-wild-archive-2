# Interpolating zeros force nonseparability in the de Branges gap

Status: candidate_partial_result_likely_valid

Baranov--Woracek ask whether their imaginary-half-line majorant space can be
proper but separable or reflexive.  This packet rules that out whenever the
zeros of the associated meromorphic inner function contain a Riesz kernel
subsequence of divergent total height.  In particular, it rules out all
interpolating zero sequences in the unresolved zero-distribution gap.

The proof uses a weighted block encoding.  Each bounded-sequence increment is
distributed over a remote zero block in proportion to zero height.  The block
retains the required Cauchy-transform mass, while its Hilbert cost is divided
by the block's total height.  Lacunary gaps bound both the function and its
sharp conjugate and recover the encoded partial sums.

The general question remains open for highly clustered or multiple zeros that
may have no divergent-height Riesz subsequence.

Novelty confidence is moderate.  Exact web/arXiv searches on August 11, 2026
found the source series and related interpolation literature but no matching
statement or full resolution.

Human review should focus on the normalized-kernel coefficient, the two
Cauchy-transform estimates, and the block recovery lower bound.

Files:

- `solution_packet.pdf`: self-contained partial theorem and proof;
- `source_paper.pdf`: arXiv:0906.2943;
- `figures/open_problem_crop.png`: Theorems 3.1--3.2 and Remark 3.3 on page 7;
- `code/verify_weighted_blocks.py`: finite weighted-block sanity check;
- `VERIFICATION.md`: dependency and build audit.

# Ordinary norm-one idempotent multipliers are coset indicators

Candidate full negative answer to the open question in the remark following
Theorem 1.1 of arXiv:0806.4643.

For every discrete group \(G\), if \(E\subset G\) is nonempty,
\(\chi_E\in MA(G)\), and its ordinary multiplier norm is one, then \(E\) is a
coset of a subgroup. Consequently \(\chi_E\in B(G)\subset M_{cb}A(G)\), with
cb multiplier norm one. In particular, the exceptional set requested in the
source cannot exist for the free group on two generators.

The decisive mechanism is that the adjoint multiplier is a unital contractive
projection on \(VN(G)\). Positivity and preservation of the canonical finite
trace force its range to be closed under the ambient Jordan product; this
forces the Fourier support to be a subgroup.

- `solution_packet.pdf`: human-review artifact
- `main.tex`: full theorem and proof
- `source_paper.pdf`: original arXiv PDF
- `figures/open_problem_crop.png`: source question on PDF page 4
- `code/check_cyclic_groups.py`: exhaustive finite cyclic sanity check
- `code/make_source_crop.py`: reproducible source crop
- `verification_report.md`: proof and provenance audit
- `attempt_log.md`: development record

Status: **candidate full proof, likely valid, pending expert review**.


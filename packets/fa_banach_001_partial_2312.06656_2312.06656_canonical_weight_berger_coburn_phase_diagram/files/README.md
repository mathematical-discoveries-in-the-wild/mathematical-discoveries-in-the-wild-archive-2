# arXiv:2312.06656 — canonical-weight Berger–Coburn phase diagram

Status: candidate partial result.

For the canonical doubling Fock space with weight `phi_m(z)=|z|^m`, this packet determines the Berger–Coburn question throughout a large sharp range of Schatten exponents. Put

`p_-(m)=2m/(m+2)` and `p_+(m)=2m/(m-2)` when `m>2`.

- If `0<m<=2`, then for every `1<p<infinity` and bounded symbol `f`, `H_f` belongs to `S_p` if and only if `H_bar(f)` does, with equivalent Schatten norms.
- If `m>2`, the same positive result holds exactly on the open interval `p_-<p<p_+` furnished by the source paper's Muckenhoupt reduction.
- If `m>2` and `1<p<=p_-`, Xia's bounded symbol gives `H_f in S_p` but `H_bar(f) notin S_p`. The endpoint divergence is logarithmic.

Thus the low endpoint is sharp. The high range `p>=p_+` for `m>2`, and the source's question for arbitrary doubling weights, remain unresolved.

Files:

- `solution_packet.pdf`: theorem, proofs, attempt audit, and exact scope.
- `source_paper.pdf`: official arXiv PDF for 2312.06656.
- `main.tex`: packet source.
- `attempts.md`: eight-attempt upgrade record.
- `verification.md`: algebra, proof, literature, and rendering checks.
- `code/verify_thresholds.py`: exact rational-arithmetic endpoint checks.

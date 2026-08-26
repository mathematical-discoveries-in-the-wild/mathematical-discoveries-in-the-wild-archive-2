# Literature-implied full answer: all dual probabilistic frames

Chen, King, and Shonkwiler's *Approximately Dual and Pseudo-Dual
Probabilistic Frames* (arXiv:2505.13885) says in the Introduction that
characterizing all dual probabilistic frames of a fixed probabilistic frame
remains open.

There is an exact measure-level characterization. If `mu` is a probabilistic
frame with frame operator `S_mu`, let

`H_mu = {h in L2(mu;R^n): integral x h(x)^t dmu(x)=0}`.

Then the complete dual class is

`D(mu) = union_{h in H_mu} {nu in P2(R^n):
          (S_mu^{-1} id+h)_#mu <=_cx nu}`,

where `<=_cx` is convex order. Equivalently, every dual measure is a
mean-preserving spread of a pushforward-type dual, and every such spread is a
dual.

The proof disintegrates a dual coupling and takes its conditional barycenter.
Conditional Jensen gives the convex-order necessity. Conversely, Strassen's
martingale theorem realizes the convex-order relation by a barycenter-preserving
kernel; composing this kernel with the admissible pushforward map gives the
required dual coupling.

Files:

- `solution_packet.pdf`: compact theorem, proof, provenance, and scope note.
- `source_paper.pdf`: arXiv:2505.13885.
- `supporting_strassen_theorem_2412.00516.pdf`: Bołbotowski--Bouchitté,
  arXiv:2412.00516, Theorem 2.3, an explicit multidimensional statement of
  Strassen's convex-order/martingale-kernel theorem.
- `main.tex`: packet source.
- `verification.md`: implication-by-implication audit.

Status: `literature_implied_answer (full)`. Strassen's theorem predates the
2025 question, but neither the source nor the preceding transport-dual paper
states this convex-order consequence. The identification is therefore not an
explicit literature answer, and no priority claim is made.

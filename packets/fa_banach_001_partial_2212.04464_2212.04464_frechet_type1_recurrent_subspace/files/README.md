# Fréchet type-1 recurrent-subspace criterion

Status: `candidate_partial_likely_valid`.

This packet gives a complete affirmative answer to Question 7.7 of arXiv:2212.04464 for Fréchet spaces with a continuous norm, and strengthens it to arbitrary Fréchet spaces in Menet's type-1 regime.

The natural diagonal equicontinuity assumption is

\[
p_s(T^{k_n}x)\le C_s p_{m(s)}(x)
\quad(n\ge N_s,\ x\in E_n).
\]

If the decreasing closed infinite-dimensional control spaces satisfy that

\[
E_n\cap\ker p_1
\]

has infinite codimension in `E_n` for one defining seminorm `p_1`, the packet proves that there are a closed infinite-dimensional `F` and a subsequence along which `T^{k_n}x -> x` for every `x in F`. In the continuous-norm case the kernel condition is automatic.

The unrestricted type-2 case remains unresolved because the available triangular basic sequences are not stable under perturbation and allow arbitrary coefficient growth.

Files:

- `solution_packet.pdf`: review packet with theorem, proof, limitations, and bibliography.
- `source_paper.pdf`: official arXiv PDF of 2212.04464.
- `supporting_paper_1208.4963.pdf`: Menet's continuous-norm basic-sequence reference.
- `supporting_paper_1302.6447.pdf`: Menet's type-1 no-continuous-norm basic-sequence reference.
- `figures/open_problem_crop.png`: Question 7.7 and its intended equicontinuity interpretation.
- `main.tex`: packet source.
- `tmp/`: build and rendered QA artifacts.

Attempt log: `runs/fa_banach_001/attempts/2212.04464_frechet_recurrent_subspace_upgrade.md`.

Human review should focus on the variable-subspace use of Menet's selection theorem, the perturbation coefficient bound, and the four-term tail estimate.

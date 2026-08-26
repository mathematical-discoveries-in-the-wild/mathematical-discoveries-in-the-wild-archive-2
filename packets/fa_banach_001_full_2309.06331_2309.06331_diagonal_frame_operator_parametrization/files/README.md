# Diagonal frame-operator parametrizations

This packet gives a candidate full solution to the two explicit
classification questions on source page 11 of arXiv:2309.06331.

Main result: if the original frame operator is S, then every operator
producing a frame with positive invertible diagonal frame operator D is
exactly

    M = D^(1/2) C S^(-1/2),

where C is a coisometry. Every additive perturbation is exactly

    d_j = D^(1/2) C e_j - v_j,

with C a coisometry from the coefficient space to the Hilbert space.

The packet also proves:

- the equivalent pairwise-orthogonal row criterion;
- an explicit canonical Parseval perturbation and its exact synthesis norm;
- the sharp bound sup_j ||S^(-1)v_j|| <= A^(-1/2) for the canonical dual;
- the exact universal componentwise-radius threshold
  ||epsilon||_2 < sqrt(A), including sharp counterexamples.

Files:

- solution_packet.pdf: final self-contained proof packet;
- main.tex: packet source;
- source_paper.pdf: locally compiled arXiv source;
- figures/source_open-11.png and figures/source_open-12.png: complete
  visually inspected source pages reproduced in the packet;
- verification.md: proof, novelty, build, and render audit.

Status: candidate full solution, likely valid. Novelty confidence is
moderate because the core factorization is elementary and may be implicit in
standard frame/operator theory even though no explicit answer was found.


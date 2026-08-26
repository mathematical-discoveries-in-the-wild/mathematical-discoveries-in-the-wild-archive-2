# No disjoint-reiterative gap for mixing weighted shifts on c0

Status: candidate_partial_result_likely_valid

This packet proves that every finite disjoint-hypercyclic tuple of mixing
unilateral weighted backward shifts on `c0(N)` is disjoint reiteratively
hypercyclic.  Consequently, a weighted-shift counterexample to Question 5.1
of Martin--Menet--Puig cannot consist of mixing shifts.

The proof converts one disjoint-hypercyclic interpolation at many shifted
coordinates into arbitrarily long arithmetic blocks of synchronized target
ratios.  Mixing controls every cross-block tail through an exact product
factorization.  The union of the blocks has positive upper Banach density, so
the `c0` characterization from Martin--Menet--Puig applies.

The general question remains open: individual reiterative hypercyclicity does
not give the uniform all-large-differences product growth used here.

Novelty confidence is moderate.  Exact web/arXiv searches on August 11, 2026
found the original 2022 question, the reflexive-space partial answer in
arXiv:2412.19115, and background work, but no matching mixing-`c0` statement.

Human review should focus on the finite ratio-interpolation lemma, the
coordinate prescription `b[s,j+rM]`, and the cross-tail identity in the proof.

Files:

- `solution_packet.pdf`: theorem, proof, limitations, and source evidence;
- `source_paper.pdf`: arXiv:2412.19115v2;
- `supporting_paper_2106.01409.pdf`: the characterization used in the proof;
- `figures/open_problem_crop.png`: Question 1.1 on source page 2;
- `code/verify_block_identities.py`: finite numerical identity/density check.

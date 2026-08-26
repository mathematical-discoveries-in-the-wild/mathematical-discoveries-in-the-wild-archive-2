# All-order compact-support modular density

Status: `candidate_full_solution_likely_valid` for Conjecture 1 of
arXiv:1711.06145.

For `u in V_0^m L_M(Omega)` with compact support inside `Omega`, take the
ordinary Friedrichs mollifications `u_epsilon`. Because `u in W^{m,1}`, every
derivative through order `m` converges in `L^1`. For each top-order derivative,
the scalar proof inside source Lemma 12 applies directly: it only needs that
the field lies in `L_M` and has compact support, not that its lower derivatives
also lie in `L_M`. Thus the top derivative converges modularly. Finite-component
convexity combines the tensor components.

This proves the conjecture for every `m>=1` under either set of source
hypotheses. The segment property is not needed because the support stays a
positive distance from the boundary.

Files:

- `main.tex`: full proof.
- `solution_packet.pdf`: compiled packet.
- `source_paper.pdf`: arXiv:1711.06145.
- `figures/conjecture-crop.png`: Conjecture 1, source PDF page 7.
- `figures/lemma12-crop.png`: source Lemma 12, PDF page 10.
- `attempts.md`: seven focused checks/upgrade attempts.
- `verification.md`: mathematical and rendering audit.

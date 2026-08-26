# Full solution: symmetry of the two primary ring-model branches

Status: candidate_full_solution_likely_valid.

Source: Romain Veltz and Olivier Faugeras, *Local/global analysis of the
stationary solutions of some neural field equations*, arXiv:0910.2247,
SIAM J. Appl. Dyn. Syst. 9 (2010), 954–998.

## Result

The packet proves the source’s three-item numerical conjecture for the named
primary one-parameter pitchfork continuations:

1. P_1 lies on the v_3-axis.
2. P_3 lies in the plane v_3=0.
3. P_1 and P_3 do not intersect.

The axis is invariant because its potential is odd and the centered sigmoid
is odd. The plane is invariant by reflection symmetry. Simple local branch
uniqueness places the two pitchforks in those subspaces, and primary
continuation without branch switching preserves them. Since the subspaces
meet only at zero, an intersection would have to be trivial; linearization
shows the branches can approach zero only at their distinct bifurcation
parameters.

## Files

- main.tex: full proof packet.
- solution_packet.pdf: rendered packet.
- verification.md: explicit verifier report.
- source_paper.pdf: original source paper.
- figures/open_conjecture-22.png: source conjecture and eigenvalue context.
- figures/source_system_symmetry-20.png: exact model and source symmetry lemma.
- code/check_roots.py: reproducible numerical stress test.

## Scope

The source defines a branch as a one-dimensional continuation obtained by
varying one parameter, and its P_i are primary pseudo-arclength curves. The
packet does not assert the stronger statement that an ambient connected
component enlarged by every possible secondary branch has no
symmetry-breaking offshoot.

## Human review focus

Review the branch-convention match, the simple-branch uniqueness step inside
the invariant subspaces, and the trivial-line accumulation argument.

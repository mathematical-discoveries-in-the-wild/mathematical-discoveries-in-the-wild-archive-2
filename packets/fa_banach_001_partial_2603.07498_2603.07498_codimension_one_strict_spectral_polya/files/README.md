# Codimension-one Schatten-to-strict-spectral convergence

Status: candidate_partial_likely_valid

Source target: Priyanka Grover and Krishna Kumar Gupta, “Properties of best approximations with respect to the Ky Fan p-k norm, and the strict spectral approximant of a matrix,” arXiv:2603.07498v2, Conjecture (5).

## Result

The source asks whether the unique Schatten-p best approximimation to a matrix from an arbitrary complex linear subspace converges, as p tends to infinity, to the strict spectral approximant. The full conjecture remains open here. This packet proves it for every complex codimension-one subspace in every finite rectangular matrix space.

Write

    M = {X : tr(G* X) = 0},    G != 0,

and c = tr(G* A). If c = 0, every relevant approximant is A. If c != 0, let

    G = U_r diag(g_1,...,g_r) V_r*,   g_i > 0,
    omega = c/|c|,                    q = p/(p-1).

Then the unique Schatten-p residual is

    A - Y_p = omega |c| U_r diag(g_i^(q-1)) V_r*
              / sum_i g_i^q,

and therefore

    A - Y_p  ->  omega |c| U_r V_r* / sum_i g_i
               = A - Y^(st).

The proof uses equality in Schatten Hölder duality for the finite-p formula. Nuclear/operator duality then shows that every spectral minimizer has a forced r-by-r block omega rho I_r, where rho = |c|/||G||_1. The zero complementary block is consequently the unique lexicographically smallest singular-value vector, hence the strict spectral residual.

This includes rank-deficient G, where ordinary spectral best approximation is genuinely nonunique, so it is not merely the source paper’s unique-spectral-approximant case.

## Files

- main.tex and solution_packet.pdf: proof packet.
- source_paper.pdf: source paper.
- figures/open_problem_crop.png: real crop of the source conjecture.
- code/check_hyperplane_formula.py: randomized numerical consistency check.

## Verification and scope

The proof is self-contained modulo standard finite-dimensional Schatten Hölder duality and its equality case. The numerical checker tested 1,000 random complex hyperplanes of varying rank and several p values; it is supporting evidence only.

Human review should focus on the equality-case step forcing the block diagonal form of all spectral minimizers, and on whether the result overlaps an uncited hyperplane theorem. The unrestricted codimension-two-and-higher conjecture is not claimed.

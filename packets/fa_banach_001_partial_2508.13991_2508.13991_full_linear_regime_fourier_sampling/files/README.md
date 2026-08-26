# Sharp Fourier sampling numbers in the full linear regime

Status: candidate_partial_likely_valid

Source target: Jonathan W. Siegel, “Nearly optimal bounds on the Fourier
sampling numbers of Besov spaces,” arXiv:2508.13991v2. The paper leaves the
correct asymptotics outside s/d > 1 - 1/p open.

## Result

Let K_q^s be the unit ball of the periodic Besov space
B^s_infinity(L_q) on the d-dimensional torus. If

    s/d > max(1/q - 1/p, 0)

and either q >= 2 or p <= q, then

    s_n^F(K_q^s in L_p)
      asymptotic-to n^(-s/d + max(1/q - 1/p, 0)).

Thus the complete linear parameter regime is settled under the sharp
compact-embedding condition, including the smoothness strip omitted from the
source theorem.

The upper bound is obtained by sampling the lowest Fourier modes and applying
the de la Vallee Poussin approximation argument already developed in the
source; that argument only needs the weaker compactness condition. The lower
bound applies to every proposed set of n sampled frequencies. For p <= q, one
unsampled exponential suffices. For q >= 2 and p > q, remove the sampled
frequencies from a block of 2n frequencies and sum the remaining exponentials.
The sum is large on a cube of side comparable to n^(-1/d), while L_2/L_infinity
interpolation controls its L_q norm. After Besov normalization this gives the
matching power of n.

## Files

- main.tex and solution_packet.pdf: complete proof packet.
- source_paper.pdf: source paper.
- figures/open_problem_crop.png: real crop of the source open problem and
  theorem.
- code/check_dense_block_scaling.py: numerical consistency check.

## Verification and scope

The proof is analytic and self-contained modulo standard de la Vallee Poussin
approximation, Besov embedding, and Bernstein’s inequality for trigonometric
polynomials. The numerical script checks representative dense-block witnesses;
it is supporting evidence only.

The nonlinear sector q < 2 and p > q is not settled, nor are the logarithmic
sharpness and Radon-measurement questions. Human review should focus on the
polynomial-to-Besov inverse estimate at q = infinity and on a deeper literature
search for the lower-bound construction.

# Linear asymptotics for the L2 regularity of tile B-splines

Status: **candidate partial result, likely valid**.

Source: T. I. Zaitseva, *Multivariate tile B-splines*, arXiv:2212.12945,
Remark 6 on PDF page 33.

The packet proves that if `alpha_l` is the L2-Hölder regularity of the
`(l+1)`-fold convolution of a normalized tile indicator in `R^d`, then

`(alpha_l + d/2)/(l+1)` is nonincreasing and converges to a constant `L_G`.
Equivalently,

`alpha_l = L_G (l+1) - d/2 + o(l)`.

The regularity sequence is also nondecreasing and discretely concave, so its
marginal gains decrease to `L_G`.  For stable tile B-splines with the usual
exact sum-rule order, `0 <= L_G <= 1`.  A geometric difference estimate gives
`L_G >= 2 alpha_0`.  Thus the open asymptotic question has a general linear
growth law and monotone finite-order bounds without any growing joint-spectral-
radius computation.

This is classified as partial because it does not compute `L_G` for the Dragon
or Bear tiles and does not settle the analogous `C`-regularity asymptotics.

Human review should focus on:

1. identification of the source's L2-Hölder exponent with the supremal
   Sobolev threshold via dyadic annuli;
2. the Hölder-inequality proof that the Fourier integrability boundary is
   concave;
3. use of the standard stability/sum-rule upper bound for tile B-splines;
4. the finite-difference/Young inequality lower bound `L_G >= 2 alpha_0`.

The detailed proof is in `solution_packet.pdf`; the eight upgrade attempts are
recorded at
`runs/fa_banach_001/attempts/2212.12945_tile_b_spline_asymptotics_attempts.md`.


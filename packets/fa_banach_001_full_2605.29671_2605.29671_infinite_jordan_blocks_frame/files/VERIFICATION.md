# Verification record

## Mathematical checks

1. For `a_j=tanh(j+1)`, the pseudohyperbolic identity
   `rho(a_j,a_k)=tanh(|j-k|)` follows from the subtraction formula for
   `tanh`. The Blaschke sum converges and the separation products have the
   uniform lower bound `(product_{r>=1} tanh(r))^2>0`.
2. By the Shapiro--Shields interpolation theorem, the normalized Hardy
   kernels at these zeros form a Riesz basis of `K_b`.
3. The standard orthogonal decomposition
   `K_{b^m}=K_b direct_sum bK_b direct_sum ... direct_sum b^{m-1}K_b`
   makes `{b^r e_j}` a Riesz basis of `K_{b^m}`.
4. Uniformly separated sampling plus the weighted Hardy derivative estimate
   proves that every fixed-order family of normalized derivative kernels is
   Bessel. Each derivative kernel of order below `m` lies in `K_{b^m}`.
5. The cross-Gram operator between `{b^r e_j}` and the derivative kernels is
   a finite upper-triangular block operator. Its `r`th diagonal block is the
   kernel Gram operator multiplied by the invertible diagonal sequence
   `r!((1-|a_j|^2)b'(a_j))^r`. Hence the cross-Gram operator, and therefore
   the derivative-kernel synthesis operator, is invertible.
6. Direct coefficient calculation gives
   `(S^*-conj(a_j))D_{j,s}=s D_{j,s-1}`. Thus every zero yields a root block
   of length exactly `m`. Taking the adjoint in Riesz coordinates transfers a
   Riesz root basis from `S_theta^*` to `S_theta`.
7. For `u=k_0^theta`, Parseval's identity gives
   `sum_n |<f,S_theta^n u>|^2=sum_n |f_hat(n)|^2=||f||^2`.

No numerical or symbolic computation is used in the proof.

## Source and layout checks

- The source paper was downloaded as `source_paper.pdf` and rendered.
- PDF page 17, containing the complete open-question sentence, was cropped
  and visually inspected.
- The packet was compiled with `latexmk` into `tmp/`.
- All packet pages were rendered and visually inspected.
- The final log was checked for undefined references, missing citations,
  overfull boxes, and other layout warnings.

## Novelty boundary

Cheap run indexes and a bounded primary-source arXiv search through 2026-08-12
used arXiv:2605.29671, its exact title, and combinations of “generalized
eigenvectors”, “Riesz basis/sequence”, “model space”, “repeated zeros”,
“derivative kernels”, “interpolating Blaschke product”, and “infinitely many
Jordan blocks”. The search found background work on model-space derivatives
but no exact resolution. This is not exhaustive proof of novelty; specialist
review is required before a priority claim.

## Main reviewer focus

Check the derivative-sampling Bessel lemma and the orientation of the
cross-Gram block matrix. Also preserve the stated normalization caveat: the
result gives infinitely many nontrivial algebraic blocks and a Riesz root
basis, not a uniform similarity to canonical unit-superdiagonal blocks.

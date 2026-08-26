# Maximal rank is not necessary for BBM coercivity

Result type: `counterexample`

Status: candidate full negative answer, likely valid pending expert review.

Source: Luca Gennaioli and Giorgio Stefani, *Sharp conditions for the BBM
formula and asymptotics of heat content-type energies*, arXiv:2502.14655,
question following Theorem 1.2 on source PDF page 3.

## Claimed contribution

The literal maximal-rank necessity question has a negative answer for every
`p in [1,infinity)`, already in dimension two.

Let `kappa_t` be the normalized indicator of the disk `B_t`, let
`v_t=(cos(log(1/t)),sin(log(1/t)))`, and put

`rho_t(z)=2 kappa_t(z) 1_{z dot v_t > 0}`.

For every `u`, the translation-difference integrand defining the BBM energy is
even in `z`. Hence the rotating half-space cut does not change the functional:

`F^{rho}_{t,p}(u)=F^{kappa}_{t,p}(u)`.

The radial family `kappa_t` satisfies the source hypotheses, has maximal rank,
and is coercive by Theorem 1.2; equality therefore transfers coercivity to
`rho_t`. On the sequence `t_k=e^{-k}`, however, the normals `v_{t_k}` have
dense tails on the circle. For every fixed cone of aperture less than a
hemisphere, infinitely many half-spaces exclude that entire cone. Its cone
mass has liminf zero, so `rho_{t_k}` does not have maximal rank.

## Why the mechanism matters

The energy depends only on the even part `(rho_t(z)+rho_t(-z))/2`, while the
source's maximal-rank condition is imposed on the unsymmetrized kernel. The
example makes the even part exactly radial and moves only the energetically
invisible odd allocation of mass.

## Files

- `main.tex`: self-contained theorem and proof.
- `solution_packet.pdf`: rendered expert-review packet.
- `source_paper.pdf`: original arXiv PDF.
- `figures/open_problem_crop.png`: Theorem 1.2 and the necessity question.
- `verification.md`: proof audit and reviewer focus.
- `tmp/`: build and rendering intermediates.

## Novelty check and scope

On 11 August 2026, run indexes and exact-phrase/arXiv searches for maximal
rank, BBM coercivity, and necessity found the source but no later resolution.
The current November 2025 revision of the source still asks the question.

The counterexample answers the stated problem for arbitrary nonnegative
measurable kernels. It deliberately exploits nonsymmetry. The refined question
obtained by requiring every kernel itself to be even is not answered here.

## Human-review recommendation

Check the source's convention for maximal rank along the selected
infinitesimal sequence and confirm that no symmetry hypothesis is imposed on
the kernels. The two central identities to audit are the exact even-part
energy equality and the dense-tail exclusion of every fixed cone.

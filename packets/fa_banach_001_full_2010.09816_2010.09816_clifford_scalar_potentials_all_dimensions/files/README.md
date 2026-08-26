# Clifford scalar potentials and confinement in every dimension

Status: `full_solution_likely_valid`

Source: Gheorghe Nenciu, Irina Nenciu, and Ryan Obermeyer,
*Essential self-adjointness of symmetric first-order differential systems and
confinement of Dirac particles on bounded domains in R^d*, arXiv:2010.09816,
Comment 5 and open problem on PDF pages 34–35.

The packet gives an explicit free Dirac system in every dimension and exactly
classifies the paper's Hermitian scalar potentials for the minimal Hamiltonian
spinor representation.  The answer has a parity dichotomy:

- for even `d`, every scalar potential is `v beta`;
- for odd `d`, every scalar potential is
  `v_1 beta + v_2 i beta Gamma_d`, where `Gamma_d` is the Clifford volume
  element.

The two odd-dimensional mass matrices are anticommuting Hermitian involutions,
so the square of a general scalar potential is `(v_1^2+v_2^2)I`.  In the
paper's standard three-dimensional representation, the second mass is
`-Gamma_12`; thus the two examples displayed in the source span the entire
class.

The packet then specializes the source paper's general coercivity theorem to a
mass-vector criterion, extends its supercritical confinement result to the
full scalar class in every dimension, and proves that the fixed-direction
critical threshold is exactly `|lambda|=1/2` in every dimension.  The positive
result is dimension-free because the proof only uses Clifford relations and
the Hardy inequality.  Sharpness follows on the unit ball from radial channels
with boundary exponents `+lambda` and `-lambda`.  In odd dimensions an exact
unitary gauge formula also handles varying mass direction.

A verifier solves the finite matrix anticommutation systems for `d=1,...,8`,
checks the predicted parity dimensions and mass identities, and verifies the
normal residue spectra.  It is a sanity check, not the proof.

Bounded official-arXiv searches through 2026-08-11 found the source but no later
answer to its exact Comment 5 problem.  Expert review should focus especially
on the standard radial limit-point/limit-circle argument used for sharpness.

Files:

- `solution_packet.pdf`: theorem, proof, source evidence, verification, and scope.
- `main.tex`: packet source.
- `source_paper.pdf`: official arXiv PDF.
- `figures/open_problem_crop_page34.png` and `...page35.png`: exact source question.
- `code/verify_clifford_classification.py`: reusable finite-dimensional checker.
- `code/verifier_report.txt`: command and output.

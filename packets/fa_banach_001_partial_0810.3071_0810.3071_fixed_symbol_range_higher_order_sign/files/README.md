# Higher-order bounded sign: expanded partial result

Status: `partial_result_likely_valid`

This packet answers the higher-order question in arXiv:0810.3071 in four
regimes: the range of the Fourier symbol of `D` is fixed; `D` is semidefinite;
the compression `PBP` to the closure of the range is self-adjoint (in
particular, `B` is self-adjoint); or the active compression has the general
one-sided spectral-triangular form `I+P_+ M_b P_-` (or its lower-triangular
analogue). The last theorem applies to every homogeneous `D` satisfying the
source hypotheses and permits both spectral signs, rotating range, and a
genuinely non-self-adjoint compression.

The new mechanism is a graph-norm proof of the missing off-diagonal estimate.
For dense-range `D`, ellipticity and the bisectorial resolvent estimate control
all intermediate derivatives of the resolvent at the correct scale.
Exponential conjugation is therefore a small graph-norm perturbation even for
order `k>1`. This gives exponential off-diagonal decay, allowing the source
paper's quadratic-estimate theorem and sign proposition to apply. A fixed
symbol range reduces to the dense-range case by a local constant-subspace
compression and two similarities.

The packet also gives an explicit abstract counterexample: a self-adjoint
injective `D0` with dense range and a bounded uniformly accretive `C0` for
which `sgn(C0 D0)` is unbounded. The construction uses an exponentially spaced
spectrum and the bilateral discrete Hilbert transform, whose forced
off-diagonal sign block has an unbounded one-sided logarithmic Fourier symbol.
Thus the full Euclidean question cannot be settled from abstract accretivity;
it must use polynomial homogeneous spectral growth and multiplication
locality.

For the new fourth regime, the spectral graph equation is the linear
Sylvester equation `A_+ X + X A_- = 2 A_+ P_+ M_b P_-`. Its Fourier solution
is bounded by splitting into comparable, high-output, and low-output
frequency regions. These are respectively an ordinary Coifman-Meyer
multiplier, a standard `BMO x L2` high-low paraproduct, and a dyadic series
with a summable scale-ratio gain. The Sylvester identity then supplies an
exact domain-preserving triangular similarity to `diag(A_+,-A_-)`.

The earlier explicit family
`diag(|xi|^(2r), -|xi|^(2r-2) xi xi*)` remains as a concrete corollary; there
the general bundle multiplier collapses to the scalar symbol
`2|alpha+eta|^(2r)/(|alpha+eta|^(2r)+|eta|^(2r))`.

The unresolved core now requires genuinely two-sided coupling between the
positive and negative spectral bundles. In that setting the linear Sylvester
equation becomes a nonlinear Riccati equation, and the available large-
coefficient factorization does not close.

Files:

- `solution_packet.pdf`: theorem, proof, verification, and scope assessment.
- `source_paper.pdf`: locally rendered copy from the exact ingested arXiv TeX
  source (the arXiv PDF endpoint timed out during packet construction).
- `figures/open_problem_crop.png`: source page 2 question and context.
- `main.tex`: packet source.
- `tmp/`: build and rendering files.

Human-review focus: check the exponential-conjugation graph estimate, the
self-adjoint-congruence domain argument, all three frequency regions in the
bundle Sylvester estimate (especially the `BMO` paraproduct), the triangular
domain similarity, and the one-sided harmonic Fourier series in the abstract
no-go theorem. No computational claim is used.

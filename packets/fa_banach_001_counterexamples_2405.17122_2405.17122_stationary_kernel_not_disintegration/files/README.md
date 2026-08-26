# A stationary probability kernel need not be a disintegration

Status: `counterexample_likely_valid`

Source target: Tattwamasi Amrutam, Martin Klötzer, and Hanna Oppelmayer,
*Relative stationary dynamical systems*, arXiv:2405.17122, Proposition 3.12
and Remark 3.13, PDF page 12.

Remark 3.13 asks whether the stationary measurable map
`phi:Y->Prob(X)` supplied by Proposition 3.12 is the disintegration map of
some factor `pi:(X,nu)->(Y,eta)`, where `nu` is the barycenter of `phi`.
The answer is negative, already for finite spaces and trivial actions.

Take `Gamma=Z/2` with its uniform probability measure and trivial actions,
`X` a singleton, and `Y={0,1}` with uniform measure. The only probability
kernel is `phi(y)=delta_*`; it is stationary and its barycenter is
`nu=delta_*`. But no map from a one-point probability space can push `nu`
forward to the uniform law on `Y`, so there is no factor map at all.

The packet also gives a non-cardinality variant: take `X=Y={0,1}` uniformly
and let `phi(y)` be uniform on `X` for both `y`. Factor maps exist, but every
measure-preserving map is a bijection and has Dirac conditional measures,
not the constant uniform kernel. Thus stationarity plus the barycenter
identity does not impose the fiber-support property required of a
disintegration.

A bounded official-arXiv search through 11 August 2026 found no later answer
to this exact remark. The counterexample answers the literal question; it
does not classify additional hypotheses that might force a stationary kernel
to arise from a factor.

Files:

- `solution_packet.pdf`: exact question, counterexamples, and scope notes.
- `main.tex`: packet source.
- `source_paper.pdf`: official arXiv PDF.
- `figures/open_problem_crop.png`: Proposition 3.12 and Remark 3.13.

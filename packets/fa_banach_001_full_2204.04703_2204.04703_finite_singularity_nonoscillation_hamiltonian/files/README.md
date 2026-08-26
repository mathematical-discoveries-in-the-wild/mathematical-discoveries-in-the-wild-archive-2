# 2204.04703 — finite-singularity nonoscillation

## Outcome

Candidate full proof of the conjecture on page 10 of Boulton--Lang,
arXiv:2204.04703.

For every \(p,q>1\) and \(\lambda>0\), a finite maximal singularity of the
associated four-dimensional system is necessarily nonoscillatory.  All four
components have fixed signs near the singular time, their absolute values
tend to infinity, and the \(u\)-components have the opposite sign from the
corresponding \(w\)-components.

The proof works for arbitrary initial states, so it is stronger than the
paper's shooting initial condition.

## Key identity

Writing \(p'=p/(p-1)\) and
\(\Phi_r(s)=\operatorname{sgn}(s)|s|^{r-1}\), the system is

\[
 u_1'=u_2,\qquad u_2'=-\Phi_{p'}(w_1),\qquad
 w_1'=w_2,\qquad w_2'=-\lambda\Phi_q(u_1).
\]

It has the conserved Hamiltonian

\[
 H=u_2w_2+\frac{|w_1|^{p'}}{p'}+
      \frac{\lambda|u_1|^q}{q}.
\]

At a zero of either derivative component, \(H\) becomes a sum of
nonnegative terms and uniformly bounds both position components.  If such
zeros accumulated at a finite endpoint, the whole state would be bounded and
the solution would extend past the endpoint.  Rolle's theorem then excludes
accumulating zeros of the position components as well.  Fixed signs force
monotonicity, and boundedness of any one component propagates around the ODE
cycle, so every component must diverge with the claimed sign pattern.

## Files

- `main.tex` — exact source transcription, theorem, proof, verification, and
  novelty audit.
- `solution_packet.pdf` — compiled packet for specialist review.
- `source_paper.pdf` — arXiv source paper.
- `figures/open_problem_crop.png` — exact conjecture on source page 10.
- `tmp/` — build and rendered-page artifacts.

## Human review

A specialist should check the interpretation of equation (11) as equality of
extended-real limits (an opposite-sign assertion, not equality of finite
blow-up rates) and independently verify the continuation argument for the
paper's chosen solution convention.  The proof uses only continuity of the
vector field at exponents below 2, so no Lipschitz assumption at the origin is
needed.


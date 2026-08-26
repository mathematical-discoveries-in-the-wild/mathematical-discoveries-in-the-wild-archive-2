# A two-state counterexample to Erbar--Fathi Conjecture 6.9

Status: candidate full counterexample, likely valid, human review required.

Source: Matthias Erbar and Max Fathi, “Poincaré, modified logarithmic
Sobolev and isoperimetric inequalities for Markov chains with non-negative
Ricci curvature,” arXiv:1612.00514, JFA 274 (2018), 3056–3089.

Conjecture 6.9 is false in its intended quantitative form. For
0 < p <= 1/4, take the two-state continuous-time chain

Q(0,1)=p, Q(1,0)=1-p, pi=(1-p,p).

Its spectral gap is exactly 1 and its entropic Ricci curvature is at least
1/2. If D_p is the intrinsic entropic-transport distance between the two
states, then

D_p^2 <= 49 log(1/p).

The invariant law has exponential concentration with M=1 and rate
rho_p=log(1/p)/D_p. Therefore rho_p^2 >= log(1/p)/49 tends to infinity,
while the spectral gap remains 1. No positive universal C(1) can give
lambda >= C(1) rho_p^2.

The source PDF prints P(C(M) rho^{-2}), although its dimensional context
and the later explicit restatement in arXiv:2309.06493 use the intended
lambda >= C(M) rho^2 form. The literal printed version is also false:
uniform time rescaling makes it fail for any fixed two-state example.

The packet does not resolve Conjecture 6.10.

Files:

- solution_packet.pdf — review-ready proof packet
- main.tex — packet source
- source_paper.pdf — original source paper
- figures/open_problem_crop.png — full Conjectures 6.9–6.10 source crop
- code/verify_two_point.py — numerical regression, not part of the proof
- code/crop_open_problem.py — reproducible source crop

Human review should focus on the one-dimensional transport tensor and on the
interpretation of the source’s apparent sign typo. The counterexample proves
both interpretations false, so the final verdict does not depend on choosing
between them.


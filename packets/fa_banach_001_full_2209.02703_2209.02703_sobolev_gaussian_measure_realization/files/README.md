# Every Sobolev Gaussian measure has a measurable process realization

Status: solution_likely_valid

Source target: Iain Henderson, *Sobolev regularity of Gaussian random
fields*, arXiv:2209.02703, concluding open question (ii), PDF page 29.

The answer is affirmative. Let mu be any Gaussian probability measure on
W^{m,p}(D), where m is a nonnegative integer and 1 <= p < infinity.
Push mu forward through the canonical continuous injection

J:W^{m,p}(D) -> L^p(D).

The result is Gaussian on L^p. The paper's Proposition 2.9 realizes it as
the law of the L^p sample classes of a jointly measurable Gaussian process.
The only hidden issue is recovering the stronger Sobolev-valued law. Since
the two spaces are Polish and J is continuous and injective,
Lusin--Souslin says that J(W^{m,p}) is Borel and that its inverse is Borel.
The process lies in this image almost surely, and applying the inverse
gives a W^{m,p}-valued Borel random element with law exactly mu.

The proof handles noncentered measures by translation, includes p=1, and
extends verbatim to every separable Banach function space continuously
injected into an L^p space for finite p.

The packet also gives a precise answer to the nuclear-norm suggestion in
question (i): nuclear norm alone cannot determine Sobolev small-ball
probabilities. Two Gaussian laws can have covariance trace one but
small-ball orders epsilon and epsilon^2. Even identical covariance
eigenvalues on the underlying L^2 space do not determine H^1 small-ball
probabilities, because the Sobolev geometry of the eigenfunctions matters.

Files:

- solution_packet.pdf: source question, full realization proof, abstract
  extension, and exact small-ball obstructions.
- main.tex: packet source.
- source_paper.pdf: official arXiv PDF.
- figures/open_problem_crop.png: concluding open questions (i)--(ii).
- code/verify_small_ball_examples.py: checks of the exact probability
  formulas.
- code/crop_open_problem.py: reproducible source crop.

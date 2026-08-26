# A sharp uniform noise bound for interpolating oblique reconstructions

Status: candidate_full_solution_likely_valid

This packet answers the explicit request immediately after Lemma 3.8 of
arXiv:1706.06444 for a meaningful bound on the operator norm of the
interpolating reconstruction Q_lambda.

If the sampling frame has lower frame bound A and
c = cos(phi_{T,U}) > 0, then for every lambda in [0,1],

    ||Q_lambda|| <= 1 / (sqrt(A) c).

The constant is optimal using only the frame bounds, the subspace angle, and
lambda: a three-dimensional example attains equality simultaneously for
every lambda and for arbitrary prescribed 0 < A <= B and 0 < c <= 1.
Thus the best universal bound has no possible favorable dependence on
lambda or on the upper frame bound B.

The proof restricts the data preconditioner to the closed range of the frame
analysis operator. Its norm contributes
(lambda+(1-lambda)A)^(-1/2), while the lower bound for the weighted analysis
map on the reconstruction space contributes the reciprocal factor. They
cancel exactly.

Files:

- main.tex: theorem, proof, exact sharpness construction, and scope.
- solution_packet.pdf: rendered proof packet.
- source_paper.pdf: arXiv:1706.06444.
- figures/open_problem_crop.png: source PDF page 16, Lemma 3.8 and question.
- code/verify_bound.py: randomized matrix checks and exact equality tests.
- tmp/: build and render intermediates.

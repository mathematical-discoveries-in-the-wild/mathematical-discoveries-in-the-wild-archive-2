# Complex centered Lp moments are not strongly Leibniz below two

This packet gives a full negative answer to the literal complex-valued
strong-Leibniz question in arXiv:1409.1207. For every fixed 1<=p<2, an
explicit one-parameter family of invertible random variables on the uniform
three-point probability space eventually violates the strong inverse
inequality.

At p=1, the rational-complex vector

f=(1,(24-7i)/25,(26+7i)/25)

already works. Its inverse centered moment is strictly larger than its
centered moment, while ||f^{-1}||_infinity=1.

The result does not address the surviving real-valued strong-Leibniz
conjecture or complex p>2. It is consistent with the known p=2 theorem.

Status: candidate_counterexample_likely_valid, pending human review.

Files:

- main.tex: exact question, all-p<2 family, explicit witness, and boundary.
- solution_packet.pdf: compiled review packet.
- source_paper.pdf: official source arXiv PDF.
- supporting_paper_1601.00440.pdf: official follow-up arXiv PDF.
- figures/open_problem_crop.png: source's open question on PDF page 2.
- code/verify_family.py: exact symbolic family and radical checks.
- VERIFICATION.md: proof, literature, build, visual-QA, and hash record.

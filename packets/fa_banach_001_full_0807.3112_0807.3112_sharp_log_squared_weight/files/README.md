# Sharp log-squared weighted Poincare threshold

Candidate full answer to the question in Example 2.28 of arXiv:0807.3112.

For

    d mu_q(x) proportional to dx / ((2+|x|) log^q(2+|x|)), q>1,

the weighted Poincare inequality with

    W_beta(x) = 1 + x^2 log^beta(2+|x|)

holds exactly for `beta >= 2`. More generally, any eventual
`o(x^2 log^2 x)` weight fails, while any positive weight eventually bounded
below by a multiple of `x^2 log^2 x` works. The proof computes the exact
one-dimensional Muckenhoupt product and gives explicit truncated Hardy
near-extremizers.

The review artifact is `solution_packet.pdf`; the proof source is `main.tex`.
The source question is preserved as the directly rendered PNG crop
`figures/source_question_page12.png`, extracted from `source_paper.pdf`.

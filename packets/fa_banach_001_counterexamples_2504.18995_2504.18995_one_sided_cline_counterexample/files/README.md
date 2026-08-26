# One-sided Cline-formula counterexample

This packet gives a full negative answer to Question 3.10 of arXiv:2504.18995.

## Result

In `B(ell^2)`, let `D e_n=e_(2n)` and let the diagonal operator `C` have
weight one on even coordinates and weight `1/n` on coordinate `2n-1`.
Then `CD=D` is left invertible, while `DC` is not even left generalized
Drazin invertible. Taking adjoints gives the right-sided failure. Thus Cline
closure fails for left and right Drazin invertibility and for left and right
generalized Drazin invertibility.

## Files

- `solution_packet.pdf`: review-ready proof.
- `main.tex`: packet source.
- `source_paper.pdf`: official arXiv source PDF.
- `figures/open_problem_crop.png`: source Question 3.10.
- `VERIFICATION.md`: proof, literature, and visual-QA record.

## Review focus

Check the algebraic obstruction lemma and the formula `(DC)^m=D^m C`. A
later paper's purported counterexample is separately flagged because its
reversed shift actually is left Drazin invertible; the present construction
does not rely on that paper.

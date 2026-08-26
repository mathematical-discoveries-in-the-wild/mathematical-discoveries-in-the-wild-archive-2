# UEP does not force a characteristic sequence: a sharp matrix-size threshold

This packet gives a candidate full negative answer to Question 1 in the “Characteristic sequences” section of arXiv:1709.01649.

For a pure vector state on `M_d` with rank-one support `p`, a characteristic sequence contained in an operator system `S` exists exactly when `p` belongs to `S`. The packet then proves:

- in `M_1` and `M_2`, the unique extension property forces `p` to belong to `S`, so the answer is affirmative;
- in every `M_d`, `d >= 3`, the operator system
  `S = {a : Tr(diag(1,1,-2,0,...,0) a)=0}`
  gives a counterexample for the state `a -> a_11`.

Thus the original unrestricted question is false already in the separable finite-dimensional algebra `M_3`, and dimension three is the first full matrix algebra in which this can happen.

Files:

- `main.tex`, `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: arXiv:1709.01649.
- `figures/open_problem_crop.png`: readable crop of the source question on PDF page 18.
- `tmp/`: build and rendering artifacts.

Novelty confidence is moderate. A bounded primary-source search found related work on pure-state restrictions and excision, but no explicit answer to this exact question or this matrix threshold. Mathematical validity is independent of that search because the proof is elementary and self-contained.

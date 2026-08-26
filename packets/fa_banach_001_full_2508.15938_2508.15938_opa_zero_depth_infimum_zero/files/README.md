# Degree-one OPA zero depth is zero

This packet gives a candidate full solution to the quantitative zero-depth
question for degree-one optimal polynomial approximants (OPAs) in
`H^2(D^2)`, asked on pages 13--14 of arXiv:2405.16943 and revisited on page
8 of arXiv:2508.15938.

Main result: for every `epsilon > 0` and each of the `l1`, `l2`, and
`l-infinity` norms, there is a polynomial `F`, nonvanishing on the closed
bidisk, whose degree-one OPA to `1/F` has a zero at norm less than
`epsilon`. Thus the sharp universal zero-exclusion radius is zero for all
three norms.

The construction concentrates the boundary probability measure `|F|^2`
near two almost co-rotating torus points. The limiting OPA is the affine
function vanishing at both points, whose coefficients grow linearly with
the codebook parameter `m`. Its exact zero depths are asymptotic to
`1/m`, `1/(sqrt(2)m)`, and `1/(2m)`. Uniform Taylor approximation upgrades
the zero-free entire construction to zero-free polynomials.

Files:

- `solution_packet.pdf`: final self-contained proof packet;
- `main.tex`: packet source;
- `source_paper.pdf`: official arXiv:2508.15938 PDF;
- `question_source_2405.16943.pdf`: official arXiv:2405.16943 PDF;
- `figures/question-13.png`, `figures/question-14.png`, and
  `figures/target-8.png`: complete visually inspected source pages used in
  the packet;
- `code/verify_two_point_construction.py`: exact finite-relation and depth
  checker;
- `verification.md`: proof, source, novelty, build, and render audit.

Status: candidate full solution, likely valid. Novelty confidence is
moderate because the primary-source search was bounded.


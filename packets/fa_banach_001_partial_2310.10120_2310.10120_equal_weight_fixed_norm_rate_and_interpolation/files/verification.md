# Verification

## Proof audit

- The source Fourier identity is used only for the zero-mass measure
  `mu_N - f dx`, with equal atomic weights and `integral f = 1`; its multiplier
  is comparable to the inhomogeneous `H^{-(d+1)/2}` norm on the torus.
- Positivity gives `(sum a_j)^u >= sum a_j^u`, so collisions among the sample
  points can only increase the smoothed empirical `L^u` norm.
- In Young's inequality, `1 + 1/u = 1/p + 1/v`, hence
  `||phi_h||_v` scales as `h^{-d(1/p-1/u)}`.
- The balancing identity
  `theta_u - (1/p - 1/u) = 1/q` was checked directly.
- The multiplier estimate for convolution follows by rapid Fourier decay and
  gives the critical factor `h^{-(d+1)}`.
- At `u=2`, the exponents reduce to the source bound. At `u=p`, they reduce to
  `N^{-1-1/d} F^{-(q-2)-q/d}`.
- For the upper construction, `f = F^q 1_Q` on a cube of volume `F^{-q}` has
  mass one and `L^p` norm exactly `F`. Centered independent cell samples have
  vanishing Hilbert-space cross terms.
- The bound
  `||delta_x-delta_y||_{H^{-(d+1)/2}}^2 <= C|x-y|` follows by splitting the
  Fourier sum at frequency `|x-y|^{-1}`; this yields the matching fixed-norm
  power along `N=H^d`.
- In the arbitrary-weight construction, `alpha_1=sqrt(N)` gives normalized
  weight norm one and total atomic mass `N^{-1/2}`. The approximate-delta
  Fourier tail is comparable to `N^{-1}h`, exactly matching every exponent in
  the source formula.

## Literature and scope audit

- Exact-title, exact-phrase, author, DOI, and citation searches through
  13 August 2026 did not locate a full resolution of the arbitrary-`L^p`
  equal-weight joint-exponent question.
- Colasanto--Focardi--Fornasier--Mattesini, arXiv:2605.18497v2, prove the
  squared energy-distance rate `N^{-1-1/d}` for `d`-Ahlfors regular targets.
  This supports the fixed-norm endpoint in a regular subclass but does not
  settle the `L^p` norm dependence here.
- Bramati--Brandolini--Travaglini, arXiv:2607.22819, study a different
  randomized jittered-sampling functional; it does not answer the target.
- The packet therefore claims a candidate partial result for the intended
  equal-weight problem and a complete observation only for the theorem read
  literally with arbitrary nonnegative weights.

## Artifact checks

- `source_paper.pdf` SHA-256: `951036445fa27a7e2c1319458c5f03ca18784271088213c52f00af7e07221246`.
- `supporting_2605.18497.pdf` SHA-256: `980d02870b041d706ca8627141793fadfadbfca51fd8962e1a35021a7291b87b`.
- `figures/open_problem_crop.png` SHA-256: `c05b2bbb693b6cfe37966b0b5d61022a2c77522b5b57f8492ee6312ad87a8ce4`.
- `solution_packet.pdf` SHA-256: `946207de3234212b2036d0306f6f0f4a30c36aea50e452dcb1f9676a4150a14b`.
- `latexmk` completed with no unresolved-reference, overfull-box, underfull-box,
  or substantive warning.
- The five-page PDF was rendered at 150 dpi. Every page was visually inspected;
  equations, theorem blocks, the source crop, proof endings, references,
  margins, and page breaks are clean.

# Triangle-Gaussian convolution is extremal

Route: arXiv:1803.06409 records the open extreme-ray classification problem
and cites arXiv:0801.0941.  Question 3 of the cited paper asks whether the
triangular extremal `f=(1-|x|)_+` convolved with `gamma=exp(-pi x^2)` remains
extremal.

Result: yes.  Gaussian deconvolution plus a critical
Phragmen--Lindelof/Paley--Wiener support lemma forces every interval component
back into `[-1,1]`; the double sinc-square zeros then force scalar
proportionality.  Together with the existing run packet proving that
`gamma(f*gamma)` is not extremal, this settles both clauses of Question 3.

Files:

- `solution_packet.pdf` — final self-contained proof packet.
- `main.tex` — packet source.
- `source/1803.06409.pdf` — official arXiv routing-source PDF.
- `source/0801.0941.pdf` — official arXiv exact-question PDF.
- `source/route_open_problem_page9.png` — real routing-passage crop.
- `source/question3_page18.png` — real exact-question crop.
- `VERIFICATION.md` — mathematical, source, rendering, and hash audit.

Complementary existing packet:
`runs/fa_banach_001/solutions/counterexamples/0801.0941_gaussian_triangle_product_not_extremal`.

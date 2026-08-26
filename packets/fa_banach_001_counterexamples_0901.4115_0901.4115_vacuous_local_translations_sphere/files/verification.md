# Verification record

## Mathematical audit

1. The normalized surface measure on `S^(d-1)` is a Borel probability and
   has support exactly `S^(d-1)`.
2. `U(t)=I` is a strongly continuous unitary representation of `R^d`.
3. If `t != 0`, then `S^(d-1) intersect (S^(d-1)-t)` lies in the affine
   hyperplane `x dot t = -|t|^2/2`; it therefore has `(d-1)`-dimensional
   surface measure zero.
4. Hence every admissible `O` and `O+t` has `mu`-measure zero for `t != 0`,
   while the required identity is tautological for `t=0`.
5. Theorem 1.1 of arXiv:1905.07032 says surface measure on the smooth boundary
   of a convex body with everywhere positive Gaussian curvature admits no
   Fourier frame.  The unit sphere meets the hypotheses.  Normalization by a
   positive scalar does not change frame existence.
6. An orthonormal basis of exponentials is a Fourier frame with frame bounds
   `1,1`, so the sphere measure is not spectral.

## Computational and artifact audit

Run:

```text
conda run --no-capture-output -n sandbox python code/verify_geometry.py
conda run --no-capture-output -n sandbox python code/make_crop.py
```

The exact source question is on PDF page 3.  Both cited PDFs are primary
arXiv artifacts.  The final packet is compiled from `main.tex`, rendered page
by page, and visually inspected.

## SHA-256 hashes

- `solution_packet.pdf`: `2493471f5475c38a5ea9c54ba0a251b782966de04b11ba981ee0475bcdc7243a`
- `source_paper.pdf`: `bb66ffee06a82c3031610d9dff896b7e293c8a5de03ae69c675435877443cef6`
- `supporting_paper_1905.07032.pdf`: `b4c058af60c0d800cfa8ced0f38d484ed71773457da8e5e7113850f496eba36e`
- `figures/local_translation_question_crop.png`: `b2b8d81231fafb544f1c9fedecdf4c6d6fccf7ba603d4de1c17f5eabcd24fb23`
- `code/make_crop.py`: `c3b70138db72746334165f12079eaeb7c8a4cd678ce0a50d8c5c60800ec5497d`
- `code/verify_geometry.py`: `543b5bae6073eeee676568ebb1afd48628fcf28d6b9871c6a6ac6e016e044d56`


# Verification notes

- Original PDF: arXiv:2009.10274, 24 pages. The exact challenge is on PDF page
  8, Remark 2(2).
- Supporting PDF: arXiv:2208.12407, 15 pages. The exact affirmative statement
  and proof are Theorem 4.1 on PDF page 6.
- Text-source cross-check: supporting `SpectralMean.tex`, Section
  `Geodesic property`, states the formula for all real `s,t`.
- Independent proof check: if `C=A^{-1}#B` and `X_u=C^u A C^u`, then
  `C^(t-s) X_s C^(t-s)=X_t`. Uniqueness in the Riccati characterization of
  `X_s^{-1}#X_t` gives `X_s^{-1}#X_t=C^(t-s)`, and functional calculus gives
  the norm identity.
- Novelty verdict: exact later literature answer, not a new run result.

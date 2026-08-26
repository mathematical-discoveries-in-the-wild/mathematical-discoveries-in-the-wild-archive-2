# Verification report

## Algebraic reduction

- [x] Checked `alpha(nu)=(2nu-1)^2=49/100` at `nu=17/20`.
- [x] Checked `A^(1/2) X B^(1/2)=T` for `X=A^(-1/2)TB^(-1/2)`.
- [x] Checked the entrywise identities `Y_ij=cosh(s(h_i-k_j))T_ij` and `Z_ij=cosh(h_i-k_j)T_ij`.
- [x] Checked the real `2×2` trace-norm identity `||M||_1^2=||M||_F^2+2|det M|`.

## Exact certificate

Run:

`conda run --no-capture-output -n sandbox python verify_counterexample.py`

The verifier uses only `fractions.Fraction` for every assertion. It encloses each hyperbolic cosine by a 24-term rational Taylor interval with a geometric tail bound. Certified conclusions:

- `||Y||_1 > 1.178`;
- `||T||_1 < 1.1402`;
- `||Z||_1 < 1.2153`;
- conjectured RHS `< 1.176999`;
- strict final gap `> 1001/10^6`.

## Source and novelty checks

- [x] Compared the target PDF to Zou's original 2013 PDF and isolated the crossed-exponent transcription error.
- [x] Checked a related 2018 primary paper and bounded exact-formula/title/citation searches.
- [x] Cheap run indexes contain no duplicate for arXiv:1709.09813 or the conjecture.

## Artifact checks

- [x] LaTeX compiled without errors or warnings.
- [x] No overfull/underfull boxes or undefined references remain.
- [x] Extracted PDF text contains the theorem, explicit matrices, and certified inequalities.
- [x] Every rendered page was visually inspected (four pages; pages 2--3 were re-rendered and rechecked after a typography correction).
- [x] File types, page count, and SHA-256 were recorded.

The final packet is a four-page, US-letter PDF 1.7.  SHA-256 values:

- `solution_packet.pdf`: `cbb55ee874ba45d28195867fb3296a451c00ac5d9740d9a481e4718d9bd3a2a1`
- `source_paper.pdf`: `8caa8e20bbe1dc3a828c35ad1c7c51e870c591ad4c4d379f8a398789847140e4`
- `supporting_zou_2013.pdf`: `85e7d97f1e3f23aad25f27cbf936da34e27592d8fb407441bd4a3199532c00bf`
- `supporting_gao_ma_2018.pdf`: `5794e5d6a91e8c4113a207500c74c2dd58442c646933f841a6f4c26aa30e2442`

## Human review

- [ ] Human expert review completed.

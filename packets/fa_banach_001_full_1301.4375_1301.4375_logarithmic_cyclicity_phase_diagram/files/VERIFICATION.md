# Verification report

## Claim audited

For

`D_alpha = {sum a_n z^n : sum (n+1)^alpha |a_n|^2 < infinity}`,

every `f` with `f, log f in D_alpha` is cyclic if and only if
`alpha >= 0`.

## Source checks

1. The exact question is Problem 3 in Section 4 of arXiv:1301.4375.
2. The source proves the cases `alpha>1`, `alpha=0`, and `alpha=1`, and
   leaves an extra approximation hypothesis in the other cases.
3. arXiv:2409.20298 explicitly includes standard `D_alpha`,
   `0<=alpha<=1`, among superharmonically weighted Dirichlet spaces; its
   Theorem 1.1 says that outer `g` with `log g in N^+(D(mu))` is cyclic.
   The same paper records `D(mu) subset N^+(D(mu))`.
4. arXiv:2504.05208 states the Korenblum--Roberts characterization for
   singular inner functions in the coefficient spaces
   `ell_A^{2,alpha}=D_alpha`, `alpha<0`, and Theorem 6.3 constructs a
   nonzero positive singular measure supported on a Beurling--Carleson set
   whose Fourier coefficients lie in `ell^p` for every prescribed `p>2`.
5. The publisher's correction of 23 March 2026 only restores a missing
   factor `t` in an integral on page 12.  It does not affect Theorem 6.3 or
   any result used in this packet.

## Positive-range proof audit

- If `0<=alpha<=1`, then `D_alpha subset H^2`, so
  `q=log f in H^2 subset H^1`.
- The standard analytic-log mean-value criterion makes `f` outer.
- Complete-Pick Smirnov inclusion gives `q in N^+(D_alpha)`.
- Aleman--Richter then gives cyclicity.
- If `alpha>1`, weighted `ell^2` convolution makes `D_alpha` a Banach
  algebra.  Thus `exp(-q)=1/f in D_alpha`; polynomial approximation and
  continuity of multiplication by `f` give cyclicity.

## Negative-range proof audit

Fix `alpha<0`.

- For `-1<alpha<0`, the interval `(2,2/(1+alpha))` is nonempty.  Any `p`
  in it satisfies `alpha*p/(p-2)<-1`.
- For `alpha<=-1`, every `p>2` satisfies the same strict inequality.
- With `r=p/2` and `r'=p/(p-2)`, Hölder gives

  `sum (n+1)^alpha |muhat(n)|^2`

  `<= (sum |muhat(n)|^p)^(2/p)`

  `   * (sum (n+1)^(alpha*p/(p-2)))^((p-2)/p) < infinity`.

- Expanding the Herglotz kernel shows that the nonconstant Taylor
  coefficients of `log S_mu` are `-2 muhat(n)` (up to Fourier convention),
  so `log S_mu in D_alpha`.
- Since `S_mu` is inner, `S_mu in H^2`; because `alpha<0`,
  `H^2 subset D_alpha`.
- The support `E` is Beurling--Carleson and `mu(E)=mu(T)>0`.  The
  Korenblum--Roberts iff criterion therefore makes `S_mu` noncyclic.

## Independent cross-check

Dayan--Seco's proof quotes a Salem measure with
`muhat(n)=O(n^{-s/2+epsilon})` on a Beurling--Carleson support.  Choosing
`s-2 epsilon>1+alpha` yields direct convergence of
`sum n^{alpha-s+2 epsilon}`.  This independently verifies the weighted
Hölder route.

## Search and novelty audit

The run's cheap indexes contain no exact prior packet or ledger.  Exact-title
and exact-phrase searches found the source and both supporting papers but no
paper stating the full phase diagram verbatim.  The packet therefore labels
the result a candidate full solution and explicitly identifies the negative
half as a short synthesis from later published ingredients.

## Artifact QA

- `main.tex` was compiled with two successful `pdflatex` passes.
- `main.log` contains no undefined-reference, overfull-box, underfull-box, or
  multiply-defined-label warning after the second pass.
- `solution_packet.pdf` has 4 letter-size pages and opens as PDF 1.7.
- Ghostscript `txtwrite` extraction recovered the complete theorem, all six
  numbered displays, and all seven bibliography entries.
- All four pages were rasterized at 140 dpi with `pdftoppm` and visually
  inspected.  Equations, links, theorem text, page breaks, and references are
  legible; there is no clipping or overlap.
- The source and two supporting arXiv PDFs open successfully.  The official
  correction PDF reports one page in `pdfinfo` and was separately inspected.
- SHA-256 of the final packet:
  `6249c8359615b00fda3f5400f64c98c22f55cbfa4ec19ea9f6a286615d52b025`.

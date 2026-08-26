# Verification notes

Status: `likely valid`; recommended for expert review.

## Line-by-line audit

1. **Coefficient map.** For a discrete crossed product
   `N = Gamma_q(H) rtimes_alpha G`, the canonical expectation onto
   `Gamma_q(H)` is faithful and normal. Hence
   `C_s(z) = E_Gamma(z(1 rtimes lambda_s)^*)` is normal.
2. **Polynomial coefficient formula.** Multiplication in the crossed product
   gives `C_s(a rtimes lambda_t) = delta_{s,t} a`; no action term survives
   because the second coefficient is the identity.
3. **Input convergence.** `x -> tau_G(x lambda_s^*)` is a normal functional,
   so weak-* convergence of `x_i` to zero forces every scalar Fourier
   coefficient `x_{i,s}` to zero.
4. **Gradient coefficient.** The defining source formula
   `partial(lambda_s) = s_q(b_psi(s)) rtimes lambda_s` gives the asserted
   coefficient exactly.
5. **Uniqueness.** The finite crossed product has the orthogonal decomposition
   `L^2(N) = direct_sum_s L^2(Gamma_q(H)) lambda_s`. A bounded `y in N` lies
   in `L^2(N)`, so vanishing of all `C_s(y)` implies `y=0`.
6. **Topological strength.** Every step is valid for arbitrary nets, not just
   sequences.
7. **Hypotheses.** Neither AP nor countability of `G` is used. The restriction
   `-1 <= q < 1` is unchanged from the source proposition.

No computational experiment is relevant or used.

## Potential failure modes checked

- Coefficient extraction is onto the base algebra `Gamma_q(H)`, not the
  different conditional expectation onto `VN(G)` used elsewhere in the
  source.
- The coefficient convention uses right multiplication by
  `(1 rtimes lambda_s)^*`; with this convention the coefficient of
  `a_t rtimes lambda_t` is exactly `a_s`.
- The proof does not assume convergence of Fourier series in operator norm.
  It uses only normal coefficient maps and the Hilbert-space Fourier
  decomposition.
- The claim does not include `q=1`, where the classical Gaussian variable is
  generally unbounded and the displayed map is not a von-Neumann-algebra-valued
  operator of the same kind.

## Bounded novelty/literature search

Search date: 11 August 2026.

Sources searched:

- the run's solution, attempt, proof-gap, and ledger indexes;
- arXiv:1903.10151v9 full source and arXiv metadata/citation links;
- web searches for the exact Remark 3.13 sentence and label;
- combinations of `weak* closable`, `Gamma_q`, `crossed product`, `gradient`,
  `AP`, and the authors/title;
- the public record for the authors' 2022 Springer Lecture Notes volume based
  on this work.

No later paper or book excerpt explicitly removing AP from Proposition 3.12
was found. This is a bounded negative search, not proof of novelty.

## Human-review recommendation

Check the coefficient convention and the `L^2` uniqueness step against the
source's crossed-product representation. If those standard facts match the
notation—as they appear to—the proof completely resolves Remark 3.13.

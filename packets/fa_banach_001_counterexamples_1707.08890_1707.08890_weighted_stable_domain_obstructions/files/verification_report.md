# Verification report — 1707.08890 weighted stable-domain obstructions

Verdict: `likely valid pair of full scoped counterexamples; human review needed`.

## Exact scope

The source asks about extending a symmetric small-characteristic-function
theorem to the attraction domain of a fixed stable distribution. The packet
separates two broad readings:

- unrestricted fixed stable targets, refuted inside a nonsymmetric strict
  normal domain;
- symmetric balanced regularly varying tails, refuted in the general stable
  domain when the slowly varying factor is nonconstant.

It does not claim that the slow-variation construction refutes a strict
symmetric normal-domain formulation.

## Adversarial checks: sign counterexample

1. **Stable input.** A positive strictly `1/2`-stable law satisfies
   `X_1+...+X_m =_d m^2 X` and is in its own strict normal domain.

2. **Coefficient condition.** For signs `a_k=+-1`, the source norm is
   `A_N=(sum |a_k|^(1/2))^2=N^2`, hence `max |a_k|/A_N=N^-2 -> 0`.

3. **Oscillating limits.** Alternating blocks that dominate their entire past
   force the positive-sign proportion to tend alternately to one and zero.
   Exact stable scaling gives endpoint limits `X` and `-X`.

4. **Centering cannot repair skewness.** Positive affine transforms of `X`
   are bounded below; positive affine transforms of `-X` are bounded above.
   The convergence-of-types lemma rules out a shared nondegenerate limit under
   arbitrary positive normalizers and centerings.

5. **Subsequence quantifier.** The base sequence is iid. Every selected
   subsequence is again iid with the same constant limit random measure, so
   the coefficient example applies to every subsequence.

## Adversarial checks: slowly varying counterexample

1. **Valid law.** Placing the unused mass at `e` makes
   `P(R>x)=1/(x log x)` for `x>=e` a probability tail. Multiplying by an
   independent symmetric sign gives balanced tails.

2. **Attraction domain.** The tail is regularly varying with exponent `-1`.
   With `b_m log b_m=m`, the symmetric iid sums divided by `b_m` converge to a
   symmetric `1`-stable law. In particular they are tight.

3. **Not itself stable.** Its tail factor `1/log x` tends to zero. No
   non-Gaussian stable distribution has that tail, and the law is not Gaussian.

4. **Recursive feasibility.** Before choosing `m_j`, the preceding weighted
   sum is fixed in law. Since `w_{j-1}m/sqrt(log m) -> infinity`, `m_j` can be
   chosen to make the preceding sum `o_P(w_j)` and `1/sqrt(log m_j) < 1/j`.

5. **Global coefficient condition.** During each repeated block the
   max-to-total ratio decreases. At the new coefficient it is at most
   `1/sqrt(log m_j)`. This covers every index, not only block endpoints.

6. **Fresh block is negligible.** Its probabilistic scale is
   `w_{j-1} b_{m_j}`, whose ratio to
   `w_j=w_{j-1}m_j/sqrt(log m_j)` is asymptotic to
   `1/sqrt(log m_j)`.

7. **Endpoint limit.** Old stages and the fresh repeated block are
   `o_P(w_j)`, leaving the final term `w_j X_j^*`; therefore `T_j/w_j ->_d X`.

8. **All normalizations ruled out.** If centered/rescaled endpoints converged
   to a nondegenerate stable law, convergence of types would make that law an
   affine transform of the nonstable `X`, a contradiction.

9. **Subsequence quantifier.** As in the first example, iid invariance makes
   the construction independent of which subsequence the source theorem
   selects.

## Residual review risk

The largest risk is interpretive, not algebraic. In strict terminology the
published phrase “normal attraction” excludes the nonconstant factor in the
second example. The first example still applies strictly but uses a
nonsymmetric target. Reviewers should decide which of these readings the
authors intended. The packet labels both results as scoped and preserves the
surviving strict-symmetric case.

## Artifact verification

- `latexmk -pdf -interaction=nonstopmode -halt-on-error` completed cleanly.
- The final log contains no warnings, undefined references, overfull boxes, or
  underfull boxes.
- All six pages of `solution_packet.pdf` were rendered at 144 dpi and visually
  inspected. Equations, theorem statements, the source screenshot, and the
  bibliography are legible and unclipped.
- `solution_packet.pdf` SHA-256:
  `3775249fea275d3a4c007284fbff82c35efb5e9a7b25f9ec9356c376cbe8fe15`.
- `source_paper.pdf` SHA-256:
  `24f36190b1dec77dff99f7fa4ef1abbe5aa1687793bfe641719c5c75acee0cd4`.

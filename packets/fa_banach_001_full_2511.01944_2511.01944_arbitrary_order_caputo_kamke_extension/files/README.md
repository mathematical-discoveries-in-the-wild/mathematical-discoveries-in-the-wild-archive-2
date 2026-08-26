# 2511.01944 — arbitrary-order Caputo–Kamke existence theorem

Status: candidate full positive result; human review requested.

Model: GPT5.6.

Source: Dušan Oberta, *On the existence of solutions of fractional
differential equations in Banach spaces*, arXiv:2511.01944.

## Result

The source proves its measure-of-noncompactness/Kamke existence theorem for
`0 < alpha < 1` and explicitly asks for arbitrary order `alpha > 0`. The
packet proves the extension for every positive Caputo order.

For `m = ceil(alpha)`, the single initial value is replaced by the initial jet
`u^(j)(a)=u_j`, and the fixed-point tube is centered on its Taylor polynomial

    P(t) = sum_{j=0}^{m-1} u_j (t-a)^j/j!.

Under the source's uniform-continuity, boundedness, singleton, and Kamke
noncompactness assumptions on that tube, a solution exists on

    [a, a + min(delta_tilde,
                (beta*Gamma(alpha+1)/M)^(1/alpha))].

This also gives existence on the whole prescribed interval whenever the tube
radius satisfies `M*delta_tilde^alpha <= beta*Gamma(alpha+1)`.

## Why the proof extends

- The integral noncompactness lemma uses only positivity and integrability of
  `(t-s)^(alpha-1)`, hence works for every `alpha > 0`.
- For `alpha > 1`, the fractional integral of a bounded function is uniformly
  Lipschitz; below one it has the source's alpha-Hölder modulus.
- Centering on the full initial polynomial leaves the crucial first-iterate
  estimate `mu(X_1(t)) = o((t-a)^alpha)`, exactly the Kamke small-time
  condition.

## Files

- `main.tex`: self-contained theorem and proof.
- `solution_packet.pdf`: compiled review packet.
- `verification.md`: adversarial proof and packaging audit.
- `source_paper.pdf` and `source_paper.tex`: primary-source evidence.
- `evidence/source_closing_question_crop.pdf`: crop containing the explicit
  arbitrary-order and full-interval questions.

## Human review recommendation

Review as a candidate full positive answer. The highest-value checks are the
all-order kernel equicontinuity lemma, the Caputo/Volterra equivalence at
integer orders, and the centered estimate (19)–(21).

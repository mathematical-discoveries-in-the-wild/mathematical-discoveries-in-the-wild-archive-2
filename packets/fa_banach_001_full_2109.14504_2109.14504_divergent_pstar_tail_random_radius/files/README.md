# 2109.14504 — divergent dual mass forces a fixed random-section radius

Status: `candidate_full_solution_human_review_needed`.

Model: `GPT5.6`.

Source: Aicke Hinrichs, Joscha Prochno, and Mathias Sonnleitner, *Random sections of ell_p-ellipsoids, optimal recovery and Gelfand numbers of diagonal operators*, arXiv:2109.14504v1.

## Result

The source's polynomial threshold conjecture was open in exactly two regimes:

- `1 < p < 2` at `lambda = 1/p*`;
- `p > 2` and `1/2 < lambda <= 1/p*`.

This packet proves the stronger general statement proposed immediately after the conjecture. If `1 < p <= infinity`, `q=p*`, and the nonincreasing semiaxes satisfy `sigma not in ell_q`, then for every fixed codimension `n` and every error probability `epsilon`, some sufficiently large ambient dimension `m` satisfies

`P[rad(E_{p,sigma}^m, ker G_{n,m}) >= sigma_1 / 2^(1/p)] >= 1-epsilon`.

Consequently the uniform random-information decay exponent is zero. For polynomial semiaxes this applies exactly when `lambda <= 1/p*`, closing both missing regimes; together with the source results it proves the whole stated threshold conjecture.

## Proof mechanism

Separate the first Gaussian column. The image of the tail `ell_p` ball under the weighted Gaussian columns is a symmetric body `K_m` with support function

`h_K(v) = (sum_{j>=2} sigma_j^(p*) |<g_j,v>|^(p*))^(1/p*)`.

A self-contained net and operator-norm argument proves a uniform empirical Gaussian small-ball lemma on every sufficiently large dyadic block. Cauchy condensation then shows that the Euclidean inradius of `K_m` tends to infinity whenever `sum sigma_j^(p*)` diverges. Thus `K_m` eventually absorbs `-sigma_1 g_1`, giving a kernel vector whose normalized first coordinate is `sigma_1/2^(1/p)`.

## Verification and novelty

The verification report audits the empirical small-ball lemma, block probabilities, condensation, support-function inclusion, normalization, and the exact uniform-in-`m` decay quantifiers.

A bounded local-index and external primary-source search on 2026-08-11 found the original arXiv/published paper but no later resolution of the conjecture. Novelty remains subject to specialist review.

## Files

- `main.tex`: complete proof packet.
- `solution_packet.pdf`: compiled human-review packet.
- `verification_report.md`: adversarial proof audit.
- `source_paper.pdf`: official 24-page arXiv v1 paper.
- `figures/open_problem_crop.png`: source page 9 crop containing the conjecture, both missing regimes, and the stronger open problem.

## Human review recommendation

Review as a likely valid full solution. The key audit points are the uniform small-ball lemma for arbitrary `q>0`, the direction of support-function inclusion, and the use of the ambient-dimension quantifier in the source definition of decay.

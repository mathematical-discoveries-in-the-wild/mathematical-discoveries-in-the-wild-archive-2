# 1412.7859 — full growth rate for k-wise Khinchine constants

Status: literature_implied_answer (full asymptotic answers to the two numbered source questions).

Model: GPT5.6.

Source: Brendan Pass and Susanna Spektor, *On Khintchine type inequalities for pairwise independent Rademacher random variables*, arXiv:1412.7859v1, source PDF pages 2–3.

Supporting sources:

- Ron Peled, Ariel Yadin, and Amir Yehudayoff, *The Maximal Probability that k-wise Independent Bits are All 1*, arXiv:0801.0059v3, especially supporting PDF pages 4–7.
- Brendan Pass and Susanna Spektor, revised paper *On Khintchine type inequalities for k-wise independent Rademacher random variables*, arXiv:1708.08775v1, Proposition 2.1 on supporting PDF page 3.

## Result

For fixed integers `k>=2`, fixed real `p>=2`, and `m=floor(k/2)`, the source constant satisfies

```text
C(N,p,k) asymp_{p,k} N^{max(0, 1/2-m/p)}.
```

Thus it is bounded exactly when `p<=2 floor(k/2)` and, when it is unbounded, this formula gives its full power growth. In the revised paper’s stated regime `p>k`, it is always unbounded and has order `N^(1/2-floor(k/2)/p)`.

## Identification

The upper bound is Pass–Spektor’s even-order moment interpolation, applied at order `2m`. For the lower bound, Peled–Yadin–Yehudayoff prove that a `k`-wise independent fair-bit law can put probability of order `N^(-m)` on the all-ones vector. After replacing bits `X_i` by signs `epsilon_i=2X_i-1` and taking equal normalized coefficients, that single atom contributes order `N^(p/2-m)` to the `p`th moment.

Neither supporting paper states this Khinchine conclusion. The first supplies the endpoint-mass construction and the second supplies the matching moment upper bound. The direct combination is therefore classified as a literature-implied answer rather than a new result.

## Files

- `main.tex`: complete derivation and provenance boundary.
- `solution_packet.pdf`: rendered literature-implied packet.
- `source_paper.pdf`: official source PDF.
- `supporting_paper_0801.0059.pdf`: official endpoint-mass paper.
- `supporting_paper_1708.08775.pdf`: official revised Khinchine paper.

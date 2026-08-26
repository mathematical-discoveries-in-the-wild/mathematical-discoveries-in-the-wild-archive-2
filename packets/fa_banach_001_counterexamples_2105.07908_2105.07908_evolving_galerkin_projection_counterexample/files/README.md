# 2105.07908 — evolving Galerkin projection counterexample

Status: `candidate_counterexample_likely_valid_human_review_needed`.

Model: `GPT5.6`.

Source: Alphonse, Caetano, Djurdjevac, and Elliott, *Function spaces, time derivatives and compactness for evolving families of Banach spaces with applications to PDEs*, arXiv:2105.07908, Remark 7.5 on source PDF page 40.

## Result

The intended uniform projection question in Remark 7.5 has a negative answer in the paper's abstract evolving-space framework.

There is a fixed weighted Hilbert Gelfand triple `X -> H -> X*`, a smooth compatible evolution `phi_t`, and a transported orthogonal Schauder basis such that, for every `t>0`, the `H`-orthogonal projections onto the first `n` transported vectors satisfy

```text
sup_n ||P_n^t|_X||_{X -> X} = infinity,
```

even though `||P_n^0||_{X -> X}=1` for every `n`.

## Construction

- `H=ell_2`.
- `X=ell_2(d)` with `d_{2k-1}=k` and `d_{2k}=1`.
- `K e_{2k-1}=e_{2k}`, `K e_{2k}=0`, so `K^2=0` and `K` is contractive on both `X` and `H`.
- `phi_t=I+(t/2)K`, with inverse `I-(t/2)K`.
- For `a=t/2`, the odd projection sends `e_{2k}` to
  `a(1+a^2)^{-1}(e_{2k-1}+a e_{2k})`, whose `X`-norm grows like a fixed positive multiple of `k`.

## Clerical scope note

Remark 7.5 prints the domain as `V_n(t)`, on which the orthogonal projection is the identity. The surrounding duality argument clearly needs boundedness of `P_n^t` on `X(t)`. The packet answers this nontrivial intended reading.

The counterexample is abstract. It does not exclude positive results for geometrically chosen eigenbases on smoothly evolving domains.

## Verification and novelty

The verification report audits the Gelfand triple, bounded invertibility and smoothness of the evolution, transported-basis condition, exact two-dimensional projection formula, and scope of the clerical correction. Bounded local-index and web/arXiv searches found no answer to the exact remark. Novelty remains subject to specialist review.

## Files

- `main.tex`: full counterexample proof.
- `solution_packet.pdf`: compiled human-review packet.
- `verification_report.md`: adversarial proof audit.
- `source_paper.pdf`: official 46-page arXiv PDF.
- `figures/open_problem_crop.png`: source PDF page 40 crop containing Remark 7.5.

## Human review recommendation

Review as a likely valid full counterexample to the intended abstract question. The highest-value check is that the source indeed intends the `X(t) -> X(t)` operator norm rather than the literal, trivial restriction to `V_n(t)`.

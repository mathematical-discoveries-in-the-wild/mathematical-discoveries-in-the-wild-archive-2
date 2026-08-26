# Verification report

Verdict: **candidate full negative resolution, likely valid**.

## Source verification

- `source_paper.pdf` is the 11-page arXiv PDF for 2506.18913.
- Questions 3.7 and 3.9 occur together on PDF page 10.
- `figures/open_questions_page.jpg` contains the entropy definition, Deutsch
  and Buzano inequalities, and both complete questions.

## Mathematical audit

1. Relative to an orthonormal basis, the source's norm Parseval identity is
   `||y||=max_j |<y,tau_j>|`.  Applying it to every vector of a second
   orthonormal basis proves that the global coherence is exactly one.
2. If `||x||=1`, all coordinate moduli are at most one and at least one is
   one.  Hence at most `n-1` terms of each entropy can be positive.
3. Over `Q_p`, a positive coordinate entropy is
   `2m p^{-2m} log p` for an integer `m>=1`.  The ratio of consecutive
   coefficients is `((m+1)/m)p^{-2}<1`, so the maximum is
   `2 log(p)/p^2` at `m=1`.
4. Equal canonical bases with `x=(1,p,...,p)` attain the resulting upper
   bound; `x=(1,...,1)` attains zero.  All coordinates are nonzero, so these
   examples lie in the source's stated entropy domain.
5. The `Q_2^8` specialization gives the exact counterexample to the
   classical upper bound.
6. Multiplying the two p-adic Cauchy--Schwarz estimates proves the Buzano
   substitute.  The orthogonal example `e_1,e_2,e_1+e_2` attains equality,
   ruling out every universal overlap improvement at zero overlap.

## Exact verifier

Run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2506.18913_padic_deutsch_buzano_degeneracy/code/verify_entropy_bounds.py
```

The script checks monotonicity of the discrete entropy coefficients, the
dimension-eight failure, and the sharp orthogonal Buzano example using exact
rational arithmetic.

## Novelty audit

- Searched run registry, solution, attempt, and proof-gap indexes for the
  arXiv id, p-adic Deutsch entropy, and p-adic Buzano terminology.
- Searched current arXiv/web indexes using both exact question wordings,
  author/title variants, and non-Archimedean variants.
- The searches found the source and adjacent p-adic uncertainty papers, but
  no later answer to either question.
- Novelty confidence: moderate, pending specialist bibliographic review.

## Upgrade-attempt audit

The initial observation was only that coherence equals one.  The required
deep upgrade optimized every entropy summand over the discrete value group,
yielding the exact sharp `Q_p` upper bound, both endpoint examples, and a
dimension-eight failure of the printed classical upper bound.  A
second avenue identified the sharp Cauchy--Schwarz product inequality and an
orthogonal equality example, fully resolving the linked Buzano question.

## Rendering audit

The final `solution_packet.pdf` builds without LaTeX warnings or overfull
boxes.  All three pages were rendered to RGB PNGs and inspected: the source
crop is legible when zoomed, the theorem and proof stay inside the margins,
all equations render correctly, and no transparency artifacts or literal TeX
commands remain.

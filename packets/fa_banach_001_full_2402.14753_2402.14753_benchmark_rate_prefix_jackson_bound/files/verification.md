# Verification record

Date: 2026-08-11

Agent: `agent_lane_06`

Status: candidate full affirmative answer, likely valid, pending human review.

## Exact target and source artifact

- The target is the question on source PDF page 9 asking whether a tighter
  Jackson bound exists or prefix-tuning/prompting inherently requires more
  trainable parameters.
- The cached arXiv source compiled locally to a 27-page PDF.
- `figures/open_question_crop.png` was cropped from rendered source PDF page 9
  and visually checked against the full page.
- Source PDF SHA-256:
  `768453eb61bfccace230a5b5008e479e25d7073cd43c956512efa628103b766e`.
- Crop SHA-256:
  `122c76576075731748d6d4fd90dbbe55bc73f7df4615797c4993f0e932ea9e2b`.

## Mathematical checks

1. A maximal geodesic `delta`-separated subset of `S^m` is a `delta`-net.
   Its radius-`delta/2` caps are disjoint.
2. The cap-area computation was checked explicitly:
   `A_(m-1) integral_0^(delta/2) sin(t)^(m-1) dt` is at least
   `A_(m-1) delta^m/(2m pi^(m-1))`.  Therefore
   `N <= C_m delta^(-m)` with
   `C_m=2m pi^(m-1) A_m/A_(m-1)`.
3. For `delta<=1/2`,
   `cos(delta)-cos(2delta)=2sin(3delta/2)sin(delta/2)` is at least
   `6delta^2/pi^2`, hence at least `delta^2/2`.
4. A denominator contribution from a closest net point gives far softmax mass
   at most `N exp(-lambda delta^2/2)`.  The stated lower bound on `lambda`
   makes this at most `delta/pi`.
5. Splitting into the `2delta` cap and its complement gives the uniform error
   `2Ldelta + pi L(delta/pi) = 3Ldelta`.
6. Direct block multiplication with the fixed matrices verifies:
   - prefix score `lambda <x,b_i>`;
   - prefix projected value `f(b_i)`;
   - every context score is zero;
   - every context projected value is zero.
   Thus the classical-head denominator is exactly the prefix denominator plus
   `T`; no limiting matrix entry is used.
7. The prefix denominator is at least `exp(lambda cos(delta))`, so the context
   correction is at most `BT exp(-lambda cos(delta))`.  The second stated
   lower bound on `lambda` makes it at most `epsilon/2`.
8. With `delta=min(1/2,epsilon/(6L))`, the localization term is at most
   `epsilon/2` even in the branch `delta=1/2`.  The total is at most
   `epsilon`.
9. The `L=0` case was checked separately: one zero-key prefix with value
   `(T+1)f` represents the constant map exactly.
10. The result is correctly described as benchmark-rate rather than minimax
    optimal.  The attempted Lipschitz-ball packing lower bound does not alone
    control an unbounded real-parameter exponential-ratio family.

## Independent numerical sanity check

Command:

```text
conda run --no-capture-output -n sandbox python code/check_softmax_net_bound.py
```

Output:

```text
delta=0.06666667
N=94 <= 94.248
lambda=3778.234
analytic_total_bound=0.60000000 <= epsilon=1.2
sampled_max_error=0.06662757
```

The script checks the gap inequality, the exact `S^1` covering count, the
analytic head bound, and 20,001 input angles for a nonconstant vector target.
It is a sanity check only; the proof is analytic.

## Literature stress test

- Cheap run indexes contained no prior result, attempt, or packet for this
  arXiv id.
- Bounded exact-phrase, title-citation, and architecture-keyword searches were
  conducted through 2026-08-11.
- arXiv:2411.16525 is adjacent prompt-tuning universality, but uses
  quantization, feed-forward layers, and a prompt indexing a discretized map
  class; it does not give the theorem here.
- arXiv:2504.19901, Theorem A.1, has a covering-number rate but places
  target-dependent parameters in a trainable linear layer and trainable
  attention matrices.  It is not a frozen-head/prefix-only result.
- No later proof of the exact fixed-head intrinsic-dimensional prefix Jackson
  bound was found.  This is a bounded novelty assessment, not a claim of
  exhaustive bibliographic certainty.

## Build and visual audit

Build command:

```text
latexmk -g -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
```

- Build succeeded.
- Final log has no undefined references, overfull boxes, underfull boxes, or
  multiply defined labels.  The sole warning is LaTeX changing the figure
  placement specifier from `h` to `ht`.
- `solution_packet.pdf` has 5 letter-size pages, is unencrypted, and contains
  no form fields.
- All five final pages were rendered at 170 DPI and inspected individually.
  No clipped text, overlaps, broken equations, black squares, illegible
  glyphs, or malformed tables were found.  The source-question crop is sharp
  and contains the complete question.
- Ghostscript text extraction contains the theorem heading, fixed-matrix
  comparison, and lower-bound limitation.
- Final packet SHA-256:
  `b952afd4c18bf912a57196878dac316e25e1c4b953c42c64c10c349fad863303`.

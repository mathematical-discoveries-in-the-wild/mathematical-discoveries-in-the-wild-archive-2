# Depth bounds for the coding memorizer (arXiv:2411.08735)

Status: `candidate_partial_result_likely_valid`, pending human verification.

The packet proves three complementary statements about the depth-efficiency
question in Remark 79 of the source:

1. for every fixed width and every finite-parameter piecewise-affine LReLU or
   stepped-LReLU family used by the paper, worst-case depth is at least
   `c 2^(d_x K/2)` (up to width factors), so subexponential depth in `K` is
   impossible;
2. if one exact depth cap must work for every output precision `M`, then depth
   is at least `2^(d_x K)/(w(w+3))`, matching the paper's memorizer order;
3. a post-source ReLU memorization construction, combined with an exact
   ReLU-to-fixed-LReLU simulation, gives width 40 and depth
   `O(sqrt(2^(d_x K)(1+d_x K+d_y M)) + 1+d_x K+d_y M)`.

The result is partial because minimal widths below 40, FLOOR-enabled networks,
and the decoder's `M` dependence are not closed.

Files:

- `main.tex` — complete argument;
- `solution_packet.pdf` — compiled packet;
- `source_paper.pdf` — current source paper;
- `source_excerpt.pdf` and `question_crop.png` — exact source question;
- `references/` — the VC-dimension and post-source memorization papers;
- `code/verify_depth_bounds.py` — deterministic algebraic checks;
- `verification.md` — build, mathematical, and visual audit.

Build:

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
```

Verifier:

```text
conda run --no-capture-output -n sandbox python code/verify_depth_bounds.py
```

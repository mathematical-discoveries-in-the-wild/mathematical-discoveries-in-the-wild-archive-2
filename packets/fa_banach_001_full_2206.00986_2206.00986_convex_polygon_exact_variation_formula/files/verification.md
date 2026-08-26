# Verification record

## Proof audit

The proof has three independent elementary inputs.

1. A proper cyclic interval of vertices of a convex polygon is strictly
   separable from the complementary vertices by a chord line through interior
   points of the two boundary edges where the interval ends.
2. For real numbers, `|a-b|` is the integral over thresholds of the indicator
   that the threshold separates `a` and `b`.
3. For complex `z`,
   `|z|=(1/2) integral_0^pi |Re(exp(-i theta)z)| dtheta`.

For a real level set with `k` cyclic runs, item 1 bounds its list-transition
count by `k*vf(S)`. Item 2 integrates these bounds and identifies the integral
of `k` with half the cyclic perimeter. Item 3 transfers the result to complex
values. No limiting interchange beyond finite sums and bounded elementary
integrals is used.

## Computational check

Run from the repository root:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2206.00986_convex_polygon_exact_variation_formula/code/verify_cyclic_cut.py
```

The script exhaustively checks all non-backtracking four-vertex words of up
to nine points against every value assignment from `{-1,0,1}^4`. It also
checks 20,000 deterministic random complex instances on polygons with four
through eight vertices. It uses the maximum transition count over cyclic
intervals, which the separating-line lemma proves is a lower bound for
`vf(S)`. The computation is a stress test, not part of the proof.

Observed output:

```text
exhaustive four-vertex real instances: 3188160
deterministic random complex instances: 20000
all cyclic-cut inequalities passed
```

## Human-review focus

Check the chord-separation lemma, particularly runs consisting of one vertex
or all but one vertex. The chosen chord endpoints lie in the relative
interiors of the two boundary edges, so no polygon vertex lies on the line and
all relevant word segments are strict type-(1) crossings.

## Final artifact audit

The final packet has five letter-size pages. All five pages were rendered to
PNG and inspected at full-page and enlarged detail after the last compilation.
There is no clipping, overlap, malformed mathematics, missing figure, or
unreadable text. The one underfull bibliography line is harmless and does not
affect layout.

```text
SHA-256(solution_packet.pdf) =
c37d36694ac574fbf1f1c54cfe1f169dff08eb1a54a9ba6d1232637837a7aa81
```

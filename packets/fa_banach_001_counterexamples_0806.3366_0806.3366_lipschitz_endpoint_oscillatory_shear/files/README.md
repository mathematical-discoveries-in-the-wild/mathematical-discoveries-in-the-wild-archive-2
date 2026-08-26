# Oscillatory-shear counterexample at the Lipschitz endpoint

Run: `fa_banach_001`

Agent: `agent_lane_14`

Status: `candidate_counterexample_likely_valid_human_review_needed`

## Source question

On PDF page 45 of Bellido--Mora-Corral, *Approximation of Holder
continuous homeomorphisms by piecewise affine homeomorphisms*,
arXiv:0806.3366, the authors state that `sup B(1,1)=1` but ask whether the
endpoint `1` belongs to `B(1,1)`.

## Full negative answer

On the unit square let

```text
g(0)=0,   g(t)=t^2 sin(1/t) for t>0,
h(x,y)=(x+g(y),y).
```

The function `g` is Lipschitz and `h` is a bi-Lipschitz homeomorphism with
explicit inverse `(u,v) -> (u-g(v),v)`.  Any map affine on a finite
triangulation restricts on the left boundary to a finite piecewise-affine
curve.  Its first coordinate therefore has a constant slope `c` on some
initial interval.  But `g'` assumes the values `-1` and `+1` along two
sequences tending to zero, so the Lipschitz seminorm of the difference is at
least

```text
max(|-1-c|,|1-c|)=1+|c|>=1.
```

Thus `h` has distance at least one from every finite piecewise-affine map,
even without imposing injectivity.  Therefore `1` is not in `B(1,1)`.
Together with source Theorem 7.6, this gives the exact classification
`B(1,1)=(0,1)`.

## Files

- `main.tex`: complete expert-facing counterexample packet.
- `solution_packet.pdf`: rendered packet for review.
- `source_paper.pdf`: local copy of arXiv:0806.3366.
- `figures/open_problem_crop.png`: source endpoint question from PDF page 45.
- `code/verify_shear.py`: deterministic numerical sanity checks.
- `verification.md`: proof and artifact audit.
- `novelty_search.md`: bounded novelty-search record.

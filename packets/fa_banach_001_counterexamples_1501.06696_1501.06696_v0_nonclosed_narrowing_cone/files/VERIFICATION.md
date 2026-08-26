# Verification report

Status: full counterexample; proof complete; ready for human mathematical
review.

## Mathematical audit

- The exact source question was checked in the official arXiv PDF, page 19:
  the authors do not know whether `V_0=V_+-V_+` is always closed.
- In block `n`, the two cone generators `p_n=(1,0)` and
  `q_n=(1,1/n)` form a basis, with inverse coordinates
  `s_n=n z_{n,2}` and `r_n=z_{n,1}-n z_{n,2}`.
- The direct-sum cone is closed because it is the intersection of the
  inverse images of closed finite-dimensional cones under continuous block
  projections.
- Every two positive vectors have nonnegative Hilbert inner product, so
  `0<=u<=v` implies `||u||<=||v||`, exactly the source's ordered-space norm
  axiom.
- A positive vector's two basis-coefficient sequences are in `ell^2`, since
  both are bounded by its first-coordinate sequence.  Positive/negative
  splitting proves the converse, giving
  `V_0={z:(n z_{n,2}) in ell^2}`.
- This subspace contains all finite-support vectors.  The vector with blocks
  `(0,1/n)` is in the ambient Hilbert space but has constant coefficient
  sequences `(-1,1)`, so it is outside `V_0` and is approached by its finite
  truncations.
- Block basis coordinates identify the order with coordinatewise order;
  maxima and minima preserve `ell^2`.  Hence both `V_+` and `V_0` are
  lattices, strengthening the negative answer.
- Taking the identity gradient relation on the Hilbert space satisfies every
  gradient-space axiom; closedness of the cone gives convergence
  compatibility.

## Independent exact checks

Command:

~~~text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/1501.06696_v0_nonclosed_narrowing_cone/code/verify_narrowing_cone.py
~~~

Observed result:

~~~text
all exact block, acuteness, coefficient, and truncation checks passed
~~~

The script uses exact rational arithmetic for the block identities and an
exhaustive finite coefficient grid for acuteness.  It also checks the
counterexample block coefficients and a numerical tail bound for truncation
convergence.  These are sanity checks, not dependencies of the proof.

## Build and visual audit

- `latexmk` completed after the necessary cross-reference rerun.  The final
  log has no warnings, undefined references, overfull boxes, underfull boxes,
  or errors.
- The final packet has 3 letter-size pages.
- Every final page was rendered at 150 dpi to an RGB PNG (1275 by 1650) and
  visually inspected.  No clipping, overlap, unreadable glyph, broken
  formula, or malformed page transition was found.
- The source evidence is a real crop from official source page 19 and includes
  both the definition of `V_0`, the surrounding lattice context, and the exact
  open sentence.
- Extracted final PDF text contains no unresolved marker.
- The ledger JSON parses and records model GPT5.6.

## SHA-256

~~~text
fe36ba20a2d2aa37913244b5fb79939c9cd9fa0cbeb21f5cd15f2c476121a76b  solution_packet.pdf
e106daa249191b4cdc7d8e0d2ec71303eaa35eb4800d90fbbac98d4dc91254e6  source_paper.pdf
1bfd39c887c50bcd31b484b44b589d3948a71fb92add45bee6a137611863bcdf  figures/open_question_page19.png
c1a6f60ed84b47319931a315ab1becaa780b0eab9814cf46a7bf7ebac94c154e  main.tex
3062882f665c8f9aecea101b283282c1d581120de3e3f5edb506de479b46d75b  code/verify_narrowing_cone.py
~~~

## Human-review focus

Check the equivalence between membership in `K-K` and square summability of
the two narrowing-basis coefficient sequences; check that the source's
preorder convergence and norm-monotonicity axioms follow respectively from
closedness and acuteness of `K`; and verify that coordinatewise lattice
operations remain in `ell^2`.

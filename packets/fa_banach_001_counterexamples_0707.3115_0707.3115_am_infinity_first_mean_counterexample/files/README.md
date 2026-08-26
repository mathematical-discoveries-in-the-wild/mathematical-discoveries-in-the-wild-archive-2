# Countably generated am-infinity counterexample

**Status:** full counterexample, likely valid; pending human review.

**Source:** Victor Kaftal and Gary Weiss, *B(H) lattices, density and
arithmetic mean ideals*, arXiv:0707.3115, question following Theorem 5.2 on PDF
page 23.

## Result

The implication asked about in the source is false, already for a countably
generated ideal contained in trace class.  The packet constructs summable
decreasing sequences

```text
u_p(n) ~ exp(-sqrt(log n)) (log n)^(p/2) / n
```

with `(u_p)_{a_infinity}=(u_{p+1})`.  Their directed union `S` is therefore
am-infinity stable.  Flattening all the `u_p` on a common sparse collection of
logarithmically thin but multiplicatively huge intervals gives sequences
`xi_p` with the same tail-mean ideals.  For `I=sum_p (xi_p)` this yields

```text
I_{a_infinity} = S = S_{a_infinity},
```

while a dilation-diagonal argument proves `u_0 notin I`.  Hence `I` is not
am-infinity stable although `I_{a_infinity}` is.

## Files and verification

- `main.tex` and `solution_packet.pdf`: complete construction and proof.
- `source_paper.pdf`: original arXiv PDF.
- `figures/open_problem_crop.png`: rendered source question on PDF page 23.
- `runs/fa_banach_001/attempts/0707.3115_am_infinity_stability_upgrade_attempts.md`:
  eight focused routes, ending with the successful common-flattening method.

The proof has no computational dependency.  Recommended human-review focus:
the directed-union use of the principal identity
`(x)_{a_infinity}=(x_{a_infinity})` for summable `x`, the summable tail-loss
estimate across all later intervals, and the final principal-ideal dilation
test.  A bounded exact-phrase and related-paper search found no later answer;
novelty remains pending specialist review.

# Verification report

Verdict: `candidate_full_classification_and_ulam_stability_likely_valid`

## Source audit

The official source is arXiv:2007.01454v1. Its final Question 1 asks for the
solution and Ulam stability of the absolute-value radical equation for every
positive integer `n` and nonzero real `a,b,c,d`.

## Exact reduction audit

Changing either input sign preserves the unordered pair of radical terms,
so exact solutions are even. With `g(s)=f(s^(1/n))` for `s>=0`, and
`A=|a|`, `B=|b|`, the equation becomes
`g(As+Bt)+g(|As-Bt|)=c g(s)+d g(t)`. Subtracting `g(0)`, the two axis
identities eliminate the scaled terms and yield the standard quadratic
equation on the half-line. Even extension gives a quadratic map on `R`.

## Classification converse audit

For `f(x)=Q(x^n)+w`, evenness of the quadratic map removes the absolute
values. The quadratic identity handles the sum/difference pair, the two
scaling eigenconditions produce coefficients `c,d`, and
`(2-c-d)w=0` handles constants. Thus the necessary conditions are exactly
sufficient.

## Stability-constant audit

For defect at most `epsilon`, sign comparison costs at most
`2 epsilon/max(|c|,|d|)`. After subtracting `g(0)`, the quadratic defect is
the signed sum of four original/axis defects and is at most `4 epsilon`.
Dyadic quadratic stabilization therefore costs
`sum_k 4 epsilon/4^(k+1)=4 epsilon/3`. In the nonresonant case the origin
costs at most `epsilon/|2-c-d|`; in the resonant case it is absorbed into
the exact constant solution.

## Scaling-limit audit

The approximate axis relations give errors at most `2 epsilon`. Evaluating
at `2^k s`, dividing by `4^k`, and taking the dyadic limit forces the exact
relations `2Q(|a|s)=cQ(s)` and `2Q(|b|s)=dQ(s)`. Therefore the stabilizing
quadratic map belongs to the exact solution class rather than merely solving
the unscaled quadratic equation.

## Novelty audit

Exact-equation, title, absolute-radical, parameter, and Ulam-stability
searches through 2026-08-11 found adjacent radical quadratic/quartic papers
but no all-positive-integer classification and uniform theorem matching this
packet. This is not a proof of novelty; expert citation review remains
appropriate.

## Render audit

Clean. The final packet compiles to four pages (211,570 bytes), with no
LaTeX warnings, undefined references, overfull boxes, or underfull boxes.
All four rendered pages were inspected at full readable resolution after the
final rebuild. The source-question crop and all formulas are sharp; margins
are intact; there is no clipping, overlap, or other layout defect.

Final packet SHA-256:
`a514c7fc1466026da0ac08ad4df0e00f0edcd209259670786c9ee7e039f00b6b`.

## Human verifier focus

1. Recheck the four-defect cancellation identity in the Ulam proof.
2. Check passage of the two scaling laws through the dyadic limit.
3. Repeat the non-arXiv novelty search, especially papers citing the source.

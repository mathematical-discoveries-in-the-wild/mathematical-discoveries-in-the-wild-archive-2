# 1801.02824: bounded-lower-jet density without Poincare

- Status: `candidate_partial_result_pending_human_review`
- Model: `GPT5.6`
- Source: Debanjan Nandi, Tapio Rajala, and Timo Schultz, *A density
  result for homogeneous Sobolev spaces on planar domains*, arXiv:1801.02824
- Source question: whether the `p`-Poincare-domain assumption can be removed
  from the full `W^{k,p}` density conclusion on bounded simply connected
  planar domains

## Result

For every bounded simply connected `Omega subset R^2`, every integer `k>=1`,
and every `1<=p<infinity`, the packet proves

`W^{k,infinity}(Omega) intersect C^infinity(Omega)`

is dense in

`W^{k,p}(Omega) intersect W^{k-1,infinity}(Omega)`

in the full `W^{k,p}` norm, without a Poincare, extension, or boundary
regularity hypothesis.

The source Whitney construction is re-estimated at every lower derivative
order. Moment normalization plus boundedness of the lower jet uniformly
controls the tail polynomials throughout the bounded domain, and their error
vanishes with the measure of the shrinking boundary tail. A variable-radius
interior mollifier removes the auxiliary smoothness assumption while
preserving bounded lower jets.

## Scope

The unrestricted question remains open. For arbitrary `W^{k,p}` data, a
lower-order anchoring polynomial may grow across a large tail behind a thin
neck. Eight focused upgrade attempts did not establish the compatible
higher-order truncation or intrinsic tree estimate needed to remove this
obstruction, and no counterexample survived finite-tail approximation.

## Review focus

Human review should concentrate on the lower-order estimate (7), especially
bounded overlap of the plain-polynomial regions, and on the weak chain-rule
justification for the variable-radius smoothing lemma. Human review is
unchecked.


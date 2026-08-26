# Canonical lower-semicontinuous Kuratowski extension, and the sharp affine obstruction

Status: `candidate full resolution (two-sided clarification; likely valid)`

Source: David Bate, Sylvester Eriksson-Bique, and Elefterios Soultanis,
*Fragment-wise differentiable structures*, arXiv:2402.11284v1 (2024),
Remark 2.1 on source PDF page 7.

## Result

Let `K:X -> l_infinity(D)` be the standard base-pointed Kuratowski embedding
over a dense coordinate set, and let `H_K` be the union of all chords joining
points of `K(X)`.  For any lower-semicontinuous
`rho:X -> [0,infinity]`, take the infimum of the affine endpoint cost over all
two-point representations and then take its lower-semicontinuous relaxation
on `H_K`.  The resulting function:

- is lower semicontinuous;
- agrees exactly with `rho` on `K(X)`;
- is the greatest lower-semicontinuous function below every affine endpoint
  cost, hence is canonical by a maximal universal property;
- is monotone, positively homogeneous, and constant-preserving.

Under the completeness hypothesis used in the source paper, a fixed arctangent
order transform and a distance-to-`K(X)` floor upgrade this to an explicit
finite real-valued lower-semicontinuous extension for **every** real-valued
lower-semicontinuous datum, with no bounded-below assumption.

The trace theorem rests on the exact Kuratowski inequality

`|| (1-t)K(a) + tK(b) - K(x) ||_infinity >= (1-t)d(a,x) + t d(b,x)`.

There is also a sharp limitation.  On the four-cycle metric, the midpoints of
the two opposite Kuratowski chords coincide.  Boundary data equal to zero on
one opposite pair and one on the other prove that no extension can be affine
on every chord.  Thus the literal semicontinuous-extension question has an
affirmative canonical answer, while the exact free-space interpolation
identity needed for weighted-gap line integrals is impossible in general.

## Packet contents

- `main.tex` and `solution_packet.pdf`: complete theorem and proof.
- `source_paper.pdf`: locally compiled PDF from the cached original arXiv TeX.
- `figures/open_problem_crop.png`: full-width crop of Remark 2.1.
- `code/check_c4_obstruction.py`: exact finite verification of the crossing
  chords and conflicting midpoint data.
- `verification.md`: proof, computation, source, and rendering audit.

## Novelty and scope

On 2026-08-11, the run registry, solution index, attempt index, and proof-gap
index had no hit for this paper or question.  Exact-phrase and close-keyword
searches of the local full-source corpus found the question only in the source
paper.  Three locally available later papers citing arXiv:2402.11284
(arXiv:2504.16657, 2508.08017, and 2510.25715) do not discuss this issue.
Bounded external web searches were attempted but returned no usable records in
this environment, so novelty confidence is moderate rather than high.

The positive results answer both the literal existence question for
real-valued data and a precise, natural stronger meaning of “canonical” for
the nonnegative integrands used in the paper: the maximal
lower-semicontinuous chord-subaffine extension.  They do **not** supply an
endpoint-affine extension or reproduce the exact weighted-gap integral used in
the source paper.  The four-cycle theorem proves that no general construction
can have that stronger property.

Human review should focus on the boundary-recovery argument for extended
values and on whether this explicit universal property matches the intended
meaning of “canonical” in Remark 2.1.

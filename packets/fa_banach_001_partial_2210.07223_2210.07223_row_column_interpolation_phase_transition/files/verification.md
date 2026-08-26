# Verification report

Verdict: `candidate_exact_subclass_classification_likely_valid`

## Source audit

Page 1 of arXiv:2210.07223 asks which operator spaces satisfy the column–row
property and gives the concrete row/column definition. The paper records the
three relevant endpoint facts: `R` fails, while `OH` and `C` have constant 1.

## Endpoint audit

- The universal estimate `gamma_n(E) <= sqrt(n)` follows from
  `||sum x_i x_i^*|| <= sum ||x_i||^2 <= n ||sum x_i^* x_i||`.
- For the first `n` row matrix units, column norm is 1 and row norm is
  `sqrt(n)`, so `gamma_n(R)=sqrt(n)`.
- For columns, synthesis operator norm is at most Hilbert–Schmidt norm, giving
  `gamma_n(C)=1`.
- `OH` is completely isometric to its opposite via the identity, so its
  transpose norm is 1.

## Interpolation audit

Matrix amplification commutes isometrically with complex operator-space
interpolation. Reiteration gives

```text
H_theta = (R,OH)_(2 theta)       for theta <= 1/2,
H_theta = (OH,C)_(2 theta - 1)   for theta >= 1/2.
```

Interpolating the same transpose operator yields the stated upper bounds.

## Lower-bound audit

For the first `n` coordinate vectors, the endpoint column norms are `1` and
`sqrt(n)`, while the endpoint row norms are `sqrt(n)` and `1`. The common
diagonal functional has dual endpoint norms `(n,sqrt(n))` for the column and
`(sqrt(n),n)` for the row. Applying the interpolation theorem directly to
this compatible functional therefore forces the exact intermediate norms

```text
column = n^(theta/2),  row = n^((1-theta)/2).
```

Their ratio matches the interpolation upper bound below the midpoint.

## Consistency audit

- At `theta=0`, the formula gives `sqrt(n)`.
- At `theta=1/2`, it gives 1.
- At `theta=1`, it gives 1.
- Applying the result to the opposite space `H_(1-theta)` gives the reverse
  formula exactly.

## Scope and novelty audit

This is a complete theorem for `(R,C)_theta`, but only a partial answer to the
source's classification of all operator spaces. Bounded arXiv/web searches on
2026-08-17 found no matching phase-transition formula. This does not establish
novelty conclusively.

## Human verifier focus

1. Check the convention `H_theta=(R,C)_theta` and reiteration parameters.
2. Check the endpoint norms and direct interpolation step for the diagonal
   functional.
3. Confirm the standard complete isometry `OH = OH^op` via the identity.
4. Search specialist operator-space literature for an earlier equivalent
   formula.

## Render audit

The final packet compiled without unresolved references, overfull boxes, or
layout warnings. All five pages were rendered at 130 dpi and inspected
individually on 2026-08-17; the source crop, theorem box, formulas, page
breaks, margins, and references are clear and unclipped.

SHA-256:

```text
source_paper.pdf       49e67f7ee4226e3048507fd6ce888164ac947bb5534ac36474b0643f7a200584
source_question_crop   f51acfce6d5d313f9ea73d8956d82b25b1c288e643829ac439e8dfa89bfb30de
solution_packet.pdf    426fe0e16dedee52a4760afe24b758e36ff85eb56bdde5c117449bc853bfed6e
```

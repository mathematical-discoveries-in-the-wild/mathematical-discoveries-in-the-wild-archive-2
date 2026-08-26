# Novelty and duplicate audit

Verdict: `candidate_new_counterexample`; priority confidence is moderate and
an exhaustive literature-priority claim is not made.

## Run-local search

On 17 August 2026 the four lightweight run indexes were searched for
`2507.09865`, `Gromov-Wasserstein`, `GW barycenter`, `Karcher mean`, and
`out-of-span`. No matching result, attempt, or proof-gap packet was present.

## Bounded external search

Searches for the exact paper title and combinations of
`Gromov-Wasserstein`, `Karcher mean`, `critical point`, `not a barycenter`,
`spurious`, and `outside the barycenter span` located the source paper and
general work on GW barycenters and tangential fixed-point iterations, but no
explicit result matching this four-point metric counterexample or its exact
weight mismatch.

The source itself notes that a critical point need not be known to minimize
the GW barycenter functional and presents only empirical out-of-span tests.
The packet's contribution is an exact rational example for genuine metric
measure spaces in which both proposed analysis algorithms agree, attain zero
surrogate residual, and nevertheless miss the unique minimizer of the true
projection functional.

## Scope

The packet gives a complete negative answer to the exact yes/no comparison in
Supplement E: the returned weights need not coincide with a minimizer of
`J`. It also disproves unconditional Karcher/barycenter equivalence. It does
not rule out useful approximation bounds under extra curvature, uniqueness,
alignment-consistency, or separation assumptions.

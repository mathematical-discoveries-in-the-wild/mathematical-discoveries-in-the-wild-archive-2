# Dyadic `JN_p` as a difference of its `A_1` cone

Status: `candidate_full_solution_likely_valid_needs_human_review`.

This packet gives a precise affirmative Coifman--Rochberg-type
characterization requested in the introduction of Juha Kinnunen and Kim
Myyrylainen, *Dyadic John--Nirenberg space*, arXiv:2107.00492.

For every finite cube `Q_0` and `1<p<infinity`,

`JN_p^d(Q_0) = (JN_p^d(Q_0) intersect A_1^d(Q_0))
               - (JN_p^d(Q_0) intersect A_1^d(Q_0))`.

The statement is quantitative: both positive summands can be chosen with
uniform dyadic `A_1` constants and with the sum of their normalized `JN_p`
norms bounded by a constant times the norm of the original function.

The proof equips `JN_p^d` with the normalized Banach norm
`|Q_0|^(1/p)|f_Q0|+[f]_JN`.  The source paper's maximal-operator theorem,
together with its weak-`L^p` embedding, makes the dyadic maximal operator
bounded for this full norm.  Rubio de Francia iteration then builds an
`A_1^d` majorant `R|f|`; the decomposition is

`f = (2 R|f| + f) - 2 R|f|`.

Both terms are positive and comparable to the same `A_1^d` majorant.  Dyadic
reverse Holder self-improvement further writes each term exactly as a bounded
positive factor times a fractional power of a dyadic maximal function,
matching the maximal-function form of the motivating Coifman--Rochberg
theorem.

The script `code/verify_finite_dyadic_rubio.py` performs an exact finite-tree
calculation of dyadic maximal functions and `JN_p` antichain seminorms, then
checks the iteration and decomposition on seeded examples.  It is a sanity
check only; the proof is analytic.

Human review should focus on whether the phrase “Coifman--Rochberg type” in
the source is intended to demand a representation with no bounded multiplier.
The theorem here is an exact characterization and gives an exact
maximal-power representation with bounded positive multipliers; it does not
claim that every summand is a bare fixed `1/p` power of one maximal function.


# Symmetric powers reflect subnormality

Status: candidate full solution to the open question after Proposition 10.5
of arXiv:1503.03692, pending expert review.

The packet proves the stronger operator-theoretic statement

    T^{odot m} subnormal  =>  T subnormal

for every bounded Hilbert-space operator `T` and every integer `m >= 1`.
Consequently the hypothesis `Phi'(0) != 0` can be removed from the “only if”
direction of Proposition 10.5: for every nonconstant admissible `Phi`,
`C_A` subnormal forces `A*` subnormal, and `C_A*` subnormal forces `A`
subnormal. Together with the already-known converse, this gives the full
equivalence for every `Phi`.

The mechanism is a singular-sequence descent. Subnormality of the symmetric
power first implies that `T` is hyponormal. If `T` is not already normal, a
nonzero boundary point `lambda` of its essential spectrum supplies a weakly
null unit sequence `y_j` with `(T-lambda)y_j -> 0`. For

    J_j x = P_sym(x tensor y_j^{tensor(m-1)}),

Lambert's criterion makes the squared orbit norms under `T^{odot m}`
Stieltjes moment sequences. Their pointwise limit is

    (1/m) |lambda|^{2k(m-1)} ||T^k x||^2.

Closure and rescaling of Stieltjes moment sequences then show that every
`{||T^k x||^2}` is a Stieltjes moment sequence, hence `T` is subnormal.

Verification:

    conda run --no-capture-output -n sandbox python code/verify_symmetrization.py

The script checks the exact symmetrization norm/intertwining identities in
400 seeded random complex cases and tests the singular-sequence limit for
unilateral-shift truncations. These are algebraic sanity checks, not part of
the proof.

The main reviewer focus should be the boundary-essential-spectrum singular
sequence lemma and the passage to the pointwise limit of Stieltjes moment
sequences. A bounded exact-question/citation search, including the 2023 survey
arXiv:2306.14807, found no later resolution.


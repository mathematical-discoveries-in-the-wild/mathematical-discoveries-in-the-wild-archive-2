# Verification notes

## Formal audit

1. Left/right equivalence sends `A_N` to
   `(P tensor I) A_N (Q tensor I)` and changes its normalized determinant by
   exactly `|det(P)det(Q)|^(1/m)`.
2. Upper triangular coefficient matrices make the transformed `mN` matrix
   block upper triangular.  Its determinant is the product of the `N x N`
   diagonal-block determinants.
3. The phase-real hypothesis makes diagonal block `j` equal to
   `exp(i theta_j) sqrt(v_j) Z_j`, where `Z_j` is marginally a standard
   normalized GUE matrix.  Correlation among different `j` is irrelevant.
4. Rank non-decrease/full free-field rank forces every `v_j` to be positive;
   otherwise the upper triangular free pencil has a zero diagonal entry.
5. Standard GUE log-determinant asymptotics give normalized determinant
   convergence to `exp(-1/2)`.  Variance `O(log N)` makes the almost-sure step
   summable after division by `N`; the arithmetic--geometric mean bound gives
   uniform integrability and hence `L^1` convergence.
6. Capacity covariance under fixed left/right equivalence has been checked
   directly from the infimum definition.
7. The source formula `Delta(S)=cap(eta)^(1/(2m)) exp(-1/2)`, combined with the
   standard triangular Fuglede--Kadison determinant identity, gives the exact
   product formula for capacity.
8. For arbitrary coefficients, fixed-epsilon regularized convergence follows
   from a.s. GUE asymptotic freeness applied to the bounded continuous function
   `log(t+epsilon^2)` of `A_N A_N^*`.  The limit as epsilon decreases to zero is
   the source Fuglede--Kadison determinant.

## Computational audit

Run from this packet directory:

`conda run --no-capture-output -n sandbox python code/verify_identities.py`

The script checks, on deterministic random examples, the finite block
triangular determinant factorization and the determinant multiplier under
left/right equivalence.  It is a sanity check, not evidence for the
asymptotic theorem.

The mechanical packet check is:

`conda run --no-capture-output -n sandbox python code/verify_packet.py`

## Remaining full-problem gap

The packet does not claim that regularization can be removed for arbitrary
rank non-decreasing covariance maps.  That exchange requires uniform control
of the small singular values of a potentially degenerate block-correlated
Gaussian ensemble.


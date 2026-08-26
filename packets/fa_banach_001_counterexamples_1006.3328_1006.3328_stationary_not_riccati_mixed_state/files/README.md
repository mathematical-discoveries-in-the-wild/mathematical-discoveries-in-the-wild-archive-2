# A mixed stationary state outside the Riccati-state family

Status: `candidate_counterexample_likely_valid_full_negative_answer`.

Source: Bartlomiej Gardas and Zbigniew Puchala, *Stationary states of
two-level open quantum systems*, arXiv:1006.3328. Remark 1 on page 5 asks
whether every stationary state is a Riccati state, or whether stationary
states that are not Riccati states can exist.

## Full negative answer

Use a two-dimensional environment and, in the qubit block decomposition, set

```text
V   = 0,
H_+ = diag(3,1),
H_- = diag(-3,-1).
```

Equivalently, with `K=diag(1,-1)`, the total Hamiltonian is
`H = 2 sigma_z tensor I + sigma_z tensor K`.  Thus the model has a nonzero,
non-scalar qubit-environment dephasing interaction even though its off-diagonal
block `V` vanishes.

The Riccati equation becomes the Sylvester equation
`X H_+ - H_- X = 0`.  Its four entrywise coefficients are `6,4,4,2`, so its
only solution is `X=0`.  Definition 3 of the source then gives only the two
normalized Riccati states `|0><0|` and `|1><1|`.

Now take the standard product assignment admitted in equation (3) of the
source,

```text
Phi(rho) = rho tensor omega,   omega = I/2.
```

For every `0<a<1`, the mixed qubit state `rho_a=diag(a,1-a)` satisfies
`[H,rho_a tensor omega]=0`.  Therefore its total state and its reduced state
are fixed for all times: `T_t(rho_a)=rho_a`.  It is not either of the two
Riccati states, and no other bounded Riccati solution exists.  Hence it is a
stationary state that is not a Riccati state.

## Interpretation, scope, and verification

The phrase *Riccati state* is used exactly as in the source: the partial trace
of a rank-one projector from the graph or orthogonal graph associated with a
bounded solution of the Hamiltonian's Riccati equation.  If one instead
redefines the term to include the convex hull of those states, then this
example belongs to that enlarged hull; the source does not make that
convexification in Definition 3.

The proof is finite-dimensional and exact.  The included verifier checks the
four nonzero Sylvester coefficients, the vanishing commutator for `a=1/3`,
and the reduced state.  Run it with:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/1006.3328_stationary_not_riccati_mixed_state/code/verify_counterexample.py
```

A bounded search through 2026-08-11 covered the run indexes; the exact open
question; the paper title and arXiv id combined with `Riccati`, `stationary`,
`counterexample`, and `open quantum`; and close phrase variants.  It found the
source paper and mirrors/versions of it, but no later paper explicitly
answering Remark 1.  Novelty confidence is moderate pending a specialist
search.

Human-review recommendation: accept as a likely valid full negative answer to
the source's literal question, while checking whether the authors intended an
unstated convexified notion of Riccati state.

Packet PDF: `solution_packet.pdf`.

# Verification report

status: likely valid candidate full counterexample

## Proof-critical checks

1. `E=c_00` carries the topology induced by `K^N`. Its continuous dual is
   exactly the finite-coordinate dual.
2. Boundedness in `E` is coordinatewise boundedness. Every coordinatewise
   bounded set is totally bounded for the product-subspace topology, so `E`
   is a generalised Schwartz space.
3. `E` is not semi-Montel: the bounded partial-sum sequence
   `(1,...,1,0,...)` has no convergent subsequence in `E`; its product-limit
   is the all-ones vector in the completion.
4. For `f(t)=(t^k chi(nt))_n`, compact support of `chi` makes `f(t)` finitely
   supported for each nonzero `t`, and `f(0)=0`.
5. Every continuous functional uses finitely many coordinates, hence every
   scalarization is smooth.
6. If the `k`th derivative at zero existed in `E`, all of its coordinates
   would equal `k!`, forcing the all-ones vector outside `E`.

## Mechanical sanity check

Run:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2301.13612_c00_finite_order_weak_strong_counterexample/code/finite_window_check.py
```

The check confirms sampled finite-support bounds and the forced derivative
prefixes for `1<=k<=8`. It is only a sanity check; the infinite-support
contradiction is proved in the packet.

## Packet QA

`solution_packet.pdf` has three pages. It was compiled after the final source
edit with no LaTeX warnings, rendered at 150 dpi, and every page was visually
inspected. SHA-256:
`ffceaea2a1292a58a0d9af873efcbf72aca9812e9cbbbcb16f83d17fa89dc770`.

## Literature and novelty check

A bounded search on 13 August 2026 found Bachir--Lancien's 2003 Schur-space
characterization and the source thesis, but no publication with this `c_00`
product-topology counterexample. The counterexample is therefore apparently
new within the bounded search, not under an exhaustive bibliographic claim.

## Recommended human focus

Check the identification of the continuous dual of product-topology `c_00`
and the precompactness of every coordinatewise bounded subset. Once those two
standard facts are accepted, the derivative obstruction is immediate.

# Critical Besov trace counterexample at the integer endpoint

Status: `candidate_counterexample_likely_valid_full_negative_besov_endpoint`.

Source: A. M. Caetano, D. P. Hewett, and A. Moiola, *Density results for
Sobolev, Besov and Triebel--Lizorkin spaces on rough sets*, JFA 281 (2021),
109019, arXiv:1904.05420v2. The open problem is Remark 6.9 on page 31 and asks
whether Proposition 6.7 extends to
`s=(n-d)/p+m+1`.

## Full negative answer for the Besov endpoint

The proposed extension fails in the stated Besov class. Take

```text
Gamma = R^(n-1) x {0},  d=n-1,  1<p<infinity,  q=1,
s=1/p+m+1,  m in N_0.
```

Choose a smooth compactly supported `eta` whose restriction to `Gamma` is
nonzero, and put

```text
u(x',x_n) = eta(x',x_n) x_n^(m+1).
```

All derivatives through order `m` have zero trace, so `u` belongs to the
kernel in Remark 6.9. But Proposition 6.2 of the source gives the continuous
critical trace

```text
tr_Gamma : B_{p,1}^{1/p}(R^n) -> L_p(Gamma).
```

Consequently `v -> tr_Gamma(D_n^(m+1) v)` is continuous on
`B_{p,1}^{1/p+m+1}` and vanishes on every test function supported off
`Gamma`. It does not vanish on `u`, because its value is
`(m+1)! eta(x',0)`. Hence `u` is in the stated trace kernel but not in the
closure of `D(Gamma^c)`.

The simplest instance is `n=2`, `p=2`, `m=0`, `s=3/2`: the function
`u(x,y)=eta(x,y)y` has zero value trace and nonzero normal trace.

## Scope, literature, and verification

This is a complete counterexample to the universal **Besov** endpoint
extension because `q=1` is explicitly allowed in Proposition 6.7. It does
not contradict the later positive Sobolev endpoint theorem in M. Hinz,
S. N. Chandler-Wilde, and D. P. Hewett, *Kernels of trace operators via fine
continuity*, arXiv:2507.04536 (Corollary 3.2 and Remark 3.3). That paper
explicitly identifies and resolves the Sobolev branch of Remark 6.9, while
not claiming the Besov endpoint.

The proof is symbolic and has no computational dependency. The main review
points are the critical `q=1` trace in source Proposition 6.2 and the
elementary jet calculation. A bounded search through 2026-08-11 covered the
run indexes, exact Remark 6.9/Proposition 6.7 searches, title/id searches with
`endpoint`, `trace`, `Besov`, and `counterexample`, and arXiv:2507.04536. No
exact prior statement of this Besov counterexample was found. Novelty
confidence is moderate pending specialist review.

Human-review recommendation: promote as a likely valid counterexample to the
Besov endpoint portion and verify the literature status before a novelty
claim.

Packet PDF: `solution_packet.pdf`.

# A sigma-closed operator with no sigma-continuous resolvent

Status: `candidate_counterexample_likely_valid_full_negative_answer`.

This packet answers the Section 3 open question in arXiv:0903.1001.

Take

```text
X = l^1,
Y = c_0 + span{(1,0,1,0,...)},
```

and let `P` swap every adjacent coordinate pair. Then `(X,Y)` is a norming
dual pair. The graph of `P` is sigma-closed because `P*` preserves the
separating subspace `c_0`, but `P` is not sigma-continuous because it sends
the extra generator of `Y` outside `Y`.

Since `P^2=I`,

```text
rho(P) = C minus {-1,1},
R(lambda,P) = (lambda I + P)/(lambda^2-1).
```

Every one of these resolvents still sends the extra dual generator outside
`Y`. Thus `rho_sigma(P)` is empty despite `rho(P)` being nonempty.

The human-facing packet is `solution_packet.pdf`.

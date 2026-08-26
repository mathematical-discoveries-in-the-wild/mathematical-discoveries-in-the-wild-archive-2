# arXiv:1211.3209 — transport--entropy for Connes--Rieffel metrics

Status: `candidate scoped full resolution in the finite tracial setting`

The introduction asks whether a transportation inequality is possible for
Rieffel's state-space metric

```text
rho_L(phi,psi) = sup{|phi(a)-psi(a)| : L(a)<=1}.
```

The packet gives a complete Bobkov--Götze characterization for an arbitrary
seminorm `L` in the source's finite-tracial normal-state framework. The optimal
constant is

```text
C_L = sup_{L(a)<=1,t!=0} 2 t^(-2) log tau(exp(t(a-tau(a)1))).
```

Thus `T1(C)` holds exactly when `C >= C_L`. If the Rieffel metric has finite
state-space diameter `Delta_L`, then `C_L <= Delta_L^2/4` and

```text
rho_L(phi_f,tau) <= Delta_L sqrt(Ent_tau(f)/2).
```

Every finite-tracial compact quantum metric space satisfies this condition.
Conversely, if `ker L` contains a non-scalar self-adjoint element, an explicit
bounded finite-entropy density lies at infinite `rho_L` distance from the
trace.

The result does not address singular states or the source's separate question
whether logarithmic Sobolev inequalities imply all `L_p` Poincaré inequalities
in full generality.

- Proof packet: `solution_packet.pdf`
- Source paper: `source_paper.pdf`
- Open-question crop: `figures/open_problem_crop.png`
- Attempt audit: `runs/fa_banach_001/attempts/1211.3209_rieffel_transport_entropy.md`
- Ledger: `runs/fa_banach_001/ledger/results/1211.3209_rieffel_transport_entropy.json`

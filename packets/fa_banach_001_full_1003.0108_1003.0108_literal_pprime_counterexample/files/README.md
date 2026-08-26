# arXiv:1003.0108 — literal property (P') is false

Status: `candidate full counterexample to property (P') as printed`

Section 6 asks whether

```
mu(P0,C) > m and C stabilizes P  =>  d_nu(P,P0) <= m.
```

This is false already for the valid abstract setup `R=S=C`. Take scalar
plants and controller

```
P0=0,  P=1,  C=0,  m=1/2.
```

Then `mu(P0,C)=1`, and `C=0` stabilizes both `P0` and `P`, but normalized
coprime factors give

```
d_nu(P,P0)=1/sqrt(2)>1/2.
```

The source also says the property is known in the rational case, while this
example consists of constant rational transfer functions. The most likely
explanation is a missing or compressed quantifier: the standard theorem gives
a guarantee for every plant in a whole uncertainty ball, not a necessity
condition for each individual plant stabilized by a controller. This packet
answers the literal printed question only and does not claim to refute a
corrected robust-ball/minimal-metric formulation.

- Proof packet: `solution_packet.pdf`
- Attempt audit:
  `runs/fa_banach_001/attempts/1003.0108_literal_pprime_counterexample.md`
- Ledger:
  `runs/fa_banach_001/ledger/results/1003.0108_literal_pprime_counterexample.json`

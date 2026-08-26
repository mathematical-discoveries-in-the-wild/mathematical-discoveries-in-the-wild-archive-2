# Singleton counterexample to the toy deep-zero problem

Status: `candidate counterexample (full negative answer)`

Source: Haakan Hedenmalm, *Deep zero problems*, arXiv:2205.11213,
Problem 1.1 on PDF page 2.

## Result

The arbitrary-subset uniqueness question is false already for a singleton.
With the source's Fock-translate convention, take

```text
E = {1},  beta = 1,
f(z) = exp(-1/2-z)(z+1).
```

Then `f` is a nonzero Bargmann–Fock function and `f'(0)=0`. Also

```text
U_1 f = z,
```

so every derivative of `U_1 f` at zero whose order is outside `E` vanishes.
This is an exact counterexample to Problem 1.1.

The packet also records an infinite family: for odd `m`, a positive zero of
the Laguerre polynomial `L_m(|beta|^2)` gives a counterexample with
`E={m}` and `f=U_{-beta}(z^m)`.

## Literature boundary

A bounded search found the source and the later arXiv:2601.09080, which
answers Hedenmalm's separate Problem 5.2 and congruence-class analogues. It
does not contain the singleton obstruction.

## Files

- `main.tex`, `solution_packet.pdf`: exact counterexample and the singleton
  family calculation.
- `source_paper.pdf`: original paper.
- `verification_report.md`: proof-obligation and artifact audit.

Ledger:
`runs/fa_banach_001/ledger/results/2205.11213_singleton_deep_zero_counterexample.json`.

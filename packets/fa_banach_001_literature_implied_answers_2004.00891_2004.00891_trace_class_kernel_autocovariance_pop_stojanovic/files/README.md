# Literature-implied answer: trace-class kernel autocovariance convergence

Status: `literature_implied_answer (full trace-class conclusion)`

Source paper: Mattes Mollenhauer, Stefan Klus, Christof Schütte, and Péter
Koltai, “Kernel Autocovariance Operators of Stationary Processes: Estimation
and Convergence,” arXiv:2004.00891v2 (2022).

Supporting theorem: Zoran R. Pop-Stojanovic, “On ergodic theorem for a Banach
valued random sequence,” *Journal of the Australian Mathematical Society* 13
(1972), 501–507, DOI: 10.1017/S1446788700009253, Corollary 2.

## Identification

Remark 11 on PDF page 9 of the source paper asks whether reflexivity is
necessary for almost-sure norm convergence of Banach-valued Birkhoff averages;
the motivating unresolved case is convergence of empirical kernel
autocovariance operators in the trace norm on the nonreflexive space
`S_1(H)`.

Pop-Stojanovic's Corollary 2 (journal page 505, proof on page 506; PDF pages
5–6) gives almost-sure norm convergence for every Bochner-integrable strictly
stationary Banach-valued sequence, with no reflexivity hypothesis. Applied to

```text
F_t = phi(X_{t+eta}) tensor phi(X_t) in S_1(H),
```

the second-moment assumption in the source paper implies
`E ||F_0||_1 < infinity` by Cauchy–Schwarz and the rank-one identity
`||u tensor v||_1 = ||u|| ||v||`. Ergodicity makes the invariant conditional
expectation equal to `E F_0 = C(eta)`. Hence, for every fixed lag `eta`,

```text
||C_n(eta) - C(eta)||_{S_1(H)} -> 0 almost surely.
```

Thus reflexivity is not necessary here, even in infinite dimension. Since
`||A||_{S_p} <= ||A||_{S_1}` for `1 <= p <= infinity`, the same conclusion
also yields convergence in every Schatten norm.

## Provenance and scope

This is an agent-identified implication of a theorem published in 1972, not a
new mathematical result. The supporting paper does not mention kernel
autocovariance operators or arXiv:2004.00891. The identification fully answers
the trace-class question motivating Remark 11 under the source paper's stated
stationarity, ergodicity, measurability, and second-moment assumptions, for
each fixed lag. It does not assert one common null set simultaneously for an
uncountable family of lags; the paper uses integer lags, so countably many lags
can be handled simultaneously by intersecting the probability-one events.

## Packet files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: arXiv:2004.00891v2.
- `supporting_paper_pop_stojanovic_1972.pdf`: decisive 1972 theorem.

Ledger record:
`runs/fa_banach_001/ledger/results/2004.00891_trace_class_kernel_autocovariance_pop_stojanovic.json`.

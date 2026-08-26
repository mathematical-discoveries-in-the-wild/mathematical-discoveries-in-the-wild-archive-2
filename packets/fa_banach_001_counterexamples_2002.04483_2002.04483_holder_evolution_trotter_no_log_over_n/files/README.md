# Hölder evolution–Trotter counterexample

**Status:** counterexample likely valid, pending human review  
**Source:** arXiv:2002.04483, Neidhardt–Stephan–Zagrebnov  
**Scope:** complete negative answer to the Hölder (A5) branch of the proposed
`O(log n/n)` improvement; the Lipschitz (A6) branch remains open here.

For every `0 < beta < 1`, the packet constructs the nonnegative periodic
Takagi–Landsberg function

```text
q(t) = sum_{m>=0} 2^(-m beta) dist(2^m t, Z).
```

With `X=C`, `A=I`, and `B(t)=q(t)I`, assumptions (A1)–(A5) of the source hold
for every `0 < alpha < beta`. At `n=2^M`, both endpoint quadrature rules miss
exactly the dyadic tail, giving Trotter error at least `c_beta n^(-beta)`.
Since `n^(1-beta)/log n -> infinity`, the error is not `O(log n/n)`.

Files:

- `solution_packet.pdf` — rendered proof packet
- `main.tex` — packet source
- `source_paper.pdf` — official arXiv source paper
- `figures/open_problem_crop.png` — exact page-14 question
- `code/check_dyadic_identity.py` — finite-truncation verifier

Run the check from the repository root:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2002.04483_holder_evolution_trotter_no_log_over_n/code/check_dyadic_identity.py
```

Human review should focus on the source question’s two branches and confirm
that this packet is described only as resolving (A5), not the separate (A6)
case.


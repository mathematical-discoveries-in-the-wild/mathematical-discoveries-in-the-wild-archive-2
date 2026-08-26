# Counterexample to the positive-gamma Poincare question as stated

Status: `counterexample_likely_valid (positive-gamma branch; uniform-in-lambda reading)`

Source: Hoai-Minh Nguyen, *Characterizations of the Sobolev norms and the
total variation via nonlocal functionals, and related problems*,
arXiv:2507.00842v2 (2025). Open Question 3 appears on PDF page 25, at the end
of Section 9.

## Claimed contribution

Under the natural reading that the displayed inequality is to hold uniformly
for every `lambda>0`, Open Question 3 has a negative answer for every
`gamma>0`. This is an actual parameter regime satisfying the hypothesis:
Gobbino--Picenni's Gamma-liminf theorem implies
`kappa_{N,p,gamma}>0` for all `N>=1`, `p>=1`, and `gamma>0`.

For `Q=(0,1)^N` and `u(x)=x_1`,

```text
int_{QxQ} |u(x)-u(y)|^p dx dy = 2/((p+1)(p+2)) > 0.
```

But for the intended normalized local functional,

```text
Phi_{lambda,Q}(u)
    <= lambda^p |S^{N-1}| N^{gamma/2}/gamma,
```

so `Phi_{lambda,Q}(u)+lambda^p -> 0` as `lambda -> 0+`. No finite
constant can make the proposed estimate hold uniformly in `lambda`. The
failure persists even if the constant is allowed to depend on `gamma`.

## Robustness

The paper writes `Phi_lambda(u)` although `u` is defined only on `Q`; the
domain-correct reading is `Phi_{lambda,Q}(u)`. If instead one extends `u` by
zero and uses the normalized global functional, the same counterexample works:

```text
Phi_lambda(u 1_Q)
    <= (2 |S^{N-1}|/gamma) lambda^{p^2/(p+gamma)} -> 0.
```

The source TeX also drops `lambda^p` in one global definition, while the local
definition and all subsequent identities use it. The packet follows the
mathematically consistent normalized definition.

## Verification

The analytic proof is exact and uses no numerical evidence. The separate
verification note audits:

- the exact oscillation integral;
- finiteness of the positive-gamma kernel on a bounded cube;
- the global-zero-extension estimate;
- positivity of `kappa` via clipping and Gobbino--Picenni's theorem;
- the free-parameter/quantifier issue in the source question.

Verdict: likely valid. The main human-review question is interpretive: whether
Open Question 3 intended all `lambda>0`, as its free displayed parameter and
its model Poincare inequality suggest, or only the asymptotic range
`lambda -> +infinity` when `gamma>0`.

## Novelty and scope

The bounded search on 11 August 2026 covered the run's lightweight indexes,
the exact arXiv id and title, exact-phrase searches for Open Question 3, the
terms `nonlocal Poincare`, `Phi_lambda`, and `kappa_{N,p,gamma}`, the source
paper's references, and arXiv:2311.05560. No later source stating this
small-lambda counterexample or an answer to Open Question 3 was found. This
supports but does not certify novelty.

The result settles the positive-gamma branch **as stated under the uniform
reading**. It does not settle `gamma<=-1`, and it does not refute a repaired
positive-gamma question restricted to sufficiently large `lambda`.

Human review recommendation: send to an analyst familiar with nonlocal
Sobolev/BV functionals. The proof itself is elementary; the reviewer should
focus on the intended quantifier and the source's `Phi_lambda` versus
`Phi_{lambda,Q}` notation.

Files:

- `source_paper.pdf`: arXiv:2507.00842v2.
- `supporting_paper_2311.05560.pdf`: the Gamma-liminf theorem used to verify
  `kappa_{N,p,gamma}>0`.
- `figures/open_problem_crop.png`: Open Question 3 on source PDF page 25.
- `main.tex`, `solution_packet.pdf`: formal counterexample packet.
- `verification.md`: adversarial proof audit.


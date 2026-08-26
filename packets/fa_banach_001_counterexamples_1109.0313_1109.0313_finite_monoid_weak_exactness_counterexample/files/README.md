# Counterexample packet: weak exactness of Hopf--von Neumann preduals

Status: `candidate_counterexample_likely_valid`

Source: Ronald G. Douglas and Piotr W. Nowak, *Every finitely generated group
is weakly exact*, arXiv:1109.0313, Question 17 in Section III (printed page
10).

## Result

Question 17 has a negative answer under the definitions printed in the
source. Let `S={0,1,2}` be the monoid with table

```text
    0 1 2
0 | 0 0 2
1 | 0 1 2
2 | 0 2 2
```

For the finite-dimensional commutative Hopf--von Neumann algebra
`M=ell_infty(S)` with `Delta f(s,t)=f(st)`, the predual is
`A=ell_1(S)`. Let `phi` be augmentation, let `X=C_phi`, and let
`E=C 1_{1}` inside `L(X,M)=M`. The left and right actions on `E` are the
two characters

```text
phi(a)=a_0+a_1+a_2,    psi(a)=a_1.
```

The map `D(delta_0)=1_{1}`, `D(delta_1)=D(delta_2)=0` is a bounded
derivation. Every inner derivation has values `lambda*(1,0,1)` on the three
point masses, while `D` has values `(1,0,0)`. Thus
`H^1(A,E) != 0`, so `A` is not weakly exact.

The coproduct is normal, unital, coassociative, and injective. The coefficient
module is an `A`-bimodule, an `M`-module, and weak-star operator closed. The
construction therefore meets all hypotheses stated in the source.

## Files

- `main.tex`: self-contained proof, convention note, novelty bounds, and
  review checklist.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source page containing Definitions 15--16
  and Question 17.
- `code/verify_counterexample.py`: direct finite verification of every
  algebraic identity used in the example.
- `code/search_finite_semigroups.py`: exact exhaustive order-two/order-three
  discovery search.
- `verification.md`: commands, outputs, and final render audit.
- `tmp/`: LaTeX intermediates and rendered inspection pages.

## Convention and scope

The source first says `X` is a right `A`-module and displays actions using
`xa`, but Definition 16 later says “left.” Here `X=C` carries the augmentation
action on both sides, while the proof uses the displayed formulas. Human
review should check this wording point and the orientation of the natural
dual action.

The result concerns the broad Hopf--von Neumann definition used in the source.
It does not claim a counterexample inside a narrower locally compact quantum
group class with extra antipode, cancellation, or Haar axioms.

## Novelty status

On 2026-08-09, the cheap run indexes, the local full-source arXiv corpus, and
exact official-arXiv searches for the question and its core terminology found
only the source paper, not a later answer. Novelty is plausible within those
bounds, not publication-level certified.

Ledger:
`runs/fa_banach_001/ledger/results/1109.0313_finite_monoid_weak_exactness_counterexample.json`

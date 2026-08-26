# Model-space Bessel systems via the vectorial Hankel RKT

Status: `literature_implied_answer (full positive answer)`

Source: Alberto Dayan, *Weakly Separated Bessel Systems of Model Spaces*,
arXiv:2102.03447v2 (2021), Question 2.5 on PDF page 8.

Supporting theorem: Sergei Treil, *A remark on the reproducing kernel thesis
for Hankel operators*, arXiv:1201.0063v2 (2012), Theorem 1.1 on PDF page 2.

## Answer

Yes, for every sequence of inner functions, and hence in particular for every
sequence of Blaschke products.  If

```text
C = sup_{z in D} sum_n (1 - |Theta_n(z)|^2) < infinity,
```

then the model spaces `K_{Theta_n}` form a Bessel system with Bessel bound at
most `4 e C`.

## Identification

Let `P_-` be the projection onto the strictly negative Hardy frequencies and
put `E = ell^2`.  The hypothesis at `z=0` implies

```text
Phi = (P_- conjugate(Theta_n))_n belongs to H^2_-(E).
```

It therefore defines a vectorial pre-Hankel operator

```text
Gamma f = (P_-(conjugate(Theta_n) f))_n.
```

For every inner `Theta` and every `f in H^2`, multiplication by `Theta` is an
isometry and

```text
Theta P_-(conjugate(Theta) f) = P_{K_Theta} f.
```

Consequently, for every normalized Szego kernel `k_z`,

```text
||Gamma k_z||^2
  = sum_n ||P_{K_{Theta_n}} k_z||^2
  = sum_n (1 - |Theta_n(z)|^2)
  <= C.
```

Treil's Theorem 1.1 applies to possibly vectorial pre-Hankel operators with
scalar domain and gives `||Gamma|| <= 2 sqrt(e C)`.  Hence

```text
sum_n ||P_{K_{Theta_n}} f||^2 <= 4 e C ||f||^2,
```

which is exactly the Bessel-system condition.  The converse is immediate by
testing the Bessel inequality on `k_z`, so the two conditions are equivalent.

## Provenance and scope

This packet is filed as a literature-implied answer rather than a new full
solution.  Treil's theorem predates Dayan's question and expressly covers the
vectorial target space needed here, but it does not mention model spaces or
Dayan's later question.  The decisive link is the projection/Hankel identity
above, identified in this run.  Dayan's bibliography does not cite Treil.

The answer has no restriction to finite Blaschke products, degree-one factors,
or finite sequences.  It covers arbitrary countable sequences of inner
functions.  The numerical constant `4e` is inherited from Treil's explicit
bound and is not asserted to be sharp.

## Search bounds

The run's cheap indexes were searched for arXiv:2102.03447, its title, the
exact displayed condition, model-space Bessel systems, vectorial Hankel
operators, and the reproducing-kernel thesis.  A bounded web/arXiv search for
the exact question and close variants found the source paper and its published
version but no later paper explicitly answering Question 2.5.  Searching the
operator-theoretic reformulation found Treil's arXiv:1201.0063, whose Theorem
1.1 is the decisive prior result.

## Files

- `source_paper.pdf`: Dayan's source paper.
- `supporting_paper_1201.0063.pdf`: Treil's supporting theorem.
- `figures/open_problem_crop.png`: Question 2.5 and Remark 2.6.
- `figures/supporting_theorem_crop.png`: Treil's vectorial RKT.
- `main.tex` and `solution_packet.pdf`: formal identification and proof.
- `verification_report.md`: proof-obligation audit.

Ledger:
`runs/fa_banach_001/ledger/results/2102.03447_model_spaces_via_vectorial_hankel_rkt.json`.


# Finite-dimensional counterexamples to the projection-band inverse-limit question

Status: `counterexample_likely_valid`

Source: Walt van Amstel and Jan Harm van der Walt, *Limits of vector
lattices*, arXiv:2207.05459, Remark 4.12 and the question on PDF page 23.

## Claimed contribution

The universal question is false exactly as stated. For every integer `n >= 1`,
the coordinate vector lattice `E = R^n` is Dedekind complete, but no proper
ideal `M` in its Boolean algebra of projection bands can make the canonical map

```text
P_M : E -> inverse_limit(I_M)
```

an isomorphism. In fact, `P_M` is never injective.

## Proof intuition

The projection bands of `R^n` are the coordinate subspaces `B_A`, indexed by
subsets `A` of `{1,...,n}`. A proper ideal in this finite Boolean algebra has a
largest member `B_U`. Properness forces `U` to omit a coordinate `j`. Every
projection belonging to the ideal therefore kills the basis vector `e_j`, so
the combined canonical map kills `e_j` as well.

This is the finite-Boolean-algebra obstruction behind the example: a finite
proper band ideal cannot separate points.

## Verification

The argument uses only the definitions in the source paper. The verifier report
checks the hypotheses, the finite-join step, the complementary coordinate, and
the kernel calculation separately. No numerical or computer-assisted step is
needed.

Verifier focus:

- Confirm that the question is read universally, as its phrase “Given a
  Dedekind complete vector lattice” naturally indicates.
- Confirm that the non-trivial-ideal convention from Example 4.11 is inherited.
  If the trivial ideal is permitted instead, the conclusion remains false:
  its inverse limit is zero and the canonical map is not injective.
- Confirm the scope caveat: the packet does not settle the repaired question
  restricted to infinite-dimensional lattices.

## Novelty and scope

The bounded novelty check on 2026-08-09 searched the run's four lightweight
indexes for arXiv:2207.05459, the title, and the projection-band/inverse-limit
phrases. It also searched the web/arXiv for the exact question, `proper ideal`
with `projection bands`, and `Dedekind complete vector lattice` with `inverse
limit`. The searches returned the source paper and its published version, but
no later paper explicitly answering this question.

This is a complete negative answer to the literal universal question, not a
solution of the natural infinite-dimensional repair. The source's positive
examples are infinite-dimensional, so a reviewer may reasonably suspect that
an infinite-dimensional hypothesis was intended but omitted. The packet keeps
that distinction explicit.

Human review recommendation: quick review by a vector-lattice specialist. The
proof is elementary and exact; the main review issue is intended scope, not the
kernel argument.

Files:

- `source_paper.pdf`: arXiv:2207.05459.
- `figures/open_problem_crop.png`: the exact question on source PDF page 23.
- `main.tex`, `solution_packet.pdf`: complete counterexample packet.
- `VERIFICATION.md`: explicit verifier report.


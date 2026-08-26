# Literature-Already-Answered Packet: Exact Matrix-Cube Dilation Constant

Run: `fa_banach_001`

Result type: `literature_already_answered`

This is a later-literature status packet, not a new proof from this run.

## Source Question

- Kenneth R. Davidson, Adam Dor-On, Orr M. Shalit, and Baruch Solel,
  *Dilations, inclusions of matrix convex sets, and completely positive maps*,
  arXiv:1601.07993.
- Local PDF: `source_paper.pdf`.
- Source location: page 35, Remark 7.21. The authors ask whether the universal
  factor `d` can be improved for a particular `d`-dimensional convex body and,
  specifically, whether `d` is optimal for the cube `[-1,1]^d`.

## Supporting Literature

- Benjamin Passer, Orr M. Shalit, and Baruch Solel,
  *Minimal and maximal matrix convex sets*, arXiv:1706.05654.
- Local PDF: `supporting_paper_1706.05654.pdf`.
- Supporting locations:
  - page 2 explicitly says that the cube problem from the earlier paper had
    only the factor `d` and that the exact factor is `sqrt(d)`;
  - page 29 proves the cube containment and its optimality;
  - page 32, Theorem 6.9, proves the more general formula
    `theta(B_{p,d}) = d^(1-|1/p-1/2|)`.

## Exact Answer

Writing

```text
theta(K) = inf { C > 0 : Wmax(K) is contained in C Wmin(K) },
```

the later paper proves

```text
theta([-1,1]^d) = sqrt(d).
```

Thus `d` is not optimal when `d > 1`; the exact optimal constant is
`sqrt(d)`. Equivalently, every `d`-tuple of self-adjoint contractions dilates
to a commuting `d`-tuple of self-adjoint operators of norm at most `sqrt(d)`,
and no smaller uniform factor is possible.

## Why This Is A Direct Literature Answer

The supporting paper cites the source as reference [6], explicitly identifies
the previously unknown cube optimality problem, and states that it finds the
best cube constant. This is therefore an explicit separate-paper answer, not
an inference newly made by this run.

## Files

- `README.md`: this status summary.
- `main.tex`: compact literature-status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: original open-question paper.
- `supporting_paper_1706.05654.pdf`: answer paper.
- `tmp/`: LaTeX build intermediates and page render used for QA.

## Human Review Recommendation

Mark the cube-constant question in arXiv:1601.07993, Remark 7.21, as already
answered by arXiv:1706.05654. The exact value is `sqrt(d)`.

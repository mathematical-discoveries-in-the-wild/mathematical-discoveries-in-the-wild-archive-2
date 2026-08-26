# Counterexample: The NC Column Ball Is Not Right Regular

Status: `candidate_counterexample_likely_valid_novelty_unconfirmed`

Model: `GPT5.6`

Source: Jeet Sampat and Orr Moshe Shalit, *Weak-* and completely isometric
structure of noncommutative function algebras*, arXiv:2411.09372v2,
Example 5.9 on PDF page 23; J. Math. Anal. Appl. 550 (2025), 129552.

## Claimed contribution

For every `d >= 2`, the nc column unit ball

```text
C_d = {X : ||sum_j X_j^* X_j|| < 1}
```

is not right regular. Since `C_1` is the one-variable row ball, which is right
regular, this gives the exact classification: `C_d` is right regular if and
only if `d=1`.

More sharply, if

```text
A_N(C_d) = sup_X ||row(X^w)_{|w|=N}||,
```

then `A_N(C_d)=d^(N/2)`.

## Proof mechanism

The upper bound is immediate because a column contraction has
`||X_j|| <= 1`, so each of the `d^N` words has norm at most one.

For the lower bound, work on the finite-dimensional space with basis indexed
by words of length at most `N`. Let `L_j` be the truncated left creation
operators and put `X_j=r L_j^*`, where `0<r<1`. Then `X` lies in `C_d`, while
every word of length `N` sends its corresponding reversed basis word to the
vacuum. Consequently,

```text
||row(X^w)_{|w|=N}|| = r^N d^(N/2).
```

Letting `r` tend to one gives the exact supremum.

Now take `f_N(Z)=Z_1^N`. Its norm on `C_d` is one, and its order-`N` right TT
coefficient column has exactly one nonzero entry, the constant function one.
Thus the left side of the right-regularity estimate equals `d^(N/2)`, which
cannot be bounded by a constant independent of `N` when `d>=2`.

## Verification

The proof is exact. The reusable numerical checker constructs the finite
truncated shifts for `d=2,3` and `N=1,...,4`, checking both the column
contraction identity and the predicted word-row norm:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2411.09372_column_ball_not_right_regular/code/verify_truncated_shifts.py
```

Result: all checks passed. These checks illustrate the proof and are not used
as proof. See `VERIFICATION.md` for the explicit proof audit.

## Novelty and scope

The bounded novelty check on 2026-08-11 covered the four lightweight run
indexes, arXiv:2411.09372, the exact phrases `column unit ball` and `right
regular`, and combinations with `nc operator ball`, `truncated shift`, and
`d^(N/2)`. The current arXiv record is v2 from 2025-04-14 and points to the
2025 journal publication. Web/arXiv-facing searches found the source question
but no separate paper claiming an answer.

The search was not exhaustive, so novelty is unconfirmed. The packet should
receive an operator-algebra expert review and a deeper citation search before
any public originality claim.

Human review recommendation: high priority. The argument is elementary once
the definition is unpacked. The main check is that the constant in right
regularity is uniform in `N`, exactly what the word-row growth contradicts.

Files:

- `source_paper.pdf`: arXiv:2411.09372v2.
- `figures/open_problem_crop.png`: source PDF page 23, Example 5.9.
- `main.tex`, `solution_packet.pdf`: complete counterexample packet.
- `VERIFICATION.md`: explicit proof-audit report.
- `code/verify_truncated_shifts.py`: finite-matrix checks.


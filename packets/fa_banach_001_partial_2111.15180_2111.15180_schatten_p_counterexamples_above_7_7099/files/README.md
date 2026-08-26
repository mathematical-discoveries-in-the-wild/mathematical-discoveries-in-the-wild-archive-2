# Normal off-diagonal counterexamples for every `p > 7.7099896695...`

Status: `partial result (proved counterexample interval)`

The question after Proposition 3.4 of arXiv:2111.15180 asks for which
Schatten exponents `p` every positive block matrix

```text
H = [ A  N  ]
    [ N* B  ]
```

with normal off-diagonal block `N` satisfies `||H||_p <= ||A+B||_p`.
The source proves the assertion at `p=2`; at `p=1` it is equality by taking
traces.  It also cites operator-norm counterexamples.

This packet gives one exact rational matrix that is a counterexample for a
whole interval.  Let `q_*` be the unique solution greater than one of

```text
(35/32)^q + 2(29/64)^q = 2.
```

Then `q_* = 7.709989669514...`, and for every `p>q_*` (including
`p=infinity`) the packet's positive block matrix has a unitary off-diagonal
block but violates the inequality.  The calculation reduces exactly to

```text
(35/32)^p + 2(29/64)^p > 2.
```

The construction is a rational variant of the cyclic-unitary mechanism in
Hayashi, arXiv:1808.00181, Problem 3 and its following example.  The interval
conclusion and the chosen rational spectra are derived here.

Files:

- `main.tex`, `solution_packet.pdf`: complete proof and scope.
- `verify_counterexample.py`: exact symbolic matrix/spectrum checks and a
  high-precision bracket for `q_*`.
- `verification.md`: reproducibility record.
- `source_paper.pdf`: arXiv:2111.15180.
- `supporting_paper_1808.00181.pdf`: Hayashi's arXiv:1808.00181.
- `figures/source_question_page7.png`: the exact Schatten question.
- `figures/hayashi_problem3_page5.png`, `figures/hayashi_example_page6.png`:
  the supporting cyclic-unitary mechanism.

Scope limitation: this does not decide the universal inequality for
`1<p<2` or for `2<p<=q_*`.  Eight focused upgrade routes are recorded in
`runs/fa_banach_001/attempts/2111.15180_schatten_p_full_characterization_upgrade_attempts.md`.


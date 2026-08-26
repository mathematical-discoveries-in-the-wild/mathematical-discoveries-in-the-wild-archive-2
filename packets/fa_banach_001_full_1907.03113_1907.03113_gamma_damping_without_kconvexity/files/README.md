# 1907.03113: exponential damping without K-convexity

- Status: `candidate_full_likely_valid`
- Model: `GPT5.6`
- Source: Loris Arnold, *Gamma-boundedness of C0-semigroups and their
  H-infinity-functional calculi*, arXiv:1907.03113v1
- Target: Question 5.8
- Answer: yes, K-convexity can be dropped

## Result

Let `(T_t)_{t>=0}` be a bounded semigroup on an arbitrary Banach space.  The
packet proves that the following are equivalent:

1. `{T_s:0<=s<1}` is gamma-bounded;
2. `{exp(-delta_0 t)T_t:t>=0}` is gamma-bounded for some `delta_0>0`;
3. `{exp(-delta t)T_t:t>=0}` is gamma-bounded for every `delta>0`.

The proof writes `t=n+s`.  The local factors are gamma-bounded, while the
discrete factors `exp(-delta n)T_n` have summable operator norms and therefore
form a gamma-bounded family.  This fully answers Question 5.8 affirmatively
without any geometric assumption on the Banach space.

As an upgrade, the packet proves on every Banach space that a C0-semigroup
which admits at least one gamma-type satisfies
`omega^gamma(A)=omega(A)`.

## Packet contents

- `main.tex` and `solution_packet.pdf`: complete proof packet.
- `source_paper.pdf`: official arXiv source PDF.
- `figures/source_question_page.png`: source-page crop containing Corollary
  5.5, Remark 5.6, and Question 5.8.
- `verification.md`: proof, novelty, and reviewer audit.
- `attempts/1907.03113_kconvex_damping_question/attempts.md`: attack and
  upgrade log.

## Limitations and review recommendation

The packet does not settle Question 5.9 or the later H-infinity-calculus
question.  Recommended for expert review as a short full solution to Question
5.8; the summable-family lemma and the growth-bound corollary are the main
review points.


# Hurwitz counterexample to cyclic Kaplansky approximants

Status: `candidate_counterexample_likely_valid` for Question 9.1 of
arXiv:2105.01110.

## Result

The proposed strengthening of Lemma 3.3 is false.  Take the normalized
complete Pick space `H^2(D)`, `m=1`, and target multiplier `phi(z)=z`.  If the
approximants could be cyclic, the lemma's norm bound and weak-star convergence
would give bounded zero-free holomorphic functions converging locally
uniformly to `z`, contradicting Hurwitz's theorem.

The answer is full for the literal Question 9.1.  It does not settle the
narrower informal target-`1` question in the sentence immediately preceding
Question 9.1.

## Files

- `main.tex`: self-contained counterexample packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv source paper.
- `figures/open_problem_crop.png`: full source page containing Question 9.1.
- `verification.md`: proof and rendering audit.

## Novelty and review focus

The 21 April 2026 source revision still asks the question.  Bounded local and
web/arXiv searches on 13 August 2026 found no explicit answer or this example.
Novelty confidence is moderate because the obstruction is elementary.

Human review should focus on the intended quantifier scope of Question 9.1:
the counterexample refutes the improvement of Lemma 3.3 for arbitrary target
`phi`, but not the target-`1` special case mentioned in the preceding prose.

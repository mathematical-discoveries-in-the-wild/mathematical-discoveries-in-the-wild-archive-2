# Tau and quasi-tau summing operators coincide isometrically

Status: `candidate_full_solution_likely_valid_needs_human_review`.

This packet gives an affirmative answer to the open problem at the end of
Geraldo Botelho and Ximena Mujica, *Spaces of sigma(p)-nuclear linear and
multilinear operators on Banach spaces and their duals*, arXiv:1608.06926,
Linear Algebra and its Applications 519 (2017), 219–237.

For all Banach spaces `E,F` and `1 <= p < infinity`,

```text
L_{tau(p)}(E;F') = L_{q tau(p)}(E;F')
```

isometrically.  The proof in fact gives the stronger multilinear and mixed
exponent identity, for every `1 <= q <= p < infinity`,

```text
L_{tau(p;q)}(E_1,...,E_n;F')
  = L_{q tau(p;q)}(E_1,...,E_n;F')
```

isometrically.

The mechanism is the principle of local reflexivity.  Given finitely many
ordinary `tau` test vectors in `F''`, it transfers their span almost
isometrically into `F` while preserving their pairings with the finitely many
operator values.  This makes the ordinary numerator exactly a quasi-`tau`
numerator.  A Hahn–Banach extension followed by Goldstine density controls
the transferred denominator by `(1+epsilon)` times the ordinary denominator.
Letting `epsilon` tend to zero yields the reverse norm inequality; the forward
inequality is the immediate restriction to the canonical copy of `F` in
`F''`.

No reflexivity or approximation property is needed.  Human review should
focus on the denominator lemma—the passage from `T*F'` in the dual of the
finite-dimensional test space to canonical elements of `F'` through
Hahn–Banach and Goldstine.  The packet makes that step explicit.

A bounded novelty search through 13 August 2026 found the authors' 2019
follow-up repeating the question as open, and found no later stated
resolution among the exact-phrase searches, the five OpenAlex-indexed citing
works, or the authors' indexed later publications.  Novelty confidence is
moderate pending specialist review; mathematical confidence is high.

The human-facing proof is `solution_packet.pdf`.  The original paper and the
open-problem crop are included locally.


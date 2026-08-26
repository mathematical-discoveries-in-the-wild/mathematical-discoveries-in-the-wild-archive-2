# Exact negative literature answer to Problem 4.15

status: `literature_already_answered`

source: Pablo Turco and Román Villafañe, *Galois connection between
Lipschitz and linear operator ideals and minimal Lipschitz operator ideals*,
arXiv:1807.10786, Problem 4.15.

supporting answer: Nahuel Albarracín and Pablo Turco, *On the Lipschitz
operator ideal Lip_0 o A o Lip_0*, arXiv:2211.14240v2, Propositions 2.13 and
2.16.

## Identification

Problem 4.15 asks whether a Banach Lipschitz operator ideal `I` must be of
composition type whenever `I^min` or `I^max` is of composition type.

The later paper explicitly gives the negative counterexample

```text
I = Lip_0 o OF o Lip_0,
```

where `OF` is the ideal of approximable linear operators. Proposition 2.13
shows that `I` is not of composition type. Proposition 2.16 shows that

```text
I^min = OF o Lip_0,
```

which is of composition type. The paper explicitly calls this a negative
answer to the source's Problem 4.15.

## Files

- `solution_packet.pdf`: checked literature-identification note.
- `source_paper.pdf`: arXiv:1807.10786, compiled verbatim from archived
  source.
- `supporting_paper_2211.14240.pdf`: the exact later answer.
- `figures/source_problem_crop.png`: source Problem 4.15.
- `figures/supporting_noncomposition_crop.png`: Proposition 2.13.
- `figures/supporting_answer_crop.png`: Proposition 2.16 proof and the
  explicit negative-answer sentence.
- `verification.md`: provenance and QA record.

## Scope

The yes/no implication in Problem 4.15 is fully answered negatively. The
later paper separately asks for other examples besides the approximable
ideal; that classification question is not part of the original problem.

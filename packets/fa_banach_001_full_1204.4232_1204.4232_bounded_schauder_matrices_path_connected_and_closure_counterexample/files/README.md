# Bounded Schauder matrices are path-connected

Status: `candidate full solution, likely valid; human review requested`.

Source: Yang Cao, Geng Tian, and Bingzhe Hou, *Schauder Bases and
Operator Theory III: Schauder Spectrums*, arXiv:1204.4232, Questions 3.8
and 3.10 on PDF page 6.

## Results

1. The norm-topological space of bounded Schauder matrices on a separable
   infinite-dimensional complex Hilbert space is path-connected. For
   `T = U|T|`, rotate the unitary polar factor `U` to the identity, then use
   the positive path `(1-s)|T| + sI`.
2. The relative norm closure of the equivalence orbit of the identity is the
   entire set of bounded Schauder matrices. Indeed,
   `U(|T| + epsilon I)` is invertible and converges to `T`.
3. Consequently, unconditionality is not preserved in orbit closure. A
   bounded conditional example is obtained by scaling any conditional
   Hilbert-space Schauder basis fast enough that its synthesis operator is
   Hilbert--Schmidt.

## Files

- `solution_packet.pdf`: rendered proof packet.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf` and `source_metadata.json`: source record.
- `figures/source_questions.png`: Questions 3.8 and 3.10.
- `verification_report.md`: proof audit and reviewer focus.

## Scope

The solution addresses the bounded-operator class and operator-norm topology
specified in source Remark 3.7. The counterexample starts from the identity;
it does not characterize orbit closures of arbitrary conditional bases.

## Novelty

Cheap run indexes and bounded exact-phrase/current-literature searches found
no prior answer to either question. Since the proof is an elementary polar
decomposition argument, it may be folklore; novelty confidence is moderate.

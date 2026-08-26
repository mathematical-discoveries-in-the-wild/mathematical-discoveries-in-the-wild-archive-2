# Counterexample: reverse weak fractional difference inequality

This packet gives a full negative answer to the reverse-inequality question
following Theorem 1.3 of arXiv:2102.09657.

For every fixed `N >= 1`, `1 < p < infinity`, and `0 < s < 1`, lacunary
modulations

```text
u_m(x) = phi(x) sum_{j=1}^m R^(-js) exp(2 pi i R^j x_1)
```

belong to the source's compact-frequency test class. Their homogeneous
Triebel--Lizorkin norms grow at least like `sqrt(m)`, whereas the weak-`L^p`
difference quotients in the question stay uniformly bounded. Hence neither
the direct reverse inequality nor the proposed holomorphic-family bound can
hold.

Files:

- `solution_packet.pdf`: self-contained proof and proof intuition.
- `source_paper.pdf`: official arXiv PDF.
- `evidence/source_question_crop.png`: unaltered crop of the exact question.
- `verify_geometric_series.py`: stress check for the uniform lacunary sum.
- `main.tex`: packet source.
- `VERIFICATION.md`: audit trail and artifact checks.

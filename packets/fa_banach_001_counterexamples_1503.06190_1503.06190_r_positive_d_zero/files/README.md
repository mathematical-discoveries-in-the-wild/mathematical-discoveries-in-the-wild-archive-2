# Positive R does not imply positive d for arbitrary Fréchet approximation schemes

Status: **candidate full counterexample, likely valid, novelty uncertain;
send to human review**.

Source question: Asuman Güven Aksoy and Grzegorz Lewicki, *Bernstein's
Lethargy Theorem in Fréchet Spaces*, arXiv:1503.06190, Remark 2.23.

## Result

Let `X=C^infinity[0,1]`, equip it with the bounded F-norm

```text
||f||_F = sum_{j>=0} 2^(-j-1) p_j(f)/(1+p_j(f)),
p_j(f) = max_{0<=k<=j} ||f^(k)||_infinity,
```

and define

```text
V_n = {f : f^(k)(0)=0 for every k>=n}.
```

Then the `V_n` are closed, strictly nested, infinite-dimensional subspaces
with dense union. Every nonzero ray saturates the F-norm, so `R(V)=1`. A
shrinking cutoff removes the one new jet between `V_n` and `V_{n+1}` and
shows `d_{n,V}<=2^(-n)`. Hence `d_V=0`.

This disproves the proposed equivalence for arbitrary approximation schemes,
even in a classical locally convex Fréchet space with closed steps.

## Files

- `solution_packet.pdf`: self-contained proof packet.
- `main.tex`: source of the proof packet.
- `problem.md`: exact formulation and scope.
- `solution.md`: plain-text proof companion.
- `verification.md`: adversarial proof audit.
- `references.md`: source and bounded novelty audit.
- `source_paper.pdf`: source paper containing Remark 2.23.
- `figures/open_problem_crop.png`: readable source-page excerpt.

No computation is used in the proof.

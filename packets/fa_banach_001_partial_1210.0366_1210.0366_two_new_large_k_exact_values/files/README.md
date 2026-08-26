# Two new exact large-k values for small subset sums

Status: **candidate proof of two previously omitted cases of Conjecture 28;
substantial partial result; likely valid, novelty uncertain; send to human
review**.

For the extremal quantity `Cbar(k,d)` in arXiv:1210.0366, the packet proves

```text
Cbar(16,6) = 17,
Cbar(40,7) = 41.
```

These fill the two endpoints immediately below the source's ranges
`k>=17` for `d=6` and `k>=41` for `d=7`. The proof retains the integer jump
parameter in the source's scalar row optimization. At these two parameters the
exact Frobenius bound forces equality in the rank inequality. The resulting
matrix must be symmetric with one nonzero eigenvalue, but its extremal row
types have an incompatible row sum.

Files:

- `solution_packet.pdf`: self-contained proof packet.
- `main.tex`: packet source.
- `problem.md`: exact source transcription and scope.
- `solution.md`: plain-text proof companion.
- `verification.md`: adversarial checks and upgrade limits.
- `references.md`: source and bounded novelty audit.
- `source_paper.pdf`: arXiv:1210.0366v2.
- `figures/open_problem_crop.png`: source Theorem 26 and Conjecture 28.
- `code/check_endpoint_maxima.py`: exact-rational sanity check.

The full assertion `Cbar(k,d)=k+1` for every `k>=2d-1` is not claimed.

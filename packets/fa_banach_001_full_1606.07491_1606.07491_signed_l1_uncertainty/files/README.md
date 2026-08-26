# Signed L1 uncertainty on the Boolean cube

Classification: candidate new full proof, likely valid, needs human review.

The packet proves the signed-function conjecture following equation (70) of
Polyanskiy--Samorodnitsky, arXiv:1606.07491.  In fact it proves the exact
finite-dimensional estimate

```text
||f||_infinity <= sqrt(C(2n,d)/C(2n,n)) ||f||_ell1
```

for every real function on `{+1,-1}^n` of Fourier-Walsh degree at most `d`.
Stirling's formula gives the conjectured exponent with an `O(log n)` remainder.

Files:

- `main.tex` -- complete proof and audit.
- `solution_packet.pdf` -- compiled review packet.
- `source_paper.pdf` -- source paper.
- `figures/open_problem_crop.png` -- exact source conjecture.
- `verify_hahn_identity.py` -- exact symbolic verification of the only special-
  function identity used in the proof.

Suggested review priorities:

1. Check the Hahn orthogonality normalization and Christoffel telescoping.
2. Check that translation and coordinate symmetrization preserve degree and the
   chosen maximum while contracting the counting L1 norm.
3. Search specifically for prior Boolean-cube L1-to-L-infinity Nikolskii
   inequalities with the constant `sqrt(C(2n,d)/C(2n,n))`.


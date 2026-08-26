# A strict upper bound for the bidisc Bohr radius

Status: **candidate substantial partial result; likely valid; human review
recommended**.

The packet proves

\[
0.3006\le K_2<\frac{313}{1000}=0.313.
\]

The lower bound is Knese's Corollary 1.2.  The new upper bound comes from an
explicit asymmetric degree-\((1,1)\) rational inner function, a disk
automorphism, and a finite exact coefficient certificate through total degree
eight.  It improves the separate later bound `K_2 < 0.3177` in Theorem 6.4 of
arXiv:2504.03236.

The proof is self-contained.  The only computer-assisted part is exact rational
arithmetic that reproduces the displayed finite certificate; it is not a
numerical dependency.

Run the verifier from this directory with:

```sh
conda run --no-capture-output -n sandbox python code/verify_certificate.py
```

Important files:

- `solution_packet.pdf`: theorem, proof, literature check, and review notes.
- `source_paper.pdf`: arXiv:2410.21693v3.
- `figures/open_problem_crop.png`: source statement on PDF page 4.
- `code/verify_certificate.py`: dependency-free exact verifier.

The original question of determining the exact value of `K_2` remains open.

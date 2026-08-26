# Positive unbounded product conjecture — answered by arXiv:1509.01571

The conjecture in Section 3 of arXiv:1401.5917 asks whether `AB` must
be self-adjoint when:

- `A` is a positive self-adjoint operator (possibly unbounded),
- `B` is bounded and self-adjoint, and
- `AB` is normal.

Gustafson and Mortad, arXiv:1509.01571, restate this as their first
main question and answer it affirmatively in Theorem 2.5.  They prove
more precisely that both `AB` and `closure(BA)` are self-adjoint and
that

```text
AB = closure(BA).
```

The packet is a literature-status identification, not a new proof.
The two bundled paper PDFs were compiled from the arXiv source trees
already present in the repository.

Build the status note with:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -jobname=solution_packet main.tex
```

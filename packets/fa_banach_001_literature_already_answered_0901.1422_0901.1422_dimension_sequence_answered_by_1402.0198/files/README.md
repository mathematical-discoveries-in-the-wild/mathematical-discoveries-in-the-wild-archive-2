# The dimension-sequence question was answered negatively

Status: **literature already answered (full negative answer)**.

Shalit--Solel, arXiv:0901.1422, ask whether every natural-number-valued
submultiplicative sequence

```text
f(m+n) <= f(m) f(n)
```

is the fiber-dimension sequence of a subproduct system.

Gerhold--Skeide, arXiv:1402.0198v2, settle the question negatively. Their
main theorem identifies subproduct-system dimension sequences with
cardinality sequences of factorial languages. The overlapping-factor map for
such a language gives the stronger necessary inequalities

```text
d_(m+n+k) <= d_(m+k) d_(n+k).
```

In particular, `d_(k+1) <= d_k^2`. Their Corollary 5.6 gives the
submultiplicative sequence `d_1=2`, `d_2=1`, `d_3=2`, and `d_k=0` for `k>3`,
which violates `d_3 <= d_2^2`. If the source's natural numbers are read as
strictly positive, the same obstruction works with `d_k=1` for every
`k>=4`; this modified sequence is still submultiplicative.

Files:

- `solution_packet.pdf`: exact question, later answer, and verification.
- `source_paper.pdf`: arXiv:0901.1422v3.
- `supporting_paper_1402.0198.pdf`: arXiv:1402.0198v2.
- `figures/source_question_crop.png`: source question on printed/PDF page 35.
- `figures/supporting_answer_crop.png`: later Corollaries 5.5--5.6 on
  printed/PDF page 14.

The identification is exact rather than merely topical: the later paper
cites Shalit--Solel and explicitly states that not every submultiplicative
sequence is a dimension sequence after transferring its word-system
corollaries to subproduct systems.


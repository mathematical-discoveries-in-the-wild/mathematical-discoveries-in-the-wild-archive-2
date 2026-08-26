# Lieb--Solovej Bergman Conjecture Answered by arXiv:2203.12349

Status: `literature_already_answered` (full problem).

Source/open-problem paper: David Békollè, Jocelyn Gonessa, and Benoît F.
Sehba, *About a conjecture of Lieb--Solovej*, arXiv:2010.14809.

Source question: equation (1.1) and the surrounding text on PDF pages 1--2
ask whether, for every real `s >= 1` and every holomorphic `F` in the
unweighted Bergman space of the upper half-plane,

```text
integral |F(x+iy)|^(2s) y^(2s-2) dx dy
 <= pi^(1-s)/((2s-1)2^(2s-2)) (integral |F|^2 dx dy)^s.
```

The source proves integer and several other special cases but says that the
non-integer case is open.

Supporting answer: Aleksei Kulikov, *Functionals with extrema at reproducing
kernels*, arXiv:2203.12349; *Geometric and Functional Analysis* 32 (2022),
938--949, DOI 10.1007/s00039-022-00608-5.

Kulikov explicitly says that his results confirm the Bergman contractivity
conjecture of Lieb and Solovej. Theorem 1.2 and Corollary 1.3 on supporting-PDF
page 3 prove contractivity between the normalized weighted Bergman spaces.
Taking `(p, alpha)=(2,2)` and `(q, beta)=(2s,2s)` gives exactly the disk form
of equation (1.1), including its sharp constant. The source's Cayley transfer
then gives the displayed upper-half-plane inequality. The case `s=1` is
equality by inspection.

This is a complete later-literature answer, not new mathematics produced by
the run. No portion of the stated inequality remains open.

Packet contents:

- `source_paper.pdf`: original arXiv:2010.14809 PDF.
- `supporting_paper_2203.12349.pdf`: Kulikov's answering paper.
- `main.tex`: compact status and normalization note.
- `solution_packet.pdf`: rendered status note.
- `verification.md`: source-location and algebra checks.
- `tmp/`: LaTeX build and render artifacts.

Ledger record:
`runs/fa_banach_001/ledger/results/2010.14809_lieb_solovej_conjecture_answered_by_2203.12349.json`.

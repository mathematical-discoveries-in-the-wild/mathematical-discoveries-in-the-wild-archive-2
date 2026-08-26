# Proper-arc quasianalytic contraction: answered by arXiv:2005.04031

Status: `literature_already_answered`

On PDF page 3 of arXiv:1712.07075, Maria F. Gamal' records the open
existence question whether there is a contraction `T` such that its
quasianalytic spectral set and spectrum coincide but are not the whole unit
circle:

```text
pi(T) = sigma(T) != unit circle.
```

Gamal's later paper arXiv:2005.04031 answers this exact existence question.
Corollary 9.7 on PDF page 27 constructs a quasianalytic contraction `R` with

```text
sigma(R) = {exp(it) : 0 <= t <= pi},
```

with unitary asymptote supported on the same semicircle.  It explicitly
concludes that `sigma(R)` equals the quasianalytic spectral set of `R` and is
not the whole unit circle.

The later abstract calls this only a “partial answer” to the broader Kérchy–
Szalai Question 2 because it does not estimate `||R^{-1}||`.  That caveat does
not weaken the answer to the exact existence question quoted in
arXiv:1712.07075.

Files:

- `source_paper.pdf`: arXiv:1712.07075; exact question on PDF page 3.
- `supporting_paper_2005.04031.pdf`: later answer; Corollary 9.7 on PDF page
  27.
- `main.tex`, `solution_packet.pdf`: compact resolution and scope audit.
- `verification.md`: source, compilation, extraction, and visual-QA record.

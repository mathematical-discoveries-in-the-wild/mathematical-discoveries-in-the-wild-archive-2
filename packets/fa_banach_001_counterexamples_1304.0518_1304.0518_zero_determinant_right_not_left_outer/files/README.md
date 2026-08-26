# Zero-determinant right outer which is not left outer

Status: `candidate counterexample (likely valid; human review requested)`

Source/open problem:

- David P. Blecher and Louis E. Labuschagne, *Outers for noncommutative
  H^p revisited*, arXiv:1304.0518, Studia Math. 217 (2013), 265-287.
- The question is on PDF page 10, immediately after Proposition 2.11: when
  `Delta(h)=0`, must right outerness of `h in H^p` imply left outerness?

Candidate result:

The answer is no.  The packet constructs a finite maximal subdiagonal algebra
`A` and a bounded element `h in A` with `Delta(h)=0` such that
`[hA]_p=H^p` but `[Ah]_p` is a proper subspace, for every
`1 <= p <= infinity`.

The construction uses the operator-valued classical Hardy algebra over a
Bernoulli crossed-product finite von Neumann algebra.  A nonconstant inner
factor

`v(z)=(zu-r)(1-rzu)^{-1}`

is left-multiplied by a bounded full-support diagonal `d`.  The random variable
`d^{-2}` has a tail heavy enough that the shifted inverse-weight model-space
energy diverges for every nonzero defect vector.  Consequently `dvA` is dense.
On the other side, `d` is left outer and right multiplication by `v` is an
isometry, so the closure of `Adv` is the proper inner subspace `H^2v`.

Verification focus:

- Check the orientation of the two module closures in the model-space step.
- Check the formula for `H^2 \ominus vH^2` as the range of the normalized
  resolvent kernel of the shift `W=L_{zu}`.
- Check the extended-positive quadratic-form calculation through the canonical
  expectation onto the Bernoulli base algebra.
- Check the use of the second Borel-Cantelli lemma for the independent shifted
  coordinates.

Novelty check:

A bounded search on 2026-08-09 covered the run indexes and local arXiv source
corpus, exact web/arXiv phrase searches for determinant-zero left/right
outerness, and the OpenAlex citation graph of DOI 10.4064/sm217-3-4 (37 records,
of which seven were substantive mathematical citing works).  Later papers on
Orlicz, symmetric, and Haagerup Hardy spaces were transfer/extension papers;
no explicit resolution or counterexample to this question was found.  This is
not proof of novelty, so the originality claim remains subject to specialist
review.

Files:

- `solution_packet.pdf`: complete proof packet.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source question on PDF page 10.


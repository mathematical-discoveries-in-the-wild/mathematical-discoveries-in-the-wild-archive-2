# Full intrinsic answer: mixed tail diameters on finite half-open partitions

status: full_solution_likely_valid

source: Erik Talvila, *The regulated primitive integral*,
arXiv:0911.2931, convergence section, PDF page 36.

## Result

For a sequence (F_n) in B_R and a nonempty set E in the extended real
line, define

    Delta(E) = sup_{x,y in E} lim_{N->infinity}
                 sup_{n,m>=N} |F_n(x)-F_m(y)|.

Then (F_n) converges pointwise on the extended line to a member of B_R if
and only if, for every epsilon>0, the extended line admits a finite
partition

    [-infinity,a_1], (a_1,a_2], ..., (a_(q-1),infinity]

on each cell I of which Delta(I)<epsilon.

The condition is intrinsic to the sequence: no candidate limit appears in
it.  The first cell encodes the normalization and left endpoint limit, the
right-closed convention encodes left continuity, and the last cell encodes
the limit at positive infinity.

## Main idea

At each fixed pair x,y, the two-index tail diameter converges to
|F(x)-F(y)| whenever a pointwise limit F exists.  Thus the criterion becomes
exactly the finite half-open step-partition characterization of a regulated
left-continuous function.  Conversely, the condition on singleton subsets
forces pointwise Cauchy convergence, and the same partitions build
left-continuous regulated step functions converging uniformly to the limit.

The order of operations is sharp.  Shrinking pulses

    F_n = 1_(0,1/n]

converge pointwise to zero, although their right traces at zero never
converge and every spatial-supremum-first/equiregulated variant fails.

## Verification and novelty bound

- The complete equivalence, endpoint conventions, and step-function
  construction are proved in main.tex and re-audited in verification.md.
- The source question is preserved as a readable crop from PDF page 36.
- Searches on 2026-08-17 covered the run indexes, the local arXiv corpus,
  exact source/title phrases, pointwise convergence of regulated functions,
  equiregulation, quasi-uniform convergence, bounded epsilon-variation, and
  pointwise selection principles.  They found sufficient criteria but no
  later exact answer to this source question.
- Novelty confidence is bounded: the theorem is an elementary intrinsic
  characterization, and a standard equivalent formulation may exist outside
  the searched sources.

## Files

- main.tex: theorem, proof, sharpness example, and integral corollary.
- solution_packet.pdf: rendered review packet.
- source_paper.pdf: arXiv:0911.2931.
- figures/open_problem_crop.png: source statement on PDF page 36.
- verification.md: proof and rendering audit.

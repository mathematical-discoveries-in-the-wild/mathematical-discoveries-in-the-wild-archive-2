# Symmetric tensor stability implies tensor stability

**Status:** candidate full proof, likely valid, requiring human review.

**Source:** G. Botelho and E. R. Torres, *Two-sided polynomial ideals on
Banach spaces*, Journal of Mathematical Analysis and Applications 462 (2018),
900--914, DOI 10.1016/j.jmaa.2017.12.054; circulated as *Polynomial ideals
from a nonlinear viewpoint*, arXiv:1603.00246. The target is the open question
on source PDF page 27 (printed page 26).

The source asks whether every symmetrically tensorstable (`s-tensorstable`)
p-normed operator ideal is tensorstable. The packet proves the answer is yes.
In fact, only stability under symmetric squares is needed.

Given two ideal operators, normalize them and put them on the diagonal of an
operator between finite `ell_1` sums. The ordinary projective tensor product
of the two original operators is exactly the mixed coordinate block of the
symmetric square of this one diagonal operator. Uniformly bounded
symmetrization and coordinate-extraction maps recover that mixed block. The
p-triangle inequality supplies a product norm estimate, and iteration gives
all tensor powers.

If the symmetric-square constant is `C_2`, the proof gives the safe (not
claimed optimal) two-operator constant

    K = 2^(2+2/p) C_2,

and n-fold constants `K^(n-1)`.

Files:

- `solution_packet.pdf` -- theorem, complete proof, and novelty audit
- `source_paper.pdf` -- arXiv:1603.00246v1
- `figures/open_problem_crop.png` -- complete source question
- `verification.md` -- adversarial check of every load-bearing map
- `code/make_open_problem_crop.py` -- reproducible source crop

**Human-review focus:** verify the convention-dependent factor `2` in the
mixed-coordinate extraction map, the symmetric projective norm bound for the
embedding map, and whether any non-indexed post-2018 source already records
this short block-diagonal argument.

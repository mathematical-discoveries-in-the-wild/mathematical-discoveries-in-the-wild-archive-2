# A weak-star-convergent-basis obstruction for Problem 6.8

**Status:** candidate partial result, likely valid, requiring human review.

**Source:** Carlo Alberto De Bernardi, *Unit balls of polyhedral Banach
spaces with many extreme points*, Studia Mathematica 275 (2024), 175--196,
DOI 10.4064/sm230710-31-12; arXiv:2303.10023. The target is Problem 6.8 on
source PDF page 20.

Problem 6.8 asks whether an infinite-dimensional polyhedral Lindenstrauss
space can already have its given unit ball equal to the closed convex hull of
its extreme points. The packet rules out a broad canonical class: real
preduals `X` of `ell_1` for which, under some isometric identification
`X*=ell_1`, the standard basis is weak-star convergent.

Such a space is isometric to

    W_f = {x in c : lim x_n = sum f_n x_n}

for the weak-star limit `f` with `||f||_1 <= 1`. The packet determines the
extreme points of `B_{W_f}` exactly. If `||f||_1<1`, there are none. If
`||f||_1=1`, every extreme point is a convergent sign sequence and, on the
support of `f`, is forced to equal either `sgn(f)` or its negative. Therefore,
when the support has at least two coordinates, all convex combinations of
extreme points satisfy a nontrivial coordinate equation while `B_{W_f}` does
not. When the support has one coordinate, `W_f` is isometric to `c`, which is
not polyhedral. Hence no member of this class solves Problem 6.8.

This includes the standard hyperplane constructions used to produce
polyhedral Lindenstrauss spaces with extreme points. It does not decide
Problem 6.8 for preduals whose dual atoms have no convergent enumeration, and
it does not settle Problems 6.3 or 6.10.

Files:

- `solution_packet.pdf` -- complete theorem, proof, scope, and search audit
- `source_paper.pdf` -- arXiv:2303.10023v1
- `figures/open_problem_crop.png` -- Problem 6.8 and its immediate context
- `verification.md` -- adversarial proof and rendering checks
- `code/make_open_problem_crop.py` -- reproducible evidence crop

**Human-review focus:** check the annihilator argument identifying an
arbitrary weak-star-convergent-basis predual with `W_f`, and the exact
extreme-point characterization in Lemma 2.

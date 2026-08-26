# No Lipschitz tube-holomorphic separator on a space containing c0

**Status:** candidate full solution, likely valid, requiring human review.

**Source:** D. Azagra, R. Fry, and L. Keener, *Real analytic approximation
of Lipschitz functions on Hilbert space and other Banach spaces*,
arXiv:1005.1050v5; Journal of Functional Analysis 262 (2012), 124--166.
The question appears on PDF page 4 immediately after Theorem 2.

The source asks whether `c0` has the Lipschitz real-analytic separating
function appearing in Theorem 2, whose holomorphic extension is Lipschitz on
a complex tube of fixed positive width.

The answer is **no**.  More strongly, no real Banach space containing an
isomorphic copy of `c0` admits such a function.  On a `c0`-basic sequence
`(u_n)`, every homogeneous Taylor polynomial has summable diagonal values
`(P(u_n))`.  Therefore the scalar restrictions `F(z u_n)` tend to zero for
small real `z`.  Global Lipschitz control of the holomorphic extension makes
these restrictions a normal family on one common horizontal strip; the
identity theorem propagates the convergence to every fixed real `z`.  This
contradicts the linear lower bound required of a separating function at a
fixed large multiple of `u_n`.

Files:

- `solution_packet.pdf` — human-readable theorem and proof
- `source_paper.pdf` — arXiv:1005.1050v5
- `figures/open_problem_crop.png` — Theorem 2 and the question on source page 4
- `verification.md` — proof and literature-audit report

**Scope caveat:** this fully answers the explicit Theorem 2 hypothesis in
which the holomorphic extension itself is Lipschitz on the fixed-width tube.
If “such” in the following sentence were intended to ask only for a
real-axis Lipschitz function with an arbitrary, not necessarily Lipschitz,
holomorphic extension to a tube, that weaker variant is not decided here.

**Human-review focus:** verify the root-of-unity diagonal lemma, the use of
Montel compactness on the scalar strip, and the interpretation of “such” as
the explicit property stated in Theorem 2.

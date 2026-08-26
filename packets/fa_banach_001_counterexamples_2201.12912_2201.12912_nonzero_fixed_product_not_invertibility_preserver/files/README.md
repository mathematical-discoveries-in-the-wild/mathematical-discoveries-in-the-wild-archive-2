# A nonzero fixed-product preserver that destroys invertibility

**Status:** candidate full counterexample, likely valid, requiring human
review.

**Source:** Hayden Julius, *Fixed product preserving mappings on Banach
algebras*, arXiv:2201.12912; Journal of Mathematical Analysis and
Applications 517 (2023), 126615. The target is Problem 3.5 on PDF page 6.

Problem 3.5 asks whether, under the hypotheses of Theorem 3.3, a nonzero
target product `d` forces the bijective continuous linear map to preserve
invertibility. The answer is **no**.

The packet constructs a separable commutative unital Banach algebra `E` with
dense invertible group, a bounded linear involution `Phi:E->E`, and a nonzero
idempotent `c=d` such that

    xy = c  implies  Phi(x)Phi(y) = d,

but `Phi` maps the unit of `E` to a noninvertible element. The mechanism is a
direct product with the unitization of the radical weighted convolution
domain `ell_1(N_{>=1}, exp(-n^2))`.

Files:

- `solution_packet.pdf` — construction, theorem, and proof
- `source_paper.pdf` — arXiv:2201.12912
- `figures/open_problem_crop.png` — Problems 3.4 and 3.5 on source PDF page 6
- `verification.md` — detailed hypothesis and artifact checks

**Human-review focus:** verify the spectral-radius proof that the weighted
convolution algebra is radical, the characterization of units in its
unitization, and the quantifier `xy=c` in the direct-product argument. A
specialist literature check is also recommended because the bounded audit did
not exhaust all seven publisher-listed citing works.


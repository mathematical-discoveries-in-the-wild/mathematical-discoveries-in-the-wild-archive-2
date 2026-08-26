# arXiv:2507.13121 — no cumulative Blaschke basis of the disk algebra

Status: `literature_implied_full_answer`.

Source paper: Emmanuel Fricain, Javad Mashreghi, Mostafa Nasri, and Maëva
Ostermann, *Schauder Basis with Finite Blaschke Products*, arXiv:2507.13121v2.

Question 7.4 asks whether the cumulative finite Blaschke products associated
with a non-Blaschke sequence can form a Schauder basis of the disk algebra.
The answer is **no**.

The key older result is Theorem 4 of Ivan V. Ivanov and Boris Shekhtman,
*Linear discrete operators on the disk algebra*, Proc. Amer. Math. Soc. 129
(2001), 1987–1993, DOI `10.1090/S0002-9939-00-05774-9`: no sequence of
point-interpolation projections on the disk algebra converges strongly to the
identity.

If the Blaschke products were a basis, its `N`th partial-sum projection would
be the Hermite interpolation projection modulo the ideal `B_N A(D)`.  For
distinct zeros this is already a point-interpolation projection, contradicting
Ivanov–Shekhtman.  Repetitions cause no gap: split each finite multiset of
zeros into nearby distinct points.  Divided-difference confluence shows that
the resulting Lagrange projection converges in operator norm to the Hermite
projection.  Choosing the splitting at stage `N` within `1/N` would therefore
produce forbidden point-interpolation projections converging strongly to the
identity.

The printed indexing `(B_n)_{n>=1}` also has an immediate literal obstruction:
every such function vanishes at `lambda_1`.  The packet proves the stronger,
clearly intended statement after adjoining `B_0=1`.

Artifacts:

- `solution_packet.pdf`: rendered answer and proof.
- `source_paper.pdf`: arXiv source PDF containing Question 7.4.
- `figures/question_7_4_crop.png`: exact source crop.
- `verification.md`: proof and source checks.
- `evidence_sources/README.md`: primary literature metadata and theorem scope.


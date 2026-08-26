# Verification report

Verdict: `literature implied answer; exact for n>=3`.

- Source Question 4.6 is on PDF page 24 of arXiv:1711.10238 and asks whether
  `SL_n(Z)` is 2-Kazhdan, at least for large `n`.
- Bader--Sauer, arXiv:2308.06517v3, Theorem A on PDF page 2 proves that
  `SL_n(Z)` has property `(T_{n-2})`. For `n>=4`, this kills degree-two
  cohomology for every unitary representation with no invariant vectors.
- The same paper's formula (1), PDF page 2, shows that continuous degree-two
  cohomology of `SL_n(R)` with trivial coefficients is zero for `n>=3`.
  Theorem C, PDF pages 2--3, transfers it to the lattice in degrees below
  `rank(SL_n(R))=n-1`; hence `H^2(SL_n(Z),C)=0` for `n>=4`.
- For an arbitrary unitary representation `V`, the orthogonal splitting
  `V=V^Gamma direct-sum (V^Gamma)^perp` splits cohomology. The second summand
  vanishes by property `(T_{n-2})`. Since `SL_n(Z)` is of finite type in degree
  two, the trivial action on `V^Gamma` gives
  `H^2(Gamma,V^Gamma)=H^2(Gamma,C) tensor V^Gamma=0`.
- Brück--Hughes--Kielak--Mizerka, arXiv:2410.22310, Theorem 1.1 on PDF page 2
  gives a finite-dimensional orthogonal `pi_3` with
  `H^2(SL_3(Z),pi_3) != 0`, proving the negative `n=3` case.
- The literature relation was found by exact-question, exact-title,
  `2-Kazhdan`, and `SL_n(Z)` unitary-cohomology searches through 11 August
  2026. It is an agent-identified implication and is therefore stored under
  `literature_implied_answers`.
- The compact packet compiled without warnings, both final pages were
  rendered to RGB PNGs, and each was inspected at original resolution.

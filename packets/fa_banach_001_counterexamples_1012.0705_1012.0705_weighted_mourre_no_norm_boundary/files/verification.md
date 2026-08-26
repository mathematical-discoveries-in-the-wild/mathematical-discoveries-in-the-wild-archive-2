# Verification Record

- Target: the question in the introduction of arXiv:1012.0705v3 asking
  whether the weighted Mourre/localised Putnam approach gives continuity
  results for norm boundary values of the sandwiched resolvent.
- The exact open sentence, Theorem 1.1, and the abstract Theorems 3.4--3.5
  were cross-checked against the parsed TeX and source PDF.
- Cheap indexes and bounded exact-sentence, title, arXiv-id, citation,
  weighted-Mourre, localised-Putnam, boundary-value, and Hölder-continuity
  searches through 17 August 2026 found no answer.  arXiv:1610.04369 repeats
  the limitation in 2017; arXiv:2002.04909 says in 2020 that the
  contradiction proof gives no continuity description.
- Proof audit:
  1. `g'(p)=(1+p^2)^(-2)` and the commutator sign give
     `[Q,iB_0]=(1+P^2)^(-2)=D^2`;
  2. scaling gives `[delta_n Q,iB_0]=C_n^2` and
     `C_n(delta_n Q-z)^(-1)C_n=S(z/delta_n)`;
  3. the direct-sum operators are self-adjoint/bounded/injective as claimed,
     and there is no pure point subspace;
  4. the cutoff conjugations are uniformly bounded by the displayed exact
     commutator expansion;
  5. the one-block Sokhotski--Plemelj limit is operator-norm convergence
     because `D:L^2(R)->H^2(R)` and the distributional error is uniformly
     `O(tau log(2/tau))` on products of `H^2` unit balls;
  6. the imaginary evaluation term makes the one-block limit nonzero;
  7. the dyadic escape argument gives a fixed positive lower bound against
     the unique candidate global limit at every height `eta>0`.
- Auxiliary command:

  `conda run --no-capture-output -n sandbox python code/verify_scaled_blocks.py`

  Result: the symbolic derivative and scaling identities passed; 100 dyadic
  heights times four escape thresholds passed.
- `solution_packet.pdf` was compiled after the required PDF artifact marker.
  The final LaTeX pass has no warnings, errors, overfull boxes, underfull
  boxes, duplicate destinations, or undefined references.
- The final PDF has four letter-size pages.  Text extraction confirmed the
  theorem, the nonexistence conclusion, the scope caveat, human-review
  section, and references.
- Every final page was rendered at 150 dpi and visually inspected after the
  latest source and evidence-crop edits.  There is no clipping, overlap,
  malformed equation, or bad page break.

Final SHA-256: `536ea405d7f13e352433a4260717451f3599427f702a8e10dccb7bc662f75f7b`.

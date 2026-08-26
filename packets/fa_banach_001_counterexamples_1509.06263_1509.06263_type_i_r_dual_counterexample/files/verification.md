# Verification report

Verdict: `candidate counterexample likely valid`.

## Mathematical audit

1. **Base frame.**  For `h=q^(-1/2)1_[0,1)`, split `m=qk+j`.  For each fixed
   translation interval and residue `j`, the modulations form an orthonormal
   basis scaled by `q^(-1/2)`.  Summing the `q` coefficient identities gives
   Parseval exactly.
2. **Adjoint normalization.**  Since `ab=1/q`, the normalized adjoint atoms
   are `sqrt(q)E_mT_{qn}h=E_m1_[qn,qn+1)`, an orthonormal family.
3. **Zak transform.**  Partitioning `R` into `t+r+qk` and applying Fourier
   series in `k` proves unitarity.  Direct substitution gives the two scalar
   coordinate multipliers for `E_1` and `T_q` and identifies the adjoint span
   with the first component.
4. **Commutation.**  `E_1,T_q` commute with every `E_{m/q},T_n`, and commute
   with each other.  Their joint bounded Borel functional calculus therefore
   supplies a positive invertible operator `A` in the primal commutant which
   also commutes with all adjoint shifts.
5. **Two frame operators.**  The identity `S_g=A^(1/2)S_hA^(1/2)=A` follows
   from commutation and `S_h=I`.  Applying `A^(1/2)` to the adjoint ONB leaves
   its span invariant and makes its frame operator `A` restricted to that
   span, namely `M_phi`.
6. **Spectral obstruction.**  Borel injectivity of `phi` makes the constant
   function cyclic for `M_phi`.  Every vector in the `q`-component ambient
   representation has a nonzero pointwise orthogonal vector, so
   `M_phi tensor I_q` is noncyclic.  Spectral projections show that
   antiunitary equivalence preserves cyclicity.
7. **Connection to type I.**  Lemma 1.3(iii) in arXiv:1509.06263 makes
   antiunitary equivalence of the two frame operators necessary.  Its failure
   is sufficient to disprove type-I R-duality; the separate dimension
   condition need not be checked.

The proof has no numerical or computational dependency.

## Novelty audit

Local registry, solutions, attempts, and proof-gap indexes were searched.
Focused arXiv/web searches used the source id and exact combinations of
`R-dual of type I`, `adjoint Gabor system`, `counterexample`, and the authors'
names.  No answer was found.  arXiv:2408.14952 still presents the question as
open in 2024.

## Human-review focus

- Confirm that the source's Lemma 1.3(iii) uses the frame operator of the
  Riesz sequence on its closed span, as used here.
- Confirm that arbitrary bounded joint Borel functions of `E_1,T_q` lie in
  the commutant used in the frame-operator calculation.
- Check the cyclicity argument under the reviewer's antiunitary convention.

## Render audit

The packet compiled with `latexmk` without undefined references, overfull
boxes, or LaTeX warnings.  All five pages were rendered to PNG at 130 dpi and
inspected individually.  The source crop is readable, equations and theorem
statements are not clipped, page breaks are clean, and the references render
correctly.

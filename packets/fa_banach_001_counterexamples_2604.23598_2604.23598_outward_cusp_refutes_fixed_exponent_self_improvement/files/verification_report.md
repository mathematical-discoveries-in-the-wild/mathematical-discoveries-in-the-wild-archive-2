# Verification report

Result: candidate counterexample to Theorem 1.6 of arXiv:2604.23598v1 for
every `n>=2`, `p>1`, and `1/p<s<1`.

Verdict: likely valid; urgent expert review recommended.

Model: GPT5.6.

Date: 2026-08-13.

## Checks completed

- Located Theorem 1.6 and the boundary-relaxation question on official-source
  PDF page 3 and included a readable crop.
- Downloaded and retained the two supporting arXiv papers used materially.
- Recomputed the general parameter interval. At `tau=1`,
  `1+(n-1)tau=n`, strictly below both `np` and `n+(1-s)p`; therefore a
  nearby `tau>1` satisfies both inequalities.
- Checked that `q_crit=np/(n+(1-s)p)>1` follows from `sp>1` and `p>1`, and
  that `q_max=np/(1+(n-1)tau)<p`.
- Checked the power-cusp integral exactly and verified every hypothesis of
  Koskela--Zhu Theorem 1.2.
- Proved the strict embedding `W^{1,q}->W^{s,p}` directly from translation
  estimates, Sobolev/Morrey, interpolation, and the Gagliardo difference
  integral. The strict choice `q>q_crit` avoids all endpoint issues.
- Audited the homogeneous conversion: outward cusps are p-Poincare domains;
  `T(u)=E(u-u_Omega)+u_Omega` has seminorm controlled only by `grad u`.
- Checked the boundary area integral and the implication from finite
  `H^{n-1}` to zero `H^{n-1+s-1/p}`.
- Tested measure density at interior points `z_r=(r,0)`, not only at the
  boundary tip, obtaining the ratio
  `O(r^{(beta-1)(n-1)}) -> 0`.
- Recomputed the explicit planar instance:
  `(n,p,s,tau,beta,q)=(2,2,3/4,5/4,6/5,5/3)`, cusp integral `5/2`,
  `q_max=16/9`, translation exponent `4/5`, and Hausdorff exponent `5/4`.
- Compiled the packet with halt-on-error, checked the LaTeX log, rendered
  every page, and visually inspected every page.

## Computational role

None. All parameter checks and estimates are exact and analytic.

## Novelty check

The four lightweight run indexes and solution/attempt trees were searched for
the source id, title, fixed-exponent fractional extension, `(1,s,p)` extension,
and outward cusps. Bounded arXiv/web searches through 2026-08-13 used the exact
source id/title and combinations with `Theorem 1.6`, `correction`, `error`,
`counterexample`, and `outward cusp`. They found arXiv:2604.23598 and the
supporting extension-domain literature but no correction or prior statement of
this counterexample. Since the source is only months old, novelty is provisional.

## Most important reviewer checks

1. Confirm the precise use of Koskela--Zhu Theorem 1.2 with auxiliary exponent
   `tau` and model function `psi(t)=t^beta`.
2. Confirm the Poincare normalization on the homogeneous Sobolev quotient.
3. Check the translation interpolation for both `q<n` and `q>n`.
4. Confirm that the standard measure-density necessity applies to the source's
   homogeneous `(1,p)` definition.
5. Refresh the very recent literature/correction search before dissemination.

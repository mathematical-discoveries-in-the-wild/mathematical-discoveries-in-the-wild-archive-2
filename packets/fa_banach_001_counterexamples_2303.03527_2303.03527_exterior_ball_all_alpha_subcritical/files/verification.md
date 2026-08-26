# Verification report

Verdict: candidate full counterexample, likely valid.

## Formal proof audit

- The exterior ball is a \(C^\infty\) exterior domain with compact boundary.
- For every compact subset of the open exterior ball, the displayed radial
  integral and its derivative are smooth; possible divergence only at the
  boundary or infinity does not affect \(W^{1,p}_{\mathrm{loc}}\).
- The boundary primitive converges precisely when \(\alpha>1-p\).
- In the complementary branch \(\alpha\le1-p\), the tail primitive converges
  because \(N\ge2\) implies \(\alpha<N-p\).
- Substitution gives weighted radial flux \(+1\) or \(-1\), so its radial
  divergence vanishes identically.
- The constant and integral solutions are positive and nonproportional.
- The source paper states: a nonnegative operator is critical iff its equation
  has a unique positive supersolution up to scale.  The constant solution also
  supplies nonnegativity via the source's AAP theorem.  Hence two positive
  solutions force subcriticality.

No missing boundary condition is being imposed: the source definition of weak
solution is local in the open domain.

## Computational regression

Command:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2303.03527_exterior_ball_all_alpha_subcritical/code/verify_radial_flux.py
```

The script tested the exact radial-flux formula at 675 parameter/radius tuples,
including both requested endpoint families and \(p<2\), \(p=2\), and \(p>2\).
Result: `PASS: 675 radial flux identities and branch checks`.  This guards
against sign and exponent mistakes but is not used as proof.

The three-page packet was rendered and visually inspected page by page.  Its
SHA-256 digest is
`7bb7c37e0e40b5e5e80db68149b7d2ed8ac7e5705d855459c0b8bd7d6748f259`.

## Human-review focus

The core calculation is elementary and high-confidence.  Review should focus
on (i) whether the source question was intended as a universal yes/no question
or as a classification for every exterior geometry, and (ii) novelty in light
of the discarded planar seed disclosed in `novelty_search.md`.

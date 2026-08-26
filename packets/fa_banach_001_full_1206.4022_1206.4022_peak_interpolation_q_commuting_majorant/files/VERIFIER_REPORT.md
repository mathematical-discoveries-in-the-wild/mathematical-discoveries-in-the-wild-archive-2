# Verifier report

Verdict: **candidate full proof, likely valid; promote for expert review.**

## Claim checked

Under all hypotheses of Corollary 5.4 of arXiv:1206.4022 except that the
invertible positive `d` is assumed to commute with the peak projection `q`
rather than with the peak element `a`, there exists `x in A` with `xq=bq` and
`x^*x<=d`.

## Dependency audit

1. With `E=oa(1,a)`, a peak projection `q` is a closed projection in `E**`,
   and the ideal `J={h in E:hq=0}` has `J**=E**(1-q)`. This is the standard
   closed-projection/peak-ideal correspondence used in the source literature.
2. `|b|a=a|b|` implies `b^*b` commutes with `E`; weak-star passage through
   the powers of `a` makes it commute with `q`.
3. For `f=d^(-1/2)`, `fq=qf`. Hence the mixed products between all q-columns
   and `(1-q)`-columns of `X=closure(bEf)` vanish.
4. The proof correctly avoids assuming joint weak-star continuity of
   multiplication. It forms two fixed orthogonal output subspaces from all
   columns of elements of `X`; weak-operator limits stay in those subspaces.
5. A bounded net in `J` converging weak-star to `1-q` proves
   `X**(1-q) subset Y**`, while `Yq=0` gives the reverse range identity.
6. Right multiplication by `1-q` is therefore an M-projection with range
   `Y**`; standard M-ideal proximinality yields exact attainment and the
   quotient norm `dist(z,Y)=||zq||`.
7. The compression inequality gives `||b d^(-1/2)q||<=1`. The attaining best
   approximation produces the claimed `x`, and the final order calculation
   is correct.

## Adversarial checks

- The source's `2 x 2` counterexample is excluded because its `d` does not
  commute with `q`.
- The proof never commutes `d^(-1/2)` through `a`.
- It does not assume `bq=qb`.
- It uses right multiplication by the weight, matching
  `x^*x<=d iff ||x d^(-1/2)||<=1`.
- The finite-matrix check passes for a non-q-commuting `b` whose modulus has
  the required commutation.

## Residual human-review focus

An operator-algebra expert should verify the canonical embedding of `X**` as
the weak-star closure in `B**` and the standard M-ideal quotient-distance
identification. These are standard, but they carry the proof's functional
analytic load. No unproved candidate-specific lemma remains.

Novelty was not certified. Bounded local and primary-source searches through
2026-08-13 found no later answer.

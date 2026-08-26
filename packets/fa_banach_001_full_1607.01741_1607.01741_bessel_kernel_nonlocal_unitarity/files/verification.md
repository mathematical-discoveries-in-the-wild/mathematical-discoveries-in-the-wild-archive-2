# Verification record

## Mathematical audit

- Under the source's unitary Fourier convention, the bilinear kernel carries
  the factor `(2*pi)^(-n)`. Gaussian inversion therefore gives the constant
  `(4*pi)^(-n/2)` in the heat-kernel formula.
- For `Re(s)<0`, the formula follows directly from the Gamma identity and
  Fubini.
- Away from zero, the heat-kernel integral converges locally uniformly for
  every complex `s`; both it and the multiplier distribution restricted off
  zero are entire in `s`. Analytic continuation is therefore legitimate.
- For real `s`, the heat-kernel integral is strictly positive. The reciprocal
  Gamma factor is zero exactly for `s` in `N_0` and nonzero otherwise.
- The check `n=1,s=-1` gives `kappa(x)=exp(-|x|)/2`, matching the explicit
  source kernel.
- Balls compactly contained in `Omega` and `int(Omega^c)` have positive
  separation. The kernel pairing is therefore an ordinary absolutely
  convergent double integral with no diagonal distribution term.
- Nonzero nonnegative test functions on the two balls produce a nonzero
  `H^s` inner product for every `s` not in `N_0`, violating exactly the
  source's Lemma 2.10 orthogonality criterion.
- For `s` in `N_0`, the multiplier is polynomial and the source's local
  derivative argument gives unitarity for every open `Omega`.

No computational check is needed; all identities are exact.

## Scope

The result settles the unitarity conjecture in Remark 2.13. It does not solve
the paper's broader surjectivity classification for rough domains or its
half-integer image questions.

## Bounded novelty search

Checked through 2026-08-11:

- all four cheap run indexes and the registry;
- arXiv:1607.01741 and DOI `10.1515/jaa-2017-0001`;
- exact title, author, proposition/conjecture phrase, restriction unitarity,
  complement-interior, Bessel-kernel, and citation searches.

No later paper or independent resolution was found. Novelty confidence is
moderate: bounded search does not establish priority.

## Human review focus

Verify the analytic-continuation step for the off-diagonal kernel. The
remaining sign and orthogonality argument is direct.

Verdict: `candidate_full_solution`, likely valid.

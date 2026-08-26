# Verification report

Candidate: `1008.5344_random_dimer_singular_off_diagonal_ccc`

## Claim checked

The unrestricted off-diagonal-density assertion is false for a scalar
finite-range ergodic family on `ell^2(Z)` with standard one-site translations.
Separately, complete localization and a bounded-density Wegner estimate do not
imply such a density in the two-site-cell covariant extension.

## Verdict

Likely valid. Confidence: 94/100.

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Exact scalar covariance | valid | Uniform measure on the two phases of a period-two potential is ergodic under the standard one-site shift. |
| Scalar Floquet bands | valid | The two bands are `2s cos(k) +/- sqrt(a^2+4t^2 cos^2(k/2))`. |
| Scalar interband current | valid | The exact squared matrix element is `4a^2t^2 sin^2(k/2)/E(k)^2`, positive on `(0,pi)`. |
| Scalar rectangle blow-up | valid | If `2s>t^2/a`, both bands decrease on `(0,pi)`; an upper-right square at `k_0=pi/2` captures order-epsilon positive ccc mass. |
| Self-adjoint finite-range model | valid | Direct sum of bounded Hermitian 2-by-2 blocks. |
| Ergodicity and covariance | valid | The i.i.d. cell shift is ergodic; translation by two physical sites is a unitary representation of `Z`, as permitted by the source's formal definition. |
| Randomness-independent velocity | valid | Only the scalar cell potential is random, so it commutes with position; `i[H,X]` is the deterministic intra-cell matrix. |
| Eigenpairs and current weights | valid | Direct 2-by-2 computation gives energies `u+/-t`, zero diagonal current matrix elements, and squared cross weight `t^2`. |
| Infinite-volume ccc formula | valid | The trace per physical site is one half of the expected cell trace, giving the displayed factor `t^2/2`. |
| Off-diagonal singularity | valid | The measure is carried by `E_1-E_2=+/-2t`; the exact one-sided rectangle quotient at `u_0=0` for the uniform law is `t^2/(4 epsilon)`. |
| Complete localization | valid | Every bounded Borel function of `H` remains block diagonal, so separated-cell kernels vanish identically. |
| Wegner estimate | valid | Each cell has two translates of the bounded density; the expected local eigenvalue count is at most `2 ||rho||_infinity |J|` per cell. |
| Match to source question | valid with scope note | The scalar periodic-phase model refutes the unrestricted formulation exactly; neither model settles the narrower i.i.d.-per-site Anderson subclass. |

## Counterexample search and computation

The accompanying standard-library script checks three sample cell energies,
both velocity matrix elements, five-cell ccc support, four rectangle scales,
the uniform-law Wegner constant, and five Floquet momenta for positivity of the
scalar interband weight and negativity of both band derivatives. It passes.
These are sanity checks only; both computations in the proof are exact.

Command:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/\
  1008.5344_random_dimer_singular_off_diagonal_ccc/code/verify_dimer_ccc.py
```

## External dependencies

None in the proof beyond elementary Bernoulli-shift ergodicity and the source's
definition of the ccc measure. Bellissard--Hislop is cited only to delimit the
known positive literature.

## Gaps and review recommendation

No mathematical gap found. Send to human review. Review the Floquet velocity
normalization (irrelevant to singularity) and keep the stated distinction
between the unrestricted question and the canonical Anderson subclass.

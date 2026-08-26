# Constant-coefficient SOS reachability: full classification

Status: `candidate_full_counterexample_likely_valid`

Source: Julius Borcea, *Classifications of linear operators preserving
elliptic, positive and non-negative polynomials*, arXiv:0811.4374v3. The final
question on PDF page 11 asks whether every nonnegative polynomial can be
written as `T(f)` for an SOS polynomial `f` and a constant-coefficient
differential operator `T` satisfying `T(SOS(n)) subset N(n)`.

## Result

The answer is no for every `n >= 2`, and the packet gives an exact
classification:

```text
{T(f) : f is SOS and T has constant coefficients with T(SOS) subset N}
= SOS.
```

Indeed, positivity of `T(g^2)` at the origin makes every finite Hankel matrix

```text
H[alpha,beta] = (alpha+beta)! q[alpha+beta]
```

positive semidefinite. The multivariate Leibniz rule then gives

```text
T(g^2)(x) = v_g(x)^T H v_g(x),
v_g,alpha(x) = partial^alpha g(x) / alpha!.
```

A Gram factorization of `H` is therefore an explicit polynomial SOS
decomposition of `T(g^2)`. Thus every admissible operator automatically maps
SOS polynomials to SOS polynomials. The reverse reachability inclusion follows
from the identity operator.

The two-variable polynomial

```text
m(x,y) = x^4 y^2 + x^2 y^4 + 1 - 3 x^2 y^2
```

is nonnegative by AM-GM and is not SOS. The packet gives a self-contained
Newton-polytope proof using its homogeneous Motzkin form. Viewing `m` as
independent of the remaining variables gives a counterexample for every
`n >= 2`.

## Verification

- The proof covers infinite-order constant-coefficient operators: every
  polynomial uses only finitely many coefficients.
- A finite-dimensional GNS argument independently recovers the SOS output.
- The `n=2` boundary is handled explicitly, not merely by a ternary form.
- The symbolic checker verifies the Leibniz/Hankel coefficient identity, the
  four lattice points in half the Motzkin Newton polytope, and the decisive
  negative coefficient.

Run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/0811.4374_constant_coefficient_sos_reachability_classification/code/verify_hankel_motzkin.py
```

Human review should begin with the multi-index identity in equation (2.4) of
the packet. Once that identity is checked, the result is a finite Gram
factorization.

## Novelty status

Bounded local-corpus and web searches through 2026-08-13 covered the exact
question, title, DOI, constant-coefficient SOS-preserver and Hankel/Gram
phrases, and the four works in the source's OpenAlex citation record. The
related papers arXiv:0902.0279 and arXiv:2407.15654 were inspected directly.
No later statement of the automatic SOS-preservation theorem, reachability
classification, or answer to the source question was found. Novelty is
plausible, not certified.

## Files

- `main.tex`: full proof.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_question_crop.png`: page-11 source evidence.
- `code/verify_hankel_motzkin.py`: exact symbolic and combinatorial checks.
- `tmp/`: build and rendering intermediates.

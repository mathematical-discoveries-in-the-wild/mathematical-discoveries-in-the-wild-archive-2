# Ritt product spaces and the explicit Stolz conformal map

Status: `partial_result_likely_valid_full_coefficient_and_map_subresults`

Source: Stephan Fackler and Matthias Hauer, *Remarks on Ritt operators,
their H-infinity functional calculus and associated square function
estimates*, arXiv:2303.03022, open-question subsection on PDF page 15.

## Result

For `M=m_1+m_2`, the source spaces are identified exactly as

```text
S_{m_1,m_2}
 = {(1-z)^M A(z^2): coefficient_n(A)=O((n+1)^(M-1))}
 = (1-z)^M(D+1)^(M-1) H_coeff^infty(z^2).
```

Thus they depend only on `M`, and their algebraic sum is the set of finite
sums of these weighted even coefficient spaces. Every such finite sum
extends holomorphically to the full unit disc. A bounded function on the
Stolz domain with a pole at a disc point outside the closed domain proves
that this sum is proper, so the fixed-coefficient formula proposed as (6.5)
cannot represent all of `H^infty(Stolz_omega)`.

The packet also gives a complete explicit normalized Riemann map. With

```text
a=1/omega, beta=arccos(a), kappa=pi/(2 beta), C(z)=(1+z)/(1-z),
T_kappa(w)=2F1(-kappa,kappa;1/2;(1-w)/2),
```

the map is

```text
F_omega(z)=(T_kappa(C(z))-1)/(T_kappa(C(z))+1).
```

It sends `0` to `0`, the left vertex to `-1`, and the distinguished vertex
`1` to `1`. The proof uniformizes the Cayley-image hyperbola as a quotient
of a strip under `u ~ -u`, resolving the apparent arccosh branch at `w=1`.

## Remaining scope

The broad request for a new elementary square-function family remains open.
Six upgrade attempts are recorded. In particular, pulling the standard disc
monomial family back through the conformal map fails its pointwise square
bound, and a general diagonal-monomial argument forces all represented
functions into the Wiener algebra. Later explicit contour atoms can be
canonically factorized using this map, but that remains a Franks-McIntosh
construction rather than the simple Ritt-adapted family sought by the paper.

## Files

- `main.tex`, `solution_packet.pdf`: theorem, proofs, and scope boundary.
- `source_paper.pdf`: original paper.
- `figures/open_question_crop.png`: exact source evidence.
- `code/verify_map_and_spaces.py`, `code/verification_output.txt`: independent
  numerical and algebraic checks.
- `verification_report.md`: artifact and proof audit.

Attempt record:
`runs/fa_banach_001/attempts/2303.03022_ritt_stolz_coefficient_spaces_conformal_map.md`.

Ledger:
`runs/fa_banach_001/ledger/results/2303.03022_ritt_stolz_coefficient_spaces_conformal_map.json`.

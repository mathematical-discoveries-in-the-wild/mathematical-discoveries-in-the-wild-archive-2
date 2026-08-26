# Every nonzero bounded companion operator on H-infinity fixes ell-infinity

Status: **full affirmative answer; likely valid; pending human review**.

Lin--Liu--Wu, arXiv:1903.10261, ask whether every bounded noncompact
companion Volterra operator

```text
(S_g f)(z) = integral_0^z f'(w) g(w) dw
```

on `H-infinity` fixes an isomorphic copy of `ell-infinity`, and hence is not
strictly singular.

The packet proves the stronger statement that every nonzero bounded `S_g`
fixes `ell-infinity`. Boundedness first forces `g` to be bounded. Choose an
`H-infinity` interpolating sequence `(z_n)` approaching the boundary with
`|g(z_n)|` uniformly bounded below. Beurling interpolation and the associated
interpolating Blaschke product give a bounded linear embedding
`J:ell-infinity->H-infinity` with

```text
J(a)(z_n) = 0,
(1-|z_n|^2) J(a)'(z_n) = a_n.
```

Since `(S_g J(a))'=g J(a)'`, the Schwarz--Pick derivative estimate gives

```text
||S_g J(a)||_infinity >= delta ||a||_infinity.
```

Thus `S_g` is bounded below on the closed copy `J(ell-infinity)`. It follows
that, among bounded companion operators on `H-infinity`, compactness, weak
compactness, and strict singularity are all equivalent to `g=0`.

Files:

- `solution_packet.pdf`: self-contained proof and novelty/status audit.
- `source_paper.pdf`: arXiv:1903.10261v3.
- `supporting_paper_2402.06774.pdf`: Anderson--Jovovic--Smith's endpoint
  operator paper (published in 2014; posted as arXiv:2402.06774).
- `figures/open_question_crop.png`: exact source question, printed/PDF page 7.
- `figures/supporting_compactness_crop.png`: supporting Proposition 3.3,
  independently showing compactness forces `g=0`.

The bounded novelty search checked all run indexes and the parsed arXiv
corpus, exact-title/citation searches, the exact question, and focused arXiv
and web searches combining `S_g`, `H-infinity`, weak compactness, strict
singularity, and fixing `ell-infinity`. No later explicit resolution was
found. This is evidence rather than an exhaustive bibliographic guarantee.

Primary review focus: the use of Beurling's bounded linear interpolation
operator and the uniform-separation estimate for the geometrically spaced
sequence.


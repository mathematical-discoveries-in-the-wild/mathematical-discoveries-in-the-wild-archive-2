# De Leeuw transference on homogeneous `dot W^{1,1}`

This packet gives a complete de Leeuw restriction and shrinking-lattice
approximation theorem for the exact homogeneous Sobolev space studied in
arXiv:1306.1437, by Krystian Kazaniecki and Michal Wojciechowski.

## Files

- `solution_packet.pdf`: review-ready theorem and proof.
- `main.tex`: packet source.
- `source_paper.pdf`: official published paper (Ann. Inst. Fourier 66 (2016)).
- `figures/open_problem_crop.png`: source PDF page 3 with the open statement.
- `VERIFICATION.md`: source, proof, novelty, build, and visual-QA record.
- `code/crop_source.py`: reproducible source-crop helper.

## Result

Let `d>=2`, let `T^d=R^d/(2 pi Z^d)`, and equip both homogeneous spaces with
the sum of the `L^1` norms of their first derivatives.  For a continuous
symbol `m:R^d -> C`, set `gamma^epsilon_k=m(epsilon k)`; the value at `k=0`
is immaterial modulo constants.

The packet proves:

1. If `m` is a multiplier on `dot W^{1,1}(R^d)`, then every sampled sequence
   `gamma^epsilon` is a multiplier on `dot W^{1,1}(T^d)` and its norm is at
   most the Euclidean norm.
2. If `epsilon_n -> 0` and the sampled torus multiplier norms are uniformly
   bounded by `C`, then `m` is a Euclidean homogeneous multiplier of norm at
   most `C`.
3. Consequently,

```text
||m||_{M(dot W^{1,1}(R^d))}
  = sup_{epsilon>0} ||(m(epsilon k))_k||_{M(dot W^{1,1}(T^d))}.
```

The source paper itself proves that every multiplier on the Euclidean space
has a bounded continuous representative.  Thus this applies to all
multipliers in its exact setting and supplies both classical de Leeuw
directions printed immediately after its open remark.

## Scope caveat

This is a full result for `dot W^{1,1}(R^d)`, `d>=2`, not a theorem for every
homogeneous order and exponent.  The source uses “the homogeneous Sobolev
spaces” broadly in the open sentence, while the paper itself studies the
specific endpoint first-order space.  Higher orders/exponents require a
separate quotient-and-density analysis.

## Review focus

The decisive checks are the local `L^1`-multiplier lemma away from frequency
zero, the measure wave-packet limit, the scaling constants in the
periodization argument, and density in the homogeneous quotient.  Each is
proved explicitly in the packet.

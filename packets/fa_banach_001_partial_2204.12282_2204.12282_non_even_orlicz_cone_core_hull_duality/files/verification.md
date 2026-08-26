# Verification report

Status: candidate major partial, likely valid.

## Logical checks

1. The reflected maximum is even, convex, lower semicontinuous, continuous at zero, coercive, and retains the source measurability hypothesis.
2. Both set inclusions in `C intersect (-C)=L_{phi_bi}` were checked directly at the modular level; the factor `2` comes only from `max(a,b)<=a+b` and convex rescaling.
3. The identity `dom(p_J)=C-C` uses only finite modular values at some scale and does not assume an infimum is attained.
4. The inequalities `p_J<=r<=2p_J` were checked in both directions with epsilon-relaxed scales/decompositions.
5. The cone-functional extension is well-defined by cancellation: `v-w=v'-w'` implies `v+w'=v'+w`.
6. The conjugate identity was independently expanded by the substitution `u=v-w`; no minimax interchange is used.
7. The subdifferential equivalence is stated only for an attained decomposition.
8. The pointwise representation is restricted to finite-dimensional `X`, a complete sigma-finite measure space, and normal-integrand hypotheses, where inf-compactness and measurable selection are available.
9. The universal constants are backed by explicit one- and two-atom families and are approached arbitrarily closely.

## Computational check

Command:

```sh
conda run --no-capture-output -n sandbox python code/verify_discrete_models.py
```

Scope:

- 500 random finite-atom power models for the core inequalities;
- 500 random scalar power models for the infimal-convolution conjugate split;
- the two asymptotically sharp model families.

Output:

```text
random core models: 500 passed
minimum recorded inequality slack: 0.000e+00
scalar conjugate splits: 500 passed
maximum relative coefficient error: 3.816e-15
core sharpness ratio: 1.999999980000
hull sharpness ratio: 1.999999990000
all checks passed
```

## Literature/novelty bounds

- Cheap run indexes had no exact hit for arXiv:2204.12282 or the core/hull keywords.
- The author's later thesis, arXiv:2401.17440 (2024), repeats the questions.
- Bounded exact/close arXiv searches covered non-even Orlicz integrands, Orlicz cones, asymmetric Orlicz/modular spaces, symmetrization, and infimal convolution.
- arXiv:2510.25200 (2025) contains max-symmetrization for abstract quasi-modular pseudometrics but not the Orlicz-cone core/hull, Grothendieck dual, or subdifferential results in this packet.

Novelty confidence is moderate rather than definitive because asymmetric modular terminology is fragmented.

## Human-review focus

The most valuable checks are:

1. the precise extended-gauge conventions in the proof of `dom(p_J)=C-C`;
2. the invocation of the one-sided Luxemburg-Amemiya polar identity;
3. the normal-integrand/measurable-selection step in the finite-dimensional corollary;
4. whether nearby cone-duality literature contains the same package under different terminology.

## PDF QA

- LaTeX compilation completed with no undefined references, package warnings, or overfull boxes (one harmless underfull bibliography line).
- All 7 pages were rendered to PNG and visually inspected at full resolution.
- The source-question crop is readable and contains the complete question block.
- No clipping, overlapping text, missing glyphs, or broken formulas were found.
- `solution_packet.pdf` SHA-256: `a601da001c920888311e30f01141231bfc4a53caa4bc917d8519bd0bd4bfb15d`
- `source_paper.pdf` SHA-256: `7064b7ba597a3e671c647f472b0b29a2d679d432fcbcbbe1aa308dab7a95b8f4`

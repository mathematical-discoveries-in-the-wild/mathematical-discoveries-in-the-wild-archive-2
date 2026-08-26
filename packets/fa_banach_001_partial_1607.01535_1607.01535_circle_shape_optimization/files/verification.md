# Verification report

Verdict: candidate substantial partial result, likely valid.

## Exact target and scope

PDF page 22 of arXiv:1607.01535 asks for shape optimization of the
deterministic observability constant `C_T` and of the geometric quantity `g_2`
under a fixed volume fraction. The packet completely solves and strengthens
the `g_2` problem on the circle and solves `C_T` there at all resonant times
`T=2pi m`. It does not claim arbitrary times or higher dimensions.

## Proof checks completed

1. Decomposing `T=2pi q+r` reduces `g_2^T` to the least mass of a sliding arc
   of length `r` plus `q` complete turns.
2. Fubini gives mean sliding-arc mass `rL`, hence the universal upper bound
   `g_2^T <= L`.
3. Periodic duty-cycle checkerboards give a uniform `O(1/N)` sliding-window
   discrepancy, proving sharpness.
4. Equality forces the sliding mass to be constant; its distributional
   derivative is `chi(x+r)-chi(x)`, giving the exact rotation-invariance
   condition. Rational rotations admit explicit invariant sets; irrational
   ergodicity forbids nontrivial ones.
5. At `T=2pi m`, time integration kills every nonzero integer temporal
   frequency, making the wave Gramian block diagonal and giving
   `C_T=(T/2)g_1` with the source normalization.
6. Phase minimization in each two-dimensional eigenspace gives the displayed
   even-Fourier-coefficient formula for `g_1`.
7. The probabilistic cell construction controls all discrete Fourier residues;
   cell integration then makes the estimate uniform over every integer
   frequency, not merely each fixed mode.
8. Fourier uniqueness applied to `chi(x)+chi(x+pi)` gives the exact `L=1/2`
   antipodal-selector attainment classification.

## Deep upgrade attempt

Rotation averaging supplies the relaxed arbitrary-time upper bound, and the
checkerboards asymptotically optimize the high-frequency geometric term. A
full arbitrary-time proof would additionally require a two-scale
microlocal/homogenization estimate for off-diagonal Gramian terms when the
observation microstructure and wave frequency vary together. Weak-* convergence
alone is insufficient. This is the documented stopping obstruction.

## Numerical sanity check

Run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/1607.01535_circle_shape_optimization/code/check_circle_formulas.py
```

The script checks sliding-window convergence, decreasing Fourier maxima for
random finite-cell designs, and vanishing even Fourier coefficients for a
half-circle selector. It is not part of the proof.

## Novelty bounds and review focus

Searches on 2026-08-11 covered the exact source, circle and sliding-window
forms of `g_2^T`, resonant deterministic constants, and citing literature.
ArXiv:1211.5655 contains antecedents for Parseval equality at common periods
and related one-dimensional randomized design/nonattainment. No located source
states the finite-time geometric theorem or the combined circle
classification. Novelty confidence is moderate.

Human review should focus on the `1/2` normalization in the deterministic
Gramian, the all-frequency bound in the Fourier-flat lemma, and the use of
essential infima for arbitrary measurable representatives.

## Artifact integrity and rendering

- Official source PDF SHA-256: `07251266cca9fc1fb8a179889ccf4b09a5ad6d8ae90ceb394dec97a8e4c939b8`.
- Open-problem crop SHA-256: `4221d4b13d5ec3102c9f087777721015a128e37bef50388fa8a756e59c4adce1`.
- Compiled packet SHA-256: `09090c5427340e8f874c7f7bc4bf3f9adbd0778faf567cd87b9a0050dff7d63c`.
- The packet compiled without undefined references or layout warnings. All five
  rendered pages were visually inspected at full-page scale; no clipping,
  overlap, or unreadable material was found.

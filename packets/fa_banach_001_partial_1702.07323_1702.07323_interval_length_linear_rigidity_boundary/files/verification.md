# Verification report

Verdict: candidate substantial partial result, likely valid.

## Scope

The source question on PDF page 3 asks whether every open finite-measure
spectral set on the real line induces a number-rigid DPP.  The packet proves an
exact linear-rigidity classification for a separated countable union of
intervals, a genuine positive infinite-component subfamily, and an explicit
family where linear number rigidity fails.  It does not claim nonlinear
non-rigidity for the latter family and therefore does not claim a full answer.

## Proof checks

1. Plancherel gives the structure factor
   `s(t)=|S|-|S intersect (S+t)|=|S triangle (S+t)|/2`, up to harmless Fourier
   and intensity normalization constants.
2. For `S=union_n (3n,3n+ell_n)` and `|t|<1`, only corresponding intervals can
   overlap, yielding the exact identity `s(t)=sum_n min(|t|,ell_n)`.
3. PDF pages 8 and 19 of arXiv:2409.18519 were checked directly: the former
   limits the paper's terminology to linear rigidity, while the latter states
   the reciprocal-integrability characterization for linear number rigidity
   of stationary DPPs.
4. Divergent reciprocal integral gives ordinary number rigidity because a
   linear `L2` reconstruction is measurable.  Interval rigidity extends to all
   bounded Borel sets by subtraction inside a containing interval.
5. For `ell_n=2^-n`, dyadic scale decomposition gives
   `s(t) asymp t log(1/t)`, whose reciprocal integral diverges.
6. For `ell_n=n^-p`, the counting term and p-series tail are both comparable to
   `t^(1-1/p)`; its reciprocal is locally integrable for every `p>1`.

## Deep upgrade attempt

The orthogonal spectral decomposition first suggested an independent
superposition of sine processes, but this is false: an orthogonal sum of
frequency projections is not a spatially block-diagonal kernel, and mixed
determinantal interference terms survive.  A direct Palm/deletion-tolerance
route was then explored.  The reduced Palm kernel is a rank-one projection
perturbation, but the structure factor does not control absolute continuity of
the corresponding laws.  Known examples of nonlinear-but-not-linear rigidity
show that non-rigidity cannot be inferred.  This is the stopping obstruction.

## Numerical check

Run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/1702.07323_interval_length_linear_rigidity_boundary/code/check_interval_lengths.py
```

The script checks the exact finite overlap identity and the predicted
exponential and polynomial ratios.  It is not used in the proof.

## Literature and review focus

Searches on 2026-08-11 covered the exact source question, infinite interval
unions, structure-factor criteria, sine-process superpositions, Palm measures,
and deletion tolerance.  ArXiv:2407.14168 gives special rigid infinite-union
examples.  ArXiv:2409.18519 supplies the linear criterion.  No located source
states the packet's interval-length classification or polynomial obstruction.

Human review should focus on the Fourier normalization in the structure-factor
identity, the precise linear/nonlinear scope of the supporting criterion, and
the extension from intervals to arbitrary bounded Borel observation sets.

## Artifact integrity and rendering

- Source PDF SHA-256: `fa5dda1800954f20068ccd53b99eb3d157652817ef5f28c74865bb5db464481c`.
- Source-page PNG SHA-256: `071e51b01478adced538f2fb35019f5da44ddb672e54596fab719e03e9710d76`.
- ArXiv:2409.18519 PDF SHA-256: `883473a6e525e65782f1f31c17081309784cb2c79b1b207f2b3ca1e0f985b7b9`.
- ArXiv:2407.14168 PDF SHA-256: `9526d459ba74e8cf1a350d3a31fdaf99cd6a066128188bb075cdd949c37b9f81`.
- Packet PDF SHA-256: `5bade234027163bfa0c3279ea6bf8a2f3d080e535293c1161f814c8ed58df470`.
- The five-page packet compiled with no undefined references or layout
  warnings. Every rendered page was visually inspected; no clipping, overlap,
  or unreadable material was found.

# Central Chebyshev-well endpoint counterexample

Status: `candidate_counterexample_likely_valid`

Source: Marc-Adrien Mandich, *Thresholds and more bands of A.C. spectrum
for the Molchanov--Vainberg Schrodinger operator with a more general long
range condition*, arXiv:2201.00410v1 (2022).

## Result

Conjecture 7.4 is false as stated, but admits a sharp complete correction.
If two points on the branches adjacent to the Chebyshev extremum
`cos(j*pi/kappa)` have the same `T_kappa` value, they are reflections in the
angular coordinate.  Their claimed distance difference is exactly

```text
2*cos(j*pi/kappa)*(1-cos(s)).
```

It is therefore positive for `j < kappa/2`, zero for `j = kappa/2`, and
negative for `j > kappa/2`.  The source range includes the equality case.
For example, `kappa=2`, `j=1`, `a=-1/2`, and `b=1/2` satisfy every hypothesis
of Conjecture 7.4, while the asserted strict inequality becomes `1/2 > 1/2`.

The same endpoint also makes the intervals asserted in Theorems 7.1 and 7.2
empty.  At `j=kappa/2`, both endpoints are zero.  Thus Theorem 7.1 fails at
`(kappa,j)=(6,3)` and Theorem 7.2 fails at `(kappa,j)=(4,2)`.  Deleting the
endpoint `j=kappa/2` is necessary in both theorem statements and gives the
sharp corrected range for the auxiliary Conjecture 7.4.

## Verification

The formal proof is in `main.tex`.  The symbolic/numerical sanity checker is
run with:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2201.00410_central_chebyshev_well_endpoint_counterexample/code/verify_chebyshev_endpoint.py
```

It checks the exact rational counterexample, the trigonometric identity, the
empty-interval witnesses, and a finite grid of the complete sign
classification.  The finite grid is only a transcription check; the proof is
exact.

## Novelty and scope

On 2026-08-09, bounded searches used arXiv:2201.00410, the exact paper title,
the author, the source conjecture wording, `T_kappa(a)=T_kappa(b)`, and the
phrases `Chebyshev threshold`, `counterexample`, and `correction`.  The arXiv
record still has only v1, and no later correction or exact answer was found.
Novelty confidence is moderate pending specialist review.

This packet settles the elementary auxiliary Conjecture 7.4 and disproves the
endpoint instances of Theorems 7.1 and 7.2.  It does not establish the
remaining spectral and Mourre conjectures, nor does it validate the sequence
construction for the corrected range `j < kappa/2`.

## Files

- `main.tex`: full proof and source-impact analysis.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: arXiv:2201.00410v1.
- `figures/source_page_24.png`: source Theorem 7.1 and the start of Theorem 7.2.
- `figures/source_page_25.png`: source Theorem 7.2 and Conjectures 7.3--7.4.
- `code/verify_chebyshev_endpoint.py`: symbolic and finite-grid checks.


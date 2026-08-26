# A continuous uniform-BV kernel whose Mercer SVE is not absolutely convergent

Status: `candidate_full_counterexample_likely_valid`

Source: Sungwoo Jeong and Alex Townsend, *Extending Mercer's expansion to
indefinite and asymmetric kernels*, ICLR 2025, arXiv:2409.16453v2.  On PDF
page 2 the authors state their belief that every continuous kernel of uniform
bounded variation has a Mercer singular-value expansion converging pointwise,
absolutely, and uniformly.

## Result

On `[-pi,pi]^2`, set

```text
b_n = 1/log(n+2),  a_n = b_n/n,
K(x,y) = sum_{n>=1} a_n sin(nx) cos(ny).
```

This is a real continuous asymmetric kernel.  A positive Fejer-kernel
construction produces an even mean-zero `h in L1(T)` whose cosine
coefficients are `b_n`.  Its periodic primitive `f` has the uniformly
convergent sine series `sum a_n sin(nt)`, and

```text
K(x,y) = (f(x+y)+f(x-y))/2.
```

Consequently every section in either variable is absolutely continuous and
has variation at most `||h||_1`, uniformly in the other variable.

For the kernel operator on `L2[-pi,pi]`, the positive singular values and
singular functions are

```text
sigma_n = pi a_n,
u_n(x) = sin(nx)/sqrt(pi),
v_n(y) = cos(ny)/sqrt(pi).
```

The singular values are strictly decreasing, so the positive singular
functions are unique up to paired signs.  Yet at `(pi/4,pi/4)` the sum of the
absolute values of the SVE terms is

```text
(1/2) sum_{n odd} 1/(n log(n+2)) = infinity.
```

Thus the source belief is false.  In fact this example's SVE converges
uniformly everywhere, so it isolates absolute convergence as the obstruction.

## Verification

The proof is self-contained.  Eight independent upgrade/audit routes check
the Fejer telescoping, the uniform convergence criterion, the primitive
identification, both variation bounds, the exact SVD, the simple spectrum,
the divergent point, and interval/scope issues.  They are recorded in:

`runs/fa_banach_001/attempts/2409.16453_uniform_bv_mercer_absolute_convergence_counterexample_upgrade/README.md`

The numerical checker is a sanity check, not part of the proof.  Run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2409.16453_uniform_bv_mercer_absolute_convergence_counterexample/code/verify_counterexample.py
```

Human review should focus first on the L1 Fejer-mixture coefficient
telescoping and then on the claim that the displayed orthogonal expansion
exhausts all positive singular values.

## Novelty status

Bounded searches through 2026-08-13 covered the local run indexes/source
corpus, the exact arXiv id and title, the quoted belief, uniform-BV Mercer SVE
and Fourier-coefficient variants, the arXiv/OpenReview records, and
title/citation searches.  No later answer or matching construction was found.
Novelty is plausible, not certified, and priority is not claimed.

## Files

- `main.tex`: full proof.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source arXiv paper.
- `figures/open_problem_crop.png`: full-width source page containing the belief.
- `code/verify_counterexample.py`: high-precision and numerical sanity checks.
- `VERIFIER_REPORT.md`: explicit verification record.
- `tmp/`: build and rendered-page intermediates.


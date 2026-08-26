# Verification report

Verdict: candidate full counterexample, likely valid.

## Exact target

Conjecture 4.1 on PDF page 13 of arXiv:2409.11679 asks whether the unique
regularized optimizer always equals the kernel embedding of one finite signed
or complex measure under Assumption 3.1. The source screenshot is
`figures/open_problem_crop.png`.

## Proof checks completed

1. `X=N` with the discrete topology is Polish, `mu({n})=2^-n` is a probability
   measure with full support, and the delta kernel is normalized.
2. The RKHS is `ell2`, with feature vectors `phi(n)=e_n`.
3. For every finite signed measure `xi`, the conjecture's integrability term is
   exactly `|xi|(X)`, hence finite.
4. The displayed cost is continuous on `R^2`, nonnegative, and strictly convex
   in its first variable. Its value at zero is `mu`-integrable.
5. With `p=2` and `lambda=1`, completing the square gives
   `J(f)=2||f-(1/n)||_2^2+2 sum 1/n^2`, proving unique optimality.
6. A finite signed measure on discrete `N` has atomic masses in `ell1`.
   Coordinate testing of the Pettis integral forces those masses to be `1/n`,
   a contradiction.
7. The finite truncation measures converge to the optimizer in `ell2`, so the
   example is consistent with the source's approximation theorem.

## Numerical sanity check

Run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2409.11679_discrete_kernel_l1_l2_counterexample/code/check_counterexample.py
```

The script reports bounded partial `ell2` norms, growing harmonic total
variation, and a zero completing-square residual. It is not part of the proof.

## Novelty bounds

On 2026-08-11, exact-id/title searches, exact conjecture terminology,
probabilistic-representer/RKHS measure searches, and nonclosed-range
kernel-mean searches found no later answer or this construction. All cheap run
indexes were also checked. Novelty confidence is moderate because the
`ell1`-versus-`ell2` range obstruction is elementary.

## Human-review focus

Confirm the source's finite signed/complex measure convention and the scope of
the cost assumptions in Theorem 2.6. Also preserve the limitation: this
disproves the conjecture as stated but not a potential theorem for narrower
translation-invariant losses with integrable subgradients.

## Artifacts and rendering

- Source PDF SHA-256:
  `84b4ac5cc125c382663367e8e0d602548e6607c0e080c5cfde6dfed8ccbb607c`
- Conjecture crop SHA-256:
  `b03af4a2656b07c21bbd73e04f642566a36b729e45b8168a860a02db44651e6b`
- Solution packet SHA-256:
  `9d47cceaa78f2ca48b1c543d94b73c295532a640a33cec4dddebebfb9ae6222d`

The four-page packet compiled without warnings, overfull/underfull boxes, or
undefined references. All four pages were rendered at 130 dpi and visually
inspected; the source crop is readable and no content is clipped.

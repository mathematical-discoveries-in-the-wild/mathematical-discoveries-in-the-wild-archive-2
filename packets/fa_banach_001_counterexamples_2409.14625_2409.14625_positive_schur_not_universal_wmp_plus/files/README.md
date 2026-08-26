# Counterexample: Positive Schur Does Not Imply Universal WMP+

Status: `counterexample_likely_valid`

Source: Jose Lucas P. Luiz and Vinicius C. C. Miranda, *On norm-attaining
positive operators between Banach lattices*, arXiv:2409.14625; Journal of
Mathematical Analysis and Applications 558 (2026), article 130379. The
question appears in Section 3 on PDF page 12, immediately before Theorem 3.6.

## Claimed contribution

The direct positive analogue of the classical Schur/WMP characterization is
false. For every `delta>0`, there is an order-continuous equivalent lattice
norm on `L1[0,1]` satisfying

```text
||h||_1 <= ||h||_F <= (1+delta)||h||_1
```

such that `F` has the positive Schur property, but `(L2[0,1],F)` fails the
positive weak maximizing property.

Let `r_n` be the Rademacher functions, `A_n={r_n=1}`, fix `c>0`, choose
`c_n` increasing to `c`, and put

```text
g_n = 1 + c_n 1_{A_n},
||h||_F = sup_n integral g_n |h|.
```

For the positive inclusion `T:L2 -> F`,

```text
||T|| = sqrt(1+c+c^2/2),
```

but `T` does not attain its norm. On the other hand,
`x_n=g_n/||g_n||_2` is a positive maximizing sequence and converges weakly
to a nonzero constant. Therefore `(L2,F)` fails WMP+ although `F` has the
positive Schur property.

## Proof mechanism

The norm of the inclusion is the supremum of the `L2` norms of the positive
densities `g_n`. Those norms approach a limit that none reaches. For each
fixed `f`, the Rademacher oscillation averages out, and the limiting value of
`integral g_n |f|` is separated strictly below the operator norm. This proves
nonattainment. In contrast, choosing the normalized density `g_n` itself
nearly norms the corresponding functional, creating the required maximizing
sequence. Its constant component survives weakly, so the sequence is not
weakly null.

## Verification

The adversarial verification report is in `verification.md`. It checks the
lattice construction, positive Schur property, exact operator norm,
nonattainment, and WMP+ witness separately. Verdict: likely valid, confidence
94/100.

No computation is used as evidence; the proof is analytic and exact.

Verifier focus:

- the strict supremum argument in the nonattainment step;
- preservation of weak topology and the positive Schur property under the
  equivalent lattice norm;
- the weak limit of the explicit maximizing sequence.

## Novelty and scope

The bounded novelty search on 11 August 2026 covered the four lightweight run
indexes, the exact arXiv id and title, the phrases `positive weak maximizing
property` and `positive Schur property`, the published JMAA page, and arXiv
searches for the exact question and close variants. The published 2026 version
still presents the characterization as a natural question. No later paper
stating a proof or counterexample was found. This supports, but cannot certify,
novelty.

The result disproves the proposed characterization; it does not provide a
replacement intrinsic characterization of universal WMP+ codomains.

Human review recommendation: send to a Banach-lattice/norm-attainment
reviewer. The construction is short and elementary, and the fixed-vector
supremum argument is the main point to audit.

Files:

- `source_paper.pdf`: arXiv:2409.14625.
- `figures/open_problem_crop.png`: source PDF page 12.
- `main.tex`, `solution_packet.pdf`: full counterexample packet.
- `verification.md`: adversarial step-by-step check.

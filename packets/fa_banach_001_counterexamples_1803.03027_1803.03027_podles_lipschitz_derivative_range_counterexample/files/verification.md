# Verification report

Status: `candidate_counterexample_likely_valid`

Date: 2026-08-13

Verifier: `agent_lane_10` (GPT5.6)

## Claim audited

For `f in C(Sp(A))`, put

```text
w_k=(f(q^(2k))-f(q^(2k+2))) q^(-k) sqrt(1-q^(2k+2))/(1-q^2).
```

The packet proves:

```text
f(A) in Lip_Dq                    iff w in ell-infinity,
partial_1(f(A)) in SU_q(2)        iff w in c_0.
```

The tail-sum choice with `w_k=(-1)^k` is a selfadjoint maximal-Lipschitz
element for which neither `partial_1` nor `partial_2` lies in `SU_q(2)`.

## Source audit

- Official arXiv PDF `1803.03027v2`, 24 pages, copied as `source_paper.pdf`.
- Exact question: Section 3, official PDF page 7.
- Source identities checked against the TeX and PDF:
  - Lemma 5.3, derivative of `p_k=chi_{q^(2k)}(A)`.
  - Proposition 6.2, norm of `f_(n,k)(b*)^2`.
  - Proposition 6.7, right-column formula for every maximal-Lipschitz
    element.
  - `partial_1(x)^*=-partial_2(x^*)`.
- The crop is a real 180-dpi rendering, 1260 by 575 pixels, with full readable
  text width and the complete two-line question.

## Proof audit

1. **Indexing and norm normalization.** Specializing Proposition 6.7 to a
   diagonal coefficient array leaves exactly one term in column `p_(k+1)`.
   Multiplying its scalar by
   `||f_(k,k+1)(b*)^2||=q^(2k+2)` gives exactly `|w_k|`.
2. **Necessity of bounded weights.** Right multiplication by `p_(k+1)` is a
   contraction, so each `|w_k|` is bounded by the maximal derivative norm.
3. **Sufficiency for the maximal domain.** Bounded weights imply the exact
   telescoping formula and `f_k-f_infinity=O(q^k)`. Finite diagonal truncations
   converge in `C*`-norm. Their interior weights are the original `w_k`, and
   their only boundary weight is at most `||w||_infinity/(1-q)`. The same bound
   applies to the adjoint derivative. Lower semicontinuity of the commutator
   seminorm therefore puts the limit in `Lip_Dq`.
4. **No missing column.** Proposition 6.7 at `p_0` gives zero for a diagonal
   element, so the regular-representation weighted shift has no hidden
   finite-rank first column.
5. **Faithfulness of column recovery.** If an element `z in SU_q(2)` acts as
   zero on `H_+`, then `za=zb=0`; faithful Haar GNS and
   `aa*+bb*=1` imply `z=0`. Thus the source's operator-column identities are
   algebra identities whenever a putative range element exists.
6. **Faithful representation phase.** With
   `rho(a)e_k=sqrt(1-q^(2k+2))e_(k+1)` and
   `rho(b)e_k=q^k e_k tensor U`, the normalized source element in column
   `k+1` is exactly `w_k E_(k,k+1) tensor U*`. The `U*` phase was checked
   directly from `f_(k,k+1)=E_(k,k+1) tensor U` and `(b*)^2`.
7. **Toeplitz obstruction.** The represented algebra is
   `C*(S tensor 1, K tensor C(T))`. Slicing a putative represented range
   element forces the scalar weighted shift into the Toeplitz algebra, hence
   forces `w_k` to converge. The pullback quotient is independent of the
   second circle variable, while its symbol is
   `L conjugate(zeta) tensor conjugate(u)`; therefore `L=0`.
8. **Sufficiency of null weights.** If `w in c_0`, the weighted shift is
   compact, so its tensor with `U*` belongs to `K tensor C(T)` and the
   orthogonal-column series converges in norm to the maximal derivative.
9. **Second derivative.** The witness is selfadjoint. If `partial_2(x)` were
   in the `*`-algebra `SU_q(2)`, the adjoint relation would put
   `partial_1(x)` there as well, a contradiction.

No unproved lemma or numerical dependency remains in the theorem.

## Computational audit

Command:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/1803.03027_podles_lipschitz_derivative_range_counterexample/code/verify_diagonal_weights.py
```

It checked 18 normalized weights and all truncation boundary weights for each
of `q=0.20, 0.50, 0.80, 0.95`. The normalized weights agreed with
`(-1)^k`; all geometric boundary estimates passed. `py_compile` also passed.
The script is an indexing audit, not a substitute for the proof.

## Literature and novelty audit

Searched the local ledger, registry, solution indexes, deterministic target
pool, and fresh web/arXiv results using the exact quotation, exact title and
authors, `Podles Lipschitz algebra`, `maximal Lipschitz`, `derivative range`,
`images of partial_1 partial_2`, and `SU_q(2)`.

- No later paper was found that explicitly restates and answers the original
  `SU_q(2)` range question or gives this diagonal characterization.
- arXiv:2102.12761 answers the separate `q -> 1` convergence question.
- The most relevant later source is Aguilar--Kaad--Kyed,
  arXiv:2104.04317, *Polynomial approximation of quantum Lipschitz
  functions*. Its source was inspected directly. It distinguishes the graph
  closure `C^1(S_q^2)` from the maximal Lipschitz algebra, says maximal
  derivatives generally require a von Neumann-algebraic framework, and proves
  `C*`-norm polynomial approximation with a uniform Lip bound. It does not
  prove graph-norm approximation, state the original inclusion question, give
  an explicit range counterexample, or derive the `ell-infinity/c_0` iff.

This later paper strongly anticipates the qualitative negative mechanism.
Novelty confidence is therefore `moderate-low` for the bare negative answer
and `moderate` for the explicit witness and complete diagonal characterization.

## Build and visual QA

- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
- Clean final log: no unresolved references, LaTeX warnings, overfull boxes,
  or underfull boxes.
- Ghostscript text extraction inspected for the projection formula, the
  `p_0=0` sentence, and the faithfulness step.
- All five pages rendered at 120/130 dpi and visually inspected. No clipping,
  overlap, broken formulas, or unreadable evidence image was found.

## Final hashes

```text
solution_packet.pdf              229999db8961022141406f84a997a7df387bad6bd53d7b4a64ffa529c2663de0
source_paper.pdf                 20b31eac5cc84bdd53db06b3fb519a9d8eb581e47ae5a0aaeb25b61122813f65
figures/open_problem_crop.png    e0bf33fc19956a84cdb8f1e3b3a2059e1dfd4a5b4c63e6a7a560aaec63a59da1
code/verify_diagonal_weights.py  5525510c6d59eb6a825cb89ef7016e422efb91e0816b20c2bd00fdbf48b69367
main.tex                         5e484585610b3244b185858e6cc89795c65f1588bcba50f75606a2a0760d5303
```

## Human-review recommendation

High-priority review. Check the phase and scalar in equation (4.7), the
faithfulness argument turning operator columns into algebra columns, and the
Toeplitz pullback identity. The domain criterion and explicit alternating
witness are elementary once the source column formula is accepted.

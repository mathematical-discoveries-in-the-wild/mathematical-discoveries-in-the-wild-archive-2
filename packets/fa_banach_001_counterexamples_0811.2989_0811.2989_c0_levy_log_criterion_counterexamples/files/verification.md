# Verification report

Verdict: `candidate_counterexample_likely_valid`

The two counterexamples and the deterministic range theorem were checked
line by line. No computational lemma is used in the proof.

## Source and literature checks

- The official arXiv PDF for 0811.2989 was downloaded and saved as
  `source_paper.pdf`.
- Printed page 12 contains the open problem. The displayed
  `figures/open_problem_crop.png` is a direct 180-dpi crop of that page and
  was visually checked for readability.
- The source defines operator topology as the strong operator topology on
  printed page 2 / `source.tex` lines 92--99. Its open problem uses that term
  on printed page 12 / `source.tex` lines 644--654.
- Applebaum, arXiv:1411.2752, Theorem 6.3 and Section 6.1, records the known
  Hilbert-space triplet criterion, logarithmic sufficiency under exponential
  stability, and the bounded-generator iff with convergence in operator norm.
- The run indexes and bounded exact-title/question/keyword searches through
  2026-08-17 found no later paper explicitly resolving the stated general
  Banach-space question. Novelty remains plausible, not certified.

## Proof audit

1. **Nilpotent example.** The zero-extended left translation is a strongly
   continuous contraction and vanishes at time one. The compound-Poisson
   integral is therefore a finite sum supported on the first unit interval.
   On the event of exactly one jump, which has probability `e^-1`, the
   logarithmic expectation contains
   `(6/pi^2) sum_m log(1+e^m)/m^2`, which dominates the harmonic series.
2. **Diagonal deterministic example.** The generator
   `A e_n=-e_n/n` is bounded. Dominated convergence gives strong stability,
   while `sup_n e^(-t/n)=1` rules out norm stability. For `y_n=1/n`, direct
   integration gives `X_t,n=1-e^(-t/n)`. Each fixed `X_t` lies in `ell2`, but
   monotone convergence makes its squared norm tend to infinity.
3. **Range theorem.** Both directions use the standard identities
   `integral_0^t T_s(-Ax) ds=x-T_t x` and
   `A integral_0^t T_s y ds=T_t y-y`; closedness of the generator completes
   the converse. Strong stability makes `ker A={0}`.
4. **Block theorem.** Independent stationary increments give iid blocks;
   `T_n T_(s-n)=T_s` gives the exact pathwise integer identity. The real-time
   statement explicitly assumes uniform tightness of the one-block
   marginals. Strong operator convergence is uniform on compact sets by
   uniform boundedness plus a finite-net argument.
5. **Exponential theorem.** The upper direction is absolute convergence after
   first Borel--Cantelli. The lower direction uses termwise convergence, the
   exponential lower bound, the tail-sum characterization of an infinite
   logarithmic moment, and second Borel--Cantelli.
6. **Block/Y(1) log moment.** With bounded generator, `T_s` and its inverse
   are uniformly bounded on `[0,1]`. Applying the standard infinitely
   divisible log-moment test to
   `nu_xi(B)=integral_0^1 nu(T_s^-1 B) ds` gives the equivalence; bounded
   annuli have finite Lévy measure.
7. **Gaussian check.** Itô isometry proves the Hilbert--Schmidt energy test.
   In the diagonal example the coordinate variance is
   `(1-e^(-2t/n))/(2n)`, its sum diverges, while twice the sum of its squares
   is uniformly bounded. Chebyshev therefore gives norm divergence in
   probability.

## Render audit

- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
  completed successfully.
- Final packet: 8 pages, no overfull boxes, undefined references, or package
  warnings. One harmless underfull theorem paragraph remains.
- All eight rendered pages were visually inspected. An initial missing
  backslash before two `qquad` commands on page 3 was detected, corrected,
  rebuilt, and the corrected page was inspected at original resolution.
- SHA-256:
  - `solution_packet.pdf`:
    `7109e434040a89d64936ac6208d3fa2f1608fe391a1015fe50147e94713a1a3f`
  - `source_paper.pdf`:
    `cba83dcebc3c53dae5d29b8a309f32ff3da0b51cd5ed45a018ed3e4e0252ff95`
  - `figures/open_problem_crop.png`:
    `ed62687eb655840a471ada42f6e74692862560018d35b018796a4d1cd479d011`

## Scope

The packet proves a full negative answer to a universal logarithmic-moment
analogue and supplies exact replacement results. It does not claim a new
general Banach-space Lévy-triplet classification; the Hilbert-space triplet
criterion is explicitly treated as prior literature.

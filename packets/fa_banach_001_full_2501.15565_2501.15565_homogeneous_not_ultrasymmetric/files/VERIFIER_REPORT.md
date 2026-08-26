# Verifier report

## Result checked

The packet claims a full negative answer to Remark 2.14 of arXiv:2501.15565:
there exists an exact 2-homogeneous rearrangement-invariant Banach function
space on `(0,infinity)` that is not ultrasymmetric for the fundamental
function `t^(1/2)`.

## Mathematical verification

### Banach-function-norm construction

- The definition uses
  `G_f(s)=exp(s/2) f**(exp(s))` and the translation-invariant Morrey
  functional `M(g)=sup_I |I|^(-1/2) integral_I |g|`.
- Rearrangement invariance follows because `G_f` depends only on `f*`.
- The exact triangle inequality follows from
  `(f+g)** <= f**+g**`; no quasi-triangle loss is present.
- Lattice monotonicity, scalar homogeneity, and definiteness are immediate.
- For `0 <= f_n` increasing to `f`, the identity
  `t f_n**(t)=sup_(|A|<=t) integral_A f_n` and monotone convergence give
  `f_n**(t)` increasing to `f**(t)`.  Monotone convergence on each interval
  and then the supremum verify the Fatou axiom.
- A characteristic function of a set of measure `a` has profile
  `a^(1/2) exp(-|s-log a|/2)`, whose Morrey functional is finite and positive.
- Monotonicity of both `f**(t)` and `t f**(t)` yields
  `G_f(s+u) >= exp(-|u|/2)G_f(s)` for `|u|<=1`.  The Morrey norm therefore
  controls point evaluation.  Together with Hardy--Littlewood,
  `integral_E |f| <= |E| f**(|E|)`, this proves the local-integral axiom.
- `(D_r f)**(t)=f**(rt)` gives
  `G_(D_r f)(s)=r^(-1/2)G_f(s+log r)`.  Translation invariance of `M` proves
  exact 2-homogeneity for every `r>0`.
- The characteristic-function computation gives the exact fundamental
  function `phi_X(a)=M(exp(-|.|/2)) a^(1/2)`.

### Non-ultrasymmetry separation

- For a center set `S`, the finite decreasing step function
  `f_S(t)=sum_i exp(-s_i/2) chi_(0,exp(s_i))(t)` is a legitimate
  nonincreasing rearrangement.
- Direct calculation verifies
  `exp(s/2) f_S*(exp(s))=sum_(s_i>=s) exp((s-s_i)/2)` and
  `G_(f_S)(s)=sum_i exp(-|s-s_i|/2)`.
- With minimum gap `L`, the first profile lies between a nearest-center
  sawtooth `Q_S` and `(1-exp(-L/2))^(-1)Q_S`.
- The exact distribution formula
  `|{Q_S>lambda}|=2 log(1/lambda)+sum_gaps min(gap,2 log(1/lambda))`
  was checked interval by interval.  It depends only on the multiset of gaps.
  Thus equal gap multisets give uniformly comparable decreasing
  rearrangements of the profiles used in Pustylnik's representation.
- In the clustered ordering, an interval of length `mL+2` captures a fixed
  positive integral from each of `m+1` kernels, giving a lower bound
  `c_L sqrt(m)`.
- In the alternating ordering, centers occur in pairs separated by
  `R_m=Lm^2`.  Exponential tails outside an interval are uniformly summable,
  and the local count is at most `min(2m+1,2|I|/R_m+5)`.  Splitting at
  `|I|=1` and `|I|=mR_m` gives a Morrey upper bound independent of `m`.
- A numerical discretization for `m=8,16,32` independently showed the
  clustered/dispersed Morrey ratio increasing from approximately `1.69` to
  `4.55`, consistent with the proved `sqrt(m)` divergence.
- Pustylnik's characterization would represent any ultrasymmetric space with
  this fundamental function by an r.i. norm of `t^(1/2)f*(t)` on
  `((0,infinity),dt/t)`.  Equal-gap rearrangement comparability would then
  force uniformly comparable norms, contradicting the Morrey separation.

Verdict: the construction is a Banach r.i. space with exact homogeneity, and
the gap-order families prove it is not ultrasymmetric.  One counterexample at
`p=2` fully refutes the universal question.

## Source verification

- `source_paper.pdf` is arXiv:2501.15565v2, Boza--Krepela--Soria,
  *Rearrangement-invariant norms commuting with dilations*.
- Source PDF page 8 contains Theorem 2.13 and the complete open question in
  Remark 2.14.
- `figures/open_problem_crop.png` is a readable crop of that page containing
  the whole remark and no clipped question text.
- The source explicitly points to Pustylnik's `dt/t` representation as a
  possible route; the packet uses the same representation contrapositively.

## Literature and novelty verification

- Cheap run indexes were searched for arXiv:2501.15565, its exact title, and
  the homogeneous/ultrasymmetric keywords; no duplicate packet or ledger
  answer was found.
- Bounded web/arXiv searches for the exact question and core terminology
  found the source article and Pustylnik's 2003 characterization, but no later
  answer.
- The arXiv source was updated in January 2026 and the journal article was
  published in July 2026 with Remark 2.14 still present.
- Novelty is high but provisional because the counterexample mechanism may
  exist in interpolation literature under different terminology.

## Build and visual verification

- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
  completed successfully.
- The final log has no LaTeX, package, overfull, underfull, or
  undefined-reference warnings.
- Poppler text extraction recovered the theorem, Banach-function axioms,
  distribution formula, both Morrey estimates, contradiction, and references.
- The final PDF has five letter-size pages.
- All five pages were rendered at 120 dpi and visually inspected.  The source
  crop is readable; there is no clipping, overlap, malformed mathematics,
  stray source syntax, or illegible text.

## Artifact hashes

- `solution_packet.pdf`: `6494a72a06b32ed1bea43c29733781fa660d778071d01455285cff3ffd8403df`
- `source_paper.pdf`: `6df09ceaaed4b8bc2dc6db964e41a55526f25447500790f55560f85b377e88f4`
- `main.tex`: `53d0f95b932f4a9afd241ae3438062dc9cba2736183883c54a91c78da7775afc`
- `README.md`: `f1b157150c0176bf6c1056cb35331b3ad601ec25160d6b4598129ce3395215e6`
- `figures/open_problem_crop.png`: `c321816ce67f46718506f50747c790ea2c91299730e6308926a4cee1f9564c23`

## Human-review recommendation

Verify the Fatou and local-integral axioms for the constructed norm, then
check the nearest-center distribution formula and the uniform dispersed
Morrey estimate.  Finally confirm the exact hypotheses and norm-equivalence
form of Pustylnik's representation theorem.  These are the only nonroutine
interfaces in the counterexample.

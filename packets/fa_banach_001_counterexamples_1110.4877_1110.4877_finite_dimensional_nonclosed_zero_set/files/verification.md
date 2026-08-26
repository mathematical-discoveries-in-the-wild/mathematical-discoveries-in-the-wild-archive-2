# Verification report

## Claim audit

- Source: H. H. Bauschke, R. I. Bo\c{t}, W. L. Hare, and W. M. Moursi,
  *Attouch--Th\'era duality revisited: paramonotonicity and operator
  splitting*, arXiv:1110.4877.
- Exact target: Remark 3.12 on source-PDF page 10.
- Claimed answer: yes, in `R^2`.
- Candidate status: `full_solution_likely_valid`.

## Independent proof checks

1. **Monotonicity.**  For `F(x,y)=(y/x^2,1/x)`, the symmetric part of
   `DF` equals `diag(-2y/x^3,0)`, positive semidefinite on `x>0,y<=0`.
   Adding the boundary normal cone preserves monotonicity.
2. **Maximality.**  The packet solves `(p,q) in (Id+A)(x,y)` for every
   `(p,q)`.  The boundary regime is `q>0,p>=1/q`.  In all other regimes,
   `y=q-1/x<0` and the scalar equation is
   `p=h_q(x)=x+q/x^2-1/x^3`.  Endpoint limits give a root.  Minty's
   surjectivity criterion applies.
3. **Second operator.**  `B=N_{R x {0}}` is maximally monotone.
4. **Zero set.**  The common domain is exactly `(0,infinity) x {0}`.
   At `(t,0)`, `A(t,0)={0} x [1/t,infinity)` and
   `B(t,0)={0} x R`, so their sum contains zero.  Thus the zero set is
   precisely the nonclosed open ray.
5. **Structural consistency.**  `A` is not paramonotone: choose the same
   positive first coordinate and two distinct negative second coordinates.
   The monotonicity pairing is zero, but the singleton values cannot be
   cross-swapped.  This matches the source paper's necessary obstruction.

No unproved lemma remains beyond the standard Minty maximality criterion for
monotone operators on Hilbert space.

## Computational check

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/1110.4877_finite_dimensional_nonclosed_zero_set/code/check_counterexample.py
```

The script samples 100,000 graph pairs and 25,000 arbitrary Minty-range
targets, checks representative zero-set scales from `10^-12` through `10^12`,
and verifies a nonparamonotonicity witness.  This is a stress test, not part of
the proof.  It passed with minimum sampled monotonicity pairing `0` and maximum
resolvent residual `4.14346e-10`.

## Bounded novelty search

On 2026-08-11, the run's four cheap indexes were searched for arXiv:1110.4877,
Attouch--Th\'era duality, paramonotonicity, and nonclosed zero sets; no prior
packet or attempt matched.  Current primary-source/web searches used the exact
Remark 3.12 wording and the phrases `zer(A+B) not closed maximally monotone
finite dimensional`, `finite-dimensional zero set maximally monotone
nonclosed`, and the explicit coordinate formula.  Citation-neighbor arXiv
records from 2013, 2016, and 2021 were also checked at title/abstract level.
No later source claiming this finite-dimensional construction or an answer to
Remark 3.12 was found.  This is bounded evidence, not a guarantee of novelty.

## PDF and evidence QA

- `source_paper.pdf` is the 23-page arXiv PDF.
- `figures/open_problem_crop.png` is a readable full-width crop of source page
  10 containing the complete question and its stated obstructions.
- The final packet was compiled with `latexmk`; all rendered pages were
  visually inspected after compilation.
- Final PDF: 5 US-letter pages, no LaTeX warnings, SHA-256
  `c70d636a3f36acf6ad57d75d83bbae37ec592c89e01823f6e31446eae28aab49`.
- Source PDF SHA-256:
  `9b5dacce1bbc7472033c6150af9d9330f41c4be2bfa3e4ff0d34612e291c018b`.
- Evidence-crop SHA-256:
  `85a636372d4bf3cf0740879e5fcef402a02645fb2efc0d885798a2e36dbedc4a`.

## Human-review recommendation

Prioritize the three cases in the proof that `ran(Id+A)=R^2`, especially the
endpoint `x=1/q` when `q>0`.  Then verify the normal-cone sign convention at
`y=0`.  If those checks pass, the construction fully resolves Remark 3.12.

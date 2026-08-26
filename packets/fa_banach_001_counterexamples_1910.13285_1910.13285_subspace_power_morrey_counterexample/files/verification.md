# Verification record

Status: `candidate_counterexample_likely_valid`  
Agent: `agent_lane_03`  
Model: `GPT5.6`  
Verified: 2026-08-11

## Mathematical checks

1. **Exact source match.** The final paragraph on source PDF page 16 asks
   whether `A_{p+lambda/n} intersect RH_{n/(n-lambda)}` is sufficient in
   Theorem 1.1. The crop in `figures/open_question_crop.png` was rendered
   directly from that page.
2. **Weight membership.** For `w(y,z)=|z|^beta` on
   `R^d x R^m`, ball scaling gives
   `avg_B |z|^gamma asymp (|z_0|+r)^gamma` for `gamma>-m`. Hence
   `w in A_q` exactly for `-m<beta<m(q-1)`, and positive beta gives
   `w in RH_s` for every finite `s`.
3. **Input estimate.** The proof separately checks `r<=t`, `t<r<=1`, and
   `r>=1`. The only geometric hypothesis used is `d>=lambda`, and all three
   regimes yield at most `C t^(m+beta)` for the p-th power of the Morrey
   norm.
4. **Output estimate.** A radius-three ball centered at any point of the
   unit ball contains the entire bounded tube, so `M f_t >= c t^m` on that
   ball. Choosing half this level in the weak norm gives a lower bound
   `c' t^m`.
5. **Divergence.** The quotient exponent is
   `[m(p-1)-beta]/p<0`, exactly the strict lower parameter condition.
6. **Explicit strong-type instance.** For
   `(n,d,m,p,lambda,beta)=(2,1,1,2,1,5/4)`, the requested class is
   `A_(5/2) intersect RH_2`, the input exponent is `9/8`, the output exponent
   is `1`, and the quotient exponent is `-1/8`.

## Independent parameter check

Command:

```bash
conda run --no-capture-output -n sandbox python code/check_scaling.py
```

Result: `PASS`. The script uses exact rational arithmetic for all strict
parameter and exponent identities, then displays monotone growth of the
predicted quotient for tube widths from `1e-1` to `1e-32`. The analytic proof
does not depend on this script.

## Literature and duplicate audit

- Cheap indexes searched: `registry_index.tsv`, `solutions/index.tsv`,
  `attempts/index.tsv`, and `proof_gaps/index.tsv`.
- Exact source ID and class expression searched.
- Title/author citations and the terms `hyperplane power`,
  `distance to subspace`, `weighted Morrey`, and `maximal operator` searched
  through 2026-08-11.
- arXiv:2010.00250 was inspected: it gives an intrinsic necessary condition
  and sufficiency after an extra local `A_p` condition, not this result.
- arXiv:2110.14259 was inspected during triage: it concerns local spaces and
  states that the global characterization remains open.
- arXiv:2211.07974 was inspected: it treats local/lacunary-center variants and
  still describes the broader global intrinsic characterization as open.

No matching counterexample or resolution was found. This is a bounded novelty
audit, not a priority claim.

## Build and visual QA

Build command from the packet directory:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
cp tmp/main.pdf solution_packet.pdf
```

- Final PDF: 4 pages.
- Final LaTeX log: no warnings, undefined references, overfull boxes, or
  underfull boxes.
- All four final pages were rendered at 150 dpi to
  `tmp/final-render-1.png` through `tmp/final-render-4.png` and inspected.
- Page 1: title/status/source definitions and intuition are fully visible.
- Page 2: weight lemma and all three input scale regimes are fully visible.
- Page 3: output contradiction, explicit example, limitations, and references
  are fully visible.
- Page 4: exact source excerpt is sharp and legible, with no clipped glyphs or
  extraneous source text.

## Hashes

```text
solution_packet.pdf          9c0742d60b8c171205212571407b4f505194aed92ea94cf16780f3415a717f34
source_paper.pdf             2717a318cc6117ff6ce5bd783cd000981743cd884ae11a1c5ab1ecddc6beffc1
supporting_2010.00250.pdf    d6c5a28d4be7898c2f91505c91214bf421502bcda8c630965abbf1578020eb72
supporting_2211.07974.pdf    9027897579f08dd167d1b6f95b4ff1d2fe9518b923c988c630d6f3016186277f
open_question_crop.png       cc24dd6efac0e102e72dca54b32ac064e3bd5f8f3d2ebe8fa39eb711974ff8c3
```

## Human-review recommendation

Review the compact ball-average proof in Lemma 1 and the `r<=t` tube estimate,
especially the use of `d>=lambda`. The construction is elementary and the
exponent gap is strict; no hidden endpoint or computational dependency is
present.


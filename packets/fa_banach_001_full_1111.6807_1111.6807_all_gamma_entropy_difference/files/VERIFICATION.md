# Verification Report

## Verdict

`candidate full solution, likely valid; needs human review`

## Proof audit

| Component | Verdict | Check |
| --- | --- | --- |
| Exact target | valid | Source PDF page 5 asks exactly for a constant depending only on fixed `gamma>0` under `beta>=n+gamma`. |
| Varentropy input | valid | Fradelizi--Li--Madiman Corollary 4.4 with `s=-1/beta` gives `Var(-log f(X)) <= beta^2 sum_i (beta-i)^-2` for `beta>n`. |
| Dimension-uniform variance reduction | valid | Monotonicity in `beta` and a two-case sum estimate give `sigma/n<=A_gamma`; the deterministic checker passed `650,000` `(gamma,n)` grid pairs. |
| Convex information levels | valid | `{f>e^-a}={V<e^(a/beta)}` is convex and has volume at most `e^a`. |
| Conditional support | valid | Given bins `j,k`, both variables lie in the level set indexed by `max(j,k)+1`; the difference lies in `K-K`. |
| Rogers--Shephard step | valid | `|K-K|<=binom(2n,n)|K|<=4^n|K|`; closure handles open superlevel sets. |
| Averaging the maximum bin | valid | `J<=(Z-h)/n` and `E max(Z-h,Z'-h)=E|Z-Z'|/2<=sigma/sqrt(2)`. |
| Integer entropy | valid | Add independent `Unif[-1/2,1/2]` and apply Gaussian maximum entropy; `sqrt Var J<=sigma/n+1/2`. |
| Countable mixture | valid | For `g=sum p_d g_d`, `g>=p_dg_d` gives `h(g)<=H(p)+sum p_d h(g_d)` directly; the right side is finite here. |
| Entropy-power conclusion | valid | `h(X-Y)-h(X)<=n c_gamma`; exponentiating `2/n` gives the requested `C_gamma`. |

## Scope and novelty

- The proof covers every `gamma>0`, all dimensions `n>=1`, and every density
  exactly of the form `V^{-beta}` with positive extended-valued convex `V` and
  `beta>=n+gamma`.
- It does not require central symmetry, centering, finite moments of `X`, or
  any concavity property of the convolution.
- Cheap registry/solution/attempt/proof-gap indexes had no exact prior result.
  Bounded arXiv/web searches covered the title, displayed formula, fixed
  additive `gamma`, `s`-concave reverse EPI, information content,
  Rogers--Shephard, and later citations. They found the sharp varentropy input
  and adjacent positional results but no exact answer.
- Novelty remains provisional because the proof is a short combination of
  known ingredients and could be unpublished folklore.

## Human-review focus

Review the conditional mixture inequality and the convention for open density
superlevel sets. Both are handled directly in the packet and do not require a
delicate limiting theorem.

## Computational evidence

`attempts/evidence/1111.6807_information_quantization/check_constants.py`
checks the only numerical simplification in the proof. It passed a logarithmic
grid of 65 gamma values and every `1<=n<=10000`. The largest observed ratio of
the exact scaled varentropy bound to the claimed `A_gamma` was
`0.7811706626`.

## PDF QA

- The final PDF compiled to five US-letter pages without final LaTeX
  warnings, undefined references, or overfull/underfull boxes.
- All five pages of the final binary were rendered at 150 dpi and visually
  inspected. The source-question crop, varentropy crop, formulas, margins, and
  page breaks are legible and unclipped.
- SHA-256: e93326bc73d2a8f9d2dead843753c155b76615516885a5f766ceade8846f4bf9.


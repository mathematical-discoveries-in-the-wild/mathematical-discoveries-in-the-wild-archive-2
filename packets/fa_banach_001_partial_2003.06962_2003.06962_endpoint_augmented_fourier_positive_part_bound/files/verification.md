# Verification report

Status: `candidate_partial_result_likely_valid_needs_human_review`

## Mathematical audit

1. **Fourier identities.** With `y=2*pi*xi` and
   `sinc(y)=sin(y)/y`, normalization gives
   `1=int F(xi) 2*sinc(y) dxi`. Smooth compact support makes `F` Schwartz,
   so Fourier inversion is legitimate and `phi(1)=0` gives
   `0=int F(xi) cos(y) dxi`.
2. **Positive/negative masses.** If `P=int F_+`, `N=int F_-`, then
   `a=phi(0)=P-N>=0`. No assumption that `F` is nonnegative is made.
3. **Sign check.** Subtracting `(2/3)` times the endpoint identity from the
   normalization yields
   `1-(4/3)a=-int F K`, where
   `K=(2/3)(2+cos(y)-3*sinc(y))`. Since `K>=0`,
   `-int F K <= (sup K)N` has the correct direction.
4. **Global nonnegativity.** For `0<=y<=pi`, the derivative of
   `y(2+cos y)-3 sin y` is
   `2 sin(y/2)(2 sin(y/2)-y cos(y/2))>=0`. For `y>=pi`, the remaining sign
   cases give the same Cusa--Huygens inequality. Thus `K>=0` on the whole
   real line.
5. **Global upper bound.** When `sin y>=0`, `K<=2`. When `sin y<0`, the
   proof separates `[pi,3*pi/2]`, `[3*pi/2,144/25]`, and the tail. The middle
   interval is controlled by a decreasing tangent comparison; the exact
   rational checkpoint is reproduced by `code/verify_constant.py`. The tail
   follows directly from Cauchy--Schwarz. These cases give
   `sup K <= (96+sqrt(2929))/72`.
6. **Final rearrangement.** The last upper bound `D` is greater than `4/3`,
   so from `1-(4/3)a <= D(P-a)` one obtains
   `DP >= 1+(D-4/3)a >=1`. Hence
   `P>=1/D=72/(96+sqrt(2929))`.

## Computational audit

Running

```text
conda run --no-capture-output -n sandbox python \
  code/verify_constant.py
```

checks the exact positive rational difference used at `y=144/25`, prints the
closed-form constant, and scans 800,001 points of `K` on `[0,80]`. The scan
locates a numerical maximum near `y=5.7634`, below the proved closed-form
upper bound. It is only a contradiction check; the proof of the global bound
is analytic.

## Literature audit

- Cheap registry, solution, attempt, and proof-gap indexes contained no row
  for arXiv:2003.06962 or the selected Fourier positive-part problem.
- The source article has two citing works in OpenAlex as of 2026-08-11; their
  titles concern generalized difference sets and smooth averaging, not this
  sharp-bound problem.
- A later paper by de Dios Pont and Madrid answers the source's separate
  average-autocorrelation compact-extremizer conjecture. It does not state an
  answer to the selected Theorem 4.1 sharp-bound question.
- Exact-constant, exact-status-sentence, title, author, endpoint, Fourier
  positive-part, and Cusa--Huygens searches found no prior version of the
  packet theorem. This is a bounded novelty audit, not a priority claim.

## Rendering audit

The final packet compiles to five letter-size pages with no LaTeX warnings,
overfull boxes, or underfull boxes. All five pages were rendered to PNG at
120 dpi and inspected at full-page scale. The theorem statement, proof
displays, exact rational fraction, citations, references, headers, and page
numbers are legible and unclipped. The source crop was separately inspected at
original resolution and is readable at normal packet zoom; it includes all of
Theorem 4.1 and the full paragraph declaring the sharp bound unknown.

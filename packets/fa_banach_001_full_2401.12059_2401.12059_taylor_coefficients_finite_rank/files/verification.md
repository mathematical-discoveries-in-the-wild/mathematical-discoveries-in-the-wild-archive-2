# Verification record

## Claim audited

For a holomorphic map `f:U -> F`, finite upper box dimension of
`f(x0 + epsilon B_E)` forces every homogeneous Taylor coefficient at `x0` to
have finite-dimensional range. Quantitatively, with
`r=floor(upper_dim_B/2)`, the new range dimension at degree `m` is at most
`(r+m)^m`. Consequently Questions 4.4 and 4.5 of arXiv:2401.12059 have
affirmative answers.

## Source audit

- Official source: arXiv:2401.12059v1, 17-page PDF downloaded from arXiv.
- Exact target: official PDF page 15, Questions 4.4 and 4.5.
- The crop includes the end of Proposition 4.2, the explicit `p=1` gap, both
  full questions, and the authors' acknowledgment that these questions
  motivated the work.
- The paper was published as Math. Nachr. 298 (2025), 567–580,
  DOI `10.1002/mana.202400042`.
- The printed `f:U -> E` in both questions is inconsistent with the introduced
  range space `F`; the packet uses the paper's globally well-typed `f:U -> F`
  formulation.

## Proof audit

1. **Metric-to-rank step.** If `Df(y)` has complex rank `s`, choose an
   `s`-dimensional domain slice and `s` range functionals with invertible
   derivative. The finite-dimensional holomorphic inverse theorem produces
   an open subset of `C^s` in a Lipschitz image of the source image. Therefore
   `2s <= upper_dim_B`, giving the uniform rank bound.
2. **Polynomial-rank step.** From `N` independent values of an
   `m`-homogeneous Banach-valued polynomial, dualize and pull back along
   `C^N -> E`. This produces `N` independent scalar polynomials. Source
   Corollary 3.3 gives maximum Jacobian rank at least `N^(1/m)-m`, while the
   pullback derivative factors through the original derivative. Hence uniform
   derivative rank `r` implies range-span dimension at most `(r+m)^m`.
3. **Noncancellation step.** Quotienting by the lower Taylor ranges makes all
   degrees below `m` vanish. An `s`-minor of the quotient derivative then has
   leading term `t^(s(m-1)) det M`; no cross-degree term can occur at a lower
   order. If `det M` is nonzero, the derivative rank of `f` exceeds the metric
   bound at nearby points, contradiction.
4. **Induction.** Each quotient Taylor range is finite-dimensional, so the
   cumulative lower-degree span remains finite-dimensional and closed. This
   justifies the next Banach quotient and yields the displayed cumulative
   bound.
5. **Entropy endpoint.** Every bounded set in a complex `D`-dimensional normed
   space has `e_n <= C 2^(-n/(2D))`, which is summable.

Edge cases checked: `m=1`; zero Taylor coefficients; nonintegral box dimension;
arbitrary (possibly large) test vectors `x`, handled by choosing small `t`;
open rather than closed balls; and use of upper box dimension without assuming
the box-dimension limit exists.

## Exact computation

Command:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2401.12059_taylor_coefficients_finite_rank/code/verify_rank_induction.py
```

Output:

```text
verified exact leading-minor orders for sizes 1..4 and degrees 1..5
verified cumulative Taylor-rank bounds for representative dimensions
```

Both Python files also pass `python -m py_compile`.

## Literature and novelty audit

Searches on 13 August 2026 covered:

- exact paper title, arXiv id, DOI, and authors;
- exact fragments of Questions 4.4 and 4.5;
- combinations of `finite box dimension`, `Taylor coefficient`, `finite
  rank`, `holomorphic Banach`, `entropy numbers`, and `ell_1 endpoint`;
- the source's current author publication pages and the Wiley publication
  record;
- visible citing literature.

The only indexed citing item located was Brandani da Silva--Della Pasqua,
*Generalized entropy numbers of sets and operators* (Adv. Oper. Theory 10,
2025). Its abstract and searchable metadata introduce generalized entropy
numbers and do not claim either answer. No later solution was found. The
search is bounded rather than exhaustive, so novelty confidence is moderate.

## Build and visual QA

- `pdflatex` run twice with `-halt-on-error`.
- Final build: five pages; no LaTeX warnings, undefined references, overfull
  boxes, or underfull boxes.
- Ghostscript text extraction completed.
- All five pages rendered at 150 dpi and inspected. Text, equations, source
  crop, caption, page breaks, and references are legible and unclipped.
- The source crop was separately inspected at original resolution.

## Hashes

Hashes are recorded after the final build:

```text
solution_packet.pdf  9e378b8842a260becd68ffd5f748bd9e42e113883856bba1510e4733fa4a3517
source_paper.pdf      77f48fdc19f51bd5310ea621d6ac2c2c28333a5c3b2c0cfb2fbdc3d8d5321dd9
open_problem_crop.png 75393a92b444f3d435b6b6054ad56b067215f37736ce691c0bdd9a2b6f91f92c
verify_rank_induction.py ca12d236d98fab08bf84aa5a67588dbb67a807e8dc1c5d509401145ceeef453e
main.tex              2221588840d5babbdb075a2c0347f637b04453376fa17f9039fc69a270dbc6cd
```

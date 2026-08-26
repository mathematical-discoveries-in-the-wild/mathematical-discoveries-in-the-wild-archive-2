# Verification audit

## Source match

The source crop reproduces Question 6.2 from page 21. The packet uses the
source's definition of “square”: equal dimensions of the kernels of `A*A` and
`AA*`, equivalently equal kernel and cokernel dimensions for a partial
isometry.

## Proof obligations

1. **Pointwise defect inequality.** With `P=I-V*V` and `Q=I-VV*`,
   Cauchy--Schwarz gives
   `|d_j| <= sqrt((1-p_j)(1-q_j))`; AM--GM gives
   `p_j+q_j <= 2(1-|d_j|)`.
2. **Trace passage.** The sum of the diagonal of a positive projection is its
   extended trace, hence is its rank, finite or infinite. Summing the
   pointwise inequality yields the sharp bound.
3. **Finite Thompson block.** For singular values `(1^(N-r),0^r)`, all
   Thompson inequalities follow from pointwise contractivity and block
   deficit at least `r`. An operator with only zero/one singular values has
   `A*A` a projection and is a partial isometry.
4. **Infinite-defect partition.** Infinite total deficit lets one greedily
   form finite blocks of deficit at least one. A direct sum of defect-one
   blocks has both defects infinite.
5. **Finite prescribed defect under infinite deficit.** One finite
   defect-`r` block leaves a tail of infinite deficit. The source's exact
   unitary criterion therefore realizes the tail.
6. **Equality boundary.** If the deficit sequence sums to the integer `r`,
   finite-rank Schur--Horn supplies a rank-`r` projection with that diagonal.
   Left multiplication of its complement by the diagonal phase operator
   gives the requested diagonal and preserves equal defects.
7. **Eventually unimodular case for positive defect.** A single finite
   Thompson block contains every deficient coordinate; the complement is a
   diagonal unitary. The source's separate unitary criterion governs defect
   zero.

## Computational checks

Run:

```bash
conda run --no-capture-output -n sandbox python code/check_deficit_bounds.py
```

The script verifies the finite Thompson inequalities on deterministic examples
and tests the pointwise inequality on randomly generated finite partial
isometries. The proof is exact and does not depend on these checks.

## Novelty and limitations

Cheap run indexes and bounded arXiv searches using the exact source question
and core partial-isometry/defect keywords found no later solution through
12 August 2026. Novelty confidence is moderate because the proof uses classical
ingredients and could be unindexed folklore. The finite-intermediate regime is
explicitly excluded; the attempt log records the failed compactness and tail
decomposition upgrades.

## Build and visual QA

`latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
completed after two passes with no remaining warnings, undefined references,
or overfull/underfull boxes. The five-page PDF was rendered at 120 dpi and
every page was visually inspected. Equations, theorem boundaries, bibliography,
and the source-question crop are legible and unclipped.

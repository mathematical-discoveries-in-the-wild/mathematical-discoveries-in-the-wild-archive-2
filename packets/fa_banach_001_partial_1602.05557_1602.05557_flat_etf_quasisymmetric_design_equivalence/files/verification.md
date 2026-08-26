# Verification record

## Mathematical audit

1. ETF tightness gives the row Gram matrix
   `Phi Phi^T = q^2(q+1) I - q J` because the frame has
   `b=q(q^2+q-1)` columns spanning the `m-1` dimensional space `1^perp`,
   where `m=q(q+1)`.
2. Column switching makes the first row all `+1` without changing balance,
   tightness, or absolute inner products.
3. Negative supports in the other `m-1` coordinates have the asserted block
   size, replication, pair-of-points count, and two block intersections.
4. Conversely, the signed incidence matrix has zero column sums, pairwise
   column inner products `+/-q`, and row Gram
   `q^2(q+1)(I-J/m)`.  This proves tightness for `1^perp`; the coherence
   `q/m=1/(q+1)` equals the Welch bound.
5. The block-graph parameters follow from
   `N^T N=(k-x_1)I+(x_2-x_1)A+x_1J` and
   `NN^T=(r-lambda)I+lambda J`.
6. Standard SRG integrality, multiplicity, complement, absolute-bound, and
   Krein tests for the `q=6` graph all pass.  No existence or nonexistence
   claim is made.

## Computational audit

Command:

```text
conda run --no-capture-output -n sandbox python code/verify_parameters.py
```

The script checks all design equations, the Welch identity, and all SRG
parameter/eigenvalue equations using exact integer and rational arithmetic for
every even `q <= 50`, then prints the `q=6` specialization.

## Artifact audit

- `source_paper.pdf`: 12 pages; Problem 2 and the `q=6` statement are on PDF
  page 10.
- Both supporting PDFs are primary arXiv sources.
- `solution_packet.pdf` is compiled from `main.tex`; every final rendered page
  is visually inspected.

## SHA-256 hashes

- `solution_packet.pdf`: `be822d5a9f4b0bc213ea31d9362fc2b6f7cbda2d7fe7f78dd998b3676d0829ec`
- `source_paper.pdf`: `c814d840ca7c647f0f78d0685dc0563338be5243933f1556719e2087e366ff9c`
- `supporting_paper_1402.3521.pdf`: `555be5e97da4020c567efa823fa227b2c5650a91af33cd93b873af8f29eac473`
- `supporting_paper_2102.05576.pdf`: `98df240bff954f8638576fa6d67b765368645f5bf8cbb2846ce8205d4d91db03`
- `figures/problem_2_q6_crop.png`: `e464815e44bf85bedf867b25c8f740c56cff76671976bf8107de361e8005881b`
- `code/verify_parameters.py`: `de542fb2d841c57d54c2ec2636ef88b76cbb4e06c42b2579b3e998be359eb0f4`

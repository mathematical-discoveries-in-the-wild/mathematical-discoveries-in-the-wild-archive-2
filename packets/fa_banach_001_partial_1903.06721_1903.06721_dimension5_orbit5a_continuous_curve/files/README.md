# A continuous squared-phase curve through the dimension-5 SIC

Status: `partial_result_likely_valid`

Source target: Marcus Appleby, Ingemar Bengtsson, Steven Flammia, and
Dardo Goyeneche, *Tight Frames, Hadamard Matrices and Zauner's Conjecture*,
arXiv:1903.06721.

## Result

The source conjectures that the squared-phase matrix associated with every
SIC in dimension greater than two lies on a continuous curve of solutions.
It gives explicit curves in dimensions 3, 4, 6, and 8, while its restricted
defect table gives only infinitesimal evidence in dimension 5.

This packet proves the missing dimension-5, orbit-5a case. After an exact
finite Clifford/displacement normalization, the squared phases of the exact
Scott--Grassl fiducial have a four-phase Zauner-invariant pattern. The
associated Hermitian `5 x 5` operator commutes with an order-three unitary and
splits into blocks of sizes `1,2,2`. Its involution condition is equivalent,
inside this ansatz, to three real analytic scalar equations. An exact-radical,
outward-rounded interval computation encloses a `3 x 3` Jacobian minor in

`[-0.881829962934411, -0.881829962934410]`.

The implicit-function theorem therefore produces a nonconstant real-analytic
one-parameter curve through the orbit-5a squared-phase matrix. By the source
paper's equivalence lemma, this simultaneously yields local curves of the
associated projector, Hermitian Hadamard matrix, two ETFs, and two
Weyl--Heisenberg covariant symmetric tight fusion frames.

## Scope and upgrade attempt

This settles the unique known extended-Clifford orbit in dimension 5, not the
all-dimensional conjecture and not hypothetical non-Weyl--Heisenberg SICs.
A deeper upgrade attempt isolates why the proof is dimension-specific: the
Zauner blocks have size at most two only in the present case. In larger
dimensions, blocks of size at least three require higher spectral equations,
whose first derivatives collapse at an involution. Thus the same regular
implicit-function argument cannot prove the general conjecture without a new
second-order or explicit parametrization idea.

## Verification

- `code/verify_interval.py` reconstructs the published exact radical
  fiducial, performs the finite normalization, builds the three equations,
  and certifies the nonzero Jacobian minor with outward-rounded intervals.
- Run it with
  `conda run --no-capture-output -n sandbox python code/verify_interval.py`.
- `source_paper.pdf` is arXiv:1903.06721.
- `supporting_paper_0910.5784.pdf` is the Scott--Grassl source of the exact
  orbit-5a fiducial.
- `figures/open_problem_crop.png` shows the conjecture on source PDF page 17.

## Novelty check

Before promotion, the run result/attempt indexes were searched for
`1903.06721`, `squared-phase`, `continuous curve`, `SIC`, `orbit 5a`, and
`restricted defect`. A bounded arXiv/web search on 2026-08-13 used the exact
conjecture phrase and combinations of `dimension 5`, `5a`, `SIC`,
`squared-phase`, and `continuous family`. It found the source paper and later
restricted-defect discussions, but no explicit curve or proof for orbit 5a.
The famous all-dimensional SIC-existence/Zauner conjecture is already recorded
elsewhere in this run and is not claimed here.

## Human-review recommendation

Review as a likely valid substantial partial result. The most important checks
are the finite normalization and four-phase pattern, the `1+2+2` block
reduction, and the exact interval determinant certificate.


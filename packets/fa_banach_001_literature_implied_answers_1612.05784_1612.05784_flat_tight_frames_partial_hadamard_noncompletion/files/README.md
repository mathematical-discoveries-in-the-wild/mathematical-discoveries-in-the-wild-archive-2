# Flat tight frames and nonextendible partial Hadamard matrices

Status: `literature_implied_answer (full negative answer)`

Source: Emily J. King, *New Constructions and Characterizations of Flat and
Almost Flat Grassmannian Fusion Frames*, arXiv:1612.05784 (latest source
revision dated 2021).

Decisive prior literature: Dursun A. Bulutoglu and David M. Kaziska,
*A counterexample to Beder's conjectures about Hadamard matrices*, `Journal of
Statistical Planning and Inference` 139 (2009), 3381--3383,
DOI [10.1016/j.jspi.2009.02.003](https://doi.org/10.1016/j.jspi.2009.02.003).

## Identification

After Theorem 4.4, on page 17 of the locally rendered source PDF, the paper
conjectures:

> Real, flat tight frames must come from an appropriately scaled submatrix of
> a Hadamard matrix.

In the immediately preceding sentence, "submatrix" means a matrix obtained by
removing rows of a square Hadamard matrix.  A real flat unit-norm tight frame
with `N` vectors in `R^k` has synthesis matrix `L = H/sqrt(k)`, where `H` is a
`k x N` sign matrix and

```text
H H^T = N I_k.
```

Thus `H` is a row-Hadamard (partial Hadamard) matrix.  The source conjecture is
exactly the assertion that every such `H` extends, up to the usual row/column
signs and permutations, to an `N x N` Hadamard matrix.

Bulutoglu--Kaziska exhibit a maximal `13 x 32` row-Hadamard matrix.  Scaling it
by `1/sqrt(13)` gives 32 flat unit vectors in `R^13` with frame operator
`(32/13) I_13`.  Maximality means that not even one further sign row can be
added, so it cannot be obtained by deleting rows from a Hadamard matrix of
order 32.  This is a full negative answer after the frame/partial-Hadamard
identification.

## Short explicit certificate

The same obstruction already has a four-row example.  Let `H4` be the
Sylvester Hadamard matrix of order four and repeat each of its columns three
times:

```text
H = H4 tensor [1 1 1].
```

Then `H H^T = 12 I_4`, so `L=H/2` is a real flat unit-norm tight frame of 12
vectors in `R^4`.  If a sign row `x` were orthogonal to `H`, split it into four
blocks of three and let `s_j` be the sum in block `j`.  Orthogonality says
`H4 s=0`, hence `s=0`.  But every `s_j` is a sum of three signs and is odd, a
contradiction.  Therefore `H` is maximal and cannot be a row-deleted submatrix
of an order-12 Hadamard matrix.  The included verifier checks the Gram matrix
and exhausts all `2^12` possible extension rows.

This short certificate is not claimed as novel: the 2009 publisher record
notes that Beder had already constructed maximal four-row examples whenever
the number of columns is an odd multiple of four.

## Scope and provenance

This is placed under `literature_implied_answers`, not `counterexamples`,
because nonextendible real row-Hadamard matrices were already in the literature
before arXiv:1612.05784.  The supporting paper does not use the source's frame
language; the equivalence is the direct identification recorded here.  A full
supporting PDF was not openly available during the bounded search; the DOI
publisher record supplies the title, abstract, maximal `13 x 32` result, and
article metadata.

## Files

- `source_paper.pdf`: locally rendered arXiv source.
- `code/verify_four_by_twelve.py`: exact finite verification of the displayed
  certificate.
- `main.tex` and `solution_packet.pdf`: compact status and identification note.

Ledger: `runs/fa_banach_001/ledger/results/1612.05784_flat_tight_frames_partial_hadamard_noncompletion.json`.


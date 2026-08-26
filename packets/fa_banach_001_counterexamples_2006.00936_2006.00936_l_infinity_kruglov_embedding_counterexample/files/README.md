# A universal-host counterexample to Kruglov necessity

**Status:** candidate counterexample, likely valid, requiring human review.

**Source:** S. V. Astashkin and G. P. Curbera, *Rosenthal's space
revisited*, Studia Mathematica 262 (2022), no. 2, 197--224,
DOI 10.4064/sm201011-4-1; arXiv:2006.00936. The target necessity problem is
stated on source PDF page 4.

The source asks whether the Kruglov property of a rearrangement-invariant
space `E` is necessary for the existence of an isomorphic embedding
`U_E -> E`, and presents only a partial result for embeddings with strong
independence and lower-tail structure.

The literal unrestricted answer is no. Take `E=L^infinity[0,1]`.
The generalized Rosenthal space `U_E` is by definition the closed span of a
countable sequence, hence separable. Every separable Banach space embeds
linearly isometrically into `ell_infinity`, and a countable positive-measure
partition embeds `ell_infinity` linearly isometrically into
`L^infinity[0,1]`. Thus `U_E` embeds into `E`.

On the other hand, the Kruglov transform of the constant function one is a
Poisson random variable of parameter one, which is essentially unbounded.
Therefore `L^infinity` does not have the Kruglov property. The example even
has the Fatou property.

Files:

- `solution_packet.pdf` -- exact counterexample and complete proof
- `source_paper.pdf` -- arXiv:2006.00936v1
- `figures/open_problem_crop.png` -- source necessity statement
- `verification.md` -- checks of separability, both isometries, and Kruglov failure
- `code/make_open_problem_crop.py` -- reproducible source crop

**Human-review focus:** decide whether the authors intended an unstated
separability/order-continuity hypothesis or a canonical-basis-preserving
embedding. The counterexample settles the words as printed, but not those
stronger variants.

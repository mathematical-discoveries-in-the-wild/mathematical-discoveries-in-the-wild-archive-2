# Full solution: Ciric quasi-contractions are unsaturated

Status: `candidate_full_solution_likely_valid`  
Source: Vasile Berinde and Madalina Pacurar, *Fixed points theorems for
unsaturated and saturated classes of contractive mappings in Banach spaces*,
arXiv:2103.15148, Open Problem 2, printed page 15.

## Result

For every nonzero real or complex Banach space `X`, the class of Ciric
quasi-contractions on `X` is unsaturated. The zero Banach space is the unique
saturated edge case.

Take `R=-I`. For any nonzero `u`, testing the quasi-contraction inequality at
`x=u`, `y=-u` makes its left side and the maximum on its right both equal to
`2||u||`; the required strict coefficient `h<1` is impossible. But
`R_(1/2)=0`, and the zero map is a Ciric quasi-contraction. Hence `R` belongs
to the enriched class but not to the original class.

The same witness also proves unsaturation for Ciric-Reich-Rus contractions,
but that first open problem was explicitly answered by Berinde and Pacurar in
2022. The candidate-new scope is Open Problem 2.

## Verification

The proof is definition-level and has been checked for:

- all five distances at the opposite pair `u,-u`;
- the allowed averaging parameter `lambda=1/2`;
- both real and complex Banach spaces;
- the zero-dimensional edge case; and
- the separate CRR inequality and its literature-status limitation.

See `verification.md` for the explicit audit.

## Packet files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source page 15 with both open problems.
- `figures/quasi_contraction_definition_crop.png`: source page 3 with the
  defining inequality referenced by Open Problem 2.
- `verification.md`: proof and scope audit.

## Human review focus

Confirm that the source definition of enrichment allows `R=-I` and
`lambda=1/2`. No external theorem enters the proof.


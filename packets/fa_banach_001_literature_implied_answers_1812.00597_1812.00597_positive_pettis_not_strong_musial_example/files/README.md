# Literature-Implied Full Negative Answer: Positive Pettis Need Not Be Strongly Pettis

Status: `literature_implied_answer (full negative)`

## Source Questions

- Source paper: D. Candeloro, L. Di Piazza, K. Musial, and A. R. Sambucini,
  "Integration of multifunctions with closed convex values in arbitrary Banach
  spaces," arXiv:1812.00597.
- Location: PDF page 11, Problems 4.7 and 4.8.
- Problem 4.7 asks whether every positive Pettis-integrable multifunction is
  McShane integrable.
- The second question in Problem 4.8 asks whether every positive
  Pettis-integrable multifunction is strongly Pettis integrable, meaning that
  its Pettis primitive is an `h`-multimeasure.

## Supporting Literature

- K. Musial, "Pettis Integrability of Multifunctions with Values in Arbitrary
  Banach Spaces," *Journal of Convex Analysis* 18 (2011), 769--810.
- Location: Example 1.12, PDF page 11 (journal page 779).
- The example starts with a scalarly integrable function
  `f : [0,1] -> c_0` for which the operator
  `T_f : ell_1 -> L_1`, `T_f(x*) = x*f`, is not weakly compact, and sets
  `Gamma(t) = conv{0,f(t)}`. It proves that `Gamma` is `ck(c_0)`-valued and
  Pettis integrable in `cb(c_0)`.

A companion paper by the same four authors, "Multifunctions determined by
integrable functions," arXiv:1906.07019, gives in Example 2.10 (PDF page 9) an
independent explicit positive Pettis-integrable multifunction that is not
McShane integrable.

## Identification and Proof

For Musial's example,

`s(x*,Gamma(t)) = (x*f(t))^+ >= 0`,

so `Gamma` is positive. Suppose its Pettis primitive `M_Gamma` were an
`h`-multimeasure. Under the Radstrom support-function embedding

`j(C)(x*) = s(x*,C)` for `x*` in the dual unit ball,

the map `m = j o M_Gamma` would be a norm-countably additive vector measure
with values in `ell_infinity(B_{ell_1})`. For every measurable `E`,

`m(E)(x*) = integral_E (x*f)^+`.

Consequently, for every decreasing sequence `E_n` with empty intersection,
vector-measure continuity gives

`sup_{x* in B_ell1} integral_{E_n} |x*f| <= 2 ||m(E_n)|| -> 0`.

Together with the same estimate on `[0,1]`, this says that
`T_f(B_ell1)` is uniformly integrable. The Dunford--Pettis criterion in `L_1`
then makes `T_f` weakly compact, contradicting the defining property recorded
in Example 1.12. Thus `M_Gamma` is not an `h`-multimeasure.

This is a full negative answer to the second question of Problem 4.8. It also
answers Problem 4.7 negatively: Theorem 4.2 of arXiv:1812.00597 says that
McShane integrability implies strong Pettis integrability.

The relation to Example 1.12 is an agent-identified implication; Musial's 2011
paper does not formulate the later Problems 4.7--4.8 or this consequence.
Accordingly, the packet is classified as a literature-implied answer rather
than a new counterexample packet.

## Scope

This packet does not answer the first question of Problem 4.8 concerning
positive Henstock-integrable multifunctions with Henstock-integrable
selections. It also does not answer the stronger positive Henstock plus Pettis
question posed as Question 2.14 of arXiv:1906.07019. Musial's example is not
shown to be Henstock integrable.

## Files

- `main.tex`: detailed status note and proof of the implication.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: arXiv:1812.00597.
- `supporting_paper_musial_2011.pdf`: decisive 2011 example.
- `supporting_paper_1906.07019.pdf`: independent later McShane counterexample.
- `figures/open_problem_page.png`: source PDF page containing Problems 4.7--4.8.
- `figures/supporting_example_page.png`: supporting PDF page containing Example 1.12.

## Review Recommendation

Verify the single functional-analytic bridge: norm countable additivity of the
Radstrom image implies uniform countable additivity of the positive scalar
densities, hence uniform integrability. If confirmed, record both Problems 4.7
and the strong-Pettis part of Problem 4.8 as negatively answered, with the
remaining Henstock questions left open.


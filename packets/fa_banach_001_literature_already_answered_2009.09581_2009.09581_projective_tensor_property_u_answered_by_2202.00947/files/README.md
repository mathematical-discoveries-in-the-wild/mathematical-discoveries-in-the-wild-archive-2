# Projective-Tensor Property-U Question Answered Negatively

Status: `literature_already_answered`.

Original source: Soumitra Daptari, Tanmoy Paul, and T. S. S. R. K. Rao, "Uniqueness of Hahn--Banach extension and related norm-1 projections in dual spaces," arXiv:2009.09581. Immediately after Theorem 3.7, the authors ask whether the theorem's equivalences for property-U and property-SU remain true when the injective tensor product is replaced by the projective tensor product.

Supporting answer: Soumitra Daptari and Tanmoy Paul, "Uniqueness of Hahn--Banach extensions and some of its variants," arXiv:2202.00947. In the subsection on tensor-product subspaces, the authors state that property-U need not be stable under projective tensor products, citing Basu--Rao, Example 2.3. They then recover only a restricted positive statement (Theorem 3.13 in the current arXiv source): if `Y` has property-SU in `Z`, every isometry in `L(X,Y^*)` has a unique norm-preserving extension to `L(X,Z^*)`. This is weaker than property-U, which quantifies over every bounded functional/operator.

The packet also gives a direct finite-dimensional counterexample satisfying all hypotheses of the original theorem:

- `X=ell_infinity^2`, an `L_1`-predual;
- `Z=ell_2^2`, whose dual has the RNP;
- `Y=span{e_1}`, which has property-SU in `Z`.

The functional `F((a,b),se_1)=s(a+b)/2` on `X tensor_pi Y` has the two distinct norm-one extensions

`G_0((a,b),(s,t))=s(a+b)/2`

and

`G_1((a,b),(s,t))=s(a+b)/2+t(a-b)/2`.

Thus `X tensor_pi Y` fails property-U in `X tensor_pi Z`, and therefore fails property-SU as well. This supplies a compact self-contained witness for the already-known negative answer.

Files:

- `source_paper.pdf`: arXiv:2009.09581
- `supporting_paper_2202.00947.pdf`: arXiv:2202.00947
- `main.tex`: compact literature-status note and explicit proof
- `solution_packet.pdf`: rendered status note

Direct-attack record: `runs/fa_banach_001/attempts/2009.09581_projective_tensor_property_u_counterexample_lane08.md`.

Ledger: `runs/fa_banach_001/ledger/results/2009.09581_projective_tensor_property_u_answered_by_2202.00947.json`.

# Candidate Counterexample: Discrete Schrodinger DOS vs Dixmier Measurability

Source paper: N. Azamov, E. Hekkelman, E. McDonald, F. Sukochev, and
D. Zanin, *An application of singular traces to crystals and percolation*,
arXiv:2202.03676 (open question on page 6).

Result type: `counterexample`

Status: candidate full negative answer to the discrete question, likely valid,
pending human review. The continuous Euclidean question remains open.

## Open Question

The source gives a diagonal self-adjoint operator with no density of states
although `f(H) M_w` is Dixmier measurable for every compactly supported
continuous `f`, and asks whether these definitions can still differ for
Schrodinger operators.

## Candidate Contribution

Yes. On the half-line, take

```text
H = Delta_D + M_v,
```

where `Delta_D` is the nearest-neighbor Dirichlet discrete Laplacian and `v`
alternates between 0 and 1 on successive dyadic blocks. Let `w_n=1/n`.

Ordinary volume averages of the diagonal of `H` oscillate because the density
of sites with `v_n=1` tends to `2/3` along `N=2^(2m)` and to `1/3` along
`N=2^(2m+1)`. Hence `H` has no DOS.

In contrast, every dyadic block has harmonic weight asymptotic to `log 2`.
For a polynomial `p`, the diagonal of `p(H)` agrees away from fixed-width
interface neighborhoods with one of the two constant-potential bulk values.
Those interface neighborhoods have finite total harmonic weight. Polynomial
approximation gives, for every `f in C_c(R)`,

```text
(1/log N) sum_(n<=N) <e_n,f(H)e_n>/n
    -> (tau_0(f)+tau_1(f))/2.
```

The source's modulated-operator eigenvalue formula converts this limit into
Dixmier measurability of `f(H)M_w` for every `f`.

## Files

- `source_paper.pdf`: original arXiv PDF.
- `figures/open_problem_crop.png`: full-width source-page crop.
- `main.tex`: complete candidate proof and review notes.
- `solution_packet.pdf`: rendered packet.
- `verification.md`: proof-obligation and QA report.
- `code/check_dyadic_schrodinger.py`: finite sanity checks.
- `tmp/`: LaTeX and PDF-rendering intermediates.

## Novelty Check

The run indexes and a bounded web/arXiv search on 2026-08-09 were searched for
the exact source sentence, arXiv id, authors, and close variants involving the
discrete Schrodinger DOS converse. No prior solution was found. Hekkelman's
2025 thesis, arXiv:2506.21950, still repeats this discrete case as unknown.
This is strong status evidence but not an exhaustive bibliographic claim.

## Human Review

Recommended for expert review as a full counterexample to the discrete
question. The main checks are the interpretation of “discrete Schrodinger
type,” application of the source's modulated eigenvalue theorem, and the
fixed-propagation locality argument. The construction does not address the
continuous Euclidean conjecture.

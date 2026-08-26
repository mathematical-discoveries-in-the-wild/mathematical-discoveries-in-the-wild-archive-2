# Little Hölder space M-ideal question from arXiv:math/0201144

Status: `literature_already_answered`

Source paper: H. Berninger and D. Werner, *Lipschitz spaces and M-ideals*,
arXiv:math/0201144, Extracta Mathematicae 18 (2003), 33–56.

Supporting answer: Nigel J. Kalton, *Spaces of Lipschitz and Hölder functions
and their applications*, Collectanea Mathematica 55 (2004), 171–217,
DOI [10.1344/CM.V55I2.4055](https://doi.org/10.1344/CM.V55I2.4055).

## Identification

Berninger and Werner ask whether, for `0 < alpha < 1`,

```text
H_alpha^0 = lip_0([0,1], |.|^alpha)
```

is an M-ideal in `H_alpha = Lip_0([0,1], |.|^alpha)`. The question appears on
page 4 at the end of the introduction and again in Section 4 through their
candidate “almond function” counterexample.

Kalton's Theorem 6.1 says that for a compact pointed metric space and a
nontrivial gauge `omega`, `lip_omega(M)` is the canonical predual of the
Lipschitz-free space and its bidual is `Lip_omega(M)`. Theorem 6.6, together
with the remark immediately after it, says that `lip(M)` is an M-ideal in
`Lip(M)` whenever `M` is compact and this predual condition holds. Taking
`M=[0,1]` and `omega(t)=t^alpha` gives the desired affirmative answer.

The conclusion is stronger than the original question: it applies to every
compact metric space with a nontrivial gauge.

## Search evidence

Cheap run indexes were searched for the arXiv id, title, Hölder/little
Lipschitz terminology, and M-ideals; no duplicate packet was found. A bounded
literature search found Kalton's primary paper and an independent later
thesis/conference abstract explicitly describing Theorem 6.6 as solving the
Berninger–Werner problem.

## Files

- `source_paper.pdf`: arXiv:math/0201144.
- `supporting_paper_kalton_2004.pdf`: decisive 2004 supporting article.
- `main.tex` and `solution_packet.pdf`: compact status note.

Ledger: `runs/fa_banach_001/ledger/results/0201144_holder_little_lip_mideal_answered_by_kalton_2004.json`.


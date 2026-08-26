# Full solution packet: block-clustered `C_0`-group generator

Run: `fa_banach_001`

Source: Grigory M. Sklyar and Vitalii Marchenko, “Hardy inequality and the
construction of infinitesimal operators with non-basis family of
eigenvectors,” arXiv:1405.2731v4, later *Journal of Functional Analysis* 272
(2017), 1017–1043.

Status: `candidate_full_solution_likely_valid`

## Result

The packet gives an affirmative answer to the question on page 32 of the
source paper.  It constructs an unbounded generator of a strongly continuous
group on a Hilbert space whose normalized eigenvectors form a Schauder basis
but not a Riesz basis.  The construction additionally makes the eigenvalues
simple and purely imaginary and gives the linear bound

```text
||T(t)|| <= 1 + |t|/2.
```

The mechanism is to repeat increasingly ill-conditioned finite prefixes of a
fixed conditional Hilbert-space basis in orthogonal blocks.  Frequencies in
block `m` are placed in a cluster of diameter inversely proportional to that
block's condition number.  The common frequency of the block tends to
infinity, making the generator unbounded, while only the tiny within-block
frequency differences interact with the bad basis geometry.

## Packet contents

- `solution_packet.pdf`: typeset proof and review notes.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: the original arXiv paper.
- `figures/open_problem_crop.png`: source page 32, containing the full question.
- `verification_report.md`: analytic verification checklist.
- `code/crop_open_problem.py`: reproducible source-page crop.

## Verification and novelty status

The proof is analytic; no numerical assertion is used.  The verifier report
checks the four possible failure points separately: the global Schauder basis,
failure of the Riesz inequalities, boundedness and strong continuity of the
direct-sum group, and identification/unboundedness of its generator.

A bounded search on 2026-08-09 used the exact wording of the question, the
authors' names, `bounded non-Riesz basis`, `conditional Schauder basis`, and
`C_0-group generator`, in the run's local arXiv corpus and web/arXiv search.
The later arXiv:1809.03079 and related 2021 paper concern complete minimal
families that do not form a basis.  No later source explicitly answering the
bounded Schauder non-Riesz question was found.  Novelty is therefore plausible,
not certified.

## Human review focus

Check the passage from unbounded finite-prefix condition numbers to the
non-Riesz orthogonal block basis, and the uniform estimate
`||T_m(t)|| <= 1 + 2^(-m)|t|`.  Once those are accepted, strong continuity and
the generator calculation follow from standard direct-sum arguments that are
included in full.

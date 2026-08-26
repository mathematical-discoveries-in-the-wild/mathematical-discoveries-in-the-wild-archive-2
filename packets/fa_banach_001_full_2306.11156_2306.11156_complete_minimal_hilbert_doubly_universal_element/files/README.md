# Candidate full solution: both universal-element questions

Status: **candidate full affirmative answer, pending expert review**.

This packet answers Questions 1 and 2 from Zhirayr Avetisyan, Martin
Grigoryan, and Michael Ruzhansky, *Elements (functions) that are universal
with respect to a minimal system* (arXiv:2306.11156), printed page 8.

It constructs one continuous dense embedding between separable
infinite-dimensional complex Hilbert spaces, one **complete minimal** system,
and one element whose Fourier series is universal both by ordinary partial
sums and by rearrangements.  The target topology is the ordinary Hilbert norm
and is strictly weaker than the source norm on the embedded copy.

The proof is self-contained.  Its two main ingredients are a coordinatewise
harmonic series whose sum range under rearrangements is all of `ell_2`, and a
dense Hilbert embedding which turns that series into the Fourier series of an
actual element without sacrificing completeness of the minimal system.

Scope limitation: this settles the abstract existential questions as stated,
but not the authors' preferred concrete case `L1(M) -> Lp(M)`, `0 <= p < 1`,
and not a classical trigonometric or Walsh system.

Files:

- `solution_packet.pdf` — expert-facing proof packet
- `main.tex` — LaTeX source
- `source_paper.pdf` — original arXiv paper
- `figures/open_problem_crop.png` — exact printed-page-8 question crop
- `verification.md` — independent proof-audit checklist
- `code/check_algebra.py` — finite identity/scheduling sanity checks (not proof)

Highest-value review points:

1. the uniform tail estimate in the countable interleaving lemma;
2. preservation of rearrangement universality after finite deletion;
3. completeness of the constructed biorthogonal system;
4. whether the source authors intended any extra restriction beyond their
   formal definition of a "non-trivial triple."

Ledger record:
`runs/fa_banach_001/ledger/results/2306.11156_complete_minimal_hilbert_doubly_universal_element.json`.

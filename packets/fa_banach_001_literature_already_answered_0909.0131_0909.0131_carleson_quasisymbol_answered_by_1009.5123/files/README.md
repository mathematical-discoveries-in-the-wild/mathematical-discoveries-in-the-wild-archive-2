# Literature answer: every bounded TTO has a Carleson-measure quasisymbol

status: `literature_already_answered`

source: A. Baranov, I. Chalendar, E. Fricain, J. Mashreghi, and D. Timotin,
*Bounded symbols and reproducing kernel thesis for truncated Toeplitz
operators*, arXiv:0909.0131.

supporting answer: A. Baranov, R. Bessonov, and V. Kapustin, *Symbols of
truncated Toeplitz operators*, arXiv:1009.5123; J. Funct. Anal. 261 (2011),
3437--3456.

## Identification

Remark 5.3 of the source (PDF page 19) asks whether every bounded truncated
Toeplitz operator on `K_Theta` has the form `A_mu^Theta` for a complex
Carleson measure `mu` for `K_Theta`.

The supporting paper explicitly says it proves Sarason's conjecture that every
bounded truncated Toeplitz operator has such a quasisymbol. Its Theorem 2.1(2)
(supporting PDF page 6) states that every bounded truncated Toeplitz operator
on `K_theta` admits a quasisymbol in `C_2(theta)`, exactly the class of finite
complex Borel measures whose total variation gives a bounded embedding
`K_theta -> L^2(|mu|)`. This is the source's definition of a complex Carleson
measure for the model space.

The supporting authors explicitly knew they were answering the Sarason
question, so this is `literature_already_answered`, not an agent-implied
reformulation and not a new run result.

## Scope

This packet settles only the Carleson-measure representation question in the
source remark. It does not settle the source's general reproducing-kernel
Question 3 or the later one-component/CLS characterization conjecture.

## Search evidence

The run indexes had no record for arXiv:0909.0131. Bounded web/arXiv searches
through 2026-08-09 used the title, exact question wording, `quasisymbol`,
`Carleson measure`, and the CLS/RKT keywords. They found the explicit theorem
in arXiv:1009.5123 and later surveys confirming the identification.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered note.
- `source_paper.pdf`: arXiv:0909.0131.
- `supporting_paper_1009.5123.pdf`: decisive later answer.
- `verification.md`: source/theorem audit and PDF QA.

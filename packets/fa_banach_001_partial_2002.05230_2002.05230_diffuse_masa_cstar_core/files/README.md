# Diffuse masa C*-core for the Koszmider state

This packet addresses the nonatomic-masa question on page 2 of Piotr
Koszmider, *A non-diagonalizable pure state*, arXiv:2002.05230.

It proves a sharp partial theorem.  Every pure state obtained from the source
projection face is multiplicative on a weak-operator dense copy of
`C([0,1])` inside a nonatomic masa of `B(ell_2)`.  Equivalently, one can find a
positive multiplicity-one contraction `A` in the state's multiplicative
domain whose generated von Neumann algebra is diffuse.  The packet also
isolates why this does not yet imply multiplicativity on the whole masa.

Files:

- `solution_packet.pdf`: self-contained three-page mathematical packet.
- `source_paper.pdf`: arXiv v3 source PDF (11 pages).
- `source_question.pdf`: page 2, containing the exact question.
- `main.tex`: packet source.
- `VERIFICATION.md`: proof and artifact checks.
- `code/check_boolean_core.py`: finite exact/rational model checks for the
  commuting Boolean construction and dyadic spectrum.

Reproduce the computational check:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2002.05230_diffuse_masa_cstar_core/code/check_boolean_core.py
```

Compile:

```sh
cd runs/fa_banach_001/solutions/partial/2002.05230_diffuse_masa_cstar_core
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
cp main.pdf solution_packet.pdf
```

Render for inspection:

```sh
/opt/homebrew/bin/gs -q -dNOPAUSE -dBATCH -sDEVICE=png16m -r170 \
  -sOutputFile=rendered/page-%02d.png solution_packet.pdf
```

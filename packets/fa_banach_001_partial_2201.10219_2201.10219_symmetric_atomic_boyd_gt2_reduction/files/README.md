# Symmetric atomic Hardy spaces above Boyd index two

This packet addresses the open remarks after Theorem 4.12 of Hong--Ma--Wang,
arXiv:2201.10219.

It proves that for `0<p<=1` and `p_E>2`, the symmetric atomic and symmetric
crude-atomic column Hardy spaces both coincide, with equivalent quasi-norms,
with the standard `(p,2)` atomic Hardy space.  Thus for `0<p<1` the remaining
equality with `h_p^c` is exactly the foundational standard atomic-decomposition
problem already left open in arXiv:2001.08775.

Files:

- `solution_packet.pdf`: self-contained proof packet.
- `source_paper.pdf`: compiled source paper arXiv:2201.10219.
- `source_factorization_and_question.pdf`: source pages 18--23.
- `supporting_atomic_paper.pdf`: compiled arXiv:2001.08775.
- `supporting_atomic_results.pdf`: supporting pages 14--17.
- `main.tex`: packet source.
- `VERIFICATION.md`: mathematical and artifact checks.
- `code/check_exponents.py`: exact rational audit of the crude-atom exponents.

Check:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2201.10219_symmetric_atomic_boyd_gt2_reduction/code/check_exponents.py
```

Compile and render:

```sh
cd runs/fa_banach_001/solutions/partial/2201.10219_symmetric_atomic_boyd_gt2_reduction
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
cp main.pdf solution_packet.pdf
/opt/homebrew/bin/gs -q -dNOPAUSE -dBATCH -sDEVICE=png16m -r170 \
  -sOutputFile=rendered/page-%02d.png solution_packet.pdf
```


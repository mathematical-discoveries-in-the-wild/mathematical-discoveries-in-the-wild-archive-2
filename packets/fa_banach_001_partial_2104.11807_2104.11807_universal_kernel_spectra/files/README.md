# Universal spectral freedom for a fixed positive kernel

This packet addresses Question 2.12 of Jorgensen--Song--Tian,
*Positive Definite Kernels, Algorithms, Frames, and Approximations*,
arXiv:2104.11807.

It gives an exact fixed-kernel theorem: a single elementary p.d. kernel on
`{0} union N` realizes every nonempty closed subset of `[0,infinity)` as the
spectrum of `T_mu T_mu^*` when only the regular atomic measure varies.  This
shows that positivity and closedness are the only kernel-independent spectral
restrictions.

Files:

- `solution_packet.pdf`: self-contained proof packet.
- `source_paper.pdf`: arXiv source PDF (37 pages).
- `source_question.pdf`: source page 7 containing Question 2.12.
- `main.tex`: packet source.
- `VERIFICATION.md`: mathematical and artifact checks.
- `code/check_diagonal_model.py`: exact finite-support checks.

Check:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2104.11807_universal_kernel_spectra/code/check_diagonal_model.py
```

Compile and render:

```sh
cd runs/fa_banach_001/solutions/partial/2104.11807_universal_kernel_spectra
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
cp main.pdf solution_packet.pdf
/opt/homebrew/bin/gs -q -dNOPAUSE -dBATCH -sDEVICE=png16m -r170 \
  -sOutputFile=rendered/page-%02d.png solution_packet.pdf
```


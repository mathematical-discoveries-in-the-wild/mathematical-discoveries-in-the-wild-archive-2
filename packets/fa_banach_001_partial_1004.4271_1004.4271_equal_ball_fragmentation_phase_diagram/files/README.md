# Exact equal-ball fragmentation phase diagram

This packet gives a substantial partial answer to Conjecture 6.1 of
arXiv:1004.4271. It proves that among all finite or countable partitions of a
fixed mass into spherical droplets, unequal masses never lower the limiting
energy. It also gives the exact droplet-count transitions, proves strict
stability under mass-preserving perturbations, and solves the variational
problem over finite unions of balls.

It does **not** claim the full liquid-drop conjecture for arbitrary shapes.

## Build and check

```sh
conda run --no-capture-output -n sandbox python verify.py
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The final artifact is `solution_packet.pdf` (copied from `main.pdf` after
successful compilation and visual inspection).

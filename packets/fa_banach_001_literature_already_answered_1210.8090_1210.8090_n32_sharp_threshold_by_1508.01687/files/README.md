# The N_{3,2} multiplier threshold is sharp

The main theorem of arXiv:1210.8090 proves the spectral multiplier theorem on
the free two-step group `N_{3,2}` under local `W_2^s` regularity for `s>3`,
and conjectures that `3=d/2` is sharp.

Martini and Müller, arXiv:1508.01687, prove a lower bound of `d/2` for every
homogeneous sub-Laplacian on every two-step stratified group.  Applied to
`N_{3,2}`, this matches the earlier upper bound and gives exact critical
threshold `3`.  The later paper explicitly cites the `N_{3,2}` theorem among
the earlier `d/2` results that its lower bound makes sharp.

The packet is a literature-status identification, not a new proof.  The two
bundled paper PDFs were compiled from the arXiv source trees already cached in
the repository.

Build the status note with:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -jobname=solution_packet main.tex
```


# Exact frequencies for quadratic parabolic Koenigs domains

Status: candidate_substantial_partial_likely_valid

Source: Carlos Gómez-Cabello and F. Javier González-Doña, *On frequencies of parabolic Koenigs domains*, arXiv:2507.08514v1.

## Result

For every c>0 and 1<=p<infinity, let

Omega_c = {x+iy : x>c y^2}.

The packet proves the exact formula

Freq_p(Omega_c) = {Re(lambda)<0} union {it : |t|<pi c/p}.

In particular, both critical imaginary frequencies +/- i pi c/p are excluded. The same formula holds for every translated quadratic boundary x>x0+c(y-y0)^2.

This completely resolves the explicit psi_Omega(t)=t^2 membership gap in Remark 5.14 of arXiv version 1. It is a substantial partial result for the general parabolic Koenigs-domain frequency problem, which remains open.

## Mechanism

The conformal map

F_c(z)=cosh(pi sqrt(cz-1/4))

maps Omega_c onto the right half-plane. On the boundary z=c y^2+i y, it equals i sinh(pi c y). Harmonic measure at 1/(4c) is therefore exactly

c sech(pi c y) dy.

This density gives the sharp necessity and endpoint failure. A separate interior estimate after a Cayley transform proves Hardy membership below the threshold.

## Source-version note

The packet stores arXiv v1 as source_paper.pdf, because its PDF page 38 contains the explicit quadratic example and is reproduced in figures/open_problem_crop.png. The current revision removes that particular sentence while retaining the surrounding general topic.

## Files

- main.tex: full proof packet.
- solution_packet.pdf: rendered packet.
- source_paper.pdf: arXiv v1 source paper.
- figures/open_problem_crop.png: full-width source crop from v1 PDF page 38.
- code/check_quadratic_map.py: numerical regression check.
- tmp/: build and rendering intermediates.

## Novelty and review

Run-index and bounded web/arXiv searches through 2026-08-17 found the source and adjacent completeness literature, but no prior exact formula for the quadratic domain. Novelty confidence is moderate because the conformal computation is elementary and could exist under different terminology.

Recommended review focus: the strip quotient, the harmonic-measure density, and the uniform disk H^p estimate.

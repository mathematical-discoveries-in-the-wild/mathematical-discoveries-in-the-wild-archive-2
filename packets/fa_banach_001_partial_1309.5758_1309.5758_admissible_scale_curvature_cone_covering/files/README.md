# Cone Covering at the Admissible Curvature Scale

Source: A. Amenta and M. Kemppainen, *Non-uniformly local tent spaces*,
arXiv:1309.5758; Publ. Mat. 59 (2015), 245–270.

Status: substantial partial result, likely valid.

## Result

The source proves its cone-covering lemma under nonnegative sectional
curvature and asks which doubling Riemannian manifolds admit such covers.
The packet extends the lemma to negative curvature under the scale-invariant
condition

```text
sec_z >= -kappa^2 / m(x)^2
for z in closure(B(x, beta m(x))), uniformly in x.
```

Rauch comparison shows that a uniformly fine net of initial directions
retains the source's decisive radial estimate. The rest of the proof uses
only the source's local-doubling extension lemma and admissibility
comparability. The result includes every complete manifold with a global
sectional-curvature lower bound and bounded admissibility function, hence
all compact manifolds under the standard bounded choices of `m`.

## Files

- `main.tex`: exact theorem and proof.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: original source PDF.
- `figures/open_question_crop.png`: PDF-page-17 crop of Remark B.6.
- `code/verify_angular_bound.py`: dimensionless angular-bound audit.
- `verification.md`: reproducibility, checksum, and visual-QA record.

## Human Review Recommendation

Check the angular Jacobi-field comparison inside the admissible ball and
the transfer of the source's two case splits after radial control is
restored.

# Verification report

## Mathematical checks

- The abelianization push-forward `Q:ell^1(F_2)->ell^1(Z^2)` is a contractive
  quotient algebra homomorphism; its kernel `I` is a closed two-sided ideal.
- `I^perp=Q^*ell^infinity(Z^2)`, so
  `I^*=ell^infinity(F_2)/ell^infinity(Z^2)` with the indicated module actions.
- Conjugation acts trivially on `I^perp`, because abelianization is constant on
  conjugacy classes.
- Every nonidentity conjugacy orbit of `F_2` has an infinite cyclic stabilizer.
  Bounded Shapiro and amenable vanishing therefore give
  `H_b^n(F_2,ell^infinity(F_2\{e}))=0` for `n>=1`; the standard contractions
  are uniformly norm-controlled, so the orbitwise product causes no gap.
- The split quasimorphism has defect at most three and is not a bounded distance
  from a homomorphism.  Hence its scalar defect class in `H_b^2(F_2,C)` is
  nonzero.
- Multiplication by the point mass at `(1,0)` gives a nonzero cocycle in the
  annihilator module, verified by the equivariant evaluation functional at
  `(1,0)`.
- Its inclusion in `ell^infinity(F_2)` takes values in functions vanishing at
  the identity, hence is a coboundary.  The quotient one-cocycle is nonzero by
  the explicit lifting contradiction in the packet.
- The derivation/cocycle dictionary was checked in both directions, including
  the right multiplication by `delta_g`, bounded extension from point masses,
  and the exact inner/coboundary correspondence.

Run the finite exact verifier with:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/0503093_free_group_not_ideally_amenable/code/verify_split_quasimorphism.py
```

## Source and literature checks

- Source page 407 explicitly asks: “Is `ell^1(F_2)` ideally amenable?”
- The source already settles the ordinary augmentation ideal positively for
  `F_2`; the packet uses the strictly different abelianization-kernel ideal.
- Johnson--White's nondiscrete augmentation counterexample does not resolve the
  discrete free-group question.
- Searches on 2026-08-17 covered the run indexes, arXiv, exact question text,
  `ideal amenability` with free-group keywords, and the abelianization-ideal /
  bounded-cohomology route.  No duplicate full resolution was found.
- A 2010 follow-up still described the group-algebra question as open.  The
  candidate novelty is the coefficient-sequence construction; all bounded
  Shapiro, amenability, centralizer, and quasimorphism ingredients are classical.

## Packet QA

- `source_paper.pdf` was rebuilt from the archived official arXiv source because
  the legacy PDF endpoint returned an error; only two unavailable legacy font
  names were replaced in a temporary build copy.  The mathematical source text
  is unchanged, and the committed `source_paper.tex` is the untouched source.
- The final packet was compiled twice and checked for unresolved references,
  citations, overfull boxes, and malformed glyphs.
- Every rendered packet page and the source-evidence image was visually
  inspected.
- Final PDF: 4 A4 pages.
- SHA-256 `solution_packet.pdf`:
  `5901af599880ffa913960a8d9fdd795412b0e9fa707b9828b049d266d139cdfd`.
- SHA-256 `source_paper.pdf`:
  `4db5fa849d61fa52e3e002a46f00820dac5f064e76f87a1199632d92aa3ceb43`.
- SHA-256 `figures/source_question_page.png`:
  `b6cd0fda0822ca720176228a35b6ac40c60a7d73d294e7a586f9037668721948`.
- SHA-256 `code/verify_split_quasimorphism.py`:
  `33370dfe964a526ea98294912c745a9ed8dc89dad9e0dd01f97819867a8016ca`.

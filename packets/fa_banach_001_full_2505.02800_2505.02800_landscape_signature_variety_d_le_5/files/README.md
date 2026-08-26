# Landscape signature varieties in dimensions at most five

Status: `candidate_full_likely_valid` (computer-assisted exact proof).

This packet proves Conjecture 4.3 of Vincenzo Galgano, Heather A. Harrington,
and Daniel Tolosa, *Discrete signature tensors for persistence landscapes*,
arXiv:2505.02800v3.  For every nontrivial dimension `2 <= d <= 5`, the
projective variety of second Chen signatures of persistence-landscape paths is
the whole loop variety

```text
P(wedge^2 C^d).
```

The proof has two parts.

1. Ten explicit integer-endpoint barcodes give a hierarchical exact basis of
   `wedge^2 R^d`: the first `binom(d,2)` work in dimension `d`.  Their exact
   rational determinant certificates are `4`, `44`, `-781/8`, and
   `-667755/2048` for `d=2,3,4,5`.
2. Barcode clusters with disjoint time supports concatenate as closed landscape
   loops, so second signatures add.  Dilation by `s` scales the second signature
   by `s^2`.  Hence every positive linear combination of the basis signatures
   is itself realized by one barcode.  This is a nonempty Euclidean-open cone,
   and therefore is Zariski dense in the whole skew space.

The exact verifier is `code/verify_signature_basis.py`.  It uses only Python's
standard-library rational arithmetic, reconstructs every landscape vertex from
tent kinks and pairwise crossings, applies the polygon-area formula, and checks
all four determinants without numerical tolerances.

Human review should focus on (i) the convention identifying the skew coordinate
with `integral lambda_i d lambda_j`, (ii) the disjoint-support concatenation
argument, and (iii) the exact finite certificate.  The original source and the
page-26 conjecture crop are included for audit.


# Verification record

## Mathematical checks

- The vectors `f_k` form an algebraic basis of `c_00` block by block.
- The cone is proper and generating by uniqueness of the `f`-coordinates.
- In standard coordinates it is the intersection of the closed half-spaces
  `x_(2j) >= 0` and `x_(2j-1) >= j x_(2j)`, hence is closed relative to
  `c_00` with its Euclidean norm.
- Empty interior is witnessed at every cone point by a small unused even
  coordinate.
- For `x_j=f_(2j)-f_(2j-1)`, coefficient uniqueness forces any decomposition
  `x_j=u-v` with `u,v` in the cone to have the `(2j-1)`st standard coordinate
  of both `u` and `v` at least one. Hence the extension norm is at least two.
- The ambient norm is `1/j`, so the two norm topologies differ.
- Andô's Lemma 1 was checked in the original 1962 paper: a closed generating
  cone in a Banach space has uniformly norm-bounded positive decompositions.
  This verifies the stated positive complement and explains why the example
  must evade completeness or closedness.

## Source and literature checks

- The local arXiv TeX source was compiled successfully to 25 pages.
- Printed page 12 contains the exact natural question.
- Printed page 22 contains the nonempty-interior sufficient condition.
- Cheap run indexes contain no prior result for arXiv:2508.17052.
- Bounded exact-phrase, title, generating-cone, bounded-decomposition, and
  Andô-theorem web searches found no later explicit answer to the source
  question. The broader bounded-decomposition theory is classical, so novelty
  is provisional and narrowly scoped.

## Packet QA

- `solution_packet.pdf` compiled with `latexmk` without fatal errors.
- All packet pages were rendered to PNG and visually inspected.
- Text extraction was checked for the theorem, sequence witness, and both
  bibliography entries.

## Checksums

- Raw arXiv source archive:
  `f667f6381a38967d5b12c0bc209dce581996c83be38f8fc995af8c6381f71c11`
- Locally compiled source paper:
  `bdc792ccd51d2fc976ec198e97f8e8ccec25e7d182793d586cd1c1e5346cf5ad`
- Open-question crop:
  `099d75d87a95e539d22090aad7b7a9741d4cbc67c1abf72f3fd77b9b5f3c3362`
- Interior-lemma crop:
  `963818a4485c758d84b43c0bd6908b023746223003c01b5c74947361c26d8d58`
- Final packet:
  `004b0d8ab1f64a95b2fed320acf86a1ae1c38b6fd09c4f684874bc55cf666919`

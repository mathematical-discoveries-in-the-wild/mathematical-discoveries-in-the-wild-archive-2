# Verification report

Status checked: `candidate_partial_result_likely_valid`.

## Mathematical checks

- The two source questions were verified in the cached official TeX for
  arXiv:1107.4532: equality of the Bonsall and orbital radii, and the
  finite-dimensional continuum-spectrum problem.
- Gripenberg's 2015 official author PDF was inspected. Example 3.1 is
  continuous, order-preserving, and homogeneous on a closed pointed convex
  cone; Lemma 3.5 gives `tilde r_C(f) >= 1` and `r_C(f) <= 1/2`.
- For `F_a(x)=sqrt(<a,x>x)`, homogeneity and continuity are immediate.
- Order preservation was checked from
  `<a,y>y-<a,x>x=<a,y>(y-x)+(<a,y>-<a,x>)x` and the Jordan
  Löwner--Heinz inequality.
- The square-root order inequality was proved self-containedly from inverse
  order reversal and the integral representation of `sqrt(s)`.
- Squaring the eigenvector equation in a Jordan frame proves the exact
  spectrum formula: all nonzero spectral coefficients of an eigenvector are
  equal, so eigenvectors are precisely positive multiples of nonzero
  idempotents.
- The Peirce rotation was expanded using `c_i z=z/2`, `c_1 c_2=0`, and
  `z^2=c_1+c_2`; it is a trace-one idempotent for every parameter value.
- The symmetric-cone iff follows because a symmetric cone is polyhedral
  exactly when every simple Jordan factor has rank one.
- In the planar base obstruction, all selected circle points are exposed;
  Milman's converse gives no other extreme points. Planar faces are points or
  edges, hence countably many. Coning preserves countability of faces, and
  the source's same-part lemma limits the spectrum to one eigenvalue per
  part.

## Upgrade and scope checks

- Four focused upgrade attempts were made. The naive assertion that every
  nonpolyhedral cone admits continuum spectrum was disproved by the explicit
  countably-faced cone.
- The source's countable atomic series cannot be promoted by replacing the
  sum with an atomless integral.
- The Jordan construction gives a full answer for all symmetric cones.
- Extension from a symmetric face to an arbitrary cone stops without a
  positive retraction; the general finite-dimensional classification is not
  claimed.

## Literature and novelty bounds

Cheap run indexes contained no result for arXiv:1107.4532. Primary-source web
searches through 11 August 2026 found Gripenberg's answer, the original
positive-semidefinite matrix example, the later Lemmens--Nussbaum book, and
papers using a different complementarity notion of cone spectrum. No source
found states the symmetric-cone iff, the exact spectrum formula for `F_a`, or
the countably-faced nonpolyhedral obstruction. This is a bounded search, not
an exhaustive novelty claim.

## Artifact checks

- `solution_packet.pdf` compiles in 3 pages with no LaTeX warnings,
  unresolved references, or box warnings.
- `source_paper.pdf` is a 14-page compilation of the cached official source.
  One invalid legacy byte in a bibliography page range was normalized to a
  double hyphen in the temporary build copy; mathematical content is
  unchanged.
- `supporting_eja_1911.00579.pdf` is a 21-page compilation of cached official
  TeX. Its single 3.1-point overfull line is in the original source and is
  visually unclipped.
- Extracted solution-packet text was checked for the exact-spectrum lemma,
  symmetric-cone theorem, nonpolyhedral obstruction, literature answer, and
  scope disclaimer.
- All 3 packet pages, all 14 source pages, and all 21 supporting-paper pages
  were rendered and visually inspected. They are legible and unclipped.

Final SHA-256 of `solution_packet.pdf`:

```text
b5c20a533bc069acc7526170ca8528f490c95f907dde0026e056afedf647b43a
```

Highest-value human checks: the standard Jordan inverse-order identity used
in Lemma 1 and the assertion that the chosen `V_12` vector can be normalized
by `z^2=c_1+c_2`. The remaining deductions are explicit.


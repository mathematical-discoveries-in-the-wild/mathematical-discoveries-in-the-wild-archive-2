# Verification report

Status: `candidate_full_solution_likely_valid`.

Verification date: 2026-08-11.

## Mathematical audit

1. **Exact source signal.** The proposed extension appears on source PDF page
   17, Section 4: the authors first restrict their Q-tensor application to
   surfaces without boundary and then say it would be interesting to extend
   Theorem 1.4 to VMO line fields. The two explicitly numbered questions in
   the introduction were checked and are answered later in the same paper.

2. **Bundle identification.** In a positive tangent frame `(e1,e2)`, the
   displayed Q-frame `(A1,A2)` was expanded directly. Rotating `(e1,e2)` by
   `theta` rotates `(A1,A2)` by `2 theta`. Hence
   `e(Sym^2_0(TN))=2e(TN)` with the stated orientation.

3. **Relative-Euler sign.** On the positively oriented disk the boundary
   tangent has angle `theta+pi/2`, so its Q-tensor has phase `2theta+pi` and
   degree `2`. A constant Q-section has relative winding `-2` and relative
   Euler number zero. This fixes the formula
   `e(E,g)=2 chi(N)+w(g)`. The annulus check gives cancelling boundary
   contributions.

4. **Obstruction completeness.** For an oriented rank-two bundle over a
   compact oriented surface, a prescribed nonzero boundary section extends
   without zeros exactly when its relative Euler class vanishes. The packet
   includes the relative CW obstruction proof; there are no cells above
   dimension two, and evaluation on the relative fundamental class detects
   `H^2(N,boundary N;Z)`.

5. **VMO regularization.** The source's averaging, fibre projection, trace
   compatibility, homotopy stability, and collar interpolation were checked
   for dependence on the tangent-vector structure. Each step uses only a
   smooth Euclidean subbundle and a smooth family of orthogonal projections,
   so it applies to `E=Sym^2_0(TN)`. For uniformly positive bounded sections,
   the elementary mean-oscillation estimate gives uniformly nonzero
   regularizations.

6. **Sufficiency gluing.** The collar field is nonzero and transports the VMO
   boundary class to a continuous nonzero section on the inner collar curve.
   Additivity identifies the core obstruction with `2 chi(N)+w(g)`. When it
   vanishes, the relative obstruction lemma supplies a continuous nonzero core
   extension. Matching on the interface makes the glued section VMO; radial
   clamping preserves VMO and the trace.

7. **Scope audit.** The theorem is stated only for the compact oriented
   surface/Q-tensor setting in the paragraph that raises the proposal. It does
   not claim a scalar classification for higher-dimensional projective tangent
   bundles or for nonorientable surfaces.

## Computational checks

Command:

```text
conda run --no-capture-output -n sandbox python \
  code/verify_transition_and_winding.py
```

Output:

```text
double_angle_max_error=2.429e-16
disk_winding_q_tau=2.000000000000
disk_relative_winding_constant_vs_q_tau=-2.000000000000
disk_relative_euler=2*chi+w=0.000000000000
annulus_total_reference_winding=0.000000000000
```

The script checks signs and local identities only; it is not used as proof.

## Literature audit

The run's four cheap indexes had no duplicate. Exact and close phrase searches
and the complete OpenAlex citing-work query for DOI
`10.1016/j.jfa.2015.09.005` found no later explicit answer. See
`novelty_search.md` for bounds and caveats.

## PDF and evidence QA

- `solution_packet.pdf`: 7 pages, PDF 1.7, 504000 bytes.
- `source_paper.pdf`: 27 pages, locally compiled official arXiv source.
- The solution packet compiled with no unresolved references, undefined
  citations, overfull boxes, or underfull boxes.
- All seven solution-packet pages were rendered at 150 dpi and visually
  inspected. Text, equations, theorem boxes, references, and margins are
  legible; no clipping or overlap was found.
- `figures/open_problem_crop.png` was rendered from source PDF page 17 and
  visually inspected. It contains the section heading, the complete sentence
  proposing the extension, and sufficient surrounding context.

SHA-256:

```text
0c0369c39c37a2df10778bc586d85bc90e28eabb2052a12e64a0180ad31fe9d0  solution_packet.pdf
825f626389801fa3a0625d7a7c458bf66d5d34fa20e37f247d8253bc98276755  source_paper.pdf
cc70733b115b57b9c0906fd0f8c26e54457d2dd9133eb7cde9392c412a48c4e2  figures/open_problem_crop.png
```

## Remaining human-review risks

- Confirm that the authors intended the surface-with-boundary Q-tensor
  interpretation, rather than a higher-dimensional projective-tangent theory.
- Check the relative-Euler sign convention against the reviewer's preferred
  boundary-orientation convention.
- Check the bundle-valued reformulation of the source's VMO collar lemma.

No mathematical dependency remains unproved within the stated scope.

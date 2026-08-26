# Verification report

Status: `candidate_partial_result_likely_valid_needs_human_review`

## Mathematical audit

1. **Boundary norm identity.** Under the isometry `X*=ell_1`, the extreme
   points of the dual ball are exactly `+-e_n`. The maximum face of the
   weak-star compact dual ball for any `x` has an extreme point, so some
   signed coordinate functional norms `x`. Hence
   `||x||=sup_n |e_n(x)|`; the map into `c` is genuinely isometric.
2. **Range calculation.** For `Y=JX`, a functional `(a_0,a) in c*` vanishes
   on `Y` iff `a_0 f+a=0` in `ell_1`. Thus
   `Y^perp=span{(1,-f)}=W_f^perp`. Both spaces are closed, so Hahn-Banach
   gives `Y=W_f`. No surjectivity assumption is hidden here.
3. **Perturbations.** If two coordinates are unsaturated, either an
   unsaturated zero coefficient gives a one-coordinate perturbation, or two
   nonzero coefficients give `f_j e_i-f_i e_j`. If the only unsaturated
   coordinate has zero coefficient, the same one-coordinate perturbation
   applies. These cases exhaust all ways an alleged extreme point can have
   an unsaturated coordinate.
4. **Equality case.** Once at most one coordinate is unsaturated, convergence
   forces the limit to be `s=+-1`. The chain
   `1 <= sum |f_n||x_n| <= ||f||_1 <= 1` forces `||f||_1=1`, saturation on
   the support, and a common sign for every nonzero `f_n x_n`. The remaining
   possible unsaturated coordinate would have coefficient zero and was
   already excluded.
5. **Converse extremality.** A sequence with every coordinate equal to `+-1`
   is extreme in the full cube `B_c`; if it also satisfies the hyperplane
   equation, it is automatically extreme in `B_{W_f}`.
6. **Hull obstruction.** For two support indices, all extreme points satisfy
   the same signed-coordinate equality. The vector
   `f_j e_i-f_i e_j` belongs to `W_f` but has signed coordinates of opposite
   signs, so a small multiple is in the ball outside the closed convex hull.
7. **Singleton support.** Norm one makes `f=+-e_k`; deleting coordinate `k`
   is an onto isometry from `W_f` to `c`. The displayed two-dimensional
   subspace of `c` has a polar with infinitely many exposed points, proving
   directly that `c` is not polyhedral.

No numerical experiment is used as evidence.

## Literature audit

- Cheap run indexes: no prior packet or attempt for arXiv:2303.10023.
- Local source corpus: searched the source, arXiv:1503.09088, and
  arXiv:1506.08559.
- External search: exact Problem 6.8 wording, title/DOI, `polyhedral
  Lindenstrauss`, `hyperplane of c`, `weak-star convergent basis`, and
  `closed convex hull of its extreme points`.
- OpenAlex metadata for DOI 10.4064/sm230710-31-12 reported zero citing works
  on 2026-08-11.
- No prior statement of the packet theorem was found. Novelty confidence is
  bounded and moderate.

## Rendering audit

The final packet compiles to five pages with no LaTeX warnings. All five
pages were rendered to PNG and inspected at full-page scale. The theorem,
proof displays, references, and footer text are legible; no content overlaps
or runs outside the page. The source-paper crop containing Problem 6.8 was
also regenerated with a tightened crop box and inspected separately at
original resolution; it is sharp, complete, and free of clipping or stray
text from the following section.

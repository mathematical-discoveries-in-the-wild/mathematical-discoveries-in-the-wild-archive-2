# Verification report

## Mathematical checks

- The endpoint rotation differs from the identity on a two-dimensional
  subspace only, so it belongs to `GL^p(H)` for every finite `p`.
- The nonfactorization proof uses the exact flag actions
  `g_+ e_1=e_1` and
  `g_- e_2 in closure(span{e_2,e_3,...})`.  No determinant, convergence, or
  tail-decoupling assumption is used.
- Direct SymPy algebra verifies the explicit factorization of the rotation
  for `cos(theta) != 0`, including determinant one of both factors.
- The upper factor has Schatten distance `|tan(theta)|` from identity, and
  the lower factor has an entry `sec(theta)`; both become unbounded at the
  nonfactorable endpoint.
- Allowing a non-unit invertible upper diagonal changes `g_+e_1=e_1` to
  `g_+e_1=c e_1` with `c != 0` and leaves the contradiction intact.

Run the verifier with:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2511.02107_no_global_triangular_factorization/code/verify_rotation_factorization.py
```

## Source and scope checks

- Source PDF page 32 gives the local factorization in Proposition 7.3 and
  asks in Remark 7.4 whether a global upper/lower decomposition exists.
- The counterexample answers that precise global triangular-factorization
  question negatively.
- Source Remark 6.6 asks a separate question about an Iwasawa decomposition
  for a restricted group on a polarized Hilbert space.  The packet makes no
  claim about it.

## Novelty check

On 2026-08-17 the run indexes were searched for arXiv:2511.02107 and for
Schatten triangular-factorization terms; no duplicate was found.  An official
arXiv API search for `triangular factorization` together with `Schatten`
returned no matching paper, and a bounded OpenAlex search for the global
upper/lower decomposition returned no result.  Since finite-dimensional LU
factorization is classically nonglobal without pivot conditions, the
underlying obstruction is elementary and may be folklore; novelty here means
the explicit finite-rank observation answering Remark 7.4, not a claim that
the pivot phenomenon itself is new.

## Packet QA

- Official source PDF and TeX are included locally.
- The source-question image is rendered from PDF page 32.
- The final LaTeX log has no box, reference, or layout warnings, and every
  rendered packet page was visually inspected.
- Final PDF: 3 A4 pages.
- SHA-256 `solution_packet.pdf`:
  `3d097471bfcc78087c60ce4749e0e47e15b87cfd73731ee4344714906ebac237`.
- SHA-256 `source_paper.pdf`:
  `bd7f9c86c2a5efa66a610f68b95b7e1999689fa3a7206e0a3dfd16dddbed3431`.
- SHA-256 `figures/source_page_32.png`:
  `de0faf64adf2d778c0626c4b75eeb2544941fa447d63b6af19fe04818cb46bfa`.
- SHA-256 `code/verify_rotation_factorization.py`:
  `ab8c89305e5764b662538fa7af6edb624ee0b3e37fb36b335532f7b8a03526de`.


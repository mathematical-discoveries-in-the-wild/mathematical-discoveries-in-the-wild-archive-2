# Verification report

Verdict: `likely valid candidate partial result`

## Formal audit

1. **Block normalization.**  For pairwise disjoint row blocks `R_l` and
   column blocks `C_l`, the restrictions satisfy
   `sum alpha_l^2 <= ||s||_2^2` and
   `sum beta_l^2 <= ||t||_2^2`.
2. **Exact scaling.**  Writing `s_l=alpha_l u_l` and
   `t_l=beta_l v_l` extracts the factor `alpha_l beta_l` from the scalar
   Rademacher sum in block `l`; zero restrictions are harmless.
3. **Source theorem used at the right scope.**  Proposition 1.4 of the source
   gives the constant-factor upper comparison for an arbitrary `0-1` mask.
   Scalar multiplication preserves it, and rectangular masks may be padded by
   zero rows or columns.
4. **Local-to-global sparse norm.**  Every `p`-sparse mask contained in one
   block is also an admissible global mask.  Its embedded operator norm is
   unchanged, so `M_p(A_l) <= M_p(A)`.
5. **No block-count loss.**  Minkowski gives a sum of
   `alpha_l beta_l`; Cauchy--Schwarz bounds this by one.  This is the decisive
   step and uses disjointness on both the row and column sides.
6. **Reverse inequality.**  The source's general lower bound applies.  The
   packet also gives the short conditional-expectation/event proof, so no
   unproved reverse estimate is hidden.

## Adversarial checks

- Arbitrarily many blocks: the proof constant is unchanged.
- Blocks with zero restrictions of `s` or `t`: omitted without division.
- Negative block scalars: absorbed into the independent Rademacher signs; the
  sparse norm already uses absolute values.
- Noninteger `p`: cardinality means at most `floor(p)`, exactly as in the
  source comparison; the event estimate still gives a factor at least `1/2`.
- Rectangular block sizes: zero-padding reduces to the square formulation.

No computational experiment is needed: the argument is a deterministic
norm inequality with all constants inherited from the proved `0-1` theorem.

## Limitations / reviewer focus

The result is partial and should not be read as a circulant solution.  A
reviewer should check the exact scope of “orthogonal direct sum”: the row
blocks must be pairwise disjoint and the column blocks must independently be
pairwise disjoint.  If only one side is disjoint, the final Cauchy--Schwarz
bound is unavailable.


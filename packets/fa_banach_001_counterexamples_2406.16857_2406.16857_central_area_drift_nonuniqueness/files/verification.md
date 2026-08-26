# Verification record

## Source and scope

- Source: Darrick Lee, *The Surface Signature and Rough Surfaces*,
  arXiv:2406.16857.
- Exact question: “Sewing with Rectangular Increments,” PDF page 56; the
  associated warning is Remark 5.23 on PDF page 41.
- Claimed scope: nonuniqueness among full multiplicative double-group lifts
  satisfying the paper's rectangular `rho`-Hölder conditions, for
  `1/2 < rho <= 2/3`.
- Not claimed: impossibility of selecting a canonical lift after adding a
  normalization, locality/naturality axiom, or smooth-approximation rule.

## Mathematical audit

1. In degree three, the Peiffer subspace is zero because its generators have
   total degree at least four.
2. The displayed Jacobi cycle expands into six distinct orthonormal free
   bimodule basis vectors, so it is nonzero and has squared norm six.
3. Its boundary is the Jacobi sum in the free Lie algebra and vanishes.
4. The cycle belongs to Kapranov's semiabelianized Lie algebra, hence its
   star-exponential is group-like at every truncation and in the completion.
5. The second Peiffer identity makes every star-product with a kernel element
   zero. Therefore `exp_*(a Omega)=1+a Omega` and these exponentials add their
   scalar parameters under multiplication.
6. With all path components equal to the identity, the horizontal and
   vertical surface compositions both reduce to star multiplication. Area
   additivity proves both multiplicativity laws, and `delta(Omega)=0` proves
   the boundary condition.
7. The only nonzero positive level is level three. With
   `sigma=rho/2 <= 1/3`, the `q=3` term in the paper's surface estimate
   dominates `Delta s Delta t` after choosing the Hölder-control constant.
8. The stronger estimate also holds: if `a<=b`, then
   `ab <= a^rho b^(2rho)` because
   `a^(1-rho)b^(1-2rho) <= b^(2-3rho) <= 1`; the other aspect ratio is
   symmetric.

## Computational verifier

Command:

`conda run --no-capture-output -n sandbox python code/verify_counterexample.py`

Result:

- exactly six nonzero degree-three coefficients;
- exact zero boundary;
- exact squared norm `6`;
- 18,876 rational horizontal and 18,876 rational vertical additivity checks;
- all 16,384 sampled mixed-regularity inequalities passed for four exponents;
- final status `PASS`.

The program supports but does not replace the symbolic proof.

## Novelty audit

On 2026-08-17, the four run indexes and the full local arXiv-source corpus
were searched by arXiv id, exact title, `unique lift`, `rectangular Hölder`,
`central kernel`, and close variants. A bounded web search used the exact
paper title and combinations of `rough surface`, `unique lift`, `rectangular
increments`, `central kernel`, `Jacobi`, and the related multiplicative
surface-signature terminology. No later explicit answer or this construction
was located. This is a bounded novelty check, not an exhaustive claim.

## Human-review recommendation

Check chiefly whether the source question intends intrinsic uniqueness among
admissible rough lifts, as Remark 5.23 suggests, or only uniqueness of a lift
operator after implicit smooth-consistency/naturality axioms. The algebraic
and regularity parts of the counterexample are direct.


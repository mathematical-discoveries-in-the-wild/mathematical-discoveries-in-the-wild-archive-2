# Verification report

Status: candidate substantial partial result likely valid; human review
requested.

## Formal audit

- The joint vector sequence is contained in a compact box, so every scalar
  subsequential limit has a vector-convergent subsubsequence. This proves the
  exact identity between scalar cluster sets and linear images of the finite
  joint cluster set.
- Inside `d^perp`, the collision equation for a nonparallel difference is a
  proper line. Avoiding finitely many such lines leaves exactly the affine
  fibers parallel to `d`.
- If an even finite set is centrally symmetric, its center is not a member.
  A functional killing one antipodal radius makes the image centrally
  symmetric and includes its center, hence the image cardinality is odd.
- Four affinely independent points have no second pair difference parallel to
  a selected edge; otherwise there is a nontrivial affine dependence. A
  generic orthogonal functional therefore gives exactly three image values.
- The packet never invokes the unproved universal finite-projection parity
  lemma.

## Literature and scope audit

- The original source's Question 1 and the statement that the `2N` case
  remains unanswered are both visible on page 2 of `source_paper.pdf`.
- arXiv:2511.08760 is currently withdrawn with the comment that an argument
  needs clarification. Its first-version genericity step does not handle
  parallel pair differences, whose collision hyperplanes coincide.
- The packet claims only four structural exclusions for three-dimensional
  candidate subspaces. It does not claim that `L(2N)` is non-lineable or not
  three-lineable.

## Computational audit

Run:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2303.03871_even_cluster_projection_subcases/code/check_small_projection_parity.py
```

The script exhaustively checks every nonempty even subset of the `4 x 4`
integer grid (32,767 cases) and every nonempty even subset of the Boolean cube.
No counterexample is found. This is a finite stress test only and is not used
as a proof.

## Artifact audit

- The official source TeX was compiled locally to a 13-page source PDF.
- Source page 2 was rendered at 180 dpi and used at full readable width.
- The final packet was compiled without LaTeX warnings, rendered page by page,
  and visually inspected.

## Reviewer focus

Verify the reverse inclusion in the exact joint-cluster identity and the
central-symmetry argument. Then check the scope label carefully: the universal
odd-projection lemma remains open in this packet.

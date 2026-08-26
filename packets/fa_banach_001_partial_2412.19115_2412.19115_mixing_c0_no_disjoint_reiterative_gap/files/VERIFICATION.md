# Verification record

## Mathematical dependency audit

- The only external theorem used is Theorem 3.6 of Martin--Menet--Puig
  (arXiv:2106.01409), the simplified characterization of disjoint
  reiterative hypercyclicity for unilateral pseudo-shifts on `c0`.
- For the common inducing map `f(j)=j+1`, its three conditions reduce exactly
  to product growth, the cross-tail quotient, and same-time target-ratio
  approximation written in the packet.
- The mixing characterization `|W[j,n]| -> infinity` for every fixed `j` is
  used only to make the lower product bound uniform over all `d >= M` for
  finitely many `j` and shifts.
- The ratio-interpolation lemma is derived directly from a disjoint
  hypercyclic vector and does not assume a disjoint hypercyclicity criterion.

## Automated sanity check

Command:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2412.19115_mixing_c0_no_disjoint_reiterative_gap/code/verify_block_identities.py
```

Transcript:

```text
verified 405 cocycle/cross-tail identities
block densities: 0.099099, 0.093656, 0.091735, 0.091184
finite sanity checks passed (not a proof)
```

The script checks the product cocycle and cross-tail identities for three
deterministic random complex weight sequences, and checks convergence of
finite block densities to `1/M`.  It is not evidence for the infinite
dimensional dynamical implications.

## Packet build and visual QA

- `latexmk` completed after two passes with no undefined references or LaTeX
  errors.  The sole box warning was an inconsequential 0.686-point overfull
  line in the ratio-interpolation proof.
- The four PDF pages were rendered at 150 dpi and inspected individually.
- The source crop was rendered from page 2 of arXiv:2412.19115v2 at 170 dpi;
  it contains the complete question and surrounding scope statement.

## Human-review focus

1. Confirm that arbitrarily late ratio interpolation follows from the tail
   density of the diagonal disjoint orbit.
2. Check the shifted-coordinate prescription and identity (6) for every
   ordered pair in a finite tuple.
3. Check that `M`-separation rules out all cross-tail cases except `m>n` with
   `m-n >= M`, and that identity (8) has the correct index orientation.
4. Treat the result as a mixing-subclass theorem only; the individual
   reiteratively hypercyclic case is not proved.

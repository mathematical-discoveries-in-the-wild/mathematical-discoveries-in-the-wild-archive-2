# Verification report

Candidate: `1009.2553_all_N_strict_pi_over_2_toeplitz_minimax`

## Claim checked

For the Courtney--Sarason self-adjoint Toeplitz mini-max constants,
`c_N>pi/2` for every integer `N>1`.

## Verdict

Likely valid. Confidence: 97/100.

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Alternating-step extremal reformulation | valid/source | The source's reverse argument and Theorems 4.1 and 5.1 show that a height-one alternating step function of order at most `N` is the minimum-norm inducer of its `N`th compression. |
| Arbitrary-level dilation decomposition | valid | Fourier support on multiples of `k` makes residue classes modulo `k` reducing subspaces. The residue-`r` block is `A_(f,floor((M-r)/k))`. |
| Norm identity | valid | The residue-zero block is `A_(f,floor(M/k))`; every other block is its principal compression. |
| Explicit order-two coefficients | valid | Direct integration gives `a0=-1/5`, the displayed `a1`, and `a2`. |
| Order-two spectral norm | valid | Centrosymmetry gives one antisymmetric eigenvalue and a 2-by-2 symmetric block. Exact rational interval arithmetic proves the norm is below `0.62877<2/pi`. |
| Propagation to `N>=4` | valid | For `k=floor(N/2)`, `floor(N/k)=2` and the dilated step has order `2k<=N`. |
| Case `N=3` | valid/source | The paper's exact polynomial-root construction gives `c_3 >= 3pi/(4sqrt(2))>pi/2`. |
| Literature/novelty status | bounded | Exact-title, author, phrase, `c_N`, and citation searches found no later resolution; this is not an exhaustive bibliography. |

## Computational and exact checks

The verifier uses only standard-library `Fraction` arithmetic. It certifies the
pi bound via Machin's formula, the sine bounds via alternating Taylor series,
the square-root bound by squaring, the final matrix-norm inequality without
floating-point arithmetic, and the residue block levels for every
`4<=N<=1000`. It reports `PASS`. The finite range check is illustrative; the
residue formula itself proves all dimensions.

Command:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/\
  1009.2553_all_N_strict_pi_over_2_toeplitz_minimax/code/\
  verify_dilation_and_seed.py
```

## Gaps and human review recommendation

No proof gap found. Send to human review. Reviewers should focus on the claim
that the dilated alternating step remains a minimum-norm inducer at the larger
level and on the block identification for non-multiple truncations. The packet
does not claim progress on Questions 2--4 beyond the stated comparison lemma.


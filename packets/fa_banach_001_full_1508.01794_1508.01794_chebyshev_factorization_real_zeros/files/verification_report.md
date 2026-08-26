# Verification report

## Claim checked

For the polynomials `p_n` in source formula (8), all zeros are real and
simple, with the residue-class factorization and location stated in the
packet.

## Source verification

- The exact formula and open conjecture were checked in the ingested arXiv
  source and in the independently rebuilt nine-page source PDF.
- The crop retains formula (8), the examples `p_2,p_3`, and the complete
  zero-distribution question on source PDF page 6.
- The question is not answered later in the source paper.

## Adversarial proof check

| Step | Verdict | Check |
| --- | --- | --- |
| Remove the divided difference | valid | `T_n+tU_{n-1}=U_n` and the `U` recurrence give `2(t-a)q_n=U_{n+1}+sqrt(2)U_n+c_n`. |
| Period-eight constant | valid | `a=cos(3pi/4)` gives `c_n=sqrt(2)sin(3pi n/4)`. |
| Five factorization rows | valid | Each row follows from the listed sine/cosine product identities and was also checked exactly through degree 80. |
| Real-rooted consecutive combinations | valid | Strict interlacing gives one root in every component of the complement of the lower-degree zero set, exhausting the degree. |
| Multiplicity after division | valid | The odd rows have disjoint factor zero sets; the even rows share only `a`, and only for `n=2 mod 4`; the single-factor row has a simple root at `a`. |
| Location | valid | Endpoint signs locate one sub-`-1` root in the stated degrees and exclude roots above `1`. |

No counterexample was found.  The proof does not rely on the numerical root
tests.

## Reproducible checks

Command:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/1508.01794_chebyshev_factorization_real_zeros/code/verify_factorizations.py
```

Output:

```text
PASS: 81 exact factorizations and real-root/location checks through degree 200
```

## Novelty bound

On 21 August 2026, the audit searched the run registry, solution, attempt, and
proof-gap indexes; exact title and arXiv-id queries; the exact zero-distribution
question; and later primary papers on Jacobi-type pencils citing the source.
No explicit later resolution or matching factorization was located.  This is
a bounded search, not a proof of novelty.

## Verdict

Likely valid; send to an expert.  Focus review on the congruence-to-common-zero
calculation and the exact zero-location strengthening.

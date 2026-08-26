# Verification record

## Mathematical checks

1. Every local measure used in the packet is a probability measure with a
   strictly positive Lebesgue density.  Hence the weighted `L^1` spaces are
   Banach function spaces and the weighted `L^{p_Q}` spaces, `0<p_Q<1`, are
   quasi-Banach function spaces on the same null sets as Lebesgue measure.
   In all cases `||chi_Q||_{X_Q}=1` exactly.
2. For the Question 6.1 witness, the truncated Laplace first moment is

   ```text
   1 - A/(exp(A)-1) <= 1,   A=ell(Q)/2.
   ```

   The classical mean oscillation of `x_1` is `ell(Q)/4`.
3. For the Question 6.2 family on a large cube, the parameters satisfy

   ```text
   q=1/b,  p=1/(a^2 b),  s=ell(Q)^(-(b-1)),
   D=log(ell(Q)/s)=ab,  pD=1/a.
   ```

4. The nested-cube estimate gives a local `L^p` scale ratio
   `R <= C_n(1+D)` for every classical BMO oscillation.  Since
   `q log R` is bounded and `p log R` is small, the mixture factor
   `[(1-q)+qR^p]^(1/p)` is uniformly bounded.
5. For `f(x)=x_1`, the two component scales `A=ell(Q)/2` and `B=s/2`
   satisfy `A^(1-q) B^q=1/2`.  The exact Bernoulli power-mean estimate gives
   a multiplicative error at most `exp(1/2)`, so the large-cube generalized
   oscillation is at most `exp(1/2)/2`.
6. The same interval-centre choice is an admissible constant in the
   best-constant seminorm.  Thus the witness lies in `BMO_X^*`, establishing
   the stronger failure claimed in the packet.

Run the independent parameter checker with:

```bash
conda run --no-capture-output -n sandbox python code/verify_parameters.py
```

The checker evaluates lengths through `log L = 10^6` without representing
`L` itself, verifies the exact identities above, and checks deliberately
generous versions of both analytic bounds.

## Source evidence

`figures/questions_6_1_6_2_crop.png` is cropped from printed page 27 of
`source_paper.pdf` at 180 dpi.  It contains the full statements of Questions
6.1 and 6.2 and the source's stronger `BMO_X^* -> BMO` variant.

## Literature audit

- Searched the run's current and build indexes for arXiv:2204.11099, the
  exact question text, and the core embedding phrases.
- Searched public exact-title, exact-question, citation, and generalized-BMO
  queries through 2026-08-11.
- Inspected arXiv:2606.01688, the only directly related later preprint found.
  It supplies sufficient median/sparse testing criteria and does not state
  these counterexamples.
- No duplicate or prior resolution was found.  This is a bounded search and
  not an exhaustive novelty guarantee.

## Packet QA

The final PDF is compiled into `tmp/`, copied to the packet root, scanned for
LaTeX warnings, validated with Ghostscript, rendered at 180 dpi, and visually
inspected page by page.

- Final length: 5 pages.
- Final LaTeX warning scan: no warnings, overfull boxes, underfull boxes, or
  undefined references.
- Ghostscript null-device validation: passed.
- All five 180-dpi page renders were visually inspected; no clipping,
  overlap, missing glyphs, malformed equations, or unreadable source text was
  found.
- `solution_packet.pdf` SHA-256:
  `6ecad1cd21314898f34dda9157b4cd83315131e58f373f4b7fbf16ef90a8a0df`.
- `source_paper.pdf` SHA-256:
  `1b86010aae95bf3aad07870b914817883acb3c0d6705260307183b574bd41071`.
- `supporting_2606.01688.pdf` SHA-256:
  `609fd21d100a115ce9ea4d7339fa262e42331ea071d49c38ec6de7d18b0d554e`.
- Exact source crop SHA-256:
  `df69e432e0bb7821d7b38a37c8efdcdb66f31f0547a0c179a1c44bd314c193e0`.

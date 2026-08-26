# Verification record

Command, run from the repository root on 12 August 2026:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/0101227_two_site_nash_dual_formula/code/verify_two_site.py
```

Environment: Python 3.11.14, SymPy 1.14.0, mpmath 1.3.0.

Output:

```text
p=4 derivative factor H(s) = 3*s**4 - 2*s**3 + 1
s_4 bracket = [0.535, 0.536]
t tail-functional bracket = [1.883, 1.884]
A_4^2 exact upper = 270634747904/63114000625 = 4.288030313781111
U_4^2 exact lower = 4545689/1000000 = 4.545689
certified strict gap: A_4 < 2.08 < 2.13 < U_4
p= 2.1 s_p= 0.6129543927471605 A_p= 2.546319287040658
p= 3.0 s_p= 0.5698402909980533 A_p= 2.196812145721939
p= 4.0 s_p= 0.5356873867918731 A_p= 2.070171566942943
p= 6.0 s_p= 0.5083449363842325 A_p= 2.010878607101369
p= 10.0 s_p= 0.5004921388796673 A_p= 2.000392393396041
PASS
```

The `p=4` derivative identities and all four strict rational comparisons are
exact. The five general-`p` lines are sanity checks only; the theorem for all
`p>2` is proved algebraically in the packet.

## Reviewer checklist

- Verify the summation-by-parts identity in Lemma 1.
- Check the Euler flux equation for a sharp finite-chain optimizer.
- Check that `H_p` has minimum `1-((p-2)/p)^p>0`.
- Check that the unique crossing of `J_1,J_2` is the unique maximizer of
  `Q_p`.
- Keep the nonlinear source-tail functional distinct from the Banach
  tail-norm functional used in the strict-gap theorem.
- Confirm that the result is scoped to the Dirichlet Sobolev/Nash partner and
  does not claim the centered ergodic Nash/logarithmic-Sobolev problem.


# Verification code

Run from the repository root:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2005.08089_fixed_point_converse_four_element_semigroup/code/verify_finite_semigroup.py
```

The script checks all 64 associativity triples, all 16 character identities,
the right-zero multiplication on `P(phi)`, and the exact rational linear
system for a normalized right-`phi` invariant functional.  The last system is
inconsistent.  This finite calculation is an independent check; the packet's
formal proof derives the contradiction directly from two test functions.

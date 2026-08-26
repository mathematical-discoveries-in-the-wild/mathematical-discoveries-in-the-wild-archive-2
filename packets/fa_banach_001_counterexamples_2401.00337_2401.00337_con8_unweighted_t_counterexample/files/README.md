# The printed Conjecture 3.7 forces t = 1/2 already for scalars

Status: `candidate_counterexample_likely_valid_full_negative_answer_as_printed_semantic_warning`.

Source: S. Freewan and M. Hayajneh, *Norm inequalities involving geometric
means*, arXiv:2401.00337, Conjecture 3.7 (label `CON8` in the source).

## Result

The displayed conjecture is false as printed.  Its left side uses the
unweighted geometric mean `sharp`, while its right side still depends on
`t`.  For `n=m=1`, the displayed inequality reduces to

```text
(AB)^(sr/2) <= A^((1-t)sr) B^(tsr).
```

Thus scalar validity for arbitrary positive `A,B` forces `t=1/2`.  In
particular, take

```text
A=4, B=1, s=3/2, r=p=1, t=1.
```

Then the left side is `2 sqrt(2)` and the right side is `1`.

This is a full negative answer only to the literal displayed statement.  The
surviving likely intended question is obtained either by fixing `t=1/2` on
the right or by replacing every unweighted `sharp` on the left by `sharp_t`.
The packet does not claim to settle either repaired conjecture.  Broad random
(280,000 matrix configurations and 700,000 Ky Fan tests) and
differential-evolution searches found no violation of the `t=1/2` repair in
the tested small matrix regimes.  Reproducers are included as
`code/search_repaired_conjecture.py` and
`code/optimize_repaired_conjecture.py`.

Run the exact check with:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2401.00337_con8_unweighted_t_counterexample/code/verify_counterexample.py
```

The human-facing packet is `solution_packet.pdf`.

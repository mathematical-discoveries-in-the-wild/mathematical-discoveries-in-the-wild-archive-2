# Verification record

## Mathematical audit

1. Each `Q_k` is the orthogonal projection onto `u_k^perp`, and direct
   substitution gives `Q_k v_{k-1} = c_k v_k`.
2. A normal created in stage `m` is supported on coordinates `m,m+1`.
   From the end of stage `m+1` onward, every path vector is supported on
   coordinates at least `m+2`; hence released recurrences act exactly as the
   identity on the intended orbit.
3. Exact valuation classes `{n: nu_2(n)=r}` have constant gap `2^(r+1)`.
   Together with the one finite activation-to-recurrence gap, this verifies
   quasiperiodicity for every index.
4. The total logarithmic loss is finite because
   `sum_m N_m theta_m^2 < infinity`, so the orbit norms tend to a positive
   constant.
5. The directions are weakly null and pass through successive orthogonal
   basis vectors.  Hence the orbit is weakly null but not norm convergent.

## Computational sanity check

Run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/1809.05858_countable_quasiperiodic_projection_counterexample/code/check_schedule.py
```

The script constructs eight finite rotation stages, applies the scheduled
projections, and checks the exact identity `x_(2k-1)=x_(2k)=a_k v_k` to
floating-point tolerance.

## Literature and render audit

- Source question checked in the local arXiv source at Section 3.4.3.
- arXiv:2405.04848 checked for scope; its pseudo-periodic hypotheses do not
  cover the all-indices-recurrent schedule here.
- Exact arXiv/title/keyword searches found no exact later answer in the
  bounded audit.
- `solution_packet.pdf` compiled without LaTeX warnings and was rendered to
  page images for visual inspection.

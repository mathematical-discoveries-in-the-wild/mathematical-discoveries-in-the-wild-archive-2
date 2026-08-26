# Multiplicative closure of Levitan and Poisson multipliers

This packet gives a full negative answer to the explicit problem on source
PDF page 13 of arXiv:2209.13576. A function in the `c` class automatically
belongs to the `c^2` class; more strongly, the intersection of the `a` and
`b` classes is contained in the `ab` class for both Levitan `(N,·)` almost
periodicity and uniform Poisson stability.

## Files

- `solution_packet.pdf`: review-ready mathematical proof.
- `main.tex`: packet source.
- `source_paper.pdf`: official arXiv source PDF.
- `figures/source_problem.png`: rendered source excerpt containing the problem.
- `VERIFICATION.md`: proof, source, literature, and visual-QA record.

## Result

For either recurrence notion, membership for multiplier `c` implies
membership for `c^m` for every integer `m >= 1`. Therefore the bounded
continuous separator requested by the paper cannot exist. The argument does
not use boundedness or continuity and works in every dimension for
normed-space-valued functions.

## Review focus

Check Definition 2.3 against the simplified compact-uniform formulations in
the packet, and check the shifted compact `K + sigma` in the two-step
composition. The Poisson proof explicitly handles the fact that its
recurrence sequence may depend on the compact set.

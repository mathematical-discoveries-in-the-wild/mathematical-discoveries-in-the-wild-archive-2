# Verification report

Verdict: candidate substantial partial result, likely valid.

Checks completed on 2026-08-17:

- The strip quotient and conformal-map identities were rederived algebraically.
- The imaginary-axis Hardy-membership direction was verified independently by a uniform disk growth estimate.
- The boundary density integrates to one and gives the claimed strict endpoint threshold.
- code/check_quadratic_map.py passes all boundary-map, normalization, and truncated-threshold regression checks.
- main.tex compiles with no LaTeX warnings, undefined references, overfull boxes, or underfull boxes.
- solution_packet.pdf has five pages; every page was rendered at 160 dpi and visually inspected.
- The source crop is full-width and contains all of Remark 5.14 from arXiv:2507.08514v1 needed to identify the quadratic residual case.

Review focus:

1. The claim that cosh(pi xi) and (xi^2+1/4)/c have exactly the same two-point fibers on the strip.
2. The change of variables from right-half-plane harmonic measure to c sech(pi c y) dy.
3. The uniform H^p disk estimate for imaginary frequencies.

SHA-256 of solution_packet.pdf:

ca9e9c051f690099484b9d8742fe12dcf6e7b2f4d34e44647fe8dd27bd846ea9

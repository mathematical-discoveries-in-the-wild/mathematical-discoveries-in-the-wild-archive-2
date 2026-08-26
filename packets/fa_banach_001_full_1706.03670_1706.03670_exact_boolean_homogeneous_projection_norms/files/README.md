# Exact Boolean homogeneous-projection norms

Status: `candidate full solution, likely valid, human review requested`

Source: A. Defant, M. Mastyło, and A. Pérez, *On the Fourier spectrum of functions on Boolean cubes*, Mathematische Annalen 374 (2019), 653–680; arXiv:1706.03670.

## Result

For integers `d >= 1` and `0 <= m <= d`, let `Lambda_{m,d}` be the supremum, over all dimensions and all nonzero real Boolean-cube functions of Fourier degree at most `d`, of

`||f_m||_infty / ||f||_infty`.

The packet proves the exact identity

`Lambda_{m,d} = M_{m,d}`,

where `M_{m,d}` is the classical sharp Markov coefficient constant for the coefficient of `t^m` in a real polynomial of degree at most `d` bounded by one on `[-1,1]`. Thus the smallest base `C` for which

`||f_m||_infty <= C^d ||f||_infty`

holds uniformly is exactly `C = 1 + sqrt(2)`, answering Section 4.3 of the source affirmatively.

The upper bound is the source's radial Markov argument. The new sharpness step uses the bounded symmetric functions

`f_n(epsilon) = T_{d'}((epsilon_1 + ... + epsilon_n)/n)`

and shows that their level-`m` values at the all-one vector converge to the extremal Chebyshev coefficient.

## Review focus

Check the parity-support counting lemma in the lower bound and the identification of algebraic multilinearization with the Fourier-Walsh polynomial. No numerical assertion is used in the proof.

## Files

- `main.tex` and `solution_packet.pdf`: complete proof packet.
- `source_paper.pdf`: local copy of arXiv:1706.03670.
- `figures/open_problem_crop.png`: source p. 24, Section 4.3.
- `code/check_chebyshev_limits.py`: optional numerical sanity check.
- `verification.md`: dependency, novelty, and artifact audit.
- Ledger: `runs/fa_banach_001/ledger/results/1706.03670_exact_boolean_homogeneous_projection_norms.json`.

Novelty confidence is provisional after a bounded exact-phrase and close-variant search; no later statement of the exact formula was found.

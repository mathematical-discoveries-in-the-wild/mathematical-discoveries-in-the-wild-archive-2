# Effective Eigenvalue Moduli on Compact Smoothness Classes

Status: `candidate_partial_result_likely_valid`

Source: Adam Parusiński and Armin Rainer, *Eigenvalue stability of Hermitian
and normal matrices*, arXiv:2603.23056, Problem 1.15 and equation (1.10)
(source PDF p. 9).

## Claimed contribution

The packet makes three effective advances on the source's broad modulus
problem.

1. On every class of Hermitian families with Lipschitz seminorm at most `C`,
   the ordered-eigenvalue map satisfies

   `||E(A)-E(B)||_{C^{0,alpha}}
    <= delta + 2 C^alpha delta^(1-alpha)`.

   The exponent `1-alpha` is optimal even in one fixed bounded
   `C^{1,beta}` ball of diagonal 2-by-2 curves.

2. On uniformly `gamma`-gapped `C^1` families, the map is locally Lipschitz
   into every `W^{1,q}`, with modulus

   `O((1+C/gamma) delta)`.

3. On the compact one-parameter diagonal subclass of the bounded
   `C^{1,beta}` ball, an explicit `W^{1,q}` modulus has power

   `min{beta/(1+beta), 1/q}`,

   with a logarithmic loss at equality. Shifted crossings and a new
   small-amplitude/high-frequency construction show the power is optimal.

The general no-gap, nondiagonal `W^{1,q}` modulus remains open; it needs a
cluster-stable argument because matrix smoothness does not uniformly control
the derivative Hölder norms of eigenvalue branches near avoided crossings.

## Packet contents

- `solution_packet.pdf`: complete proof and review packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/source_problem_crop.png`: rendered Problem 1.15 and class K.
- `code/verify_effective_moduli.py`: sharpness and gapped-estimate verifier.
- `code/verification_output.txt`: saved PASS output.
- `VERIFIER_REPORT.md`: adversarial review.
- `main.tex`: packet source; build files and rendered pages are under `tmp/`.

## Reproduce the verification

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2603.23056_effective_eigenvalue_moduli/code/verify_effective_moduli.py \
  --suite
```

## Human-review focus

Check the scalar thin-sublevel lemma, the diagonal sorting-network reduction,
and the stated boundary between diagonal/gapped results and the unresolved
general no-gap cluster problem. Novelty remains plausible rather than
certified.

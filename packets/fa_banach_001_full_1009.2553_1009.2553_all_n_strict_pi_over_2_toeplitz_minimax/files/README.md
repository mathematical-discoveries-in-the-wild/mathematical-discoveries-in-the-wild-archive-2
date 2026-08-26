# Strict Courtney--Sarason lower bound in every dimension

This packet gives a full affirmative answer to Question 1 of arXiv
`1009.2553`: the self-adjoint Toeplitz mini-max constants satisfy

```text
c_N > pi/2  for every integer N>1.
```

The new ingredient is a non-multiple version of the paper's dilation
proposition. If `g(z)=f(z^k)`, then at an arbitrary truncation level `M`, the
Toeplitz compression for `g` splits into residue-class blocks and

```text
||A_(g,M)|| = ||A_(f,floor(M/k))||.
```

An explicit order-two alternating step function has compression norm strictly
below `2/pi`. Taking `k=floor(N/2)` copies that witness into every `N>=4`;
the paper's exact order-three witness handles `N=3`.

Status: candidate full solution of Question 1, likely valid subject to human
review.

Scope: Questions 2--4 (strict monotonicity, the supremum, and uniqueness/order
of maximizers) remain open. The new dilation lemma gives additional
non-adjacent comparisons but not adjacent monotonicity.

Main artifact: `solution_packet.pdf`.


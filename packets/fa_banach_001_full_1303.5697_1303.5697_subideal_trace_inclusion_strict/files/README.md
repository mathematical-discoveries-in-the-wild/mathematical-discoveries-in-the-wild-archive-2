# The two notions of subideal-trace are different

Status: `full_solution_likely_valid`

Source: Sasmita Patnaik and Gary Weiss, *A survey on subideals of
operators and an introduction to subideal-traces*, arXiv:1303.5697,
Definition 5.11 and the question on PDF page 9.

## Claimed contribution

The inclusion asked about in the source is proper. Let `H0=l2(N)`,
`H=H0 direct_sum H0`, and

```text
D = diag(1,1/2,1/3,...),
S = D direct_sum (-D),
J = K(H),
I = (S)_J.
```

The principal `K(H)`-ideal `I` is not a `B(H)`-ideal. Its standard coefficient
functional

```text
tau(alpha S + X) = alpha,
X in J S + S J + J(S)J,
```

is invariant under every unitary in `1+J`, hence is a subideal-trace in the
sense of Definition 5.3. But the block-swap unitary `W(x,y)=(y,x)` normalizes
`I` and satisfies `W S W* = -S`. Therefore

```text
tau(W S W*) = -1 != 1 = tau(S).
```

Thus `tau` is not invariant under the larger normalizer class from Definition
5.11, and the displayed inclusion on source PDF page 9 is strict.

## Proof intuition

The coefficient trace remembers the scalar multiplying the chosen generator
and ignores the `J`-multiplicative remainder. Small unitaries of the form
`1+J` can only perturb the generator by such remainder terms, so they cannot
change the coefficient. To defeat invariance under the full normalizer, choose
a generator with symmetric signed spectrum. Swapping its positive and negative
halves preserves the generated ideal but reverses the remembered coefficient.

## Verification

The proof separately verifies:

- the singular values of `S` are `(1,1,1/2,1/2,...)`, so the Fong-Radjavi
  criterion excludes `I` from being a `B(H)`-ideal;
- the source's principal-subideal decomposition makes `tau` well-defined;
- conjugation by `1+A`, `A in J`, preserves the coefficient;
- the block swap normalizes `I`, is not a compact perturbation of the identity,
  and changes `tau(S)` from `1` to `-1`.

No numerical or computer-assisted step is used.

## Novelty and scope

The bounded novelty check on 2026-08-09 searched all four run indexes, the
exact arXiv id and title, the phrases `subideal-trace`, `U^I subideal trace`,
`proper inclusion`, and the exact wording of the source question. It searched
the web/arXiv and the locally parsed arXiv corpus. The only later local citation
found, arXiv:2301.09425, uses the subideal terminology but does not discuss this
trace question. No later explicit answer or equivalent signed-generator
construction was found.

The result proves existence of a non-`B(H)` subideal for which the two classes
differ. It does not classify all subideals for which they agree, nor does it
describe the full space of either kind of trace.

Human review recommendation: send to an operator-ideals specialist. The key
audit points are the use of the Fong-Radjavi criterion and uniqueness of the
coefficient in the principal `J`-ideal decomposition.

Files:

- `source_paper.pdf`: arXiv:1303.5697.
- `figures/open_problem_crop.png`: Definition 5.11 and the exact question on
  source PDF page 9.
- `main.tex`, `solution_packet.pdf`: complete proof packet.
- `VERIFICATION.md`: explicit verifier report.


# Boundary-regular symbols are rotations

Status: `candidate_partial_likely_valid`.

Source: R. F. Allen, K. C. Heller, and M. A. Pons, *Isometric composition
operators on the analytic Besov spaces*, arXiv:2207.12634.

## Result

Let `p>2` and let `phi:D->D` be holomorphic on a neighborhood of the closed
unit disk. If `C_phi` is an isometry on the analytic Besov space `B_p` with
the source norm, then

```text
phi(z)=lambda z,  |lambda|=1.
```

The same proof covers every rational disk self-map with no pole on the closed
disk. The unrestricted source conjecture remains open in this packet.

The proof first uses fullness to show that a boundary-regular symbol maps the
unit circle onto itself and hence is a finite Blaschke product. The exact
fiber identity for an isometric symbol is

```text
sum_{phi(z)=w}
  ( |phi'(z)|(1-|z|^2)/(1-|w|^2) )^(p-2) = 1.
```

As a regular value tends to the unit circle, every inverse branch of a finite
Blaschke product contributes one. Thus the degree is one, and the condition
`phi(0)=0` makes the automorphism a rotation.

## Scope and related audit

A later Shabazz--Tjani classification claims the full result, but the
available primary dissertation proof replaces a full fiber sum by one local
branch. A separate packet records that issue without claiming the theorem is
false:

`proof_gaps/2207.12634_shabazz_tjani_fiber_truncation_gap/`.

## Files

- `solution_packet.pdf`: review-ready proof packet.
- `main.tex`: packet source.
- `source_paper.pdf`: arXiv:2207.12634.
- `figures/open_problem_crop.png`: source conjecture on page 6.
- `verification.md`: proof and rendering checks.
- `novelty.md`: bounded literature/duplicate audit.
- `code/make_crops.py`: reproducible evidence-crop script.

Human review should focus on the fullness-to-inner boundary lemma and the
boundary limit of the finite-Blaschke fiber identity.


# A strictly positive-field counterexample to the proposed equality

Status: **candidate counterexample; likely valid; human review recommended**

## Source and target

- Søren Fournais, Rupert L. Frank, Magnus Goffeng, Ayman Kachmar, and Mikael
  Sundqvist, *Counting Negative Eigenvalues for the Magnetic Pauli Operator*,
  arXiv:2307.16079v1 (2023), later Duke Math. J. 174 (2025), 313--353.
- Target: Proposition 5.2 and Remark 5.3 on arXiv-v1 PDF page 18.  The latest
  TeX source renumbers these as Proposition 6.3 and Remark 6.4.
- Question: whether the inequalities comparing the holomorphic and
  antiholomorphic compressions with boundary-Dirac intersection dimensions
  become equalities when `B >= 0`.

The packet gives a full negative answer: the first inequality is strict on the
unit disc with Neumann data and a smooth polynomial field satisfying the
stronger hypothesis `B > 0` everywhere.

## Result

On the unit disc, put `g=0`,

    a = 399/200,  b = 6/25,
    phi(r,theta) = (a/2)(r^2-1) - b(r^3-r^5)cos(3theta),
    A = (-phi_y,phi_x).

Then

    A_tau = a+2b cos(3theta),
    B = curl A = Delta phi = 2a+16b r^3 cos(3theta) >= 3/20.

Nevertheless,

    N(H^O_{A,0},0) >= 3
      > 2
      = dim(E_{-A_tau} intersect gamma_0(B(D))).

Thus the first inequality in Proposition 5.2 can remain strict even for a
strictly positive magnetic field.

The proof also gives a family: the same conclusion holds whenever

    1<a<2,  b != 0,  a>=8|b|,  and  (2-a)(5-a)<b^2.

Strict positivity holds if `a>8|b|`.

## Proof mechanism

The boundary symbol has only Fourier modes `0,+3,-3`.  Consequently the
holomorphic compression splits by Fourier index modulo three.  The modes `1`
and `z` give two negative directions, and the block on `span{z^2,z^5}` has
negative determinant, giving a third.

The comparison space is computed exactly rather than estimated.  The
boundary-Dirac eigenfunctions are `z^m E(z)` for `m<=1`, where

    E(z)=exp((b/3)(z^3-z^(-3))).

Factoring `E=E_+E_-` turns the holomorphic-intersection condition into the
preimage of `span{1,z}` under an invertible coanalytic Toeplitz operator.
Hence that space has dimension exactly two.

## Verification

Run the exact symbolic checker from the repository root:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2307.16079_nonnegative_field_strict_bergman_compression/code/exact_symbolic_check.py
```

It verifies the polynomial Laplacian, the boundary tangential potential, the
global lower bound `B>=3/20`, and the exact determinant
`-1703/40000`.  These checks use exact symbolic/rational arithmetic.  The
infinite-dimensional Hardy/Toeplitz step is proved in `main.tex` and is not
delegated to computation.

See `verification.md` for the full proof audit and SHA-256 provenance.

## Novelty check and limitations

The run registry, solution index, attempt tree, and cheap paper indexes were
searched for the arXiv id, title, exact remark wording, and the core magnetic
Pauli/Bergman keywords.  Fresh web/arXiv searches on 2026-08-13 used the exact
title, exact question phrase, arXiv id, remark number, all five authors, and
combinations of `nonnegative magnetic field`, `Bergman compression`, and
`equality`.  They found the source preprint, its 2025 journal publication, and
unrelated papers, but no later claimed answer or matching example.  The
latest available TeX source still contains the question.  This is a bounded
search, so novelty confidence is moderate rather than definitive.

Only the first equality is refuted.  That is enough to answer the source's
general equality question negatively; the packet makes no claim about a
separate characterization of equality in the antiholomorphic inequality.

## Human-review recommendation

Prioritize three points:

1. the source orientation identity `A_tau=partial_r phi` for
   `A=(-phi_y,phi_x)` on the disc;
2. the `m<=1` cutoff in the negative boundary-Dirac subspace;
3. the equivalence between holomorphic intersection and the invertible
   Toeplitz preimage used to prove the dimension is exactly two.

All three are expanded in the proof and independently cross-checked against
the source conventions.

## Packet contents

- `main.tex`, `solution_packet.pdf`: full counterexample and proof.
- `source_paper.pdf`: local arXiv-v1 source PDF.
- `figures/open_problem_crop.png`: real full-width crop of Remark 5.3.
- `code/exact_symbolic_check.py`: exact reusable checker.
- `verification.md`: verifier report, novelty bounds, and artifact hashes.
- `tmp/`: LaTeX intermediates and rendered review pages.


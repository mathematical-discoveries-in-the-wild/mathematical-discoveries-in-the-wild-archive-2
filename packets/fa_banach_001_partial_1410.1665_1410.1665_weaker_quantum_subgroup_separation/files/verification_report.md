# Verification report

Status: `likely valid partial result`

## Source and target

- Open question verified in arXiv:1410.1665, Remark 6.8, PDF page 19.
- The source proof of Theorem 6.5 was checked through the point where it gives
  `y P=P=P y`; the packet does not reuse the later structural condition (6.2).
- The open-question crop contains the complete remark and its comparison of
  the two premises.

## Proof obligations checked

1. `P=(theta tensor id)(W_G)` follows from the subgroup bicharacter identity
   and the Haar slice giving the trivial dual block.
2. Injectivity of the universal Fourier transform turns `yP=P=Py` into the
   two convolution absorption identities.
3. In the coamenable case,
   `z=(mu tensor id)delta(a^*a)` is positive and has zero faithful Haar value;
   the counit slice of `z` is exactly `mu(a^*a)`.
4. In the compact case, coinvariants map to scalars under `Phi`, so absorption
   gives `mu|_R=epsilon`.
5. Because `Pol(H)` is cosemisimple and `Pol(G)->Pol(H)` is surjective, the
   relevant comodule is faithfully coflat. Takeuchi correspondence yields
   `ker pi=R^+ Pol(G)` with the orientation used in the proof.
6. GNS Cauchy--Schwarz kills every term `r x` with `r in R^+`.
7. Peter--Weyl spectral projections preserve the invariant C*-ideal
   `ker Phi`, so its polynomial part is norm dense.

## Counterexample audit

The explicit Kac--Paljutkin/Sekine finite quantum groups were checked as the
most plausible counterexample family. Their non-Haar idempotent states do not
absorb any proper subgroup Haar state in the required way. The compact theorem
subsumes this calculation and rules out all finite quantum group pairs.

## Literature bounds

Exact-phrase/title/author searches and searches for quantum subgroup
separation, Haar idempotents, and finite quantum groups found no answer to
Remark 6.8. arXiv:2309.10046 cites the source but addresses a different family
of separation properties.

## Artifact QA

- LaTeX compiled with `latexmk -pdf -interaction=nonstopmode -halt-on-error`.
- Build log checked for undefined references, overfull boxes, and fatal errors.
- Every packet page and the source crop were visually inspected.

Primary human-review focus: Takeuchi identity orientation and density of the
polynomial kernel in the universal compact C*-kernel.

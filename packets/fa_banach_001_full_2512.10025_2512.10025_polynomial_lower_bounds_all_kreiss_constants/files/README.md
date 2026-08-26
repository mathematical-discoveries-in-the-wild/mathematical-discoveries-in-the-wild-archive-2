# Polynomial lower bounds for every fixed Kreiss constant

**Status:** candidate full solution, likely valid; novelty unconfirmed.

**Source:** Nikolaos Chalmoukis, Georgios Tsikalas, and Dmitry Yakubovich,
“Operators with small Kreiss constants,” arXiv:2512.10025v2 (2026).
Question 6.1 appears on PDF page 18.

## Result

Let `P(N,K)` be the largest power growth forced among `N x N` Hilbert-space
matrices with Kreiss constant at most `K`, as in the source.  For
`0<a<1/2`, put

```text
gamma(a) = a sqrt(6/((1-2a)(1-a))),
beta(a)  = a log(2)/(4(1+a log(2))).
```

The packet proves

```text
P(N,1+gamma(a)) >= C_a N^beta(a)    (N >= 1).
```

Thus every fixed `K>1` admits a positive polynomial exponent.  Combining
this with Nikolski’s bound for `K>pi+1` gives a strictly increasing exponent
function tending to zero at `1+` and to one at infinity, exactly as requested
in Question 6.1.

## Proof mechanism

Let `J=[[0,1],[0,0]]`.  On `ell_2(N; (C^2)^(tensor m))`, use the matrix
weights

```text
B_(m,k) = (I + (a/m) log(k/(k-1)) J)^(tensor m).
```

Products telescope inside each tensor factor.  The `n`-step block beginning
at coordinate `j` is

```text
(I + (a/m) log((j+n)/j) J)^(tensor m).
```

Its deviation from the identity is at most `((j+n)/j)^a-1`.  A scalar
averaging lemma then bounds the Cesaro average of the deviation from the
unweighted shift by `gamma(a)`, uniformly in `m`.  Abel summation converts
this into Kreiss constant at most `1+gamma(a)`.

Compressing to `L` coordinates gives dimension `2^m L`.  With
`m=floor(a log L)`, the `(L-1)`st power is at least `2^(m/2)`, which becomes
the asserted polynomial lower bound after padding to arbitrary dimensions.

## Packet contents

- `main.tex`: complete proof and review notes.
- `solution_packet.pdf`: compiled expert-facing packet.
- `source_paper.pdf`: current arXiv v2 source PDF.
- `figures/open_problem_crop.png`: real crop of Question 6.1.
- `code/verify_tensor_shift.py`: finite numerical sanity checks.
- `VERIFICATION.md`: verification scope and results.

## Novelty check

The four lightweight run indexes were searched for arXiv:2512.10025,
`small Kreiss constants`, `P(N,K)`, polynomial lower bounds, tensor products,
and weighted shifts.  No matching result was found.  Bounded web/arXiv
searches used the exact source title and combinations of `Kreiss constant`,
`tensor power`, `weighted shift`, and `polynomial lower bound`; they found the
source paper and background computation papers, but no later answer to
Question 6.1.  The current source is v2 dated 2026-03-11 and still labels the
problem Question 6.1.  This search is not exhaustive, so novelty is
unconfirmed.

## Human review recommendation

Review the scalar averaging lemma, its Abel-summation conversion to the
resolvent bound, and the final exact-dimension padding.  These are the three
load-bearing steps; the tensor-product identities themselves are elementary.


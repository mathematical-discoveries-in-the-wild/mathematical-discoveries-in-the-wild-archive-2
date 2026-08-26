# Multidimensional continuous factorization at the stable-rank scale

Status: `candidate_full_solution_likely_valid`.

Source: Yuying Dai, Ankush Hore, Siqi Jiao, Tianxu Lan, and Pavlos Motakis,
*Continuous factorization of the identity matrix*, arXiv:1909.00807v2,
Question 2 on printed page 13.

## Answer

Let `A:R^d -> M_N(R)` be continuous, `||A(x)|| <= 1`, and suppose every
column has norm at least `theta>0`.  Put

`q = ceil(3 N theta^2/(4-theta^2))`.

Then, for every

`1 <= n <= max(1,q-d)`, 

there are continuous matrices `R:R^d -> M_{N x n}(R)` and
`L:R^d -> M_{n x N}(R)` such that

`L(x)A(x)R(x)=I_n` and `||L(x)|| ||R(x)|| <= 2/theta`

for every `x`.  In particular the conjectured multidimensional version is
affirmative, with dimension of order `theta^2 N-d`.  The source's original
diagonal hypothesis `|a_ii(x)|>=delta` implies the column hypothesis with
`theta=delta`.

## Mechanism

For `B=A^*A`, one has `0<=B<=I` and `tr(B)>=N theta^2`.  Hence at least `q`
eigenvalues of `B(x)` are strictly larger than `theta^2/4` at every point.
The high spectral subspaces (eigenvalues strictly above `theta^2/4`) form a
lower-semicontinuous field of subspaces of dimension at least `q`.  Michael's
finite-dimensional selection theorem selects a continuous unit section from
such a field whenever its dimension is at least `d+1`.  Repeating this in the
orthogonal complement of the sections already chosen supplies `q-d`
continuous orthonormal sections.  Their frame `Q` satisfies

`Q^*B(x)Q > (theta^2/4) I_n`.

Set `R=Q` and use the canonical continuous left inverse

`L=(R^*A^*AR)^{-1}R^*A^*`.

The compression bound makes the least singular value of `AR` larger than
`theta/2`, giving the required norm estimate.

## Literature boundary

The source's Question 1 (the optimal `theta^2 N` scale for a one-dimensional
parameter) is already answered by Fan--Montemurro--Motakis--Praveen--Rusonik--
Skoufranis--Tobin, arXiv:2201.04238 / *Operators and Matrices* 16 (2022),
Theorem 3.10.  Their final section explicitly leaves multidimensional domains
for future research.  Its sole indexed later citation, Müller--Tomilov,
arXiv:2512.15467 / JLMS (2026), treats time-dependent operator functions on an
interval and only suggests arbitrary compact metric domains as future work.
A bounded arXiv phrase audit found no other continuous restricted-invertibility
paper or multidimensional answer through 2026-08-11.

## Files

- `main.tex`: theorem, selection lemma, proof, and novelty boundary.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: arXiv:1909.00807v2.
- `supporting_fan_et_al_2201.04238.pdf`: the 2022 one-dimensional solution.
- `supporting_muller_tomilov_2512.15467.pdf`: the sole indexed 2026 citation.
- `figures/`: source question and comparison-page renders.
- `verification.md`: mathematical and visual audit record.

Human review recommendation: scrutinize the lower semicontinuity of the high
spectral field and the inductive use of Michael's finite-dimensional selection
theorem on the noncompact base.  The spectral count and pseudoinverse step are
elementary.

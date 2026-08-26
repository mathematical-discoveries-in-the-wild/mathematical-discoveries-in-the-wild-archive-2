# Verification Report

Candidate: arXiv:1711.10932, Question 6 on almost overcomplete sequences as hypercyclic subsets.

## Claim checked

There exist a separable complex Hilbert space `H`, an overcomplete sequence `C` in `H`, and a bounded operator `T` such that `Orb(C,T)` is dense but `T` is not hypercyclic. Thus the source question has a negative answer, even with “almost overcomplete” strengthened to “overcomplete.”

## Verdict

`candidate_full_solution_human_review_needed`

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Exact source target | valid | Source PDF page 33, Question 6: “Are almost overcomplete sequences hypercyclic subsets?” The authors expect a negative answer. |
| Hypercyclic building block | valid | For `S=2B`, finitely supported `u,v` satisfy `u+2^{-m}F^m v -> u` and `S^m(u+2^{-m}F^m v)=v` for large `m`. Hence `S` is mixing and has a dense `G_delta` set of hypercyclic vectors. |
| Choice `x_0 != 0` | valid | The hypercyclic vectors of a topologically transitive operator form a dense `G_delta`; this set intersects the open dense set of vectors with nonzero zeroth coordinate. |
| Non-hypercyclic direct sum | valid | For `T=4I direct-sum S`, the first coordinate of an orbit is `{4^m a}`. If `a=0` it is zero; otherwise it stays at least `|a|` from zero. It is never dense in `C`. |
| Analytic curve | valid | `h(t)=sum 2^{-k}t^k e_k` is `ell^2`-valued analytic on `|t|<2`; on the closed unit disk its norm is at most `2/sqrt(3)`. |
| Tail-dense targets | valid | Repeating a countable dense subset with nonzero first coordinates produces a sequence every tail of which is dense. Nonzero first coordinates ensure all selected `t_n` are nonzero. |
| Inductive hitting-time choice | valid | A hypercyclic orbit remains dense after deleting finitely many terms, so each prescribed vector ball is hit at arbitrarily large times. Large time enforces both scalar smallness bounds. Pairwise distinctness excludes at most one time for each earlier parameter. |
| Dense `C`-orbit | valid | At the chosen time, the first coordinate is exactly `alpha_n`. The vector error is `<1/n + |alpha_n|2^{-m_n}M < 2/n`. A vanishing perturbation of a tail-dense sequence is dense. |
| Every subsequence is total | valid | Any infinite subsequence of distinct `t_n -> 0` gives an accumulating zero set for `L(f(t))`. The identity theorem forces all Taylor coefficients to be annihilated. These coefficients span the full direct sum because `x_0 != 0`. Hahn–Banach gives dense closed span. |
| Linear independence | valid | In a finite relation, the scalar and `e_0` coordinates first give the moment equations of orders one and zero (using `x_0 != 0`); the remaining `e_k` coordinates give all higher moments. The resulting Vandermonde system forces every coefficient to vanish. |
| Exact logical conclusion | valid | `C` is overcomplete, hence almost overcomplete. `T` is `C`-hypercyclic but not hypercyclic, so `C` is not a hypercyclic subset. One example gives the full negative answer to the universal question. |

## Adversarial stress tests

- The proof does not confuse “the Taylor coefficients span” with “the curve values span.” The bridge is the scalar analytic identity theorem applied separately to every continuous annihilating functional.
- The all-subsequences quantifier is explicit: every infinite subsequence still consists of distinct parameters converging to the interior point zero.
- The zeroth-coordinate hypothesis on `x` is essential. Without it, the constant coefficient `(0,x)` together with the higher Taylor coefficients might fail to separate `(0,e_0)` from `(1,0)`.
- Tail density is used, not merely density of one once-enumerated target sequence; this guarantees that errors tending to zero preserve density.
- The growth rates are ordered correctly: the desired scalar is produced by `4^{m_n}t_n=alpha_n`, while the perturbation in the shift summand is bounded by `2^{m_n}|t_n|=|alpha_n|2^{-m_n}`.
- The sequence is bounded and converges to `(0,x)`, so it is compatible with the known relative-compactness theorem for bounded almost overcomplete sequences.
- No claim is made that every almost overcomplete sequence fails to be a hypercyclic subset, or that the packet characterizes the positive examples.

## Novelty check

On 2026-08-11, the exact arXiv id and exact question, plus the phrases `almost overcomplete hypercyclic subset`, `overcomplete hypercyclic subset`, and close arXiv variants, were checked against the run registry, solution, attempt, and proof-gap indexes and by bounded web/arXiv search. Results included the source paper and background work on almost overcomplete sequences, but no later paper claiming to answer Question 6. This is a bounded check, not a guarantee of novelty.

## Artifact verification

- `source_paper.pdf` is the official 35-page arXiv PDF.
- `figures/open_problem_crop.png` is rendered from source PDF page 33 and shows the complete question and the authors’ negative-answer expectation.
- The packet is self-contained apart from standard Birkhoff transitivity/Hahn–Banach/identity-theorem facts; it also gives the elementary mixing calculation for `2B`.
- No numerical or computer-assisted claim enters the proof.

Confidence: 97/100.

Recommended action: high-priority review by a linear-dynamics specialist. If confirmed, this appears to be a concise full negative solution of Question 6.

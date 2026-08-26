# Candidate Partial Result: The Markov Group Conjecture for Triangular Processes

Status: `partial_result_likely_valid`

Model: GPT5.6

Source: Jochen Glueck, *On the decoupled Markov group conjecture*,
arXiv:2004.05995 (2020), Conjecture 1.1 on PDF page 1.

## Claimed contribution

Let `(T_t)` be a Markovian `C_0`-semigroup on `l1(N)`, write
`p_ij(t)=(T_t e_j)_i`, and assume it is triangular:
`p_ij(t)=0` whenever `i<j`. If `T_1` is bijective and
`M=||T_1^{-1}||`, then

`||T_t-I|| <= 2(1-M^{-t})` for every `t>=0`,

and the generator `A` is bounded with

`||A|| <= 2 log M`.

This proves the Markov group conjecture for every one-way/acyclic countable
Markov process that is triangular after a fixed relabeling. These processes
need not split into finite invariant blocks, so this is structurally different
from the decoupled theorem proved in the source.

The full Markov group conjecture remains open in this packet.

## Proof mechanism

Triangularity makes the diagonal transition probabilities multiplicative in
time, hence `p_jj(t)=exp(-q_j t)`. On the dual, each initial coordinate space
`span{e_1^*,...,e_j^*}` is invariant under `T_1^*`; its finite triangular
restriction shows that `p_jj(1)` is an eigenvalue. Boundedness of the inverse
therefore forces `p_jj(1)>=1/M`, uniformly in `j`, so `q_j<=log M`.

For a stochastic matrix on `l1`, the norm of `T_t-I` is the supremum of its
column norms, and column `j` has distance exactly `2(1-p_jj(t))` from `e_j`.
This gives the quantitative norm-continuity bound and hence a bounded
generator.

## Verification

- The proof never assumes that the basis vectors belong to the generator
  domain; operator-norm continuity is established directly.
- The spectral step uses actual eigenvectors of finite-dimensional invariant
  subspaces of `T_1^*`, not a possibly false infinite-triangular spectral
  assertion.
- The bound also handles `M=1`, when it forces every diagonal probability to
  be one and the semigroup to be the identity.
- No computational evidence and no unproved lemma are used.

Verifier verdict: likely valid. The three short checks listed in the attempt
note are written out explicitly in `main.tex`.

## Novelty and search bounds

On 2026-08-11, the run's lightweight indexes were searched for the exact
arXiv id, the conjecture, and triangular/acyclic/pure-birth variants. The local
parsed arXiv corpus contained no later citation or duplicate result. Bounded
official-arXiv searches used the exact conjecture and combinations of
`triangular`, `acyclic`, `pure birth`, `bijective`, and `bounded generator`;
only the source paper was relevant. No exact prior statement of this estimate
was found. Novelty confidence is modest because triangular and pure-birth
classes may have been treated in older non-arXiv Markov-chain literature.

## Files

- `main.tex`: complete candidate partial-result packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: real crop of Conjecture 1.1 from source PDF
  page 1.
- `../../../attempts/2004.05995_markov_group_conjecture_attack.md`: failed full
  routes and the successful triangular route.

Human review recommendation: verify the dual finite-subspace eigenvalue step
and the column-norm identity. If accepted, retain this as a quantitative
partial result for acyclic processes, not as a solution of the full Markov
group conjecture.


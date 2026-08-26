# Entrywise counterexamples and an exact signless-Laplacian resolvent formula

Status: `counterexample likely valid` and `full formula likely valid`.

For arXiv:1203.6812, Conjecture 8.1 is false under its literal entrywise
hypothesis.  In fact, for every `n>=3` and `alpha,m>0`, matrices

`J_epsilon=(alpha+m-epsilon)I+epsilon 11^T`

give strict counterexamples when `epsilon>0` is sufficiently small.

The packet also fully answers Problem 8.2.  It writes every entry of
`(alpha I+ell 11^T+tP)^(-1)` as a quotient of two finite incidence-minor
sums.  Restricting those sums by the number of selected graph edges gives
every coefficient of the numerator and denominator polynomials in `t`.

Conjecture 8.3 from the same source was already proved by Minghua Lin
(arXiv:1212.1934).  The stronger, motivating repair of Conjecture 8.1 with
a separate upper bound on diagonal dominance remains open.

Packet: `solution_packet.pdf`  
Source: `source_paper.pdf`  
Verification: `verification.md`  
Code: `code/verify_resolvent_formula.py`  
Ledger: `runs/fa_banach_001/ledger/results/1203.6812_inverse_lower_bound_counterexample_and_resolvent_formula.json`

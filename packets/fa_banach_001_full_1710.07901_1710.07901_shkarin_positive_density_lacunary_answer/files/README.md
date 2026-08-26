# Lacunary return sets answer Shkarin's question

Status: `candidate_full_likely_valid_positive_answer`.

Question 3.3 of arXiv:1710.07901 asks whether a frequently hypercyclic
vector can have a return set containing no subset of positive natural
density. The answer is yes.

The key observation is latent in the source proof. Its detecting return set
is contained in dyadic blocks whose indices lie in
`J = 5N union (5N+2)`. It is therefore empty across the consecutive blocks
with indices `5q+3` and `5q+4`. For any subset `A` of the return set, the
count of `A` is unchanged between

```text
N_q = 2^(5q+3)-1  and  M_q = 2^(5q+5)-1,
```

while `M_q/N_q -> 4`. If `A` had density `delta`, this would force
`delta = delta/4`, hence `delta = 0`.

The source construction applies explicitly to `T=2B` on `ell^2(N_0)`, using
the bilateral orbit `x_{-m}=2^{-m}e_m`, `x_n=0` for `n>=1`, and the zeroth
coordinate functional. This supplies the requested operator and vector.

Run the nonessential exact sanity checker with:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/1710.07901_shkarin_positive_density_lacunary_answer/code/check_lacunary_gap.py
```

The review packet is `solution_packet.pdf`. The proof is analytic; the code
only checks finite instances and exact endpoint ratios.

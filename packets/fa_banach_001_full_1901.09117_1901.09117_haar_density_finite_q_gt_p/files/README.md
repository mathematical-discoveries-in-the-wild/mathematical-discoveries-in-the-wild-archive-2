# Haar-span density at the limiting Besov edge

Status: `candidate full solution, likely valid`.

## Result

For

`d/(d+1) <= p < 1`,

the algebraic span of the inhomogeneous Haar system is dense in
`B^1_{p,q}(R^d)` **if and only if**

`p < q < infinity`.

The source paper proves non-density for `q <= p`, observes non-density for
`q = infinity` by nonseparability, and asks what happens for `q > p`.  The
packet supplies the missing positive result for every finite `q > p`.

## Proof mechanism

For a smooth compactly supported `f`, partition a fixed dyadic cube into
`M` equal dyadic slabs.  On slab `i`, approximate `f` by the dyadic
conditional expectation at a different fine level `N_i`.  The resulting
function is one finite Haar combination.

At its natural scale, the defect on a slab occupying a fraction `1/M` of
space costs `(1/M)^(1/p)` in `L^p`.  Distributing the `M` defects over `M`
different scales therefore costs

`M^(1/q - 1/p)`,

which tends to zero exactly when `q > p`.  A local-means lemma controls the
extra jumps at the slab boundaries by `2^(-N_0)`.

## Files

- `solution_packet.pdf`: self-contained proof packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: official arXiv PDF for arXiv:1901.09117.
- `figures/open_problem_crop.png`: screenshot of the exact source question.
- `verify_exponents.py`: finite numerical check of the convolution/exponent
  calculation used in the proof.
- `VERIFICATION.md`: proof, literature, and artifact audit.

The multi-route investigation is recorded at
`runs/fa_banach_001/attempts/1901.09117_haar_density_endpoint_attempts.md`.

## Review recommendation

Recommended for expert review as a full solution.  The key item to audit is
the uniform local-means estimate for a defect restricted to a thin slab;
the packet proves it by separating neighborhoods of the level-`N` grid and
the slab boundary.

# A permutation-group counterexample to interpolation of cocompactness

**Status:** candidate full counterexample, likely valid, requiring human
review.

**Source:** Michael Cwikel and Kyril Tintarev, *On interpolation of
cocompact imbeddings*, arXiv:1008.4371v3; Revista Matemática Complutense 26
(2013), 33–55. The question is Remark 1.7 on PDF page 3.

The source asks whether the additional hypotheses in its interpolation
theorem can be removed—equivalently, whether cocompactness persists under
interpolation for every group `D`.

The answer is **no**. Let `D` be the full group of coordinate permutations on
`N`, and let both Banach couples be `(ell_infinity,ell_1)`. The endpoint
identity on `ell_1` is `D`-cocompact by the Schur property. For any
`theta in (0,1)`, however, complex interpolation gives `ell_p`, where
`p=1/theta`, and the real method with second parameter `p` gives the same
space. The norm-one vectors

    u_k = k^(-1/p)(e_1 + ... + e_k)

are weakly null after every sequence of coordinate permutations. Hence they
are `D`-weakly null in `ell_p`, but they do not converge in norm. The
interpolated identity is therefore not `D`-cocompact.

Files:

- `solution_packet.pdf` — exact theorem, intuition, and proof
- `source_paper.pdf` — arXiv:1008.4371v3
- `figures/open_problem_crop.png` — source Remark 1.7 on PDF page 3
- `verification.md` — hypothesis, proof, artifact, and novelty checks

**Human-review focus:** verify the quantifiers in the `D`-weak convergence
estimate, the standard interpolation identities in the reversed order
`(ell_infinity,ell_1)`, and whether any later literature not captured by the
bounded audit already records this elementary counterexample.

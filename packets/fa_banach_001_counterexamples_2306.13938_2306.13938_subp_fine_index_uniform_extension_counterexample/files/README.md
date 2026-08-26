# A sub-p fine index destroys the uniform limiting constant

Result type: `counterexample`

Status: candidate full negative answer to the sharp uniform extension, likely
valid pending expert review.

Source: V. I. Kolyada, *Rearrangement estimates and limiting embeddings for
anisotropic Besov spaces*, arXiv:2306.13938, Theorem 1.2 and the paragraph
immediately after it on source PDF page 3.

## Claimed contribution

The sharp normalized estimate (1.4) cannot extend with a constant bounded in
the limiting regime once even one fine index is below `p`.

Fix `1<p<n` and `1<=s<p`, set `theta_1=s` and
`theta_2=...=theta_n=p`, and take all smoothness indices equal to
`rho->1`.  The target fine index is

`1/theta=(1/n)(1/s+(n-1)/p)>1/p`.

For every `epsilon` with
`0<epsilon<(1/n)(1/s-1/p)`, the best constant in the proposed extension
grows at least like

`(1-rho)^{-[(1/n)(1/s-1/p)-epsilon]}`.

The witness is a fixed compactly supported radial function which near the
origin equals

`|x|^{-(n-p)/p}[log(e/|x|)]^{-(1/p+epsilon)}`.

It lies in `W^{1,p}`.  Translation estimates keep every normalized directional
Besov factor bounded as `rho->1`, but its Lorentz norm at
`q_rho=np/(n-rho p)` diverges at the displayed rate.

## Scope

This is a counterexample to the only nontrivial reading of the source's open
extension: preserving the sharp factors `(1-beta_j)^{1/theta_j}` with a
constant bounded as the smoothness tends to one.  It does **not** deny the
known embedding for any fixed set of parameters.  For fixed `rho<1`, the
normalizing factors are merely positive constants and the older unnormalized
embedding still applies; its constant must blow up in this regime.

## Files

- `main.tex`: self-contained theorem, quantitative proof, and scope audit.
- `solution_packet.pdf`: rendered expert-review packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source Theorem 1.2 and open sentence.
- `verification.md`: proof audit and reviewer focus.
- `code/check_asymptotic_integral.py`: numerical check of the one-dimensional
  Laplace-integral asymptotic (not part of the proof).

## Novelty check

Run indexes and bounded arXiv searches through 12 August 2026 used the arXiv
id, exact title, quoted open phrase, author, `theta_j<p`, sharp limiting
constant, anisotropic Besov, and Lorentz endpoint terms.  They found the
source, the older fixed-parameter anisotropic embedding literature, and no
later paper recording this negative sharp-uniform conclusion.  Novelty is
moderate pending specialist citation review.

## Human-review recommendation

Confirm that the source's open sentence is read in its surrounding sharp
asymptotic sense (otherwise it is vacuous because the no-factor embedding is
already known).  Then audit the two elementary estimates: the uniform
normalized Besov bound from `W^{1,p}`, and the rearrangement lower bound for
the logarithmic radial singularity.


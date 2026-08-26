# 2506.15621 — fractional-dimensional Moser–Trudinger inequality

Status: candidate full result, likely valid, human review needed.

Model: GPT5.6.

Source: Samuel Bronstein, *Dominating manifolds by radial spaces*, arXiv:2506.15621, the remark on source PDF page 18 asking for a finer Moser–Trudinger inequality when the curvature-dimension parameter is non-integer.

## Result

The question has a positive answer under the same geometric nondegeneracy conditions used by the source for its integer-dimensional theorem.

For real p>1, let q=p/(p-1), k=ceil(p-1), and

    E_p(t) = exp(t) - sum_{j=0}^{k-1} t^j/j!.

If the isoperimetric profile I of an infinite-volume space satisfies

    I(s) >= c*s^(1-1/p)  for 0<s<=s_0,
    I(s) >= h*s          for s>=s_0,

then every Sobolev function with integral lip(u)^p at most one satisfies

    integral E_p(alpha*|u|^q) <= C

for every alpha<=c^q.

For integer p=n this is exactly the source's truncation. For non-integer p, the ceiling is the minimal truncation whose first surviving power is controlled by L^p.

Applying the source's small-volume isoperimetric estimate with p=N proves the natural inequality for real CD(K,N) spaces having positive unit-ball volume and positive Cheeger constant.

## Endpoint upgrade

A crude rearrangement estimate gives only alpha<c^q. The packet upgrades this to alpha=c^q by splitting the rearrangement energy at s_0. The large-volume energy controls the value v(s_0), and an exact convexity maximization reduces the small-volume integral to Moser's one-dimensional lemma for real p.

## Files

- main.tex: full theorem and proof.
- solution_packet.pdf: compiled human-review packet.
- verification_report.md: adversarial proof audit.
- source_paper.pdf: official arXiv PDF.
- figures/open_problem_crop.png: source PDF page 18 crop containing the definition, question, and surrounding theorem.

## Human review recommendation

Review as a likely valid full positive result. The highest-value checks are the rearrangement inequality in measure coordinates and the shifted endpoint lemma; both are written explicitly in the packet.

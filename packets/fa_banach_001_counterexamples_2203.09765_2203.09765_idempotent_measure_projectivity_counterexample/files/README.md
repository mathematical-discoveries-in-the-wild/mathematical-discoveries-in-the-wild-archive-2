# Idempotent-measure metric-projectivity counterexample

This packet gives a full negative answer to the conjecture after Proposition 3.2.4 of arXiv:2203.09765.

For `G=S_3`, let

    q = (delta_e + delta_(12))/2,
    a = delta_(23),
    x = (delta_e-q)*a*q,
    mu = q+x.

Then `q*x=0`, `x*q=x`, and `x*x=0`, so `mu` is idempotent. Moreover, `mu*q=mu` and `q*mu=q`, hence

    l1(S_3)*mu = l1(S_3)*q.

The common ideal is metrically projective because `q` is a norm-one idempotent. But `q` and `x` have disjoint supports, `||x||_1=1`, and therefore `||mu||=2`. The unique Haar density of `mu` cannot have norm one. This refutes the conjectured necessity.

The packet upgrades the example to every discrete group having a finite nonnormal subgroup.

Files:

- `source_paper.pdf`: official arXiv source PDF.
- `figures/source_conjecture_crop.png`: source Proposition 3.2.4 and exact conjecture.
- `main.tex`: proof packet source.
- `solution_packet.pdf`: compiled result.
- `verification_report.md`: proof and novelty audit.
- `code/check_s3.py`: exact rational convolution checker.
- `code/crop_source.py`: reproducible source crop.

Status: candidate full counterexample, likely valid, human review recommended.

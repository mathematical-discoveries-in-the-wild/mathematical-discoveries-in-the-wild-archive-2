# One-dimensional counterexample to G_M = F_M

Status: counterexample_likely_valid

Source: Stephen Simons, *Faces of quasidensity*, arXiv:2407.00479,
Remark 11.4 on official PDF page 20. The source asks whether every closed,
monotone, quasidense (CMQd) subset of B=E x E* satisfies G_M=F_M on B*.

## Claimed contribution

The conjecture fails already for E=R. For every lambda>0, take

    M_lambda = {(s, lambda*s) : s in R}.

This line is closed and monotone, and its quasidensity expression at
(a,c) is exactly

    (1/2) * ((1+lambda)*s - (a+c))^2,

whose infimum is zero. Hence M_lambda is CMQd. Exact minimization gives

    P_M(u,v) = (v-lambda*u)^2 / (4*lambda),
    G_M(y,z) = (y-lambda*z)^2 / (4*lambda),
    F_M(y,z) = 0         if y=lambda*z,
                 +infinity otherwise.

Thus at lambda=1 and (y,z)=(0,1), one has G_M=1/4 but F_M=+infinity. The
packet proves the full formula for the positive-slope scalar family.

## Verification

Run:

    conda run --no-capture-output -n sandbox python \
      runs/fa_banach_001/solutions/counterexamples/2407.00479_scalar_identity_graph_G_F_counterexample/code/verify_counterexample.py

The checker validates the quasidensity, P_M, G_M, and F_M normal forms in
exact symbolic arithmetic and verifies the concrete witness.

## Novelty and review

The bounded search on 2026-08-11 covered all cheap run indexes, exact
arXiv-id and title matches, the exact conjecture text, CMQd, quasidensity,
G_M, and F_M, plus local citing records and targeted web/arXiv queries. No
matching later resolution or scalar counterexample was found. This is
negative search evidence, not a priority claim.

Human review should focus on the leading minus sign in the source definition
of F_M and the fact that its stated codomain allows +infinity.

Files:

- source_paper.pdf: official arXiv PDF.
- source_material/source_paper.tex: ingested source TeX.
- figures/open_problem_crop.png: real crop from official PDF page 20.
- main.tex, solution_packet.pdf: proof packet.
- code/make_source_crop.py: reproducible source crop.
- code/verify_counterexample.py: exact symbolic checks.
- verification.md: build and review record.

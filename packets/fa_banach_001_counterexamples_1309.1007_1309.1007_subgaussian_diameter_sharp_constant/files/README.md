# The subgaussian-diameter concentration constant is sharp

Status: likely valid full negative answer and sharpness theorem.

Source: Aryeh Kontorovich, “Concentration in unbounded metric spaces and
algorithmic stability,” arXiv:1309.1007, ICML 2014.

The packet answers the source’s constant-recovery question negatively. On the
uniform two-point metric space, the subgaussian diameter squared is exactly
1/2. The coordinate function has absolute centered deviation 1/2 almost
surely, so the sharp McDiarmid coefficient 2 fails after replacing ordinary
diameter by subgaussian diameter.

More strongly, for a Bernoulli law of mass p on one endpoint, the subgaussian
diameter squared is asymptotic to 1/(2 log(1/p)). The rare endpoint has a
deviation tending to 1 with probability p. This proves that no universal
coefficient larger than 1/2 can hold. Since Theorem 1 of the source proves
coefficient 1/2, its constant is universally optimal.

The packet also proves:

- metric diameter equals subgaussian diameter exactly when two independent
  samples are at full diameter almost surely, hence never on a nontrivial
  Polish, countably supported, or Radon space;
- if every Lipschitz function has a subgaussian centered law, then the
  subgaussian diameter is finite, although the quantitative nearly-matching
  lower-bound problem remains open.

Files:

- solution_packet.pdf — review-ready proof packet
- main.tex — packet source
- source_paper.pdf — original arXiv source PDF
- figures/open_question_crop.png — Section 8 tightness question
- code/verify_bernoulli.py — numerical regression only

Human review should focus on the uniform three-range asymptotic estimate and
the scope of the source’s verbatim-replacement formulation.

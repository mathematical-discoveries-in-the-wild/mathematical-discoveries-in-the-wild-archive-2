# The bounded-trajectory conditioning in Conjecture 3.18 is null

This packet gives a full negative resolution, as written, of Conjecture 3.18
in arXiv:0906.2535.  On every infinite connected resistance network, a random
walk has probability zero of remaining forever in any fixed finite vertex
set.  Since the network admits a countable finite exhaustion, the event that
the entire trajectory lies in *some* finite subnetwork is also null.
Consequently the conjectured ordinary conditional probability is undefined.

The proof also pinpoints the failure in the proposed equation (3.27): the
finite free-network walk changes boundary transition probabilities and is not
the original walk conditioned on a zero-probability eternal-survival event.
A limit of finite-network laws is a possible well-defined replacement, but it
is not the conditional probability appearing in the conjecture.

Files:

- `solution_packet.pdf` — self-contained proof and diagnosis.
- `main.tex` — LaTeX source.
- `source_paper.pdf` — arXiv:0906.2535.
- `figures/open_problem_crop.png` — source PDF page 22, Conjecture 3.18 and Remark 3.19.
- `VERIFIER_REPORT.md` — mathematical, source, novelty, and visual checks.

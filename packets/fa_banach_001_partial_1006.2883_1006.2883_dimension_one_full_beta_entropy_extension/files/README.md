# Sharp one-dimensional extension of the Pareto entropy theorem

**Status:** candidate substantial partial result, likely valid; novelty
uncertain pending comparison with a 2024 inverse-Hölder preprint.

**Source:** Sergey G. Bobkov and Mokshay Madiman, *The entropy per coordinate
of a random vector is highly constrained under convexity conditions*,
arXiv:1006.2883, IEEE Transactions on Information Theory 57 (2011),
4940--4954, DOI `10.1109/TIT.2011.2158475`.

## Result

The source asks whether its Pareto extremal-entropy theorem can be extended
from `beta>=n+1` to the full normalizable range `beta>n`. This packet proves
the full extension when `n=1`:

If `beta>1` and `f=varphi^(-beta)` is a probability density on an interval,
where `varphi` is positive and convex, then

`h(f)+log ||f||_infinity <= beta/(beta-1)`.

The bound is sharp, with equality for an affine one-sided Pareto density. Thus
the entire missing interval `1<beta<2` is settled in dimension one.

The key new lemma is that

`p -> (p-1) int varphi^(-p)`

is log-concave for every `p>1`. It follows from a hinge representation of the
concave sublevel-length function.

## Scope

The all-dimensional question remains open in this packet for `n>=2`. The same
proof would work if the normalized negative-moment log-concavity extended to
all `p>n`; the packet isolates that as the sole obstruction and includes a
numerical counterexample probe, not a proof.

## Contents

- `solution_packet.pdf`: theorem, proof, source excerpt, and limitations.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: original source paper.
- `figures/open_problem_crop.png`: source PDF page 13.
- `verification.md`: proof audit.
- `code/negative_moment_probe.py`: exact piecewise-affine numerical stress
  test for the higher-dimensional normalized Mellin transform.

## Novelty check

Exact-title, arXiv-id, phrase, arXiv API, Crossref, OpenAlex, and author-page
searches found no explicit later answer to the `beta>n` question. A 2024
primary paper cites an unpublished/preprint work by Bobkov, Fradelizi,
Langharst, Li, and Madiman titled *When can one invert Hölder's inequality?
(and why one may want to)*. Its text could not be located, and its title makes
overlap plausible. Human review should compare that preprint before any
novelty claim.

## Human-review recommendation

Review the sublevel-length hinge representation and Tonelli calculation first.
Then check the one-line insertion into the source derivative argument. The
mathematics is elementary; literature overlap is the larger uncertainty.

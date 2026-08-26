# Complete local-dimension universality at countable convolution fibres

Status: `candidate_full_likely_valid`

Source: Kevin G. Hare and Joaquin G. Prandi, *Bounding the Local Dimension of
the Convolution of Measures*, arXiv:2502.18337, Section 5, PDF page 12.

## Full result

For every `0 < lambda <= 1` and every prescribed finite `beta >= 0`, the
packet constructs compactly supported probability measures `mu,nu` on the
real line such that:

- `lower_dim mu(x) >= lambda` at every support point;
- the fibre over zero is exactly `{(0,0)} union {(x_n,-x_n):n>=1}`;
- every representation pair has product lower local dimension at least
  `lambda`;
- the actual local dimension, not merely the lower dimension, satisfies
  `dim_loc(mu*nu)(0)=beta`.

Thus an exactly countably infinite fibre imposes no numerical restriction at
all on the convolution local dimension. This is a full negative resolution
of the source's countable-fibre question in the lower-local-dimension setting.

Three constructions cover the whole range:

- `0 < beta <= 1`: aligned uniform packets and atoms with
  `p_n^2` comparable to `ell_n^beta`;
- `beta=0`: the same model with widths `exp(-n^2)`, giving exponent zero at
  every small scale;
- `beta>1`: aligned one-sided power-law packets whose endpoint exponents sum
  to `beta`.

Geometric separation sends every off-diagonal interaction into a tail. Its
mass is `O(r^2)` in the first model and `O(r^(2D))` with `2D>beta` in the
second.

The packet also retains the earlier bad-centre decay criterion. It restores
lower-dimension inheritance while strictly weakening the source paper's
common-scale almost-everywhere hypothesis.

## Scope and novelty

The result is full for what countability and the stated pointwise numerical
data can imply. It does not classify upper local dimensions on arbitrary
groups or solve the source's separate higher-dimensional boundary problem.

Local indexes and bounded web searches on 2026-08-09 found the source and
Prandi's 2026 thesis, but no resolution or matching universality construction.
The thesis's later “addition of measures” chapter concerns the ordinary sum
of measures; its convolution chapter leaves this question open. Expert
bibliographic review remains required.

## Files

- `solution_packet.pdf`: source questions, proof intuition, universality
  theorem, complete proof, averaged rescue criterion, and limitations.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source-page crop showing both questions.
- `VERIFICATION.md`: proof audit and reviewer focus.
- `novelty_search.md`: bounded novelty record.
- `code/check_construction.py`: parameter and asymptotic sanity checks.
- `code/crop_source.py`: reproducible source crop.

Human review should focus on the common off-diagonal tail lemma, the
every-scale argument for `beta=0`, and the beta-integral in the `beta>1`
construction.

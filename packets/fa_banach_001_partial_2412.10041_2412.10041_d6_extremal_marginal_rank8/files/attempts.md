# Upgrade attempts

## Attempt 1: isolate the first open exact subcase

The source's introductory remains-open sentence is partially superseded by
the paper itself. Its actual surviving target is the general construction
problem. The smallest equal-dimension case not covered in the paper is d=6,
where sharpness requires Choi rank 8.

## Attempt 2: operator scaling

Random Kraus operators followed by operator scaling numerically produced
doubly stochastic maps, but the scaling matrices were irrational numerical
objects. Turning the output into a concise exact certificate would have
required a separate algebraic reconstruction step, so this route was
discarded.

## Attempt 3: balanced monomial Gaussian-integer Kraus operators

Eight permutations of six coordinates were regarded as an 8-regular
bipartite multigraph. Decomposing its edges into eight perfect matchings
assigned moduli 1 through 8 so every input column and output row receives
each modulus once. Random fourth-root phases then yielded a full-rank
combined Kraus-product matrix on the first trial. The saved d=6 instance has
a leading 64-by-64 determinant equal to 19 modulo 101 and gives the promoted
result.

## Attempt 4: general-dimension upgrade

The same balanced-monomial search returned exact full-rank modular
certificates on first trials for several additional dimensions, suggesting a
generic theorem. A proof for every dimension would need a uniform
nonvanishing argument for the determinant polynomial or a structural-rank
matching theorem compatible with both marginal constraints. Pure dimension
counting is not enough, as shown by the exceptional d=2 bistochastic case.
No uniform proof was obtained, so unrecorded exploratory instances were not
promoted.

## Attempt 5: tensor and induction propagation

The source's tensor theorem propagates an exact base construction, but the
Kraus rank and dimension multiply while the target bound is
floor(sqrt(2)d). Unless the base ratio is an exceptionally close lower
rational approximation to sqrt(2), sharpness persists only for finitely many
multipliers. A block-extension induction would also need one or two new
Kraus operators at every dimension and simultaneous control of all mixed
products; no general independence lemma was found. This does not close the
all-dimensions question.

# Full result: all bivariate quartic tracial measures reduce to size two

status: `candidate_full_likely_valid`

model: `GPT5.6`

source: Abhishek Bhardwaj and Aljaž Zalar, *The singular bivariate
quartic tracial moment problem*, arXiv:1611.00494.

decisive prior packet: `runs/fa_banach_001/solutions/full/2001.11614_tracial_y2_single_2x2_reduction/`

packet: `runs/fa_banach_001/solutions/full/1611.00494_all_quartic_atoms_size_two/`

## Result

Every normalized bivariate quartic real tracial moment sequence which has a
representing measure by real symmetric matrices of arbitrary finite sizes also
has a representing measure using only scalar and `2x2` atoms.

This completes the atom-size program left one case short in arXiv:1611.00494.
The source already gives:

- scalar atoms for the commutative case;
- at most fifteen `2x2` atoms when the `7x7` moment matrix is positive
  definite;
- size-at-most-two atoms for singular ranks at most five;
- after affine normalization, size-at-most-two atoms for three of the four
  rank-six normal forms.

The sole missing normal form is rank six with `Y^2=1`.  The prior GPT5.6 full
packet proves more: every representable quartic sequence satisfying `Y^2=1`
has a representation of type `(m,1)`, with one `2x2` atom and at most four
scalar atoms.  The ranks `1,...,7` and all four rank-six forms are therefore
exhausted.

## Verification

- The formal proof checks the commutative reduction directly from the
  commutator-square identity and then partitions by `rank(M_2)`.
- The decisive source passages were checked on pages 3--4 of the arXiv PDF;
  the `Y^2=1` conjecture and its proof are included as local supporting PDFs.
- `code/verify_rank_exhaustion.py` verifies the commutator identity on 2,000
  seeded random symmetric matrix pairs and mechanically checks that every
  rank/normal-form branch is assigned a size-two theorem.
- A bounded local-index and primary arXiv search through 2026-08-11 found the
  source, arXiv:2001.11614, and the existing run packet, but no paper stating
  the all-rank synthesis as a theorem.

## Human-review focus

Confirm that the source's affine normalization in Proposition 4.1 is
invertible (so atom size is preserved) and that its page-4 phrase “the first
three cases” covers exactly the three rank-six forms other than `Y^2=1`.
The remaining step is precisely Theorem 1 of the supporting GPT5.6 packet.


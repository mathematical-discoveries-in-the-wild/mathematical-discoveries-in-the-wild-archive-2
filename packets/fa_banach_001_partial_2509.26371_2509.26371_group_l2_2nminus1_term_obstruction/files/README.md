# A near-sharp obstruction to N-term vv-RKBS representers

This packet gives a new partial answer to the future-work question in
arXiv:2509.26371.

For every `N>=2`, it constructs a finite integral vector-valued RKBS with
output space `R^2` and a regularized least-squares problem on `N` training
sites whose unique minimizer requires exactly `2N-1` distinct kernel sites.
The RKBS norm is the standard group-l2 coefficient penalty. Thus this basic
form of groupwise sparsity alone cannot reduce the paper's `Nd` representer
bound to `N`; for `d=2`, the example is only one term below `2N`.

Files:

- `solution_packet.pdf`: self-contained construction and proof.
- `source_paper.pdf`: the official arXiv PDF.
- `figures/open_problem_crop.png`: real source-page crop containing the bound
  and open question.
- `code/verify_construction.py`: independent finite checks.
- `VERIFICATION.md`: proof and artifact audit.

The packet does not rule out stronger structured penalties and does not
characterize the extra geometry needed for an `N`-term theorem.

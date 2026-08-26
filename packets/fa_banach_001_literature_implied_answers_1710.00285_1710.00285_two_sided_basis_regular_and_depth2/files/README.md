# Literature-implied partial answer: two-sided Pimsner--Popa bases

Run: `fa_banach_001`  
Agent: `agent_lane_15`  
Result type: `literature_implied_answer (partial subcases)`

## Result

The open question in Remark 3.14 of arXiv:1710.00285 asks whether every
finite-index irreducible subfactor admits a two-sided Pimsner--Popa basis.
Two direct follow-ups give affirmative proper subcases:

- arXiv:1904.05612, Theorem 3.10: every finite-index regular inclusion of
  `II_1` factors has a two-sided basis;
- arXiv:2102.01462, Theorem 3.14 and Corollary 3.15: every finite-index
  irreducible depth-two inclusion has a two-sided orthonormal basis, including
  nonregular Kac-algebra subfactors.

The unrestricted extremal/irreducible question remains outside these results.
The source's separate polynomial-growth conjecture for minimal intermediate
subfactors is also untouched.

## Evidence

- `source/1710.00285.pdf`: official source PDF; question on page 8.
- `source/1904.05612.pdf`: official regular-case paper; Theorem 3.10 on page 13.
- `source/2102.01462.pdf`: official depth-two paper; Corollary 3.15 on page 9.
- `source/source_question_page8.png`: real crop from the official source PDF.
- `main.tex`, `solution_packet.pdf`, and `VERIFICATION.md`: packet and audit.

## Human review recommendation

Verify the regular theorem and the depth-two corollary independently, and keep
the packet's caveat that depth-two nondegeneracy/tensor-splitting does not
follow for arbitrary finite-depth irreducible inclusions.

# Verification report

Verdict: **candidate full resolution, likely valid**.

## Source verification

- `source_paper.pdf` is the 28-page arXiv PDF for 2402.13574.
- Question 2.9 appears on PDF page 8.
- `figures/open_question_crop.jpg` contains the preceding context and complete
  question.

## Mathematical audit

1. From a left group inverse `x` of `b=a^n`, the element `e=xb` is idempotent
   and satisfies `be=eb=b`. Thus `p=1-e` obeys `bp=pb=0`.
2. The right annihilator of `b` is exactly `pR`: if `br=0`, then `er=xbr=0`
   and hence `r=pr`. Since `b(ap)=0`, this forces `eap=0`, giving the claimed
   lower-triangular Peirce form of `a`.
3. Its diagonal corners satisfy `A^n=b` and `D^n=0`. The element `exe` left
   inverts `A^n`, so `L=(exe)A^(n-1)` left inverts `A`.
4. The finite sum `T=sum D^k C L^(k+1)` lies in `pRe`, has `T^2=0`, and
   telescopes to `TA-DT=C`. Therefore `(1-T)a(1+T)=A+D`.
5. In diagonal coordinates, `L` satisfies all three left-Drazin equations at
   exponent `n`; similarity carries it back to the original element.
6. The reverse implication follows from the commuting Peirce idempotent of a
   left-Drazin inverse: the nilpotent corner vanishes in `a^n`, while the good
   corner remains left invertible, which is precisely left group
   invertibility.
7. The right-handed result is the left-handed theorem in the opposite ring.
8. Minimal-index equality requires excluding the preceding power; the theorem
   therefore resolves the source's index ambiguity sharply.

No topology, completeness, or spectral argument is used, so the unital-ring
strengthening is justified.

## Exact verifier

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2402.13574_power_criterion_one_sided_drazin/code/verify_block_conjugation.py
```

The exact SymPy run checks the block construction at exponent three, including
the similarity and every generalized-inverse equation. It is a regression
check, not a substitute for the general proof.

## Novelty audit

- Searched the run registry, solution, attempt, and proof-gap indexes for the
  arXiv id and core one-sided Drazin/group-inverse power terminology.
- Searched arXiv/web indexes using the exact question and variants involving
  `a^n`, left/right group inverses, powers, and one-sided Drazin index.
- Inspected the local source of the author's follow-up arXiv:2504.18995. It
  clarifies that the index is minimal and proves other fundamental results,
  but no answer to this power criterion was found.
- Novelty confidence: moderate, pending specialist bibliographic review.

## Upgrade-attempt audit

The initial route sought a counterexample caused by a group inverse of `a^n`
that failed to commute with `a`. The deep upgrade replaced that obstruction by
an explicit finite Sylvester conjugation: the noncommuting Peirce idempotent can
always be tilted to an idempotent commuting with `a`. This produced a full
power criterion and strengthened the setting from Banach algebras to rings.

## Rendering audit

The final `solution_packet.pdf` builds without LaTeX warnings or overfull
boxes. All three pages were rendered to PNG and inspected at full resolution:
the source question is legible, displayed equations and references remain
inside the margins, no literal TeX commands survive, and the formerly sparse
reference page has been consolidated cleanly onto page three.

# Verification Report

Verdict: `likely valid`, candidate full answer.

## Exact checks

1. For `S(x)=0` on `x<=2` and `S(x)=-1/3` on `x>2`, same-branch pairs have zero image distance. For a cross-branch pair `x<=2<y`, the image distance is `1/3`, while
   `(1/7)(|x|+|y+1/3|) > (1/7)(7/3)=1/3`.
2. With `T=2S-I`, both sides of the Kannan inequality for `S` are multiplied by two, giving the enriched Kannan inequality for `T` with `(k,a)=(1,1/7)`.
3. At `x=1,y=-1`, ordinary Kannan for `T` would require `2<=4c`, hence `c>=1/2`; this is forbidden.
4. An enriched Banach inequality with parameters `(b,theta)` implies the Lipschitz bound `|Tx-Ty| <= (b+theta)|x-y|`. The displayed `T` jumps from value `-2` at `2` to right limit `-8/3`, so it cannot be enriched Banach.
5. `R` is a Banach space, `k=1>=0`, and `a=1/7` lies in `[0,1/2)`.

No computational experiment is used as evidence or proof.

The evidence crop was produced after rendering source PDF pages 4--5 at 180 dpi, using `code/make_open_problem_crop.py`. The script performs only reproducible cropping, stitching, and page labeling; it does not alter the mathematical text.

## Novelty bounds

Searched on August 11, 2026:

- local registry, solutions, attempts, and proof-gap indexes;
- parsed arXiv source corpus;
- exact phrases `"strictly enriched Kannan"`, `"find a strictly enriched Kannan mapping"`, and `"not an enriched contraction"`;
- arXiv id `1909.02382` combined with `open problem` and `enriched Kannan`;
- close web combinations of `enriched Kannan`, `enriched contraction`, `independent`, and `counterexample`.

The search found the source question and later papers restating or extending these mapping classes, including work in Banach, ordered, and CAT(0) settings. It found no paper presenting a map claimed to answer this exact question. This is a bounded search, not a certification of novelty.

## Reviewer focus

- Confirm the source paper's definition of “strictly enriched Kannan.”
- Recheck the strict cross-branch inequality at the limiting pair `x=0`, `y downarrow 2`.
- Consider a specialist MathSciNet/zbMATH citation search before public novelty claims.

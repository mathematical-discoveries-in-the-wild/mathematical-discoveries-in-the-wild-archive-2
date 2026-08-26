# Verification report

verdict: likely valid full answer to the literal pointwise-convergence
question, pending human judgment on whether the source intended a more
restrictive notion of a useful criterion.

## Logical audit

1. For fixed x,y, if F_n(x)->F(x) and F_m(y)->F(y), then

       lim_N sup_{n,m>=N}|F_n(x)-F_m(y)| = |F(x)-F(y)|.

   Both inequalities follow by the triangle inequality and independent
   tail convergence at x and y.

2. Necessity uses only the standard fact that a regulated left-continuous
   function with endpoint limits is uniformly approximable by a finite
   left-continuous step function.  Refining at the finitely many jumps makes
   its constancy cells exactly

       [-infinity,a_1], (a_1,a_2], ..., (a_(q-1),infinity].

   If the uniform approximation error is below epsilon/3, the oscillation
   of the limit on every cell is below 2epsilon/3.

3. For sufficiency, every point x belongs to one cell of every selected
   partition.  Since Delta({x})<=Delta(I), the scalar sequence F_n(x) is
   Cauchy.  Completeness of the reals gives a pointwise limit F.

4. Reapplying item 1 identifies Delta(I) with diam F(I).  On the first cell
   choose the step value 0; this is within epsilon because F(-infinity)=0
   lies in that cell.  On every later cell ending at a_j choose F(a_j).
   The result is left continuous, regulated, normalized at minus infinity,
   and constant near plus infinity.  Its uniform distance from F is below
   epsilon.

5. A uniform limit of such step functions is left continuous, has right
   limits at every finite point, tends to zero at minus infinity, and has a
   finite limit agreeing with its value at plus infinity.  Hence F is in
   B_R.

## Edge cases

- A one-cell partition is allowed and covers the identically convergent
  case.
- The endpoint values are included in the first and last cells, so the
  source paper's escaping-mass example F_n(x)=H_1(x-n) fails the criterion:
  the last cell has mixed diameter one.
- Jumps are permitted because a breakpoint belongs to the cell on its left.
- No uniform boundedness in n is assumed or needed; the partition condition
  itself forces pointwise Cauchy tails.

## Sharpness check

For F_n=1_(0,1/n], every fixed x has F_n(x)->0, so the exact mixed diameter
vanishes on every set.  However, on every positive cell adjacent to zero,
the stronger quantity obtained by taking the spatial supremum before the
index limit stays equal to one.  The right traces F_n(0+) also stay equal to
one.  Therefore neither trace convergence nor equiregulation is hidden in
the claimed equivalence.

## Source and rendering audit

- arXiv source id and PDF: 0911.2931.
- Open statement location: journal/preprint PDF page 36, convergence section.
- The crop retains the complete paragraph and readable margins.
- Every rendered packet page was visually inspected after the final build.

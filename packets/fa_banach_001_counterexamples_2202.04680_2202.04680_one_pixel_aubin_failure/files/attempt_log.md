# Attempt log

Target: arXiv:2202.04680v3, source PDF page 17.

1. Located all three scanner signals. The displayed multiclass segmentation
   problem is the paper's model definition, and the conclusion's deep-learning
   discussion is non-propositional. The only genuine open statement asks
   whether the Aubin and dual-smallness conditions from nonlinear PDHG theory
   hold for the discrete functional.
2. Reconstructed the cited convergence theorem from arXiv:1309.5032v2. Its
   linearized saddle map is H_x(z)=(partial G + K'(x)^*y, partial F^* -
   K'(x)u-c_x), and local convergence assumes the Aubin property of its inverse
   plus a small nonlinear dual component.
3. Tested the smallest admissible discretization: one pixel, two classes, and
   zero feature maps. This makes the full operator K=(gradient,M) identically
   zero while retaining the source's simplex constraint and dual balls.
4. Computed the inverse saddle map exactly as the product of inverse normal
   cones. Small perturbations t(1,-1) select one simplex vertex, while the
   unperturbed inverse contains the barycenter. The resulting fixed
   1/sqrt(2) displacement contradicts every Aubin modulus as t tends to zero.
5. Stress-tested the construction against the informal dual-smallness
   condition: the reference dual variable is zero. Also checked the separate
   strong-convexity hypothesis in the cited theorem; the source's conjugate is
   an indicator of nontrivial dual balls and is not strongly convex on the
   nonlinear block.
6. Bounded exact-title, exact-question, arXiv-id, Aubin-property, and
   dual-variable searches found the source and general variational-analysis
   literature but no explicit answer to this source question.

Outcome: candidate full counterexample to automatic satisfaction of the
convergence conditions. No numerical experiment is required.

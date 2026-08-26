# Little-Zygmund graph counterexample to Conjecture 6.1

Status: candidate_counterexample_likely_valid.

Source: Maxim V. Balashov and Dusan Repovs, *Weakly convex sets and modulus
of nonconvexity*, arXiv:1007.0162, Conjecture 6.1.

## Result

The packet disproves Conjecture 6.1 even in the Euclidean plane, hence even
with a smooth uniformly convex ambient norm.

Choose an even smooth cutoff chi which is one near zero and define

    f(x)=chi(x) x sin(log log(e/|x|)),  f(0)=0.

Let A be the epigraph of f. Then cl(R^2\A) is the hypograph of f and
cl(int A)=A. Both sets are weakly convex, and both exact moduli of
nonconvexity satisfy

    gamma(epsilon)/epsilon -> 0.

The reason is that f has uniformly vanishing normalized second differences:

    sup_x |f(x+h)+f(x-h)-2f(x)| / |h| -> 0.

Nevertheless f(x)/x oscillates between -1 and 1 as x tends to zero. A direct
normal-cone argument shows that the epigraph has no nonzero Frechet normal at
(0,0), hence no unit normal or proximal unit normal there. The conjectured
normal field therefore fails already at existence.

## Verification and scope

The proof is self-contained. The key analytic check splits into
|x|>=2|h|, where |f''(x)| is bounded by
C/(|x|log(e/|x|)), and |x|<2|h|, where multiplicative slow variation of
sin(log log(e/r)) gives the uniform estimate.

The included verifier samples the second-difference ratio and the two secant
phases. It is a sanity check only; the proof does not depend on numerics.

A bounded novelty search through 11 August 2026 covered the exact title,
Conjecture 6.1, weak-convexity normal fields, and close proximal-smoothness
phrases. It found the source and adjacent stronger-hypothesis results but no
later resolution. Novelty confidence is moderate to high, subject to checking
the source's intended meaning of a common modulus for the two sides. The
packet proves the stronger unambiguous statement that each exact modulus is
o(epsilon).

## Files

- main.tex: complete statement and proof.
- solution_packet.pdf: rendered proof packet.
- source_paper.pdf: locally rendered from the exact archived arXiv TeX and EPS
  sources.
- figures/open_problem_crop.png: source Theorem 5.2 and Conjecture 6.1.
- code/verify_second_difference.py: numerical sanity check.
- tmp/: source build, LaTeX, and visual-QA intermediates.

Human review should focus on the uniform little-Zygmund estimate and the
translation from graph second differences to the source's exact modulus of
nonconvexity.

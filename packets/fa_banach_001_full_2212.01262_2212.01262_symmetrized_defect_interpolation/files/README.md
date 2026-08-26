# Symmetrized-defect interpolation

Status: likely-valid full positive answer to the interpolation question in arXiv:2212.01262, with human review recommended and low novelty confidence.

## Result

For an order-sublinear operator T and a linear reference operator A, set

    D(f) = T(f) - A(f),
    Q(f) = D(f) vee D(-f).

Then Q is a conventional nonnegative sublinear operator and

    |T(f)-A(f)| <= Q(f).

Consequently, every real-interpolation estimate for sublinear operators applies to the approximation defect. If

    ||T(f)-A(f)||_{Y_i} <= a_i ||f||_{X_i},  i=0,1,

then

    ||T(f)-A(f)||_{(Y_0,Y_1)_{theta,q}}
        <= 2 a_0^(1-theta) a_1^theta
           ||f||_{(X_0,X_1)_{theta,q}}.

The packet proves this directly from the lattice decomposition property and the K-functional.

## Korovkin consequence

Combining the theorem with the endpoint estimates in the source paper gives, for 1<p<infinity,

    ||T(f)-f||_p <= C_p lambda_1^(1/p) lambda_infinity^(1-1/p)
                        ||f||_{(W_1^3,W_infinity^2)_{1-1/p,p}}.

If T is bounded on L^p, a second approximation step gives an all-L^p K-functional estimate. For the paper's nonlinear Bernstein example T_n=max(B_n,B_{n+1}), the smooth-class rate is O(1/n).

## Scope and novelty

The broad interpolation question is resolved at the operator-theoretic level. The theorem does not assert that every desired sharp estimate follows from one fixed pair of endpoints; the relevant endpoint inequalities must still be proved and inserted into the interpolation theorem.

General sublinear interpolation is classical. The contribution here is the defect symmetrization that converts the source paper's one-sided order-sublinearity into the standard sublinear object required by the theory, together with the explicit Korovkin corollary. Exact searches found no prior use of this reduction for the stated question, but novelty confidence is low.

## Files

- solution_packet.pdf: self-contained proof packet.
- main.tex: packet source.
- source_paper.pdf: arXiv source paper.
- figures/open_problem_crop.png: source page 11 open-question crop.


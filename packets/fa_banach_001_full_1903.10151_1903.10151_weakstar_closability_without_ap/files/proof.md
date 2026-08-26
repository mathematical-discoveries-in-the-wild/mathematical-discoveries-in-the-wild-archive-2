# Proof: AP is unnecessary for weak-* closability

## Setting

Let `G` be a discrete group, let `b_psi: G -> H` be the real 1-cocycle used
in arXiv:1903.10151, and let `alpha` be the induced trace-preserving action on
the q-Gaussian von Neumann algebra `Gamma_q(H)`, where `-1 <= q < 1`. Put

`N = Gamma_q(H) rtimes_alpha G`.

On the Fourier polynomials `P_G` in `VN(G)`, the source defines

\[
\partial_{\psi,q}(\lambda_s)
=s_q(b_\psi(s))\rtimes\lambda_s.
\]

## Theorem

For every discrete group `G`, with no approximation-property assumption,

\[
\partial_{\psi,q}:\mathcal P_G\subseteq\mathrm{VN}(G)\to N
\]

is weak-* closable.

## Proof intuition

The gradient is diagonal with respect to group Fourier coefficients. Weak-*
convergence preserves every coefficient because coefficient extraction is a
normal map. Thus a weak-* graph limit above zero has every coefficient zero,
and crossed-product Fourier coefficients determine the element.

## Proof

Let `E_Gamma: N -> Gamma_q(H)` be the canonical normal faithful conditional
expectation, and for `s in G` define

\[
C_s(z)=E_\Gamma\bigl(z(1\rtimes\lambda_s)^*\bigr).
\]

Right multiplication by the fixed unitary `1 rtimes lambda_s` is normal, so
`C_s` is weak-* continuous. On a Fourier polynomial,

\[
C_s\left(\sum_{t\in F}a_t\rtimes\lambda_t\right)=a_s.
\]

Suppose a net `(x_i)` in `P_G` satisfies

\[
x_i\overset{w^*}{\longrightarrow}0,
\qquad
\partial_{\psi,q}(x_i)\overset{w^*}{\longrightarrow}y\in N.
\]

Write `x_i = sum_t x_{i,t} lambda_t`, with finite support depending on `i`.
For each fixed `s`,

\[
x_{i,s}=\tau_G(x_i\lambda_s^*)\longrightarrow0,
\]

because `x -> tau_G(x lambda_s^*)` is a normal functional on `VN(G)`. By the
formula defining the gradient,

\[
C_s(\partial_{\psi,q}(x_i))
=x_{i,s}s_q(b_\psi(s)).
\]

Weak-* continuity of `C_s` therefore gives

\[
C_s(y)=\lim_i x_{i,s}s_q(b_\psi(s))=0
\qquad(s\in G).
\]

It remains only to use uniqueness of crossed-product Fourier coefficients.
Indeed, with the canonical finite trace,

\[
L^2(N)=\bigoplus_{s\in G}^{\perp}
L^2(\Gamma_q(H))(1\rtimes\lambda_s),
\]

and `C_s(y)` is the `s`-th Fourier coordinate of `y`. Since `y` is a bounded
element of the finite von Neumann algebra `N`, it belongs to `L^2(N)`. Every
orthogonal coordinate of `y` is zero, hence `y=0` in `L^2(N)` and therefore in
`N`. This is exactly weak-* closability. QED.

## Scope

The argument proves the net version, stronger than the sequential formulation
in footnote 26 of the source. It retains `q < 1` because boundedness of the
q-Gaussian field operators in the target von Neumann algebra is used in the
definition. No statement is made about the separate later questions concerning
Lipschitz algebras or optimal commutator estimates.

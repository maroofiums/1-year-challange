# Day 343 - Mathematics for Data Science 

A concise cheatsheet covering all core math concepts needed for data science.

---

## 1. Linear Algebra
- **Vectors:** `v = [v1, v2, ..., vn]`  
  - Dot product: `a · b = a1*b1 + a2*b2 + ... + an*bn`  
  - Norm: `||v|| = sqrt(v1^2 + v2^2 + ... + vn^2)`
- **Matrices:**  
  - Multiplication: `C = A · B`  
  - Transpose: `A^T`  
  - Inverse: `A^-1` (only if det(A) ≠ 0)
- **Eigenvectors & Eigenvalues:** `A*v = λ*v`
- **Applications:** PCA, embeddings, linear transformations

---

## 2. Calculus
- **Derivative:** rate of change of a function  
  - `f'(x) = limit (Δx -> 0) [(f(x+Δx) - f(x)) / Δx]`
- **Partial derivative:** `∂f/∂x`
- **Gradient:** `∇f = [∂f/∂x1, ∂f/∂x2, ..., ∂f/∂xn]`
- **Chain Rule:** `dz/dx = dz/dy * dy/dx`
- **Gradient Descent:** `θ = θ - α * ∇θ J(θ)`

---

## 3. Probability & Statistics
- **Probability:** `P(A) = favorable/total`  
- **Conditional Probability:** `P(A|B) = P(A∩B)/P(B)`  
- **Bayes:** `P(A|B) = P(B|A)*P(A)/P(B)`
- **Random Variables:** mean `E[X] = Σ x*P(x)`, variance `Var(X) = E[X^2] - (E[X])^2`
- **Correlation:** `Corr(X,Y) = Cov(X,Y)/(σ_X*σ_Y)`

---

## 4. Regression & ML Basics
- **Linear Regression:**  
  - `y = Xβ + ε`  
  - Loss: `MSE = (1/n) Σ (yi - ŷi)^2`  
  - Closed form: `β = (X^T X)^-1 X^T y`
- **Logistic Regression:**  
  - Sigmoid: `σ(z) = 1 / (1 + e^-z)`  
  - Loss: Cross-entropy = `-(1/n) Σ [y log ŷ + (1-y) log (1-ŷ)]`

---

## 5. Discrete Math / Combinatorics
- **Permutations:** `P(n,r) = n! / (n-r)!`  
- **Combinations:** `C(n,r) = n! / (r! (n-r)!)`
- **Sets:** union, intersection, difference  
- **Graphs:** nodes, edges, adjacency matrix/list

---

## 6. Optimization
- **Convex function:** `f(λx + (1-λ)y) ≤ λf(x) + (1-λ)f(y)`  
- **Lagrange multipliers:** solve `∇f = λ ∇g` for constraint `g(x,y)=0`  
- **Gradient Descent Variants:** SGD, Mini-batch, Adam

---

## 7. Practice Tips
- Always connect math → Python implementation → ML use  
- Visualize concepts: matrices, gradients, distributions  
- Keep a notebook of formulas and examples
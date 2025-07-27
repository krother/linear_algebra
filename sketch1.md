
# Linear 

## Introduction

- why do we need LinAlg?
- overview
- 4Mat


## vectors and matrices

Example: Supermarket

- what are vectors and matrices?
- addition, substraction -> 2D plot
- data vector interpretation
- geometrical interpretation
- vector multiplication: scalar, vector, dot, cross
  - scalar multiplications -> longer and shorter
  - dot product -> weighted sum, projection, 0 if orthogonal
  - cross product -> orthogonal, 0 if colinear?
- special matrices: square, identity, null, inverse, invertible


EXERCISE: determine supermarket prices

## linear transformations

Example: Wall clock

- vector-matrix multiplication
- multiplications have angle aspect
- 1 angle
- how do dimensions change?
- simple rotation example: Tetris bricks
- transpose
- rotation matrix
- scaling
- matrix-matrix multiplication
- special matrices: square matrix, unity matrix, 
- 3 angles in 3D
- application: 3D vector graphics, CAD, Unreal engine

- Exercise: transform vectors for clock hands

## determinants and norms

Example: recommender

- length of vector
- regularization
- norms: measuring distance
- manhattan distance
- euclidean distance
- cosine similarity
- Exercise: find most similar user
- matrix factorization
- determinant: area + orientation
- determinant: linearly independent
- correlation matrix

Exercise: recommend a movie

## graph analysis


- adjacency matrix
- similarity matrix
- distance matrix
- symmetric matrix  : A = A.T
- centrality: random movement
- ML methods: clustering, manifold learning

- pagerank
- eigenvectors
- Example: number images
- PCA
- eigenvectors

Example: Markov chain
- supermarket

Example Application: Language tree

### Feature Engineering

How to use Linear Algebra on things that are not vectors

Images
- Convolution

Text
- word embeddings
- Spacy example
- TF projector
- enumerate embedding dimensions

### solving equation systems

- gauss elimination
- example: base fare + per mile * km

A chemist has 70 mL of a 50% methane solution. How much of an 80% solution must she add so the final solution is 60% methane?

- linear solvers
- traffic flow through network
- timetable problem, burrito

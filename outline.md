
# Linear Algebra for Data Science

## Description

How can you analyze large quantities of data? As soon as you consider tools like Linear Regression, Clustering, Network Analysis or Machine Learning, Linear Algebra is around the corner.
Linear Algebra is a branch of mathematics that revolves around vectors and matrices. It helps to build efficient algorithms on massive datasets. This workshop will help you to develop an understanding for this key component of data science.

This workshop addresses students who never attended a Linear Algebra course. The aim is to present mathematical concepts which are a prerequisites for topics like Machine Learning and Causal Inference. The workshop will cover many practical examples using Linear Algebra to create and modify image data.

Core topics:

- vectors and matrices
- linear transformations
- determinants and norms
- solving equation systems
- graph analysis
- eigenvectors

## Old Material

https://ds3.ai/2023/linear-algebra

## Outline

1. Vectors
2. Matrices
3. Linear Transformations
4. Distances and Norms
5. Recommender Systems
6. Graph Analysis
7. Linear Equation Systems
8. Vectorizing images and text


## Detailed outline

- why do we need LinAlg?
- overview

### 0. Introduction

**PUNCHLINE: linear algebra is a set of useful mathematical shortcuts for large datasets**

- why do we need LinAlg?
- self
- overview
- 4Mat

### 1. Vectors

**PUNCHLINE: vectors are arrays of numbers that represent geometrical entities or just data.**
**PUNCHLINE: there are four ways to multiply vectors.**

Example: Supermarket

- what are vectors?
  - a geometric entity with a direction and length
    geometric interpretation: a coordinate in n-dimensional cartesian coordinates
    physics

  - data interpretation: feature vector: an observation (data point) consisting of multiple features 
    
  - both are arrays of n real numbers

- notation:
  - lowercase letters, with arrow (not always)
  - written as (a b c)
  - can have any number of dimensions

- addition, substraction -> 2D plot

- 4 ways to multiply vectors

- scalar multiplications (scale) -> multiply each item, make the vector longer and shorter

-  component-wise product -> multiply each item with the corresponding position
   (Hadamard or Schur product)

- dot product -> projection, multiply then sum
  - 0 if orthogonal; ex (1 0) (0 1)
  (inner product)

- cross product -> calculate orthogonal vector, 0 if colinear
  - equation
  - IMAGE normal on 2 vectors
  - non-commutative
  - works for > 3 dimensions but more complicated
  (outer product)

- special vectors
  - Null vector
  - unit vector (1 0), length 1 along an axis, define a coordinate system
  - binary vectors (consist of 0 and 1)

Exercises:

- what happens if you swap the arguments of the cross product?
- which vectors are colinear?

which vector is orthogonal to (1 2)

(2 1) (-1 -2) (2 4) (2 -1) (0 0)

- create a large vector (arange)
- plot

### 2. Matrices

**PUNCHLINE: matrices are n, m tables of numbers.**
**PUNCHLINE: dot products work with matrices, too.**

Example: Supermarket

- what are matrices?
  a two-dimensional array of real numbers
  denoted by capital letters
  dimension n x m (rows x columns)
 
- what is their meaning?
  - a table with data
  - a linear transformation from one coordinate system to another (see next chapter)

- addition, substraction, scalar multiplication -> same as vectors

- matrix-vector product 
  - like the dot product, but with each row or column
  - matrix-vector product: vector called a column vector, a (n, 1) matrix
  - vector called a **row vector**, a (1, n) matrix, often denoted by transpose
  - one dimension has to be the same, watch the indices!
  - non-commutative!
  - trick: write down dimensions: (3) * (3, 2) works
  - EXAMPLE WITH NUMBERS

- special matrices
  - square matrix
  - identity matrix
  - transposed matrix

Exercise: determine supermarket prices

- linear regression
- dot product is the foundation of Machine Learning and Neural Networks
- NVidia and other GPU chips are optimized hardware for calculating dot products and similar operations on matrices

PENGUINS: Linear Regression


### 3. Linear Transformations

Matrices represent linear transformations of coordinate systems

Example: transform vector image

- matrix-matrix multiplication
  - simple rotation example: Tetris bricks
  - multiply vector or matrix
  - resulting dimension is the remaining one of matrix
  - lenghts and proportions may change
  - left-top trick

- rotation matrix
  - example with 1 angle
  - example with 3 angles
  - application: 3D vector graphics, CAD, Unreal engine, 3D superposition of molecules

- other linear transformations:
  - scale
  - squash (non-proportional scaling)
  - flip

Exercise: transform vectors for clock hands

PENGUINS: MSE, MAE
?? PENGUINS: Regularization

### 4. Distances and Norms

- how to compare two vectors?
  - here we use 3 methods

- L1 Norm: Manhattan distance
- L2 Norm: Euclidean distance (length of vector) WITH SQRT
- cosine similarity: angle between vecotrs

  cos(phi) = a dot b / ||a|| * ||b||

- Application: regularization in Machine Learning

- relationship between dot product / cross product and angle
- distance matrix
- clustering


PENGUINS: distance matrix
PENGUINS: min-max scaling
PENGUINS: clustering

Example Application: Language tree
- Frobenius norm for Matrices

### 5. Recommender Systems

some recap. 
Example: recommender system

- Exercise: find most similar user
  - find closest vector
  - RAG
  - which distance to use?

- matrix-matrix multiplication
- matrix factorization
- norm of matrix

Exercise: recommend a movie

PENGUINS: similarity search


### 6. Graph Analysis

Example: Markov chain
IMAGE: map of Europe

- adjacency matrix
- distance matrix (for graph with weights)
- similarity matrix
- symmetric matrix  : A = A.T
- unsymmetric: 

- centrality
  - we want to find out the important nodes
  - random movement
  - Markov chain
    - transition probability matrix
    - Markov rule A(t+1) = A(t) M
  - eigenvectors
    - pagerank

Example: number images

Application - PCA


### 7. Linear Equation Systems

PENGUINS: Linear Independence

  - inverse matrix (not the same as transpose!); not all matrices are invertible; singular matrix: ???

- determinant: area + orientation
  The determinant of a 2-D array [[a, b], [c, d]] is ad - bc:
- use determinant to check for linear independence (CHECK)

Add property weight in kg
- correlation matrix

- gauss elimination: requires square matrix N equations with N unknowns
- example: base fare + per mile * km
- robust: works with transposed matrices

A chemist has 70 mL of a 50% methane solution. How much of an 80% solution must she add so the final solution is 60% methane?

Example applications:
- linear solvers
- traffic flow through network
- timetable problem, burrito


### 8. Converting images and text to vectors

How to use Linear Algebra on things that are not vectors

- Feature Engineering
- one-hot encoding of penguin species

Images
- Convolution
- IMAGE: CNN
- interactive MNIST tool

Text
- Word vectors
- coffee, espresso, cappuccino
- hand + glove = foot + shoe
- document vectors
- word embeddings
- Spacy example
- TF projector
- enumerate embedding dimensions
  -> applications: Neural

## Links

Linalg in 4 pages

https://courses.lumenlearning.com/cuny-hunter-collegealgebra/chapter/systems-of-linear-equations-two-variables/


09:00 AM Session Starts

Linear Algebra for Data Science (Part I)
11:00 PM Short Break
11:15 PM Session Continues

Linear Algebra for Data Science (Part II)
01:00 PM Session Ends 


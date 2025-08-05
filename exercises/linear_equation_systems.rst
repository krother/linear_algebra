
Linear Equation Systems
=======================

.. image:: fruit.jpg

Image by `Jonas Kakaroto <https://unsplash.com/de/@jkakaroto?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash>`__ on `Unsplash <https://unsplash.com/de/fotos/rote-apfelfrucht-neben-grunem-apfel-und-gelbe-frucht-auf-braun-geflochtenem-korb-5JQH9Iqnm9o?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash>`__.
      

In this exercise, we will use **linear equations** to find unknown variables.

Consider the following four persons shopping fruit.
You know how many items everybody has bought and how much they spent, but the item prices are unknown.

+------------+-----------+------------+-------------+-------------+-----------+
| fruit      | apple 🍎  | banana 🍌  | cherry 🍒   | grapes 🍇   | **total** |
+============+===========+============+=============+=============+===========+
| Ada        | 2         | 0          | 4           | 2           | 24        |
+------------+-----------+------------+-------------+-------------+-----------+
| Bashir     | 1         | 2          | 6           | 4           | 39        |
+------------+-----------+------------+-------------+-------------+-----------+
| Choi       | 2         | 0          | 8           | 8           | 58        |
+------------+-----------+------------+-------------+-------------+-----------+
| Deryl      | 2         | 1          | 9           | 4           | 51        |
+------------+-----------+------------+-------------+-------------+-----------+


We can treat this data as a set of linear equations, e.g. for Ada:

.. equation::

   ada = 2 \cdot apple + 0 \cdot banana + 4 \cdot cherry + 2 \cdot grapes = 24

That is, we have four equations with four unknowns.
You could use high school algebra to solve this manually.

Matrix representation
---------------------

The shortcut linear algebra offers represents the fruit items as a matrix **F**, and the total bill as a column vector :math:`\vec{bills}`:

.. code:: python

    import numpy as np

    F = np.array([
        [2, 0, 4, 2],
        [1, 2, 6, 4],
        [2, 0, 8, 8],
        [2, 1, 9, 4]])

    bills = np.array([24, 39, 58, 51])

.. warning

   Careful, we have a square matrix once again!


Is the equation system solvable?
--------------------------------

Not all linear equation systems are solvable.
Some have an infinite number of solutions, others are not solvable at all.

By checking, whether the matrix **F** is invertible, we verify that it is actually possible to solve the problem:

.. code:: python3

   G = np.linalg.inv(F)

When you multiply, the inverted matrix with the original one, you should obtain an identity matrix:

.. code:: python3

   np.dot(F, G) 

Another way to ensure the matrix is non-singular is checking that its **determinant** is nonzero:

.. code:: python3

   np.linalg.det(F)

Gauss-Jordan Elimination
------------------------

The `Gauss-Jordan Elimination <https://en.wikipedia.org/wiki/Gaussian_elimination>`__ procedure now rearranges the values in the matrix to the **row echelon form** so that each row allows to determine one of the variable.
NumPy does all the work for us:

.. code:: python3

   prices = np.linalg.solve(F, bills)
   prices


Use the dot product to check whether you can reproduce the original bills:

.. code:: python3

   np.dot(..., ...)

.. warning::

    If you accidentally transpose the matrix, you will get an entirely different result.
    In this case, some prices will be negative.
    But it is important to make some manual sanity check if the numbers are reasonable.

Unsolvable matrices
-------------------

Not all square matrices can be inverted. They are **singular**.
For instance, when nobody has bought any bananas, we won't be able to figure out the price:

.. code:: python3

   F2 = np.array([
        [2, 0, 4, 2],
        [1, 0, 6, 4],
        [2, 0, 8, 8],
        [2, 0, 9, 4]])

   np.linalg.inv(F2)

This should result in an error without even looking at the prices.

Matrices are also singular when rows are **colinear** (multiples of each other):

.. code:: python3

   F3 = np.array([[3, 1, 50], [10, 10, 10], [20, 20, 20]])
   np.linalg.inv(F3)

Apply some changes to make these matrices invertible.

For many singular matrices it is not immediately obvious what exactly is making them singular.

Visualize the matrix
--------------------

To visualize the fruit baskets I recommend a grouped bar plot:

.. code:: python3

    import pandas as pd
    from matplotlib import pyplot as plt

    plt.figure(figsize=(4, 4))
    df = pd.DataFrame(F, columns=["apple", "banana", "cherry", "grapes"],
                      index=["Ada", "Bashir", "Choi", "Deryl"])
    df.plot.barh()
    plt.xlabel("fruit [kg]")

.. seealso::

   Linear Equations go much deeper. Here are some starting points:

   - The `Gurobi Burrito Optimization Game <https://www.gurobi.com/burrito-optimization-game/>`__ lets you explor more complex linear problems.
   - `PuLP <https://coin-or.github.io/pulp/>`__  is a free linear problem solver for Python.
   - `Gauss-Jordan Elimination on Wikipedia <https://en.wikipedia.org/wiki/Gaussian_elimination>`__

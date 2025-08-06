
Matrices
========

In this exercise, you continue using vectors to calculate the price of fruit baskets.
This time, you will need **matrices**.


Define a matrix containing a shopping list for two people.
Each row is a person, the columns are the fruit types (*apple, banana, cherry*).

.. code:: python3

   import numpy as np
   from matplotlib import pyplot as plt

   M = np.array([10, 2, 0], 
                [4, 7, 10])

Inspect the shape
-----------------

Inspect the shape, your most important debugging operation:

.. code:: python3

   M.shape

.. hint::

    Put this command under your pillow, really.
    When working with vectors and matrices in Python, you will need to inspect the shape before googling or doing anything else.
    While I was learning this line of work, 50% of my bugs had to do with wrong shapes.


Matrix arithmetics
------------------

Not too exciting, but you might want to try them out anyway:

.. code:: python3

   M + 10

   M * 5


Transposition
-------------

Swap the axes - note that this is not a rotation.

.. code:: python3

   M.transpose()
   M.transpose().shape


Multiplying matrices with vectors
---------------------------------

Which of the following dot products work?
Try them one by one and check the shapes to explain your observation

.. code:: python3

    prices = np.array([1.0, 0.5, 0.05])

    np.dot(M, prices)
    np.dot(prices, M)
    np.dot(M.transpose(), prices)
    np.dot(prices, M.transpose())


Create a matrix from two vectors
--------------------------------

Create a matrix from a row and column vector and plot it:

.. code:: python3

    a = np.arange(100)
    b = a.reshape(100, 1)
    c = a.reshape(1, 100)
    d = b * c
    print(d.shape)
    plt.imshow(d)

Useful phrases
--------------

.. code:: python3

   B = np.arange(6).reshape((3, 2))

Position-wise multiplication, if matrices have the same size:

.. code:: python3

   M * B

Create a random matrix:

.. code:: python3

   M = np.random.randint(low=0, high=5, size=(3, 4))

Plot a matrix:

.. code:: python3

   plt.imshow(M)


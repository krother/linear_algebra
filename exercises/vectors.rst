Vectors
=======

.. note::

   Run these exercises by copy-pasting the code into a Jupyter notebook or Google Colab.
   You can also use the notebook :download:`exercises_part1.ipynb`

IMAGE FRUIT BASKET

Create Vectors
--------------

Lets create a vector containing shopped fruit:

.. code:: python3

   import numpy as np
   from matplotlib import pyplot as plt

   # apples, bananas, cherries
   a = np.array([3, 1, 50])


Create a second vector that lists another shopping session for the same types of fruit in the same order

.. code:: python3

   b = ...


Add both fruit vectors together:

.. code:: python3

   fruit = a + b
   fruit

Scalar multiplication
---------------------

Now shop 10 times as much

.. code:: python3

   fruit = fruit * ...

Plot the vector:

.. code:: python3

   plt.bar(fruit)
   # plt.show()  # if not running in Jupyter


Position-wise multiplication
----------------------------
Define a set of fruit prices

.. code:: python3

   prices = np.array([1.0, 0.5, 0.05])

See how much each position costs

.. code:: python3

   fruit * prices

Dot product
-----------

The dot product calculates the total amount on the bill:

.. code:: python3

   np.dot(fruit, prices)


Cross Product
-------------

The cross product does not make much sense with fruit shopping.
Instead, define two *x, y, z* vectors:

.. code:: python3

   a = np.array([2, 0, 0])
   b = np.array([0, 1, 0])
   np.cross(a, b)

Check the following:

- what happens if you swap the arguments of the cross product?
- what happens if you calculate the cross products of a vector with itself?
- what happens if you calculate a dot product from a with the cross product of a and b?

Colinear and orthogonal vectors
-------------------------------

Which vectors are colinear, which are orthogonal?

.. code:: python3

   a = np.array([1, 2])
   b = np.array([-1, -2])
   c = np.array([2, 4])
   d = np.array([1, -2])
   e = np.array([-2, 1])

Useful NumPy phrases
--------------------

Create a large vector 

.. code:: python3

   a = np.arange(100)

Create a vector with interpolated numbers

.. code:: python3

   b = np.linspace(10, 20, 100)

Draw a parabola by filling the gaps:

.. code:: python3

   x = np.linspace(...)
   y = ...
   plt.plot(x, y)

Plot a random vector:

.. code:: python3

   v = np.random.normal(0, 10, 1000)
   plt.plot(v)

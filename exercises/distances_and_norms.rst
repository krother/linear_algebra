
Distances and Norms
===================

.. figure:: penguins.png

*Palmerpenguins Artwork by @allison_horst*

In this exercise you will compare vectors using three different methods.
You will calculate the length of vectors using **norms**, and the angle between two vectors using the **cosine similarity**.
We will do all this with a dataset of 333 penguins:

.. code:: python3

    import numpy as np
    import pandas as pd
    import seaborn as sns
    from matplotlib import pyplot as plt

    data = sns.load_dataset("penguins")
    data = data.dropna()  # remove missing values
    data.head()

    X = data[["body_mass_g", "flipper_length_mm", "bill_length_mm", "bill_depth_mm"]]

We store the numerical features in a matrix **X** for the following exercises.


L1 Norm or Manhattan Distance
-----------------------------

The L1 norm or Manhattan Distance sums up the difference along each axis:

.. math::
    
    ||\vec{a}||_1 = \sum_i |a_i|


The Python code below implements the Manhattan Distance as a reusable function:

.. code:: python3

    def manhattan_dist(a, b):
        return np.abs(a - b).sum()


To calculate the distance between the first and second penguin, use:

.. code:: python3

   manhattan_dist(X.values[0], X.values[1])


L2 Norm or Euclidean Distance
-----------------------------

The L2 norm squares the numbers before summing them up.
It is using the same logic as the Pythagorean theorem, only with potentially a lot more dimensions:

.. math::

    ||\vec{a}||_2 = \sqrt{\sum_i a_i^2}

You can use the Python function in an equivalent way:

.. code:: python3

    def euclidean_dist(a, b):
        return np.sqrt(((a - b) ** 2).sum())


Cosine similarity
-----------------

An alternative that works well in high-dimensional spaces is calculating the angle between the two vectors:

.. math::
    
    cos(\theta) = \frac{\vec{a} \cdot \vec{b}}{||\vec{a}||_2 \cdot ||\vec{b}||_2}

and in Python:

.. code:: python3

    def cosine_similarity(a, b):
        norma = np.sqrt((a ** 2).sum())
        normb = np.sqrt((b ** 2).sum())
        return np.dot(a, b) / (norma * normb)

.. note::

   The cosine function explains why the dot product is zero if two vectors are orthogonal.

Scaling
-------

When you try the cosine similarity function, you will notice that the cosine values are very close to 1 (almost identical).
Part of the reason is that the body mass of the penguins dominates the other numbers.
This problem also was present with the L1/L2 norm, but less dramatic.
Lets scale the data so that all columns have values between 0 and 1 (min-max-scaling):

.. math::

    x_{scaled} = \frac{x - min(x)} {max(x) - min(x)}


Fortunately NumPy and pandas make this very straightforward:

.. code:: python3

   Xscaled = (X - np.min(X, axis=0)) / (np.max(X, axis=0) - np.min(X, axis=0))


Now you should see a considerable difference between the first and 300th penguin:

.. code:: python3

   cosine_similarity(Xscaled.values[0], Xscaled.values[300])


Penguin search
--------------

You can use any of the norms and distances to find similar penguins in the dataset.
Here is a straightforward code sniplet:

.. code:: python3

    best_dist = 99999999999999999
    index = 0
    query = Xscaled.values[0]

    for i, pingu in enumerate(Xscaled.values):
        dist = manhattan_dist(query, pingu)
        if i > 0 and dist <= best_dist:
            best_dist = dist
            index = i

    print("best match:", data.iloc[index])


Check if the choice of metric leads to a different result.


Clustering
----------

A more interesting approach is to calculate the distances between **all** penguins.
This leads us to a new type of square matrix, the **distance matrix**.
It should have a shape of *(333, 333)* and contain the distances for each pair of penguins:

.. code:: python3

    dist_matrix = np.array([
        [
        euclidean_dist(p1, p2) 
        for p1 in Xscaled.values
        ]
        for p2 in Xscaled.values
    ])
    dist_matrix.shape

Inspecing the numbers in a distance matrix can be quite a pain, but they are fortunately easy to visualize.
Here, plot a **similarity matrix**, the exact opposite of the distance matrix:

.. code:: python3

    sim_matrix = 1 - dist_matrix
    sns.heatmap(sim_matrix, vmin=0.0, vmax=1.0)
    plt.xticks([], [])
    plt.yticks([], [])

How many groups of penguins do you see?


Optional: KMeans Clustering
---------------------------

The ``scikit-learn`` package contains many clustering algorithms, e.g. **k-Means**:

.. code:: python3

    m = KMeans(n_clusters=3).fit(Xscaled)
    clusters = m.predict(X)
    data["cluster"] = clusters.astype(str)

    plt.figure(figsize=(4, 4))
    sns.scatterplot(data=data, x="bill_length_mm", y="body_mass_g", hue="cluster")


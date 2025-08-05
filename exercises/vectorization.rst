
Vectorizing Data
================

.. figure:: convolution.png

**Convolutional operators applied to recognize horizontal and vertical lines.**

In this exercise, you will look at a few different ways to convert non-numerical data to vectors and matrices.


Categorical Columns
-------------------

On categorical data, **one-hot-encoding** or **dummy encoding** converts one column to binary columns.
On binary columns, all the usual linear algebra tools are applicable.


.. code:: python3

  import pandas as pd
  import seaborn as sns

  data = sns.load_dataset("penguins").dropna()
  
  pd.get_dummies(data["species"]).astype(int)

What is the size of the resulting data?


2D Convolution
--------------

.. figure:: con_face.png

**Convolution** is the fundamental operation that neural networks use to interpret pixel images.
During the past decade it has led to tremendous progress in the field of image recognition.
Convolution is based on sliding a 2D matrix (the kernel) over the image and calculating a dot product at each step.

The parameters of the kernel are typically trained as part of a neural network.

On `adamharley.com/nn_vis/cnn/3d.html <https://adamharley.com/nn_vis/cnn/3d.html>`__ you can see a convolutional neural network that recognizes digits in action. Switch all but the first layer off and observe the row of highlighted images when you draw a shape. Each of them represents the output of one convolutional kernel. What do the individual kernels recognize?


Word Embeddings
---------------

Go to `projector.tensorflow.org/ <https://projector.tensorflow.org/>`__ .
Type some common words into the search box and look for related words in the vector space.

Extensive training by a neural network is required to train vector embeddings for each word.
The size may differ, e.g.:

- word vectors around 2015 had a size of 50-300
- word vectors optimized for retrieving short text documents have a size of around 700
- word vectors in GPT-3 have a size of more than 12000.


Word Vectors in Spacy
---------------------

**Spacy** is a powerful language processing library. It contains embeddings for words and documents.
The installation involves a very big download:

.. code::

    pip install spacy
    spacy download en_core_web_lg


The following code example uses spacy to look up some word vectors from the downloaded model and calculates word similarities:

.. code:: python3

    import spacy
    import numpy as np

    nlp = spacy.load('en_core_web_lg')

    w1 = nlp("coffee")
    w2 = nlp("espresso")
    w3 = nlp("tea")
    w4 = nlp("giraffe")
    words = [w1, w2, w3, w4]

    print(w1.vector.shape)

    def l2_norm(a):
        return np.sqrt((a**2).sum())

    def cosim(a, b):
        return np.dot(a.vector, b.vector) / (l2_norm(a.vector) * l2_norm(b.vector))

    # all words against all
    for word1 in words:
        for word2 in words:
            similarity = cosim(word1, word2)
            print(f"{str(word1):10} {str(word2):10} {similarity:5.2f}")


.. seealso::

   - `Convolution with NumPy <https://www.academis.eu/numpy_graphics/convolution/README.html>`__
   - `Convolutional Neural Networks <https://www.academis.eu/machine_learning/deep_learning/convolutional_neural_networks/README.html>`__
   - `Spacy <https://spacy.io/>`__

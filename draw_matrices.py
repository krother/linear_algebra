
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

RESOLUTION = 1.0


def plot_matrix(a, filename):
    xsize = a.shape[1] * RESOLUTION
    ysize = a.shape[1] * RESOLUTION
    plt.figure(figsize=(xsize, ysize))
    sns.heatmap(a, annot=True, cbar=False, vmin=-1)
    plt.xticks([], [])
    plt.yticks([], [])
    plt.savefig(filename, dpi=300)


a = pd.DataFrame([[0, 1], [1, 0]], dtype=np.uint8)
plot_matrix(a, "rotate.png")

a = pd.DataFrame([[0, 0, 0], [0, 0, 0], [0, 0, 0]], dtype=np.uint8)
plot_matrix(a, "null.png")

a = pd.DataFrame([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=np.uint8)
plot_matrix(a, "identity.png")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap


def feature2d_to_polynomial(feature1, feature2, poly_degree):
    out = np.ones(len(feature1)).reshape(len(feature1), 1)
    for i in range(1, poly_degree + 1):
        for j in range(i + 1):
            terms = (feature1 ** (i - j) * feature2 ** j).reshape(len(feature1), 1)
            out = np.hstack((out, terms))
    return out


def plot_decision_regions_polynomials(X, y, classifier, test_idx=None, resolution=0.02,
                                      poly_degree=1, plotter=plt):
    # setup marker generator and color map
    X = feature2d_to_polynomial(X.iloc[:, 0].values, X.iloc[:, 1].values, poly_degree=poly_degree)
    markers = ("s", "x", "o", "^", "v")
    colors = ("red", "blue", "lightgreen", "gray", "cyan")
    cmap = ListedColormap(colors[:len(np.unique(y))])

    def mapFeaturePlot(x1, x2, degree):
        """
        take in numpy array of x1 and x2, return all polynomial terms up to the given degree
        """
        out = np.ones(1)
        for i in range(1, degree + 1):
            for j in range(i + 1):
                terms = (x1 ** (i - j) * x2 ** j)
                out = np.hstack((out, terms))
        return np.squeeze(out)

    w = classifier.coef_
    u_vals = np.linspace(np.min(X[:, 1]) - 1, np.max(X[:, 1]) + 1, 50)
    v_vals = np.linspace(np.min(X[:, 2]) - 1, np.max(X[:, 2]) + 1, 50)
    z = np.zeros((len(u_vals), len(v_vals)))
    for i in range(len(u_vals)):
        for j in range(len(v_vals)):
            z[i, j] = np.dot(w, mapFeaturePlot(u_vals[i], v_vals[j], degree=poly_degree))
    plt.contourf(u_vals, v_vals, z.T, 0, alpha=0.3, cmap=cmap)
    plt.xlabel("x1")
    plt.ylabel("x2")

    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 1], y=X[y == cl, 2],
                    alpha=0.8, c=colors[idx], marker=markers[idx],
                    label='B' if cl == 0 else 'A', edgecolor="black")

    # highlight test sample
    if test_idx:
        # plot all samples
        X_test, y_test = X[test_idx, :], y[test_idx]

        plt.scatter(X_test[:, 1], X_test[:, 2], c="", edgecolor="black",
                    alpha=1.0, linewidth=1, marker="o", s=100, label="test set")

    plt.legend(loc=0)

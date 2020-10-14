'''
@author : jhhalls
'''


import numpy as np
import matplotlib.pyplot as plt


def plot_group_kfold():
    from sklearn.model_selection import GroupKFold
    groups = [0, 0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 3]

    plt.figure(figsize=(10, 2))
    plt.title("GroupKFold")

    axes = plt.gca()
    axes.set_frame_on(False)

    n_folds = 12
    n_samples = 12
    n_iter = 3
    n_samples_per_fold = 1

    cv = GroupKFold(n_splits=3)
    mask = np.zeros((n_iter, n_samples))
    for i, (train, test) in enumerate(cv.split(range(12), groups=groups)):
        mask[i, train] = 1
        mask[i, test] = 2

    for i in range(n_folds):
        # test is grey
        colors = ["grey" if x == 2 else "white" for x in mask[:, i]]
        # not selected has no hatch

        boxes = axes.barh(y=range(n_iter), width=[1 - 0.1] * n_iter,
                          left=i * n_samples_per_fold, height=.6, color=colors,
                          hatch="//", edgecolor="k", align='edge')
        for j in np.where(mask[:, i] == 0)[0]:
            boxes[j].set_hatch("")

    axes.barh(y=[n_iter] * n_folds, width=[1 - 0.1] * n_folds,
              left=np.arange(n_folds) * n_samples_per_fold, height=.6,
              color="w", edgecolor='k', align="edge")

    for i in range(12):
        axes.text((i + .5) * n_samples_per_fold, 3.5, "%d" %
                  groups[i], horizontalalignment="center")

    axes.invert_yaxis()
    axes.set_xlim(0, n_samples + 1)
    axes.set_ylabel("CV iterations")
    axes.set_xlabel("Data points")
    axes.set_xticks(np.arange(n_samples) + .5)
    axes.set_xticklabels(np.arange(1, n_samples + 1))
    axes.set_yticks(np.arange(n_iter + 1) + .3)
    axes.set_yticklabels(
        ["Split %d" % x for x in range(1, n_iter + 1)] + ["Group"])
    plt.legend([boxes[0], boxes[1]], ["Training set", "Test set"], loc=(1, .3))
    plt.tight_layout()


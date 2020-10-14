'''
@author : jhhalls
'''

def plot_threefold_split():
    plt.figure(figsize=(15, 1))
    axis = plt.gca()
    bars = axis.barh([0, 0, 0], [11.9, 2.9, 4.9], left=[0, 12, 15], color=[
                     'white', 'grey', 'grey'], hatch="//", edgecolor='k',
                     align='edge')
    bars[2].set_hatch(r"")
    axis.set_yticks(())
    axis.set_frame_on(False)
    axis.set_ylim(-.1, .8)
    axis.set_xlim(-0.1, 20.1)
    axis.set_xticks([6, 13.3, 17.5])
    axis.set_xticklabels(["training set", "validation set",
                          "test set"], fontdict={'fontsize': 20})
    axis.tick_params(length=0, labeltop=True, labelbottom=False)
    axis.text(6, -.3, "Model fitting",
              fontdict={'fontsize': 13}, horizontalalignment="center")
    axis.text(13.3, -.3, "Parameter selection",
              fontdict={'fontsize': 13}, horizontalalignment="center")
    axis.text(17.5, -.3, "Evaluation",
              fontdict={'fontsize': 13}, horizontalalignment="center")

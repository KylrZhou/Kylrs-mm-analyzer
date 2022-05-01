import numpy as np
import matplotlib.pyplot as plt
def plotplot(data_dict):
    key_list = data_dict.keys()
    fig, ax = plt.subplots(1,1)
    ax.grid()
    for i in key_list:
        if i == 'epoch' or i == 'iter':
            x = data_dict[i]
            ax.set_xlabel(i)
        else:
            y = data_dict[i]
            ax.set_ylabel(i)

    ax.scatter(x, y)
    plt.show()
    return

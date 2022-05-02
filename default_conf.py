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
    try:
        data_dict.pop('epoch')
    except:
        data_dict.pop('iter')
    key_list = data_dict.keys()
    for i in key_list:
        ax.scatter(x, data_dict[i], label = i)
    ax.legend()
    plt.show()
    return

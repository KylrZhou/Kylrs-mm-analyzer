import numpy as np
import matplotlib.pyplot as plt
def line_parser(a):
    parsed = dict()
    a = ' '+a+' '
    parsed['l'] = ''
    parsed['f'] = ''
    for i in range(len(a)):
        if a[i].isalpha():
            if a[i+1].isalpha() or a[i-1].isalpha():
                parsed['l'] = parsed['l'] + a[i]
        elif a[i].isdigit():
            parsed['f'] = parsed['f'] + a[i]
    parsed['f'] = int(parsed['f'])
    return parsed
def set_analyzer(ax, set_dict):
    parsed = dict()
    parsed = line_parser(set_dict['title'])
    print(parsed)
    ax.set_title(parsed['l'], fontsize = parsed['f'])
    parsed = line_parser(set_dict['x'])
    print(parsed)
    ax.set_xlabel(parsed['l'], fontsize = parsed['f'])
    parsed = line_parser(set_dict['y'])
    print(parsed)
    ax.set_ylabel(parsed['l'], fontsize = parsed['f'])
    #return ax
def plotplot(data_dict, set_dict):
    fig, ax = plt.subplots(1,1)
    if set_dict != {}:
        set_analyzer(ax, set_dict)
    ax.grid()
    min_len = 10000
    max_epoch = -1
    for i in data_dict.keys():
        try:
            if data_dict[i]['epoch'].size < min_len:
                min_len = data_dict[i]['epoch'].size
        except:
            min_len = 10000

    if min_len != 10000:
        for i in data_dict.keys():
            if data_dict[i]['epoch'][min_len-1] > max_epoch:
                max_epoch = data_dict[i]['epoch'][min_len-1]

        for i in data_dict.keys():
            tmp = min_len
            while data_dict[i]['epoch'][tmp-1] < max_epoch:
                tmp += 1
            if data_dict[i]['epoch'][tmp-1] > max_epoch:
                tmp -= 1
            x = 0
            y = 0
            for j in data_dict[i].keys():
                if j == 'epoch':
                    x = data_dict[i][j][0:tmp]
                else:
                    y = data_dict[i][j][0:tmp]
                    ax.scatter(x, y, label = '['+i+']'+' '+j)
    ax.legend()
    plt.show()
    return

import numpy as np
import matplotlib.pyplot as plt
import math
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

def plottable(data_dict, set_dict):
    interval = set_dict['invl']
    f_name = dict()
    number = 0
    value_dict = dict()
    for filename, sub_dict in data_dict.items():
        value_dict[filename] = dict()
        number += 1
        for k, v in sub_dict.items():
            if(k != 'epoch' and k != 'iter'):
                f_name[filename] = k
        for i in range(sub_dict['epoch'].size):
            tmp = sub_dict['epoch'][i]
            value_dict[filename][str(tmp)] = sub_dict[f_name[filename]][i]
    max_epoch = -1
    min_len = 10000
    for filename, sub_dict in data_dict.items():
        if sub_dict['epoch'].size < min_len:
            min_len = sub_dict['epoch'].size
    for filename, sub_dict in data_dict.items():
        if sub_dict['epoch'][min_len-1] > max_epoch:
            max_epoch = sub_dict['epoch'][min_len-1]
    counts = 0
    epoch_list = []
    if interval == 1:
        while True:
            tmp = 0
            for filename, sub_dict in data_dict.items():
                #print(sub_dict['epoch'][counts])
                if  sub_dict['epoch'].size > counts and sub_dict['epoch'][counts] <= max_epoch:
                    epoch_list.append(sub_dict['epoch'][counts])
                else:
                    tmp += 1
                if tmp >= number:
                    break
            if tmp >= number:
                break
            counts += interval
    else:
        counts = interval-1
        while True:
            tmp = 0
            for filename, sub_dict in data_dict.items():
                if  sub_dict['epoch'].size > counts and sub_dict['epoch'][counts] <= max_epoch:
                    epoch_list.append(sub_dict['epoch'][counts])
                else:
                    tmp += 1
                if tmp >= number:
                    break
            if tmp >= number:
                break
            counts += interval
    epoch_list = list(set(epoch_list))
    epoch_list.sort()
    #for filename, sub_dict in data_dict.items():
    val_mat = np.zeros(shape=(number, len(epoch_list)))
    counts = 0
    for i in epoch_list:
        county = 0
        for k, v in f_name.items():
            try:
                val_mat[county,counts] = value_dict[k][str(i)]
            except:
                county = county
            county += 1
        counts += 1
    row_name = []
    for k, v in f_name.items():
        tmp = '['+k+']'+' '+v
        row_name.append(tmp)
    col_name = []
    for i in epoch_list:
        tmp = 'Epoch '+str(int(i))
        col_name.append(tmp)
    plt.figure(figsize=(4,4), dpi = 150)
    stp = 0
    tmp = 0
    counts = 15
    col_num = val_mat.shape
    col_num = col_num[1]
    table_number = len(epoch_list)/15
    table_number = math.ceil(table_number)
    table_serial = 1
    while stp != -1:
        if col_num > tmp:
            if col_num < counts:
                counts = col_num
                stp = -1
            plt.subplot(table_number, 1, table_serial)
            tab = plt.table(cellText = val_mat[:,tmp:counts],
                            colLabels = col_name[tmp:counts],
                            colWidths = [0.1] * (counts-tmp),
                            rowLabels = row_name,
                            loc = 'center',
                            cellLoc = 'center',
                            rowLoc = 'center')
            tab.auto_set_font_size(False)
            tab.set_fontsize(8)
            plt.axis('off')
            plt.tight_layout()
            counts += 15
            tmp += 15
            table_serial += 1
        else:
            break

    plt.show()
    return

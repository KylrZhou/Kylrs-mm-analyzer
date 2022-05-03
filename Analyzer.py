from itertools import islice
import numpy as np
global null
null = None
def Analyze(workdir):
    f = open(workdir, 'r')
    stat_pointer = 0
    train_key = dict()
    val_key = dict()
    for i in f:
        i = eval(i)
        md = next(iter(i))
        if md == "mode" and i[md] == 'train':
            del i['mode']
            counter = 1
            for j in i.keys():
                tmp = 't'+str(counter)
                train_key[tmp] = j
                counter += 1
        elif i[md] == 'val':
            del i['mode']
            counter = 1
            for j in i.keys():
                tmp = 'v'+str(counter)
                val_key[tmp] = j
                counter += 1
            break
        else:
            stat_pointer += 1
    data_dict = dict()
    data_dict = Input_Var(f, train_key, val_key)
    f.close()
    print(":::~DATA LOADED~:::")
    return data_dict

def Input_Var(f, train_key, val_key):
    f.seek(0,0)
    train_verse = dict()
    val_verse = dict()
    while True:
        print("Train:", ' ', end='')
        for k, v in train_key.items():
            train_verse[v] = k
            print(k, ')', ' ', v, '    ', end='',sep='')
        print('')
        print("Val:", ' ', end='')
        for k, v in val_key.items():
            val_verse[v] = k
            print(k, ')', ' ', v, '    ', end='',sep='')
        print('')
        print("Input the Key Value for Data to Process, Stop Using Command <#X> :")
        istrue = False
        epc_itr = "epoch"
        while True:
            print("  X-Axis: ",end='')
            ax_x = input()
            if ax_x == '#X':
                print("Program Stopped")
                return
            for k, v in train_key.items():
                if ax_x == k or ax_x == v:
                    istrue = True
                    break
            if istrue:
                try:
                    if ax_x == 'epoch':
                        ax_x = train_verse[ax_x]
                        break
                    elif train_key[ax_x] == 'epoch':
                        break
                except: istrue = True

                try:
                    if ax_x =='iter':
                        ax_x = train_verse[ax_x]
                        epc_itr = 'iter'
                        break
                    elif train_key[ax_x] == 'iter':
                        epc_itr = 'iter'
                        break
                except:
                    print("Only <epoch> and <iter> Are Supported for X-axis, Try Again:")
            else:
                for k, v in val_key.items():
                    if ax_x == k or ax_x == v:
                        istrue = True
                        break
                if istrue:
                    try:
                        if ax_x == 'epoch':
                            ax_x = val_verse[ax_x]
                            break
                        elif val_key[ax_x] == 'epoch':
                            break
                    except: istrue = True

                    try:
                        if ax_x =='iter':
                            ax_x = val_verse[ax_x]
                            epc_itr = 'iter'
                            break
                        elif val_key[ax_x] == 'iter':
                            epc_itr = 'iter'
                            break
                    except:
                        print("Only <epoch> and <iter> Are Supported for X-axis, Try Again:")
                else:
                    print("False Input, Try Again:")
        istrue = False
        while True:
            print("  Y-Axis: ",end='')
            ax_y = input()
            if ax_y == '#X':
                print("Program Stopped")
                return
            for k, v in train_key.items():
                if ax_y == k:
                    istrue = True
                    break
                elif ax_y == v:
                    ax_y = train_verse[ax_y]
                    istrue = True
                    break
            if istrue:
                break
            else:
                for k, v in val_key.items():
                    if ax_y == k:
                        istrue = True
                        break
                    elif ax_y == v:
                        ax_y = val_verse[ax_y]
                        istrue = True
                        break
                if istrue:
                    break
                else:
                    print("False Input, Try Again:")
        data_dict = dict()
        MODE = 'train'
        if  ax_x in train_key.keys():
            ax_x = train_key[ax_x]
            ax_y = train_key[ax_y]
            data_dict[ax_x] = []
            data_dict[ax_y] = []
            key_list = data_dict.keys()
            fstline = f.readline()
            if epc_itr == 'epoch':
                sndline = f.readline()
                sndline = eval(sndline)
                for i in key_list:
                    data_dict[i].append(sndline[i])
                eph = 0
                counts = 1
                for line in f:
                    line = eval(line)
                    if line['mode'] == MODE:
                        if line['epoch']-1 == eph:
                            counts += 1
                            for i in key_list:
                                data_dict[i][eph] += line[i]
                        else:
                            for i in key_list:
                                data_dict[i][eph] /= counts
                                data_dict[i][eph] = round(data_dict[i][eph], 5)
                                data_dict[i].append(line[i])
                            eph += 1
                            counts = 1
                for i in key_list:
                    data_dict[i][eph] /= counts
                    data_dict[i][eph] = round(data_dict[i][eph], 5)
            elif epc_itr == 'iter':
                counts = 0
                key_list = list(key_list)
                for i in key_list:
                    if i == 'iter':
                        break
                    else:
                        counts += 1
                key_list.pop(counts)
                counts = 1
                for line in f:
                    line = eval(line)
                    if line['mode'] == MODE:
                        for i in key_list:
                            data_dict[i].append(line[i])
                        data_dict['iter'].append(round(counts, 5))
                        counts += 1
        elif ax_x in val_key.keys():
            MODE = 'val'
            ax_x = val_key[ax_x]
            ax_y = val_key[ax_y]
            data_dict[ax_x] = []
            data_dict[ax_y] = []
            key_list = data_dict.keys()
            counts = 0
            fstline = f.readline()
            for line in f:
                line = eval(line)
                if line['mode'] == MODE:
                    for i in key_list:
                        data_dict[i].append(line[i])

        key_list = data_dict.keys()
        for i in key_list:
            data_dict[i] = np.array(data_dict[i])
        return data_dict

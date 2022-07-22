def Json2DFconverter(file_name):
    import json
    import seaborn as sns
    import pandas as pd
    import matplotlib.pyplot as plt

#open file
    f = open(file_name,'r')

#create val data dict
    val = {}
    val['AP'] = []
    val['AP .5'] = []
    val['AP .75'] = []
    val['AP (M)'] = []
    val['AP (L)'] = []
    val['AR'] = []
    val['AR .5'] = []
    val['AR .75'] = []
    val['AR (M)'] = []
    val['AR (L)'] = []

#if file has env-info data
    firstline = f.readline()
    firstline = json.loads(firstline)
    try:
        firstline['env_info']
        firstline = f.readline()
        firstline = json.loads(firstline)
        f.seek(0,0)
        f.readline()
    except:
        f.seek(0,0)

#acquire all the variables
    firstline.pop('mode')
    firstline.pop('epoch')
    firstline.pop('iter')
    firstline.pop('lr')
    firstline.pop('memory')
    firstline.pop('data_time')
    firstline.pop('time')
    vari = {}
    vari_name = []
    for k,v in firstline.items():
        vari[k] = [0]
        vari_name.append(k)
    del firstline,k,v

#fill data dict
    counter = 0
    epoch = 1
    while True:
        line = f.readline()
        try:
            line = json.loads(line)
            if line['mode'] == 'train':
                if line['epoch'] == epoch:
                    counter += 1
                    for i in vari_name:
                        vari[i][epoch-1] += line[i]
                else:
                    for i in vari_name:
                        vari[i][epoch-1] /= counter
                        vari[i][epoch - 1] = round(vari[i][epoch - 1],5)
                        vari[i].append(line[i])
                    counter = 1
                    epoch += 1
            else:
                val['AP'].append(line['AP'])
                val['AP .5'].append(line['AP .5'])
                val['AP .75'].append(line['AP .75'])
                val['AP (M)'].append(line['AP (M)'])
                val['AP (L)'].append(line['AP (L)'])
                val['AR'].append(line['AR'])
                val['AR .5'].append(line['AR .5'])
                val['AR .75'].append(line['AR .75'])
                val['AR (M)'].append(line['AR (M)'])
                val['AR (L)'].append(line['AR (L)'])
        except:
            break
    f.close()
    for i in vari_name:
        vari[i][epoch - 1] /= counter
        vari[i][epoch - 1] = round(vari[i][epoch - 1], 5)

#convert data to DataFrame
    vari = pd.DataFrame(vari)
    val = pd.DataFrame(val)
    del counter,epoch,f,i,json,line,pd,vari_name,
    return val,vari
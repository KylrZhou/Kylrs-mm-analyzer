def Concat(target, tmp):
    if target == {}:
        target = tmp
    else:
        tar_key = target.keys()
        tmp_key = tmp.keys()
        x_exist = False
        for i in tar_key:
            if i == 'epoch':
                for j in tmp_key:
                    if j == 'epoch':
                        x_exist = True
                        break
                break
            else:
                print("ERROR: There Is a not <epoch> X")
                return
        if len(target['epoch']) < len(tmp['epoch']):
            min_len = len(target['epoch'])
            for i in tmp_key:
                tmp[i] = tmp[i][0:min_len]
        elif len(target['epoch']) > len(tmp['epoch']):
            min_len = len(tmp['epoch'])
            for i in tar_key:
                tar[i] = tar[i][0:min_len]
        else:
            min_len = len(target['epoch'])
        tmp.pop('epoch')
        for i in tmp_key:
            target[i] = tmp[i]
    return target

def Set_printer():
    dic = dict()
    print(">>> Input the Title of Graph:")
    print(">>> ",end='')
    tmp = input()
    if tmp != '':
        dic['title'] = tmp
    print(">>> Input the Label of X-axis:")
    print(">>> ",end='')
    tmp = input()
    if tmp != '':
        dic['x'] = tmp
    print(">>> Input the Label of Y-axis:")
    print(">>> ",end='')
    tmp = input()
    if tmp != '':
        dic['y'] = tmp
    return dic

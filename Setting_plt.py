def Set_printer():
    dic = dict()
    print(">>> Input Plot Types (Outputs Coordinates Diagram by Default)")
    print(">>> Input C for Coordinates Diagram, T for Table:")
    while True:
        print(">>> ",end='')
        tmp = input()
        if tmp == 'T':
            print(">>> Input Sample Interval (Default: 1):")
            print(">>>",end='')
            tmp = input()
            if tmp == '':
                tmp = 1
            else:
                tmp = int(tmp)
            dic['invl'] = tmp
            print(">>> Input y to SWAP X and Y Axis or n Not to (Default: n):")
            print(">>> ",end='')
            tmp = input()
            if tmp == '':
                tmp = 'n'
            elif tmp == 'Y':
                tmp = 'y'
            elif tmp == 'N':
                tmp = 'n'
            dic['swap'] = tmp
            return dic, 'T'
        elif tmp == 'C' or '':
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
            return dic, 'C'
        else:
            print("Input ERROR, Try Again:")

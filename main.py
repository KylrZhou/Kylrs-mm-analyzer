from Logo import Logo
from Analyzer import Analyze
from default_conf import plotplot, plottable
from Setting_plt import Set_printer
from os import listdir, access
from os.path import exists
import os
filedir = os.path.abspath(os.path.dirname(__file__)) + '/'
def clear():
    os.system('clear')
def set_workdir():
    if exists(filedir + 'workdir.txt'):
        f = open(filedir + 'workdir.txt','r')
        workdir = f.readline()
        f.close()
        if workdir != '':
            print("Original Workdir is <",workdir,'>',sep = '')
        else:
            print("No Default Workdir")
    else:
        print("No Default Workdir")
    print("Input Your Workdir:")
    print(">>>",end = '')
    workdir = input()
    f = open(filedir + 'workdir.txt','w')
    if workdir != '':
        if workdir[-1] == '/':
            workdir = workdir
        else:
            workdir = workdir + '/'
        f.write(workdir)
    f.close()
    return workdir

clear()
Logo()
data_dict = dict()
tmp_dict = dict()
print("")
try:
    f = open(filedir + 'workdir.txt','r')
    workdir = f.readline()
except:
    workdir = set_workdir()
    clear()
    Logo()
print("<", workdir[0:-1], ">")
print("  Enter:")
print("    ~ !D to Change Default Work Dir")
print("    ~ !A to Start Analyze Mode")
print("    ~ #X to Exit")
print(">>>", end = '')
Fpath = input()
while Fpath != "#X":
    if Fpath == "!D":
        clear()
        Logo()
        print('')
        set_workdir()
        clear()
        Logo()
        print('')
        print("<", workdir[0:-1], ">")
        print("  Enter:")
        print("    ~ !D to Change Default Work Dir")
        print("    ~ !A to Start Analyze Mode")
        print("    ~ #X to Exit")
        print(">>>", end = '')
        Fpath = input()
        continue

    elif Fpath == "!A":
        while Fpath != "#X" and Fpath != "!S":
            clear()
            Logo()
            print('')
            print("Input the Serial Number or Address of the JSON File to Be Analyzed")
            filels = listdir(workdir)
            for i in range(0,len(filels),4):
                print("  ", sep='', end='')
                for j in range(4):
                    if i+j < len(filels):
                        tmp = str(i+1+j) + ")" + ' ' + filels[i+j]
                        print('{:<35}'.format(tmp), sep = '', end='')
                    else:
                        break
                print('')
            while True:
                print(">>> ",end='')
                Fpath = input()
                if Fpath.isdigit():
                    filename = filels[int(Fpath)-1]
                    Fpath = workdir + '/' + filels[int(Fpath)-1]
                else:
                    if exists(Fpath) == False:
                        filename = Fpath
                        Fpath = workdir + '/' + Fpath
                        if exists(Fpath) == False:
                            print("Given File Does Not Exist, Input Again:")
                            continue
                    if access(Fpath, mode = os.R_OK) == False:
                        print("Given File Does Not Accessable, Input Again:")
                        continue
                break
            clear()
            Logo()
            print('')
            counts = 0
            for i in filename:
                if i == '.':
                    break
                else:
                    counts += 1
            filename = filename[0:counts]
            tmp_dict = Analyze(Fpath)      #if the same file name exists in and out of the default path, we will process the one in the default pass first.
            #data_dict = Concat(data_dict, tmp_dict)
            data_dict[filename] = tmp_dict
            tmp_dict = dict()
            print("Enter Any Character to Add Data Or Use Command <#X> to Plot Selected Data Or Use Command <!S> to Set Matplotlib Attributes:  ")
            print(">>> ",end='')
            Fpath = input()
            clear()
            Logo()
            print('')
        else:
            continue
    set_dict = dict()
    plot_mode = 'C'
    if Fpath == "!S":
        set_dict, plot_mode = Set_printer()
    if plot_mode == 'C' or '':
        plotplot(data_dict, set_dict)
    elif plot_mode == 'T':
        plottable(data_dict, set_dict)
    set_dict = dict()
    data_dict = dict()
    clear()
    Logo()
    print('')
    print("  Enter:")
    print("    ~ !D to Change Your Default Work Dir")
    print("    ~ !A to Start Analyze Mode")
    print("    ~ #X to Exit")
    print(">>>", end = '')
    Fpath = input()

from Logo import Paint_Logo
from Analyzer import Analyze
from default_conf import plotplot
from os import listdir, access
from os.path import exists
import os
Paint_Logo()
workdir = "/home/kylrzhou/Documents/ExperimentResults"
homedir = '/home/kylrzhou'
data_dict = dict()
print("")
print("<", workdir, ">")
print(":::~ Enter:")
print("::::::::::~ !D to Change Your Default Workd Dir")
print("::::::::::~ !S to Enter Setting Mode")
print("::::::::::~ !A to Start Analyze Mode")
print("::::::::::~ #X to Exit")
Fpath = input()
while Fpath != "#X":
    if Fpath == "!D":
        print("Directory Changing")

    elif Fpath == "!S":
        print("Setting Mode Started")

    elif Fpath == "!A":
        print("Input the Serial Number or Address of the JSON File to Be Analyzed")
        filels = listdir(workdir)
        for i in range(len(filels)):
            print(i+1, ")", ' ', filels[i], sep = '', end = '    ')
        print('')
        while True:
            Fpath = input()
            if Fpath.isdigit():
                Fpath = workdir + '/' + filels[int(Fpath)-1]
            else:
                if exists(Fpath) == False:
                    Fpath = workdir + '/' + Fpath
                    if exists(Fpath) == False:
                        print("Given File Does Not Exist, Input Again:")
                        continue
                if access(Fpath, mode = os.R_OK) == False:
                    print("Given File Does Not Accessable, Input Again:")
                    continue
            break
        data_dict = Analyze(Fpath)      #if the same file name exists in and out of the default path, we will process the one in the default pass first.
        plotplot(data_dict)
    print(":::~ Enter:")
    print("::::::::::~ !D to Change Your Default Workd Dir")
    print("::::::::::~ !S to Enter Setting Mode")
    print("::::::::::~ !A to Start Analyze Mode")
    print("::::::::::~ #X to Exit")
    Fpath = input()

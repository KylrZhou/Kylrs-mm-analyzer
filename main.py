from Logo import Paint_Logo
from Analyzer import Analyze
from os import listdir, access
from os.path import exists
import os
Paint_Logo()
workdir = "/home/kylrzhou/Documents/ExperimentResults"
homedir = '/home/kylrzhou'
print("")
print("<", workdir, ">")
print("Input the Address of the JSON File to Be Analyzed (Or Input !S to Enter Setup Mode):")
Fpath = input()
while Fpath != "#X":
    if Fpath == "!D":
        print("Directory Changing")

    elif Fpath == "!S":
        print("Setting Mode Started")

    elif Fpath == "!A":
        print("Analysis Mode Started")
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
            print(Fpath)
            Analyze(Fpath)
            break
        #print("Fpath Recived")
        Analyze(Fpath)      #if the same file name exists in and out of the default path, we will process the one in the default pass first.
    Fpath = input()

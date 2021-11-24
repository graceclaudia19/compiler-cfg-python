from algorithm.convertcfg import *
from algorithm.parsing import *
from algorithm.cyk import *
import argparse
import sys
import os

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid input. Try typing 'python main.py <filename>.py'\n")
        sys.exit(1)
    parser = argparse.ArgumentParser()
    parser.add_argument("pythonfile")
    args = parser.parse_args()

    filename = args.pythonfile

    # CFG TO CNF
    convertCFG(os.getcwd() + '\grammar\CFG.txt')
    cnfInput = os.getcwd() + '\grammar\CNF.txt'

    # CNF PARSINNG
    # terminate (returning empty list) if invalid varname or invalid use of ticks (' and "),
    # if all valid, it will return array and proceed to cyk algorithm

    valid = True
    while (valid):
        file = filename
        list = pyToStr(file)
        # check before parse process
        # print(list)
        
        list2 = removeCommentHashtag(list)

        list3 = removeMultilineComment(list2)


        qMarksTwo = True
        list4 = strCheckDoubleTick(list3)
        if (list4 == '.'):
            valid = False
            qMarksTwo = False
            break

        qMarksOne = True
        list5 = strCheckOneTick2(list4)
        if (list5 == '.'):
            valid = False
            qMarksOne = False
            break
        
        varCheck = True

        gram = grammarParse(cnfInput) 

        # print(list5)
        strcyk = checkNumVar(list5, gram)
        if (list5 == '.'):
            valid = False
            varCheck = False
            break
    
        # print(strcyk)
        break

    # check after parse
    # buat cek yang ganti ''
    # print(list1) 
    # buat cek yang ganti ""
    # print(list2) 
    # print(strcyk) -> buat cek yg ganti number sm var

    # CYK ALGORITHM
    if (valid) and states(filename):
        cykInput = strcyk
        if cykInput == []:
            print("Accepted")
        else:
            table = cykalgo(gram, cykInput)
            # displayMatrix(table)
            top = table[len(cykInput)][0]
            acc = False
            for i in top:
                if i == 'MAIN_STATES':
                    acc = True
                    break
            if (acc):
                print("Accepted")
            else:
                print("Not accepted")
    else:
        print("Not accepted")
        # if not(qMarksOne):
        #     print('Invalid use of symbol " ') 
        # elif not (qMarksTwo):
        #     print("Invalid use of symbol ' ")
        # elif not (varCheck):
        #     print("Invalid variable name")



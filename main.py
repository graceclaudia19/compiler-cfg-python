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

    # CNF PARSING

    valid = True
    while (valid):
        file = filename
        list = pyToStr(file)
        
        list2 = removeCommentHashtag(list)

        list3 = removeMultilineComment(list2)


        list4 = strCheckDoubleTick(list3)
        if (list4 == '.'):
            valid = False
            break

        list5 = strCheckOneTick2(list4)
        if (list5 == '.'):
            valid = False
            break
        

        gram = grammarParse(cnfInput) 

        strcyk = checkNumVar(list5, gram)
        if (list5 == '.'):
            valid = False
            break
        break

    # CYK ALGORITHM
    if (valid) and states(filename):
        cykInput = strcyk
        if cykInput == []:
            print("Accepted")
        else:
            table = cykalgo(gram, cykInput)
            top = table[len(cykInput)][0]
            acc = False
            for i in top:
                if i == 'MAIN_STATES':
                    acc = True
                    break
            if (acc):
                print("Accepted")
            else:
                print("Syntax Error")
    else:
        print("Syntax Error")

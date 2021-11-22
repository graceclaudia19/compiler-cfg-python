from parsing import *
from cyk import *

# CFG TO CNF
#TARO ALGO AZKA DISINI GW GA NGERTI IMPORT2NYA DLL
# taro di var namanya cnfinput ok? sementara cnf inputnya w txt dl
cnfInput = "CNF.txt"

# CNF PARSINNG
# terminate (returning empty list) if invalid varname or invalid use of ticks (' and "),
# if all valid, it will return array and proceed to cyk algorithm
valid = True
filename = input("Masukkan nama file yang akan dicek dalam .txt/.py: ")
while (valid):
    file = "function.py"
    list = pyToStr(file)
    # check before parse process
    # print(list)

    qMarksOne = True
    list1 = strCheckOneTick(list)
    if (list1 == []):
        valid = False
        qMarksOne = False
        break

    qMarksTwo = True
    list2 = strCheckTwoTick(list1)
    if (list2 == []):
        valid = False
        qMarksTwo = False
        break

    varCheck = True
    gram = grammarParse(cnfInput) 
    strcyk = strCheckNumVar(list2, gram)
    if (strcyk == []):
        valid = False
        varCheck = False
        break
    break

# check after parse
# print(list1) -> buat cek yang ganti ''
# print(list2) -> buat cek yang ganti ""
# print(strcyk) -> buat cek yg ganti number sm var

# CYK ALGORITHM
if (valid):
    cykInput = mergeList(strcyk)
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
    if not(qMarksOne):
        print("Invalid use of symbol ' ")
    elif not (qMarksTwo):
        print('Invalid use of symbol " ')
    elif not (varCheck):
        print("Invalid variable name")



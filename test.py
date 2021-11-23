# # ITS GC PLAYSPACE GABOLEH DI DELET AWAS LO SMUA GUE DELET CYK.PY KALO ADAD YG DELETE!!! MAU LU HA
# def removeCommentHashtag(list):
#     el = 0
#     while el < len(list):
#         if list[el][0] == "#":
#             list.pop(el)

#         else:
#             pop = False
#             i = 0
#             while i < len(list[el]):
#                 if list[el][i] == "#":
#                     pop = True 
#                 if pop:
#                     list[el].pop(i)
#                 else:
#                     i+=1
#             el+=1

#     return list

# def mergeList(list):
#     l = []
#     for i in range (len(list)): 
#         l+=list[i]
#     return l

# def removeMultilineComment(list):
#     l = mergeList(list)
#     i = 0 
#     ticks = False
#     while i < len(l)-3 :
#         if l[i]=="'" and l[i+1]=="'" and l[i+2]=="'":
#             ticks = not ticks
#         if not ticks and l[i]=="'":
#             l.pop(i+2)
#             l.pop(i+1)
#             l.pop(i)
#         if ticks:
#             l.pop(i)
#         else:
#             i+=1
#     return l


# def pyToStr(file):
#     with open(file) as f:
#         lines = f.readlines()
#         element = []
#         symbols = ['(', ')','[',']','{','}','+','-','*',':','/', '>','<' ,'"',"'",',','.','%','=','!','#']
#         for line in lines:
#             #mereplace string dri beberapa symbol agar dapat di split dengan space 
#             for symbol in symbols:
#                 line = line.replace(symbol, " "+symbol+" ")
#             line = line.split()
#             element.append(line)
#         return element
# x = pyToStr('function.py')
# print(x)
# y = removeCommentHashtag(x)
# print(removeMultilineComment(y))

from cyk import grammarParse
from parsing import mergeList


def check_value_grammar(gramParsed, value):
    exist = False
    for key, values in gramParsed.items():
        for val in values:
            if val == value:
                exist = True
    return exist

def varChecker(varName):
    # pengecekan huruf pertama dari nama variabel (hanya boleh huruf dan _ )
    if (varName[0] == '_' or (ord(varName[0])>65 and ord(varName[0])<122)):
        for i in range (1,len(varName)):
             # pengecekan sisa hurruf selain huruf pertama dari nama variabel menggunakan ascii value (hanya boleh huruf, _, dan angka )
            if not (varName[i]== "_" or (ord(varName[0])<=65) or (ord(varName[0])>=122) or (ord(varName[0])<=57) or (ord(varName[0])>=48)):
                return False
        return True
    return False

def checkNumVar(list, gram):
    idx = 0
    for i in list:
        if not (check_value_grammar(gram, i)):
            isInt = True 
            try:
                int(i)
            except:
                isInt = False
            if (isInt):
                list[idx] = "num"
            else:
                if (varChecker(list[idx])):
                    list[idx] = "word"
                else:
                    print(i)
                    return []
        idx+=1
    return list

def grammarParse(grammar):
    gram = {}
    with open(grammar) as f:
        lines = f.readlines()
        for line in lines:
            line = line.split('->')
            if (line[0].strip() in gram.keys()):
                gram[line[0].strip()] += [line[1].replace('\n','').strip()]
            else:
                gram[line[0].strip()] = [line[1].replace('\n','').strip()]
    return gram

def pyToStr(file):
    with open(file) as f:
        lines = f.readlines()
        element = []
        symbols = ['(', ')','[',']','{','}','+','-','*',':','/', '>','<' ,'"',"'",',','.','%','=','!','#',';']
        for line in lines:
            #mereplace string dri beberapa symbol agar dapat di split dengan space 
            for symbol in symbols:
                line = line.replace(symbol, " "+symbol+" ")
            line = line.split()
            element.append(line)
        return element

def mergeList(list):
    l = []
    for i in range (len(list)): 
        l+=list[i]
    return l

x = pyToStr('function.py')
gram = grammarParse('CNF.txt')
print(x)
y = mergeList(x)
print(checkNumVar(y, gram))


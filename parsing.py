from cyk import grammarParse 

#FUNCTION PENGECEKAN NAMA VARIABEL
def varChecker(varName):
    # pengecekan huruf pertama dari nama variabel (hanya boleh huruf dan _ )
    if (varName[0] == '_' or (ord(varName[0])>65 and ord(varName[0])<122)):
        for i in range (1,len(varName)):
             # pengecekan sisa hurruf selain huruf pertama dari nama variabel menggunakan ascii value (hanya boleh huruf, _, dan angka )
            if not (varName[i]== "_" or (ord(varName[0])<=65) or (ord(varName[0])>=122) or (ord(varName[0])<=57) or (ord(varName[0])>=48)):
                return False
        return True
    return False

def check_value_grammar(gramParsed, value):
    exist = False
    for key, values in gramParsed.items():
        for val in values:
            if val == value:
                exist = True
    return exist

def get_key(gramParsed, value, elementM):
    for key, values in gramParsed.items():
        for val in values:
            if val == value:
                if key not in elementM:
                    elementM.append(key)
    return elementM

#FUNCTION PENGUBAHAN PYTHON KE STRING
def pyToStr(file):
    with open(file) as f:
        lines = f.readlines()
        element = []
        symbols = ['(', ')','[',']','{','}','+','-','*',':','/', '>','<' ,'"',"'",',','.','%','=','!','#']
        for line in lines:
            #mereplace string dri beberapa symbol agar dapat di split dengan space 
            for symbol in symbols:
                line = line.replace(symbol, " "+symbol+" ")
            line = line.split()
            element.append(line)
        return element

#check ' trus ganti jd word
def strCheckOneTick(list):
    ticks = False
    l = []
    for el in list:
        li = []
        for i in el:
            if i == "'":
                ticks = not ticks
                li.append(i)
                if ticks:
                    li.append("word")
            elif ticks:
                pass
            else:
                li.append(i)
        l.append(li)
    if (ticks):
        l = []
    return l

            

#check " trus ganti jd word
def strCheckTwoTick(list):
    ticks = False
    l = []
    for el in list:
        li = []
        for i in el:
            if i == '"':
                ticks = not ticks
                li.append(i)
                if ticks:
                    li.append("word")
            elif ticks:
                pass
            else:
                li.append(i)
        l.append(li)
    if (ticks):
        l = []
    return l


def strCheckNumVar(list, gram):
    idxArr = 0
    for el in list:
        idx = 0
        for i in el:
            #untuk string
            if not (check_value_grammar(gram, i)):
                #untuk num
                isInt = True
                try:
                    int(i)
                except ValueError:
                    isInt = False
                if (isInt):
                    list[idxArr][idx] = "num"
                #untuk nama variabel
                else:
                    if (varChecker(list[idxArr][idx])):
                        list[idxArr][idx] = "word"
                    else:
                        return []
                        
            idx+=1
        idxArr+=1
    return list

                

        

# KALO DIA GAGAL DI SATU TEMPAT DIA LANGSUNG KEMBALIIN LIST KOSONG -> END PROGRAM DI MAIN

file = "function.py"
list = pyToStr(file)

print("original list")
print(list)

print("list without ' ")
list1 = strCheckOneTick(list)
print(list1)

print('list without " ')
list2 = strCheckTwoTick(list1)
print(list2)

gram = grammarParse('CNF.txt') 
strcyk = strCheckNumVar(list2, gram)
print(strcyk)



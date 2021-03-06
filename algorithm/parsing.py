from algorithm.cyk import grammarParse 

#FUNCTION PENGECEKAN NAMA VARIABEL
def varChecker(varName):
    # pengecekan huruf pertama dari nama variabel (hanya boleh huruf dan _ )
    if (varName[0] == '_' or (ord(varName[0])>=65 and ord(varName[0])<= 90) or (ord(varName[0]) >= 97 and ord(varName[0]) <= 122)):
        for i in range (1,len(varName)):
             # pengecekan sisa hurruf selain huruf pertama dari nama variabel menggunakan ascii value (hanya boleh huruf, _, dan angka )
            if not (varName[i] == '_' or (ord(varName[i]) >= 48 and ord(varName[i]) <= 57) or (ord(varName[i])>=65 and ord(varName[i])<= 90) or (ord(varName[i]) >= 97 and ord(varName[i]) <= 122)):
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
def strCheckOneTick2(list):
    ticks = False
    li = []
    for i in list:
        if i == "'":
            ticks = not ticks
            li.append(i)
            if ticks:
                li.append("word")
        elif ticks:
            pass
        else:
            li.append(i)
    if (ticks):
        li = '.'
    return li

            

#check " trus ganti jd word
def strCheckDoubleTick(list):
    ticks = False
    li = []
    for i in list:
        if i == '"':
            ticks = not ticks
            li.append(i)
            if ticks:
                li.append("word")
        elif ticks:
            pass
        else:
            li.append(i)
    if (ticks):
        li = '.'
    return li

def mergeList(list):
    l = []
    for i in range (len(list)): 
        l+=list[i]
    return l

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
                    return '.'
        idx+=1
    return list

    
def removeCommentHashtag(list):
    el = 0
    while el < len(list):
        pop = False
        i = 0
        while i < len(list[el]):
            if list[el][i] == "#":
                pop = True 
            if pop:
                list[el].pop(i)
            else:
                i+=1
        el+=1

    return list

def removeMultilineComment(list):
    l = mergeList(list)
    i = 0 
    ticks = False
    l += [".", ".", ".", "."]
    while i < len(l)-4 :
        if l[i]=="'" and l[i+1]=="'" and l[i+2]=="'" and l[i+3] != "'":
            ticks = not ticks
            l.pop(i+2)
            l.pop(i+1)
            l.pop(i)
        if ticks:
            l.pop(i)
        else:
            i+=1
    l.pop()
    l.pop()
    l.pop()
    l.pop()
    return l

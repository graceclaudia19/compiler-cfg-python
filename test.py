# ITS GC PLAYSPACE GABOLEH DI DELET AWAS LO SMUA GUE DELET CYK.PY KALO ADAD YG DELETE!!! MAU LU HA
def removeCommentHashtag(list):
    el = 0
    while el < len(list):
        if list[el][0] == "#":
            list.pop(el)

        else:
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

def mergeList(list):
    l = []
    for i in range (len(list)): 
        l+=list[i]
    return l

def removeMultilineComment(list):
    l = mergeList(list)
    i = 0 
    ticks = False
    while i < len(l)-3 :
        if l[i]=="'" and l[i+1]=="'" and l[i+2]=="'":
            ticks = not ticks
        if not ticks and l[i]=="'":
            l.pop(i+2)
            l.pop(i+1)
            l.pop(i)
        if ticks:
            l.pop(i)
        else:
            i+=1
    return l


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
x = pyToStr('function.py')
print(x)
y = removeCommentHashtag(x)
print(removeMultilineComment(y))
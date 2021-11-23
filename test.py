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
print(removeCommentHashtag(x))
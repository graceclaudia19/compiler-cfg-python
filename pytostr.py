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


# file = 'function.py'
# print(pyToStr(file))
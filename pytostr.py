def pyToStr(file):
    with open(file) as f:
        lines = f.readlines()
        element = []
        for line in lines:
            #mereplace string dri beberapa symbol agar dapat di split dengan space 
            line = line.replace('(',' ( ')
            line = line.replace(')',' ) ')
            line = line.replace('[',' [ ')
            line = line.replace(']',' ] ')
            line = line.replace('+',' + ')
            line = line.replace('-',' - ')
            line = line.replace('*',' * ')
            line = line.replace(':',' : ')
            line = line.replace('/',' / ')
            line = line.replace('>',' > ')
            line = line.replace('<',' < ')
            line = line.replace('"',' " ')
            line = line.replace("'"," ' ")
            line = line.replace(',',' , ')
            line = line.replace('.',' . ')
            line = line.replace('%',' % ')
            line = line.replace('=',' = ')
            line = line.split()
            element.append(line)
        return element

file = 'function.txt'
print(pyToStr(file))


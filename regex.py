import re
from parsing import pyToStr, mergeList



def regex(file):
    result = ''
    f = open(file,'r')
    for line in f.readlines():
        result += line
    result = '\n' + result

    f.close()

    def removeComments(string):
        string = re.sub(re.compile('[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',re.DOTALL ) ,"" ,string) # remove all occurrences streamed comments (/*COMMENT */) from string
        string = re.sub(re.compile('[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',re.DOTALL ) ,"" ,string)
        string = re.sub(re.compile("#.*?\n" ) ,"" ,string) # remove all occurrence single-line comments (//COMMENT\n ) from string
        return string
        
    with open('temp.txt','w') as file:
        file.write(removeComments(result))
    return mergeList(pyToStr('temp.txt'))

print(regex('py.py'))

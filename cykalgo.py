from typing import DefaultDict


def grammarParse(grammar):
    gram = {}
    with open(grammar) as f:
        lines = f.readlines()
        for line in lines:
            line = line.split('->')
            gram[line[0].strip()] = [i.strip() for i in line[1].replace('\n','').split('|')]
    return gram

def cykalgo(gramParsed, word):
    table = [ [ '' for i in range(len(word)) ] for j in range(len(word)+1) ]
    blank = 0
    rules = gramParsed
    for i in range (len(word)+1):
        for j in range (len(word)-blank):
            if (i==0):
                table[0][j] = word[j]
            else:
                lenStr = i
                str = word[j:j+len+1]   
                lenSubstr = i-1
                
    
    return table
                





# print(grammarParse('grammar.txt'))
# cyk = DefaultDict(set)
# cyk[0].add(1)
# cyk[0].add(2)
# print(cyk)
# print(cyk[0])
print(cykalgo('',"halo"))
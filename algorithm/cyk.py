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

def displayMatrix (matrix):
    for i in range (len(matrix)):
        for j in range (len(matrix[0])):
            print(matrix[i][j], end= " ")
        print()

def states(file):    
    f = open(file)
    words = {'def' : "DEF" , 'return' : "RETURN" , "while" : "WHILE" , "break" : "BREAK" , "continue" : "CONTINUE" , "for" : "FOR"}

    DEF,WHILE,FOR = [],[],[]
    result = []

    def tabCounter(s):
        count = 0
        for i in s:
            if i == ' ':
                count+=1
            else:
                break
        return count//4

    def containWord(s):
        string = -1
        word = ""
        for i in s:
            if (i == "'" or i == '"'): #salah penutup ga penting bakal di handle di cyk
                string *= -1
                continue
            if string == -1:
                if i == " ":
                    if word in words:
                        return words[word]
                    word = ""
                else:
                    word += i
        if word in words:
            return words[word]
        return "NOTHING"


    comment = False
    for line in f.readlines():
        if line.strip() != '' and line.strip()[0] != '#' and line.strip()[:3] != "'''" and line.strip()[-3:] != "'''" and line.strip()[-3:] != '"""' and line.strip()[-3:] != '"""':
            result.append(line.replace('\n',''))
        else:
            if (line.strip()[:3] == "'''" or line.strip()[:3] == '"""') and not comment:
                comment = True
            elif (line.strip()[-3:] == "'''" or line.strip()[-3:] == '"""') and comment:
                comment = False
    types = ([containWord(i) for i in result])
    indents = ([tabCounter(i) for i in result])

    status = True

    for i in range(len(types)):
        if types[i] == "DEF":
            if tabCounter(result[i]) not in DEF:
                DEF.append(tabCounter(result[i]))
            else:
                for typ in [DEF,WHILE,FOR]:
                    for el in typ:
                        if el > tabCounter(result[i]):
                            typ.remove(el)
        elif types[i] == "FOR":
            if tabCounter(result[i]) not in FOR:
                FOR.append(tabCounter(result[i]))
            else:
                for typ in [DEF,WHILE,FOR]:
                    for el in typ:
                        if el > tabCounter(result[i]):
                            typ.remove(el)
        elif types[i] == "WHILE":
            if tabCounter(result[i]) not in WHILE:
                WHILE.append(tabCounter(result[i]))
            else:
                for typ in [DEF,WHILE,FOR]:
                    for el in typ:
                        if el > tabCounter(result[i]):
                            typ.remove(el)
        elif types[i] == "BREAK" or types[i] == "CONTINUE":
            temp = tabCounter(result[i])
            if WHILE == [] and FOR == []:
                status = False
                continue
            ok = False
            for el in WHILE:
                if el < temp:
                    ok = True
                    break
                else:
                    status = False
                    break
            if not ok:
                for el in FOR:
                    if el < temp:
                        break
                    else:
                        status = False
                        break
        elif types[i] == "RETURN":
            temp = tabCounter(result[i])
            if DEF == []:
                status = False
                continue
            for el in DEF:
                if el < temp:
                    continue
                else:
                    status = False
                    break
        elif types[i] == "NOTHING":
            for typ in [DEF,WHILE,FOR]:
                for el in typ:
                    if el > tabCounter(result[i]):
                        typ.remove(el)
        if not status:
            break

    if status:
        return True
    else:
        return False


def cykalgo(gramParsed, word):
    table = [ [ '' for i in range(len(word)) ] for j in range(len(word)+1) ]
    rules = gramParsed
    keyRules = {}

    for i in range (len(word)+1):
        for j in range (len(word)):
            # i==0 untuk mengassign kata
            if (i==0):
                table[0][j] = word[j]
            # i==1 membaca grammar saja
            elif (i==1):
                # element = [] karena ada value yang keynya dua
                el = []
                for key,value in rules.items():
                    for val in value:
                        # jika huruf pada kata ada di value grammar:
                        if table[0][j] == val:
                            el.append(key)
                            table[1][j] = el
                            keyRules[val] = el
            else:
                #string merupakan ba,aa,ab,ba,baa,aab,aba,baab,aaba,baaba
                str = word[j:j+i]
                #dalam indexing string, jika mis: [a:b] jika b melebihi len dari str tersebut akan ttp keluar dgn elemen yang kurang dri semestinya
                if len(str) == i:
                    # print("string",str)
                    #jika string sesuai
                    #mencari substring dri string
                    substrings = []
                    #untuk elemen dari tabel
                    elementM = []
                    # inisiasi x dengan 0 untuk pemisah substring
                    x = 0
                    for a in range (len(str)):
                        #element depan dari substring
                        front = str[:x]
                        #element belakang dari substring
                        other = str[x:]
                        
                        #pengecekan apabila substring tidak kosong atau tidak sama panjangnya dengan kata aslinya
                        if (len(front)!=0 and len(other)!=0 and len(front)!=i and len(other)!=i):
                            substrings.append(front)
                            substrings.append(other)
                        #penambahan x setiap kali menambah panjang substring depan
                        x+=1
                    #untuk setiap substring akan di iterate dan dicari terminalnya
                    for sub in range (0,len(substrings),2):
                        keySubstr = []
                        #kondisi front lebih dri 1
                        if (len(substrings[sub])!=1):
                            #dijoin
                            sub1join = " ".join(substrings[sub])
                            #dicari key nya
                            keySubstr.append(keyRules[sub1join])
                            #kondisi other lebih dari 1
                            if (substrings[sub+1][0]!=1):   
                                sub2join = " ".join(substrings[sub+1])
                                keySubstr.append(keyRules[sub2join]) 
                            #kondisi other 1
                            else:
                                keySubstr.append(keyRules[substrings[sub+1][0]])
                        #kondisi front 1
                        else:
                            keySubstr.append(keyRules[substrings[sub][0]])
                            #kondisi other lebih dari 1
                            if (substrings[sub+1]!=1):
                                sub2join = " ".join(substrings[sub+1])
                                keySubstr.append(keyRules[sub2join])
                            #kondisi other 1
                            else:
                                keySubstr.append(keyRules[substrings[sub+1][0]])
                        # perkalian silang antar parsingan elemen misalnya BA dan BC
                        elements = [a+" "+b for a in keySubstr[0] for b in keySubstr[1]]
                        for el in elements:
                            # dengan menggunakan join mencari apakah ada key value
                            keyJoin = " ".join(el)
                            # jika value ada di grammar
                            if (check_value_grammar(rules, el)):
                                #append key ke element dari table
                                get_key(rules, el, elementM)
                            # jika element ada di parsingan kata dari sebelumnya, ambil keynya (terminal)
                            elif (keyJoin in list(keyRules.keys())):
                                if (el not in elementM):
                                    elementM.append(keyRules[el])
                            else:
                            # selain itu pass
                                pass
                    table[i][j] = elementM
                        # menambahkan info terminal elemen tersebut untuk elemen selanjutnya
                    strJoin = " ".join(str)
                    keyRules[strJoin] = elementM
    return table

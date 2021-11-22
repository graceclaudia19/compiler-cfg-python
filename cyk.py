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
                            # print("front", front)
                            # print("other", other)
                            substrings.append(front)
                            substrings.append(other)
                        #penambahan x setiap kali menambah panjang substring depan
                        x+=1
                        # print("substrings")

                        # print(substrings)
                    #untuk setiap substring akan di iterate dan dicari terminalnya
                    for sub in range (0,len(substrings),2):
                        keySubstr = []
                        # print("keyRules",keyRules)
                        # print(len(substrings[sub][0]))
                    
                        #pengecekan apakah elemen FRONT dari substring lebih dari 1 atau tidak, jika iya maka akan di join untuk pembacaan
                        #pengecekan apakah elemen OTHER dari substring lebih dari 1 atau tidak, jika iya maka akan di join untuk pembacaan

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
                        # print("keysubstr")
                        # print(keySubstr)
                        # perkalian silang antar parsingan elemen misalnya BA dan BC
                        elements = [a+" "+b for a in keySubstr[0] for b in keySubstr[1]]
                        for el in elements:
                            # print("element",el)
                            # dengan menggunakan join mencari apakah ada key value
                            keyJoin = " ".join(el)
                            # print("keyjoin", keyJoin)
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
                    # print(elementM)
                    table[i][j] = elementM
                    # print(keyRules)
                        # menambahkan info terminal elemen tersebut untuk elemen selanjutnya
                    strJoin = " ".join(str)
                    keyRules[strJoin] = elementM
                    # print("elementM")
                    # print(elementM)
                    # print(keyRules)
    return table

# word = ["b","a","a","b","a"]
# gram = grammarParse('CNF.txt')
# word = ['word', '=', 'num', 'elif', '(', 'word', '=', '=', 'num', ')', ':', 'print', '(', '"', 'word', '"', ')']
# table = cykalgo(gram,word)

# displayMatrix(table)
# top = table[len(word)][0]
# for i in top:
#     if i == 'MAIN_STATES':
#         print("yey di acc")
# print("bye")

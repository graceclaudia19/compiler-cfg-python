def grammarParse(grammar):
    gram = {}
    with open(grammar) as f:
        lines = f.readlines()
        for line in lines:
            line = line.split('->')
            gram[line[0].strip()] = [i.strip() for i in line[1].replace('\n','').split('|')]
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

def cykalgo(gramParsed, word):
    table = [ [ '' for i in range(len(word)) ] for j in range(len(word)+1) ]
    blank = 0
    rules = gramParsed
    keyRules = {}
    # membalik key-value menjadi value-key agar lebih mudah dalam pengerjaan:
    # for key,value in rules.items():
    #     for val in value:
    #         keyRules[val] = key
    # print(keyRules)

    for i in range (len(word)+1):
        #blank akan ditambah 1 saat bertambah linenya
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
            # elif (i==2):
            #     #string merupakan ba,aa,ab,ba,baa,aab,aba,baab,aaba,baaba
            #     str = word[j:j+i]
            #     #dalam indexing string, jika mis: [a:b] jika b melebihi len dari str tersebut akan ttp keluar dgn elemen yang kurang dri semestinya
            #     if len(str) == i:
            #         #jika string sesuai
            #         print(str)
            #         #mencari substring dri string
            #         substrings = []
            #         for x in range (i):
            #             substr = str[x:x+i-1]
            #             if (len(substr) == i-1):
            #                 # jika panjang benar akan diappend ke substr
            #                 substrings.append(substr)
            #         print(substrings)
            #         # ini merupakan pengingat terminal di atasnya yang pernah dilewati agar tidak mengulang pencarian
            #         keySubstr = []
            #         #untuk melakukan perkalian silang antar elemen dibutuhkan parsing tingkat sebelumnya dari substring tersebut (mis: b jadi B a jadi A, C)
            #         for substr in substrings:
            #             keySubstr.append(keyRules[substr])
            #         print(keySubstr)
            #         # perkalian silang antar parsingan elemen misalnya BA dan BC
            #         elements = [a+b for a in keySubstr[0] for b in keySubstr[1]]
            #         print(elements)
            #         elementM = []
            #         for el in elements:
            #             # jika value ada di grammar
            #             if (check_value_grammar(rules, el)):
            #                 #append key ke element dari table
            #                 get_key(rules, el, elementM)
            #             # jika element ada di parsingan kata dari sebelumnya, ambil keynya (terminal)
            #             elif (el in list(keyRules.keys())):
            #                 elementM.append(keyRules[el])
            #             else:
            #             # selain itu pass
            #                 pass
            #         #pengisian elemen ke dalam tabel
            #         table[i][j] = elementM
            #         # menambahkan info terminal elemen tersebut untuk elemen selanjutnya
            #         keyRules[str] = elementM
            #         print(keyRules)
            else:
                #string merupakan ba,aa,ab,ba,baa,aab,aba,baab,aaba,baaba
                str = word[j:j+i]
                #dalam indexing string, jika mis: [a:b] jika b melebihi len dari str tersebut akan ttp keluar dgn elemen yang kurang dri semestinya
                if len(str) == i:
                    #jika string sesuai
                    print(str)
                    #mencari substring dri string
                    substrings = []
                    elementM = []
                    x = 0
                    for a in range (len(str)):
                        front = str[:x]
                        other = str[x:]

                        if (len(front)!=0 and len(other)!=0 and len(front)!=i and len(other)!=i):
                            substrings.append(front)
                            substrings.append(other)
                        x+=1
                    print("substrings")

                    print(substrings)
                    
                    print(len(substrings))
                    for sub in range (0,len(substrings),2):
                        keySubstr = []
                        print(keyRules)
                        keySubstr.append(keyRules[substrings[sub]])
                        keySubstr.append(keyRules[substrings[sub+1]])
                        print("keysubstr")
                        print(keySubstr)
                         # perkalian silang antar parsingan elemen misalnya BA dan BC
                        elements = [a+b for a in keySubstr[0] for b in keySubstr[1]]
                        print(elements)
                        for el in elements:
                            # jika value ada di grammar
                            if (check_value_grammar(rules, el)):
                                #append key ke element dari table
                                get_key(rules, el, elementM)
                            # jika element ada di parsingan kata dari sebelumnya, ambil keynya (terminal)
                            elif (el in list(keyRules.keys())):
                                if (el not in elementM):
                                    elementM.append(keyRules[el])
                            else:
                            # selain itu pass
                                pass
                    table[i][j] = elementM
                        # menambahkan info terminal elemen tersebut untuk elemen selanjutnya
                    keyRules[str] = elementM
                    print("elementM")
                    print(elementM)
                    # print(keyRules)

                    # # ini merupakan pengingat terminal di atasnya yang pernah dilewati agar tidak mengulang pencarian
                    # keySubstr = []
                    # # element dalam m nanti yg digunakan
                    # elementM = []
                    # #untuk melakukan perkalian silang antar elemen dibutuhkan parsing tingkat sebelumnya dari substring tersebut (mis: b jadi B a jadi A, C)
                    # for substr in substrings:
                    #     keySubstr.append(keyRules[substr])
                    # print(keySubstr)
                    # # perkalian silang antar parsingan elemen misalnya BA dan BC
                    # elements = [a+b for a in keySubstr[0] for b in keySubstr[1]]
                    # print(elements)
                    # for el in elements:
                    #     # jika value ada di grammar
                    #     if (check_value_grammar(rules, el)):
                    #         #append key ke element dari table
                    #         get_key(rules, el, elementM)
                    #     # jika element ada di parsingan kata dari sebelumnya, ambil keynya (terminal)
                    #     elif (el in list(keyRules.keys())):
                    #         elementM.append(keyRules[el])
                    #     else:
                    #     # selain itu pass
                    #         pass
                    # #pengisian elemen ke dalam tabel
                    # table[i][j] = elementM
                    # # menambahkan info terminal elemen tersebut untuk elemen selanjutnya
                    # keyRules[str] = elementM
                    # print(keyRules)


    # print(keyRules)
    print()
    return table
                





# print(grammarParse('grammar.txt'))
# cyk = DefaultDict(set)
# cyk[0].add(1)
# cyk[0].add(2)
# print(cyk)
# print(cyk[0])
gram = grammarParse('grammar.txt')
word = "baaba"
table = cykalgo(gram,word)

top = table[len(word)][0]
for i in top:
    if i == 'S':
        print("yey di acc")
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
            else:
                #string merupakan ba,aa,ab,ba,baa,aab,aba,baab,aaba,baaba
                str = word[j:j+i]
                #dalam indexing string, jika mis: [a:b] jika b melebihi len dari str tersebut akan ttp keluar dgn elemen yang kurang dri semestinya
                if len(str) == i:
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
                        keySubstr.append(keyRules[substrings[sub]])
                        keySubstr.append(keyRules[substrings[sub+1]])
                        # perkalian silang antar parsingan elemen misalnya BA dan BC
                        elements = [a+b for a in keySubstr[0] for b in keySubstr[1]]
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
    return table

gram = grammarParse('grammar.txt')
word = "baaba"
table = cykalgo(gram,word)

top = table[len(word)][0]
for i in top:
    if i == 'S':
        print("yey di acc")

def getCFG(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    i = 0
    cfg = []
    for line in lines:
        line = line.replace(' -> ', ' ').replace('\n', '')
        wpw = line.split()
        if ('|' in wpw):
            temp = [wpw[0]]
            for i in range(1, len(wpw)):
                if (wpw[i] == '|'):
                    cfg.append(temp)
                    temp = [wpw[0]]
                else:
                    temp.append(wpw[i])
            cfg.append(temp)
        else:
            cfg.append(wpw)
    return cfg

def getTerminals(filename):
    terminals = []
    file = open(filename, 'r')
    lines = file.readlines()
    for line in lines:
        terminals.append(line.replace('\n', ''))
    termRules = []
    for terminal in terminals:
        rule = terminal.upper() + "_rule"
        termRules.append([rule, terminal])
    return terminals, termRules

def removeUnitProd(cfg, terminals):
    delete = []
    for prod in cfg:
        if ((len(prod) == 2) and (not(prod[1] in terminals))):
            if (prod[1] != prod[0]):
                i = 0
                while(i < len(cfg)):
                    if (prod[1] == cfg[i][0]):
                        temp = [prod[0]]
                        for j in range(1, len(cfg[i])):
                            temp.append(cfg[i][j])
                        cfg.append(temp)   
                    i += 1
            delete.append(prod)
    for prod in delete:
        cfg.remove(prod)
    return cfg

def getRule(terminal, rules):
    for rule in rules:
        if (rule[1] == terminal):
            return rule[0]

def checkRHS(cfg, terminals, rules):
    count = 1
    idx = 1
    for prod in cfg:
        if (len(prod) > 2):
            if any(elmt in prod for elmt in terminals):
                for i in range(len(prod)):
                    if (prod[i] in terminals):
                        prod[i] = getRule(prod[i], rules)
    for prod in cfg:
        if (len(prod) > 3):
            rule = []
            for i in range(2, len(prod)):
                rule.append(prod[i])
            for i in range(2, len(prod)):
                prod.pop()
            newvar = rule[0] + "_rule"
            for elmts in cfg:
                if (newvar in elmts[0]):
                    newvar += str(count)
                    break
            prod.append(newvar)
            rule.insert(0, newvar)
            if rule not in cfg:
                cfg.insert(idx, rule)
        idx += 1    
    return cfg

def convertCFG(filename):
    file = open("CNF.txt", 'w')   #change
    cfg = getCFG(filename)
    print("INITIAL CFG:")
    print(cfg)
    terminals, rules = getTerminals("terminal.txt")   #change
    print("\nTERMINALS:")
    print(terminals)
    cfg = removeUnitProd(cfg, terminals)
    print("\nAFTER UNIT PRODUCTION REMOVAL:")
    print(cfg)
    cfg.append(rules)
    cfg = checkRHS(cfg, terminals, rules)
    cfg.remove(rules)
    print("\nAFTER CONVERTING TO CNF (terminal rules not included):")
    print(cfg)
    for prod in rules:
        str = (' -> '.join(prod))
        file.write(str + "\n")
    for prod in cfg:
        str = (' '.join(prod)).replace(' ', ' -> ', 1)
        file.write(str + "\n")
    file.close()
    print("\nCHECK DUMMY_CNF.TXT")
    return

# convertCFG("dummy_cfg.txt")

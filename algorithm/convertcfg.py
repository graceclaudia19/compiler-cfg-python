import os

def getCFG(filename):
    '''
    get CFG from file
    change each production rule from 'A -> B C | d to [A, B, C, |, d]
    return list of production rules
    '''
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    cfg = []
    for line in lines:
        # ignore comments
        if (line.startswith('/*') and line.endswith('*/\n')) or line == '\n':
            continue
        # remove arrows
        line = line.replace(' -> ', ' ').replace('\n', '')
        wpw = line.split()
        if ('|' in wpw):
            # multiple production rules
            temp = [wpw[0]]
            for i in range(1, len(wpw)):
                if (wpw[i] == '|'): # split RHS
                    cfg.append(temp)
                    temp = [wpw[0]]
                else:
                    temp.append(wpw[i])
            cfg.append(temp)
        else:
            # singular production rule
            cfg.append(wpw)
    return cfg

def getTerminals(filename):
    '''
    get terminals from a file
    create its non-terms and production rule
    return list of terminals and list of prod rules
    '''
    terminals = []
    file = open(filename, 'r')
    lines = file.readlines()
    for line in lines:
        # ignore comments
        if (line.startswith('/*') and line.endswith('*/\n')) or line == '\n':
            continue
        terminals.append(line.replace('\n', ''))
    termRules = []
    for terminal in terminals:
        rule = terminal.upper() + "_rule" # create LHS
        termRules.append([rule, terminal]) # create prod rule
    return terminals, termRules

def removeUnitProd(cfg, terminals):
    '''
    remove unit productions from CFG
    convert RHS of 'A -> B' where B is a non-term with 'B -> A S d'
    so that 'A -> B' becomes 'A -> A S d'
    return CFG with no unit productions
    '''
    delete = []
    for prod in cfg:
        # handle one non-term RHS
        if ((len(prod) == 2) and (not(prod[1] in terminals))):
            if (prod[1] != prod[0]): # ignore S -> S
                i = 0
                # search for prod rule with LHS that matches RHS of unit prod
                while(i < len(cfg)):
                    if (prod[1] == cfg[i][0]):
                        # change RHS of unit prod
                        temp = [prod[0]]
                        for j in range(1, len(cfg[i])):
                            temp.append(cfg[i][j])
                        cfg.append(temp)   
                    i += 1
            delete.append(prod)
    # remove all unit productions
    for prod in delete:
        cfg.remove(prod)
    return cfg

def getRule(terminal, rules):
    '''
    return the corresponding non-term of the given terminal
    '''
    for rule in rules:
        # check if non-term's terminal matches given terminal
        if (rule[1] == terminal):
            return rule[0]

def checkRHS(cfg, terminals, rules):
    '''
    check for cases where RHS contains both non-term and term, more than 1 term, or more than 2 non-terms
    return list of CFG that has been conformed to CNF's conditions
    '''
    for prod in cfg:
        # check for more than 1 term in RHS
        if (len(prod) > 2):
            if any(elmt in prod for elmt in terminals):
                for i in range(len(prod)):
                    if (prod[i] in terminals):
                        prod[i] = getRule(prod[i], rules) # convert term to its corresponding non-term
    count = 1
    idx = 1
    for prod in cfg:
        # check for more than 2 non-terms in RHS
        if (len(prod) > 3):
            rule = []
            # store leftover RHS
            for i in range(2, len(prod)):
                rule.append(prod[i])
            # delete leftover RHS
            for i in range(2, len(prod)):
                prod.pop()
            # create new non-term for leftover RHS
            newvar = rule[0] + "_rule"
            for elmts in cfg:
                if (newvar in elmts[0]):
                    newvar += str(count) # add numbers to distinguish new non-term from existing ones
                    break
            # create rule with new non-term as LHS and leftover RHS as RHS
            prod.append(newvar)
            rule.insert(0, newvar)
            if rule not in cfg:
                cfg.insert(idx, rule) # add new rule to cfg
        idx += 1    
    return cfg

def convertCFG(filename):
    '''
    convert CFG to CNF and save its result to "CNF.txt"
    '''
    file = open(os.getcwd() + '\grammar\\CNF.txt', 'w')
    cfg = getCFG(filename)
    terminals, rules = getTerminals(os.getcwd() + '\grammar\\terminal.txt')
    cfg = removeUnitProd(cfg, terminals)
    for rule in rules:
        cfg.append(rule)
    cfg = checkRHS(cfg, terminals, rules)
    for rule in rules:
        cfg.remove(rule)
    for prod in rules:
        str = (' -> '.join(prod))
        file.write(str + "\n")
    for prod in cfg:
        str = (' '.join(prod)).replace(' ', ' -> ', 1)
        file.write(str + "\n")
    file.close()
    return
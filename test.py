#JGN GANGGU PNY GC
list = [['def', 'my_function', '(', 'fname', ')', ':'], ['x', '=', '300'], ['print', '(', 'fname', '+', '"', 'refsnes', '"', ')']]
# , ['print', '(', 'fname', '+', '"', 'refsnes', '"', ')'], ['print', '(', "'", 'lalala', "'", ')']

ticks = False
l = []
for el in list:
    li = []
    for i in el:
        if i == '"':
            ticks = not ticks
            li.append(i)
            if ticks:
                li.append("word")
        elif ticks:
            pass
        else:
            li.append(i)
    l.append(li)
print(l)

def strCheckOneTick(list):
    ticks = False
    l = []
    for el in list:
        li = []
        for i in el:
            if i == '"':
                ticks = not ticks
                li.append(i)
                if ticks:
                    li.append("word")
            elif ticks:
                pass
            else:
                li.append(i)
        l.append(li)
    return l
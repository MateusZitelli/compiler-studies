lines = None
switches = {}
statesS = {}
states = 0
thereIsChars = True
char = 0
statesToGo = [{"number": 0, "words": None}]
with open("language") as f:
    statesToGo[0]["words"] = [(w.strip(), w.strip()) for w in list(f.readlines())]


def printStructIntern(struct, d = 0):
    print "  " * (d * 3),
    print("switch (letra) {")
    for k in struct:
        print "  " * (d * 3 + 1),
        print "case '%s':"%(k)
        for token in struct[k]['toCheck']:
            print "  " * (d * 3 + 2),
            print("if( palavra == \"%s\"){"%(token))
            print "  " * (d * 3 + 3),
            print("return new Token(TokenType.%s , String.valueOf(palavra)); // retornar token para %s"%(token, token))
            print "  " * (d * 3 + 2),
            print("}")
        if struct[k]['final'] and len(struct[k]['words']) > 0:
            token = struct[k]['words'][0][1]
            print "  " * (d * 3 + 2),
            print("if( palavra == \"%s\"){"%(token))
            print "  " * (d * 3 + 3),
            print("return new Token(TokenType.%s , String.valueOf(palavra)); // retornar token para %s"%(token, token))
            print "  " * (d * 3 + 2),
            print("}")
        elif not struct[k]['final']:
            print "  " * (d * 3 + 2),
            print("state = %i;"%(struct[k]['stateToGo']))
        print "  " * (d * 3 + 2),
        print "break;"

    print "  " * (d * 3 + 1),
    print "default:"
    print "  " * (d * 3 + 1),
    print "// Definir um erro"
    print "  " * (d * 3 + 2),
    print "break;"
    print "  " * (d * 3),
    print("}")

def printStruct(struct, d = 0):
    print("switch (state) {")
    for s in struct:
        print "  " * (d * 2 + 1),
        print "case %i:"%(s)
        printStructIntern(struct[s], d + 1)
    print "  " * (d * 2 + 1),
    print "default:"
    print "  " * (d * 2 + 1),
    print "// Definir um erro"
    print "  " * (d * 2 + 1),
    print "break;"
    print "  " * (d * 2),
    print("}")

while(len(statesToGo) > 0) :
    newStates = {}
    for state in statesToGo:
        switches[state["number"]] = {}
        sState = switches[state["number"]]
        for word in state["words"]:
            if word[0][0] in sState:
                if word[0][0] in newStates:
                    ans = newStates[word[0][0]]
                    ans["words"].append((word[0][1:], word[1]))
                else:
                    if(not word[0][1:]):
                        sState[word[0][0]]["toCheck"].append(word[1])
                    else:
                        states += 1
                        if(len(sState[word[0][0]]['words']) == 0):
                            newStates[word[0][0]] = {"words": [(word[0][1:], word[1])], "number": states}
                        else:
                            newStates[word[0][0]] = {"words": [(word[0][1:], word[1]), (sState[word[0][0]]['words'][0][0][1:], sState[word[0][0]]['words'][0][1])], "number": states}
                        sState[word[0][0]]["final"] = False
                        sState[word[0][0]]["stateToGo"] = states
                        sState[word[0][0]]["words"].append(word)
            else:
                sState[word[0][0]] = {"final": True, "words": [], "toCheck": []}
                if(len(word[0]) == 1):
                    sState[word[0][0]]["toCheck"].append(word[1])
                else:
                    sState[word[0][0]]["words"].append(word)

    statesToGo = newStates.values()

printStruct(switches)

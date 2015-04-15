lines = None
switches = {}
statesS = {}
states = 0
thereIsChars = True
char = 0
statesToGo = [{"number": 0, "words": None}]
with open("language") as f:
    statesToGo[0]["words"] = list(f.readlines())


def printStructIntern(struct, d = 0):
    print "  " * (d * 2),
    print("switch (state) {")
    for k in struct:
        print "  " * (d * 2 + 1),
        print "case '%s':"%(k)
        if struct[k]['final']:
            print "  " * (d * 2 + 1),
            print("return new Token(TokenType. , String.valueOf(palavra)); // retornar token para %s"%(struct[k]['words'][0]))
        else:
            print "  " * (d * 2 + 1),
            print("state = %i;"%(struct[k]['stateToGo']))

    print "  " * (d * 2 + 1),
    print "default:"
    print "  " * (d * 2 + 1),
    print "// Definir um erro"
    print "  " * (d * 2 + 1),
    print "break;"
    print "  " * (d * 2),
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
            if word[0] in sState:
                if word[0] in newStates:
                    newStates[word[0]]["words"].append(word[1:])
                else:
                    states += 1
                    newStates[word[0]] = {"words": [word[1:], sState[word[0]]['words'][0]], "number": states}
                sState[word[0]]["final"] = False
                sState[word[0]]["stateToGo"] = states
                sState[word[0]]["words"].append(word)
            else:
                sState[word[0]] = {"final": True, "words": [word]}
    statesToGo = newStates.values()

printStruct(switches)

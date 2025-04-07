from collections import namedtuple

import syntacticanalyzer

node = namedtuple("node", "Lexeme Token")

c = node("start", "start")
d = node("varstart", "varstart")
e = node("varend", "varend")
f = node("write", "write")
g = node("read", "read")
h = node("if", "if")
i = node("then", "then")
j = node("endif", "endif")
k = node("end", "end")
l = node("integer", "integer")
m = node("then", "then")
n = node("literal", "literal")
o = node("real", "real")

simbleTable = [c, d, e, f, g, h, i, j, k, l, m, n, o]

tokens = []
lexemes = []

def lexic(line):
    i = 1
    if(line[0].isalpha() == True):
        while(len(line) < i or line[i].isalpha() == True or line[i].isdigit() == True or line[i] == "_"):
            i = i + 1
        createNode(line[:i], "id")
        syntacticanalyzer.__settype__("id", len(tokens))
        if(line[i:] != ""):
            if(line[i] == " "):
                i += 1
            lexic(line[i:])
    elif(line[0].isdigit() == True):
        while(len(line) < i or line[i].isdigit() == True or line[i] == "E" or line[i] == "."):
            i = i + 1
        createNode(line[:i], "num")
        syntacticanalyzer.__settype__("num", len(tokens))
        if (line[i:] != ""):
            if (line[i] == " "):
                i += 1
            lexic(line[i:])
    elif(line[0] == "("):
        createNode(line[:1], "ab_p")
        syntacticanalyzer.__settype__("(", len(tokens))
        if (line[1:] != ""):
            lexic(line[1:])

    elif(line[0] == ")"):
        createNode(line[:1], "fc_p")
        syntacticanalyzer.__settype__(")", len(tokens))
        if (line[1:] != ""):
            lexic(line[1:])

    elif(line[0] == "+" or line[0] == "-" or line[0] == "/" or line[0] == "*"):
        aux = line[0]
        createNode(line[:1], "opm")
        syntacticanalyzer.__settype__(aux, len(tokens))
        if (line[1:] != ""):
            lexic(line[1:])

    elif(line[0] == ";"):
        createNode(line[:1], "pt_v")
        syntacticanalyzer.__settype__(";", len(tokens))
        if (line[1:] != ""):
            lexic(line[1:])

    elif(line[0] == "<" and line[1] == "-"):
        createNode(line[:2], "rcb")
        syntacticanalyzer.__settype__("=", len(tokens))
        if (line[2:] != ""):
            lexic(line[2:])

    elif(line[0] == "<" and line[1] == "="):
        aux = line[0]
        aux = aux + line[1]
        createNode(line[:2], "opr")
        syntacticanalyzer.__settype__(aux, len(tokens))
        if (line[2:] != ""):
            lexic(line[2:])

    elif(line[0] == ">" and line[1] == "="):
        aux = line[0]
        aux = aux + line[1]
        createNode(line[:2], "opr")
        syntacticanalyzer.__settype__(aux, len(tokens))
        if (line[2:] != ""):
            lexic(line[2:])

    elif(line[0] == "<" and line[1] == ">"):
        aux = line[0]
        aux = aux + line[1]
        createNode(line[:2], "opr")
        syntacticanalyzer.__settype__(aux, len(tokens))
        if (line[2:] != ""):
            lexic(line[2:])

    elif(line[0] == "<" or line[0] == ">" or line[0] == "="):
        aux = line[0]
        createNode(line[:1], "opr")
        syntacticanalyzer.__settype__(aux, len(tokens))
        if (line[1:] != ""):
            lexic(line[1:])
    elif(line[0] == '"'):
        while(len(line) < i or line[i] != '"'):
            i = i + 1
        createNode(line[:i], "literal")
        syntacticanalyzer.__settype__("literal", len(tokens))
        i += 1
        if (line[i:] != ""):
            if (line[i] == " "):
                i += 1
            lexic(line[i:])
    elif(line[0] == ""):
        createNode("", "EOF")
        syntacticanalyzer.__settype__("EOF", len(tokens))
    elif (line[0] == "$"):
        createNode("$", "$")
        syntacticanalyzer.__settype__("$", len(tokens))
    else:
        print('Erro. Token Invalido')

def createNode(lexeme, token):
    new = node(lexeme, token)
    newrsv = node(lexeme, lexeme)
    check = nodeExists(new, newrsv)
    if (check == 2):
        tokens.append(lexeme)
        lexemes.append(lexeme)
    else:
        simbleTable.append(new)
        tokens.append(token)
        lexemes.append(lexeme)


def __gettoken__(i):
    return tokens[i]

def __getlexeme__(i):
    return lexemes[i]

def __settoken__(token, i):
    tokens[i] = token

def __setlexeme__(lexeme, i):
    lexemes[i] = lexeme
def __getindex__(lexeme):
    return lexemes.index(lexeme)

def nodeExists(node, nodersv):
    i = 0
    while (len(simbleTable) > i):
        if(nodersv == simbleTable[i]):
            return 2
        elif (node == simbleTable[i]):
            return 1
        i = i + 1
    return 0

def __init__():
    file = open("text.alg", "r")
    line = file.readline()
    while(line != ""):
        lexic(line)
        line = file.readline()
    if(line == ""):
        createNode("$", "EOF")
    file.close()
    for p in simbleTable:
        print(p)

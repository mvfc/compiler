from collections import namedtuple

import analisadorsintatico

node = namedtuple("node", "Lexema Token")

c = node("inicio", "inicio")
d = node("varinicio", "varinicio")
e = node("varfim", "varfim")
f = node("escreva", "escreva")
g = node("leia", "leia")
h = node("se", "se")
i = node("entao", "entao")
j = node("fimse", "fimse")
k = node("fim", "fim")
l = node("inteiro", "inteiro")
m = node("entao", "entao")
n = node("literal", "literal")
o = node("real", "real")

tabelaSimbolo = [c, d, e, f, g, h, i, j, k, l, m, n, o]

tokens = []
lexemas = []

def lexico(linha):
    i = 1
    global retorno
    if(linha[0].isalpha() == True):
        while(len(linha) < i or linha[i].isalpha() == True or linha[i].isdigit() == True or linha[i] == "_"):
            i = i + 1
        criaNode(linha[:i], "id")
        analisadorsintatico.__settipo__("id", len(tokens))
        if(linha[i:] != ""):
            if(linha[i] == " "):
                i += 1
            lexico(linha[i:])
    elif(linha[0].isdigit() == True):
        while(len(linha) < i or linha[i].isdigit() == True or linha[i] == "E" or linha[i] == "."):
            i = i + 1
        criaNode(linha[:i], "num")
        analisadorsintatico.__settipo__("num", len(tokens))
        if (linha[i:] != ""):
            if (linha[i] == " "):
                i += 1
            lexico(linha[i:])
    elif(linha[0] == "("):
        criaNode(linha[:1], "ab_p")
        analisadorsintatico.__settipo__("(", len(tokens))
        if (linha[1:] != ""):
            lexico(linha[1:])

    elif(linha[0] == ")"):
        criaNode(linha[:1], "fc_p")
        analisadorsintatico.__settipo__(")", len(tokens))
        if (linha[1:] != ""):
            lexico(linha[1:])

    elif(linha[0] == "+" or linha[0] == "-" or linha[0] == "/" or linha[0] == "*"):
        aux = linha[0]
        criaNode(linha[:1], "opm")
        analisadorsintatico.__settipo__(aux, len(tokens))
        if (linha[1:] != ""):
            lexico(linha[1:])

    elif(linha[0] == ";"):
        criaNode(linha[:1], "pt_v")
        analisadorsintatico.__settipo__(";", len(tokens))
        if (linha[1:] != ""):
            lexico(linha[1:])

    elif(linha[0] == "<" and linha[1] == "-"):
        criaNode(linha[:2], "rcb")
        analisadorsintatico.__settipo__("=", len(tokens))
        if (linha[2:] != ""):
            lexico(linha[2:])

    elif(linha[0] == "<" and linha[1] == "="):
        aux = linha[0]
        aux = aux + linha[1]
        criaNode(linha[:2], "opr")
        analisadorsintatico.__settipo__(aux, len(tokens))
        if (linha[2:] != ""):
            lexico(linha[2:])

    elif(linha[0] == ">" and linha[1] == "="):
        aux = linha[0]
        aux = aux + linha[1]
        criaNode(linha[:2], "opr")
        analisadorsintatico.__settipo__(aux, len(tokens))
        if (linha[2:] != ""):
            lexico(linha[2:])

    elif(linha[0] == "<" and linha[1] == ">"):
        aux = linha[0]
        aux = aux + linha[1]
        criaNode(linha[:2], "opr")
        analisadorsintatico.__settipo__(aux, len(tokens))
        if (linha[2:] != ""):
            lexico(linha[2:])

    elif(linha[0] == "<" or linha[0] == ">" or linha[0] == "="):
        aux = linha[0]
        criaNode(linha[:1], "opr")
        analisadorsintatico.__settipo__(aux, len(tokens))
        if (linha[1:] != ""):
            lexico(linha[1:])
    elif(linha[0] == '"'):
        while(len(linha) < i or linha[i] != '"'):
            i = i + 1
        criaNode(linha[:i], "literal")
        analisadorsintatico.__settipo__("literal", len(tokens))
        i += 1
        if (linha[i:] != ""):
            if (linha[i] == " "):
                i += 1
            lexico(linha[i:])
    elif(linha[0] == ""):
        criaNode("", "EOF")
        analisadorsintatico.__settipo__("EOF", len(tokens))
    elif (linha[0] == "$"):
        criaNode("$", "$")
        analisadorsintatico.__settipo__("$", len(tokens))

def criaNode(lexema, token):
    new = node(lexema, token)
    newrsv = node(lexema, lexema)
    check = nodeExists(new, newrsv)
    if (check == 2):
        tokens.append(lexema)
        lexemas.append(lexema)
    else:
        tabelaSimbolo.append(new)
        tokens.append(token)
        lexemas.append(lexema)


def __gettoken__(i):
    return tokens[i]

def __getlexema__(i):
    return lexemas[i]

def __settoken__(token, i):
    tokens[i] = token

def __setlexema__(lexema, i):
    lexemas[i] = lexema
def __getindex__(lexema):
    return lexemas.index(lexema)

def nodeExists(node, nodersv):
    i = 0
    while (len(tabelaSimbolo) > i):
        if(nodersv == tabelaSimbolo[i]):
            return 2
        elif (node == tabelaSimbolo[i]):
            return 1
        i = i + 1
    return 0

def __init__():
    arquivo = open("texto.alg", "r")
    linha = arquivo.readline()
    while(linha != ""):
        lexico(linha)
        linha = arquivo.readline()
    if(linha == ""):
        criaNode("$", "EOF")
    arquivo.close()

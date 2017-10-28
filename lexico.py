from collections import namedtuple

node = namedtuple("node", "Token Lexema Tipo")

c = node("inicio", "inicio", "rsv")
d = node("varinicio", "varinicio", "rsv")
e = node("varfim", "varfim", "rsv")
f = node("escreva", "escreva", "rsv")
g = node("leia", "leia", "rsv")
h = node("se", "se", "rsv")
i = node("entao", "entao", "rsv")
j = node("fimse", "fimse", "rsv")
k = node("fim", "fim", "rsv")
l = node("Inteiro", "Inteiro", "rsv")
m = node("entao", "entao", "rsv")
n = node("literal", "literal", "rsv")
o = node("real", "real", "rsv")

tabelaSimbolo = [c, d, e, f, g, h, i, j, k, l, m, n, o]

arquivo = open("texto.alg")

def lexico(linha):
    if(linha[0].isalpha() == True):

    if(linha[0].isdigit() == True):

    if(linha[0] == ""):

    if(linha[0] == "("):

    if(linha[0] == "\""):

    if(linha[0] == ")"):

    if(linha[0] == "+" or linha[0] == "-" or linha[0] == "/" or linha[0] == "*"):

    if(linha[0] == )

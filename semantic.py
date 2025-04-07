import syntacticanalyzer
import lexic

class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.type = None
        self.lexeme = None
        self.token = None
        self.father = None

root = Tree()
tree = None

x = 0

def __init__():
    file = open("program.c", "w")
    file.write("#include <stdio.h>\n\n")
    file.write("typedef char literal[256];\n")
    file.write("void main(void)\n{\n\n")
    file.close()

def __semantic__(lexeme, token, rule, i):
    global x
    global tree
    file = open("program.c", "a")
    if(rule == 1):
        if(tree.father == None):
            tree.father = Tree()
        tree.father.lexeme = "P'"
        if(tree.father.left == None):
            tree.father.left = tree
        else:
            tree.father.right = tree
        tree = tree.father
    elif(rule == 2):
        if (tree == None):
            tree = Tree()
            tree.token = "start"
            tree.lexeme = "start"
            tree.type = "start"
        if (tree.father == None):
            tree.father = Tree()
        tree.father.lexeme = "P"
        if (tree.father.left == None):
            tree.father.left = tree
        else:
            tree.father.right = tree
        tree = tree.father
    elif(rule == 3):
        if (tree == None):
            tree = Tree()
            tree.token = "varstart"
            tree.lexeme = "varstart"
            tree.type = "varstart"
        if (tree.father == None):
            tree.father = Tree()
        tree.father.lexeme = "V"
        if (tree.father.left == None):
            tree.father.left = tree
        else:
            tree.father.right = tree
        tree = tree.father
    elif(rule == 4):
        if (tree.father == None):
            tree.father = Tree()
        tree.father.lexeme = "LV"
        if (tree.father.left == None):
            tree.father.left = tree
        else:
            tree.father.right = tree
        tree = tree.father
    elif(rule == 5):
        file.write("\n\n\n")
        if (tree == None):
            tree = Tree()
            tree.token = "varend"
            tree.lexeme = "varend"
            tree.type = "varend"
        if (tree.father == None):
            tree.father = Tree()
        tree.father.lexeme = "varend"
        if (tree.father.left == None):
            tree.father.left = tree
        else:
            tree.father.right = tree
        tree = tree.father
    elif(rule == 7):
        if (tree == None):
            tree = Tree()
            tree.token = "int"
            tree.lexeme = lexeme
            tree.type = "int"
        if (tree.father == None):
            tree.father = Tree()
        tree.father.lexeme = "type"
        if (tree.father.left == None):
            tree.father.left = tree
        else:
            tree.father.right = tree
        tree.father.type = "int"
        tree.father.token = "int"
        tree = tree.father
    elif(rule == 8):
        if (tree == None):
            tree = Tree()
            tree.token = "real"
            tree.lexeme = lexeme
            tree.type = "double"
        if (tree.father == None):
            tree.father = Tree()
        tree.father.lexeme = "type"
        if (tree.father.left == None):
            tree.father.left = tree
        else:
            tree.father.right = tree
        tree.father.type = "double"
        tree = tree.father
    elif(rule == 9):
        if (tree == None):
            tree = Tree()
            tree.token = "literal"
            tree.lexeme = lexeme
            tree.type = "literal"
        if (tree.father == None):
            tree.father = Tree()
        tree.father.lexeme = "type"
        if (tree.father.left == None):
            tree.father.left = tree
        else:
            tree.father.right = tree
        tree.father.type = "literal"
        tree.father.lexeme = lexeme
        tree = tree.father
    elif(rule == 6):
        if (tree.father == None):
            tree.father = Tree()
        tree.father.lexeme = lexic.__getlexeme__(i-3)
        if (tree.father.left == None):
            tree.father.left = tree
        else:
            tree.father.right = tree
        tree.father.type = tree.type
        tree = tree.father
        file.write( tree.type +" "+tree.lexeme+";\n")
        if(tree.type == "int"):
            syntacticanalyzer.__settype__("int", i-3)
        else:
            syntacticanalyzer.__settype__(tree.type, i-3)
    elif(rule == 10):
        if (tree.father == None):
            tree.father = Tree()
        tree.father.lexeme = "A"
        if (tree.father.left == None):
            tree.father.left = tree
        else:
            tree.father.right = tree
        tree = tree.father
    elif(rule == 11):
        if(syntacticanalyzer.__gettype__(lexic.__getindex__(lexic.__getlexeme__(i-2))) == "id"):
            print("Error: Undeclared variable:" + lexic.__getlexeme__(i-2))
        else:
            if(syntacticanalyzer.__gettype__(lexic.__getindex__(lexic.__getlexeme__(i-2))) == "literal"):
                file.write('scanf("%s", '+lexic.__getlexeme__(i-2)+');\n')
            if(syntacticanalyzer.__gettype__(lexic.__getindex__(lexic.__getlexeme__(i-2))) == "int"):
                file.write('scanf("%d", &' + lexic.__getlexeme__(i-2) + ');\n')
            if(syntacticanalyzer.__gettype__(lexic.__getindex__(lexic.__getlexeme__(i-2))) == "real"):
                file.write('scanf("%lf", &' + lexic.__getlexeme__(i-2) + ');\n')
        if (tree.father == None):
            tree.father = Tree()
        tree.father.lexeme = lexeme
        if (tree.father.left == None):
            tree.father.left = tree
        else:
            tree.father.right = tree
        tree = tree.father
    elif(rule == 12):
        if (tree.father == None):
            tree.father = Tree()
        tree.lexeme = lexic.__getlexeme__(i-2)
        if('"' in tree.lexeme):
            file.write('printf(' + tree.lexeme + '");\n')
        else:
            file.write('printf(' + tree.lexeme + ');\n')
        if (tree.father.left == None):
            tree.father.left = tree
        else:
            tree.father.right = tree
        tree = tree.father
    elif(rule == 13):
        if (tree.father == None):
            tree.father = Tree()
        if (tree.father.left == None):
            tree.father.left = tree
        else:
            tree.father.right = tree
        tree.father.lexeme = lexeme
        tree.father.token = token
        tree.father.type = "literal"
        tree = tree.father
    elif(rule == 14):
        if (tree.father == None):
            tree.father = Tree()
        if (tree.father.left == None):
            tree.father.left = tree
        else:
            tree.father.right = tree
        tree.father.lexeme = lexeme
        tree.father.token = token
        tree.father.type = "num"
        tree = tree.father
    elif(rule == 15):
        syntacticanalyzer.__settype__("id", i)
        if (tree.father == None):
            tree.father = Tree()
        if (tree.father.left == None):
            tree.father.left = tree
        else:
            tree.father.right = tree
        tree.father.type = "id"
        tree.father.lexeme = lexeme
        tree.father.token = token
        tree = tree.father
    elif(rule == 16):
        if (tree.father == None):
            tree.father = Tree()
        tree.father.type = "A"
        if (tree.father.left == None):
            tree.father.left = tree
        else:
            tree.father.right
        tree = tree.father
    elif(rule == 17):
        if(lexic.__getlexeme__(i-5) == ";"):
           if(lexic.__getlexeme__(i-1) == ";"):
               file.write(lexic.__getlexeme__(i-4)+syntacticanalyzer.__gettype__(i-3)+lexic.__getlexeme__(i-2)+"\n")
           elif(syntacticanalyzer.__gettype__(lexic.__getindex__(lexic.__getlexeme__(i-4))) == "id"):
                print("Error: Undeclared variable:" + lexic.__getlexeme__(i-3))
           else:
                if(syntacticanalyzer.__gettype__(lexic.__getindex__(lexic.__getlexeme__(i-2))) == syntacticanalyzer.__gettype__(i-2)):
                    file.write(lexic.__getlexeme__(i-4)+syntacticanalyzer.__gettype__(i-3)+lexic.__getlexeme__(i-2)+"\n")
                else:
                    print("Error: different types for attribution")
        else:
            if (syntacticanalyzer.__gettype__(i - 5) == "id"):
                print("Error: Undeclared variable:" + lexic.__getlexeme__(i - 5))
            else:
                if (syntacticanalyzer.__gettype__(i - 6) == syntacticanalyzer.__gettype__(i - 4)):
                    file.write(str(lexic.__getlexeme__(i - 6)) + str(syntacticanalyzer.__gettype__(i - 5)) + tree.lexeme + "\n")
                else:
                    print("Error: different types for attribution")
        if (tree.father == None):
            tree.father = Tree()
        tree.father.type = "CMD"
        if (tree.father.left == None):
            tree.father.left = tree
        else:
            tree.father.right = tree
        tree = tree.father
    elif(rule == 18):
        file.write(syntacticanalyzer.__gettype__(lexic.__getindex__(lexic.__getlexeme__(i-3)))+" "+"T"+str(x)+"\n")
        file.write("T"+str(x)+" = "+lexic.__getlexeme__(i-3)+" "+syntacticanalyzer.__gettype__(i-2)+" "+lexic.__getlexeme__(i-1)+"\n")
        x = x + 1
        if (tree.father == None):
            tree.father = Tree()
        tree.father.type = "LD"
        if (tree.father.left == None):
            tree.father.left = tree
        else:
            tree.father.right = tree
        tree.father.lexeme = "T"+str(x-1)
        if(tree.right != None):
            tree.father.type = tree.right.type
        else:
            tree.father.type = tree.left.type
        tree = tree.father
    elif(rule == 19):
        if (tree.father == None):
            tree.father = Tree()
        tree.father.type = tree.type
        if (tree.father.left == None):
            tree.father.left = tree
        else:
            tree.father.right = tree
        tree.father.type = tree.type
        tree.father.lexeme = tree.lexeme
        tree.father.token = tree.token
        tree = tree.father
    elif(rule == 20):
        if (tree.father == None):
            tree.father = Tree()
        if (tree.father.left == None):
            tree.father.left = tree
        else:
            tree.father.right = tree
        tree.father.type = "id"
        tree.father.lexeme = lexic.__getlexeme__(i-1)
        tree.father.token = token
        tree = tree.father
    elif(rule == 21):
        if (tree.father == None):
            tree.father = Tree()
        if (tree.father.left == None):
            tree.father.left = tree
        else:
            tree.father.right = tree
        tree.father.type = "num"
        tree.father.lexeme = lexic.__getlexeme__(i-1)
        tree.father.token = token
        tree = tree.father
    elif(rule == 22):
        if (tree.father == None):
            tree.father = Tree()
        tree.father.lexeme = "A"
        if (tree.father.left == None):
            tree.father.left = tree
        else:
            tree.father.right = tree
        tree = tree.father
    elif(rule == 23):
        file.write("}\n")
        if (tree.father == None):
            tree.father = Tree()
        tree.father.lexeme = "COND"
        if (tree.father.left == None):
            tree.father.left = tree
        else:
            tree.father.right = tree
        tree = tree.father
    elif(rule == 24):
        file.write("if(T"+str(x-1)+") {\n")
        if (tree.father == None):
            tree.father = Tree()
        tree.father.lexeme = tree.lexeme
        if (tree.father.left == None):
            tree.father.left = tree
        else:
            tree.father.right = tree
        tree = tree.father
    elif(rule == 25):
        file.write("\n"+syntacticanalyzer.__gettype__(lexic.__getindex__(lexic.__getlexeme__(i-3))) + " " + "T" + str(x)+"\n")
        file.write("T" + str(x) + " = " + lexic.__getlexeme__(i-3) + " " + syntacticanalyzer.__gettype__(i-2) + " " + lexic.__getlexeme__(i-1)+"\n")
        x = x + 1
        if (tree.father == None):
            tree.father = Tree()
        tree.father.lexeme = tree.lexeme
        if (tree.father.left == None):
            tree.father.left = tree
        else:
            tree.father.right = tree
        tree = tree.father
    elif(rule == 26):
        if (tree.father == None):
            tree.father = Tree()
        tree.father.lexeme = "BODY"
        if (tree.father.left == None):
            tree.father.left = tree
        else:
            tree.father.right = tree
        tree = tree.father
    elif(rule == 27):
        if (tree.father == None):
            tree.father = Tree()
        tree.father.lexeme = "BODY"
        if (tree.father.left == None):
            tree.father.left = tree
        else:
            tree.father.right = tree
        tree = tree.father
    elif(rule == 28):
        if (tree.father == None):
            tree.father = Tree()
        tree.father.lexeme = "BODY"
        if (tree.father.left == None):
            tree.father.left = tree
        else:
            tree.father.right = tree
        tree = tree.father
    elif(rule == 29):
        if (tree.father == None):
            tree.father = Tree()
        tree.father.lexeme = "BODY"
        if (tree.father.left == None):
            tree.father.left = tree
        else:
            tree.father.right = tree
        tree = tree.father
    elif(rule == 30):
        tree = Tree()
        if (tree.father == None):
            tree.father = Tree()
        tree.father.lexeme = "A"
        if (tree.father.left == None):
            tree.father.left = tree
        else:
            tree.father.right = tree
        tree = tree.father
    file.close()

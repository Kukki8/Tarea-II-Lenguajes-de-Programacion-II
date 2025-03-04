import Graph

rules = {}
init = ""
terminalList = []
precOp = ["<",">","="]

class terminal:
    equalPrec = []
    morePrec = []
    lessPrec = []

# Revisar en el input que el noTerminal este en mayus
# Funcion que anade regla al diccionario de reglas de la gramatica
def addRule(noTerminal, sList):
    # Verificar reglas de gramaticas de operadores
    # No lambda producciones
    if(len(sList) == 0):
        if(not isInit(noTerminal)):
           print("Esta es una lambda-produccion y el simbolo " + noTerminal + " no es inicial")
           return False
        
    # No 2 no-terminales juntos
    for i in len(sList) - 1 :
        j = i + 1
        if(sList[i].isUpper() and sList[j].isUpper()):
            print("La regla contiene los siguientes 2 (dos) simbolos no-terminales juntos: ")
            print(sList[i] + " y " + sList[j])
            return False

    # Si la regla logro pasar las verificaciones, se agrega al diccionario
    # Hay que verificar si el no-terminal ya existe en el diccionario
    if(noTerminal in rules):
        # Actualizar regla
        rules[noTerminal].append(sList)

    else:
        rules[noTerminal] = [sList]
    
    return True

# Funcion que verifica si un simbolo es el inicial
def isInit(symbol):
    # Verificamos si ya se determino un simbolo inicial en la gramatica
    if(not init):
        return False
    # Verificamos si el simbolo coincide con nuestro simbolo inicial
    return symbol == init

# Funcion que establece el simbolo inicial de la gramatica
def setInit(noTerminal):
    if(not init):
        init = noTerminal
        return True
    elif(noTerminal == init):
        print("Este simbolo ya fue seleccionado como el inicial anteriormente")
        return True
    else:
        print("El simbolo inicial de la gramatica ya ha sido establecido, es: " + init)
        return False

# Funcion que agrega las precedencias a la gramatica
def addPrec(terminal1, op, terminal2):
    # Verificar si los terminales ya existen en la gramatica
    if(terminal1 not in terminalList):
        print("El simbolo " + terminal1 + " no existe en la gramatica")
        return False
    if(op not in precOp):
        print("El operador " + op + " no es valido")
        return False
    if(terminal2 not in terminalList):
        print("El simbolo " + terminal2 + " no existe en la gramatica")
        return False
    
    # Agregar precedencia
    if(op == "<"):
        terminal1.morePrec.append[terminal2]
        terminal2.lessPrec.append[terminal1]
        return True
    elif(op == ">"):
        terminal1.lessPrec.append[terminal2]
        terminal2.morePrec.append[terminal1]
        return True
    elif(op == "="):
        terminal1.equalPrec.append[terminal2]
        terminal2.equalPrec.append[terminal1]
        return True

# Funcion que genera el grafo respectivo
# Debe verificar la existencia de ciclos 
def build():
    return True
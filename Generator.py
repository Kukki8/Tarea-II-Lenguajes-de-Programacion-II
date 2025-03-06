from Graph import Graph

rules = {}
init = None
terminalList = {}
precOp = ["<",">","="]
isBuilt = False

class Terminal:
    def __init__(self,name):
        self.name = name
        self.equalPrec = []
        self.morePrec = []
        self.lessPrec = []


# Revisar en el input que el noTerminal este en mayus
# Funcion que anade regla al diccionario de reglas de la gramatica
def addRule(noTerminal, sList):

    # Verificar reglas de gramaticas de operadores
    # No lambda producciones
    if(len(sList) == 0):
        if(not isInit(noTerminal)):
           print("ERROR: Esta es una lambda-producción y el símbolo " + noTerminal + " no es inicial")
           print("No corresponde con una gramática de operadores")
           return False
        
    # No 2 no-terminales juntos
    for i in range(len(sList) - 1) :
        j = i + 1
        if(sList[i].isupper() and sList[j].isupper()):
            print("ERROR: La regla contiene los siguientes 2 (dos) símbolos no-terminales juntos: ")
            print(sList[i] + " y " + sList[j])
            print("No corresponde con una gramática de operadores")
            return False

    for i in sList:
        if(i not in terminalList and not i.isupper()):
            terminalList[i] = Terminal(i)

    # Si la regla logro pasar las verificaciones, se agrega al diccionario
    # Hay que verificar si el no-terminal ya existe en el diccionario
    if(noTerminal in rules):
        # Actualizar regla
        rules[noTerminal].append(sList)
        
    else:
        rules[noTerminal] = [sList]

    rulePrint = rulePrepForPrint(sList)
    print("La regla \"" + noTerminal + " -> " + rulePrint + "\" ha sido agregada a la gramática")
    return True

# Funcion que verifica si un simbolo es el inicial
def isInit(symbol):
    global init

    # Verificamos si ya se determino un simbolo inicial en la gramatica
    if(init is not None):
        return False
    # Verificamos si el simbolo coincide con nuestro simbolo inicial
    return symbol == init

# Funcion que prepara la regla deseada en forma de string para ser impresa con facilidad
def rulePrepForPrint(sList):
    rulePrint = ""
    for i in range(len(sList) - 1):
        rulePrint += sList[i] + " "

    rulePrint += sList[-1] 
    return rulePrint

# Funcion que establece el simbolo inicial de la gramatica
def setInit(noTerminal):
    global init

    if(init is None):
        init = noTerminal
        print("El símbolo \"" + noTerminal + "\" ha sido seleccionado como símbolo inicial de la gramática ")
        return True
    elif(noTerminal == init):
        print("WARNING: Este símbolo ya fue seleccionado como el inicial anteriormente")
        return True
    else:
        print("ERROR: El símbolo inicial de la gramática ya ha sido establecido anteriormente, es: " + init)
        return False

# Funcion que agrega las precedencias a la gramatica
def addPrec(terminal1Str, op, terminal2Str):
    # Verificar si los terminales ya existen en la gramatica
    if(terminal1Str not in terminalList):
        print("ERROR: El símbolo " + terminal1Str + " no existe en la gramática")
        return False
    if(op not in precOp):
        print("ERROR: El operador " + op + " no es válido")
        return False
    if(terminal2Str not in terminalList):
        print("ERROR: El símbolo " + terminal2Str + " no existe en la gramática")
        return False
    
    # Los terminales existen en la gramatica

    terminal1 = terminalList[terminal1Str]
    terminal2 = terminalList[terminal2Str]

    # Agregar precedencia
    if(op == "<"):
        terminal1.morePrec.append(terminal2)
        print(" \"" + terminal1Str + "\" tiene menor precedencia que \"" + terminal2Str + "\"")
        return True
    elif(op == ">"):
        terminal1.lessPrec.append(terminal2)
        print(" \"" + terminal1Str + "\" tiene mayor precedencia que \"" + terminal2Str + "\"")
        return True
    elif(op == "="):
        terminal1.equalPrec.append(terminal2)
        print(" \"" + terminal1Str + "\" tiene igual precedencia que \"" + terminal2Str + "\"")
        return True

# Funcion que genera el grafo respectivo
# Debe verificar la existencia de ciclos 
def build(terminalList):

    # Verificar si hay un ciclo. De ser asi, mostrar error/evidencia

    graph = Graph()

    # 1) Armar el grafo/diccionario con las keys/nombres de los terminales
    for k,t in terminalList.items():
        graph.addNode("f" + t.name)
        graph.addNode("g" + t.name)

    # 2) Buscar si existen terminales con igual precedencia para armar las clases de equivalencia
        # 2.1) Unir tales nodos siguiendo el procedimiento del libro
    for k,t in terminalList.items():
        for p in t.equalPrec:
            graph.joinNodes(t.name,p.name)
        

    # 3) Establecer aristas a traves de las precedencias de los terminales
    for k,t in terminalList.items():
        for lp in t.lessPrec:
            graph.addEdge("f" + t.name,"g" + lp.name)
        
        for mp in t.morePrec:
            graph.addEdge("g" + mp.name, "f" + t.name )

    # 4) Usar DFS para buscar los caminos mas largos desde c/nodo
    for currentKey,value in graph.nodes.items():
        graph.DFS(currentKey)

    # 5) Imprimir resultados de F y G
    print("Analizador sintáctico construido")

    # Imprimir valores de f
    print("Valores para F: ")
    for currentKey,value in graph.nodes.items():
        
        if(currentKey.startswith("f")):
            print(currentKey,value.longestPath)

    # Imprimir valores de g
    print("Valores para G: ")
    for currentKey,value in graph.nodes.items():
        if(currentKey.startswith("g")):
            print(currentKey,value.longestPath)

    return True

# Funcion que realiza el proceso de analisis sintactico 
def parse(terminal, terminalList):
    push($)
    e,result <- trunc(W), <>
    repetir
        p <- top()
        if(p == $ and e == $):
           return result
        if(p < e or p = e):
            push(e)
            shift(e,w)
        elif(p > e):
            while(top() < x)
                x <- pop()
            result <- result++ <A -> a)
        else:
            error()
    return True


def main():
    print("Bienvenido a su Generador de analizadores sintácticos para gramáticas de operadores de preferencia! (Sí es su favorito, no? O.O!)")
    dolar = Terminal("$")
    terminalList["$"] = dolar

    while True:
        command = input() 
        strCommand = command.split()
        caseCommand = strCommand[0].lower()

        match caseCommand:
            case "rule":
                noTerminal = strCommand[1]
                if(not noTerminal.isupper()):
                    print("ERROR: \"" + noTerminal + "\" no es un símbolo no-terminal")
                    continue

                addRule(noTerminal,strCommand[2:])

            case "init":
                noTerminal = strCommand[1]
                if(not noTerminal.isupper()):
                    print("ERROR: \"" + noTerminal + "\" no es un símbolo no-terminal")
                    continue

                setInit(noTerminal)

            case "prec":
                if(len(strCommand) != 4):
                    print("ERROR: Cantidad de argumentos inválida. Verifique el comando nuevamente")
                    continue
                
                terminal1Str = strCommand[1]
                op = strCommand[2]
                terminal2Str = strCommand[3]

                addPrec(terminal1Str, op, terminal2Str)

            case "build":
                isBuilt = build(terminalList)

            case "parse":
                if(not isBuilt):
                    print("ERROR: Aún no se ha construido el analizador sintáctico")
                    continue
                elif(init is None):
                    print("ERROR: Aún no se ha determinado un símbolo inicial")
                    continue

                parse()

            case "exit":
                print("Nos vemos pronto! (Verdad que sí...? O.o??)")
                break


if __name__=="__main__":
    main()
 #!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# se importan las libre
import os
from time import time

class Node: # declaracion de variables para crear los nodos
    # properties
    probability = 0.0 # inicializamos 
    symbol = ""
    encoding = "" 
    visited = False
    parent = -1 # longitud de 0 a -1

class Huffman: # declaracion de variables para la creacion del arbol de Huffman
    Tree = None # retornar arbol
    Root = None # retornar raiz
    Nodes = [] #Lista
    probs = {} #bloque
    dictEncoder = {}
    
    # methods
    def __init__(self, symbols):
        self.initNodes(symbols)
        self.buildTree()
        self.buildDictionary()

    def initNodes(self, probs): # creamos los nodos con sus respectivas probabiliddes
        for symbol in probs:
            node = Node() # inicializamos el node
            node.symbol = symbol 
            node.probability = probs[symbol] # asignamos una probabilidad a cada simbolo o letra
            node.visited = False # variable q no es fija que va ir cambiando 
            self.Nodes.append(node) # creamos una lista por cada nodo creado
            self.probs[symbol]=probs[symbol]  # establece para cada probabilidad un simbolo         


    def buildTree(self): # Realizamos las operaciones de acuerdo al regamente para la construccion del arbol de Huffman
        indexMin1 = self.getNodeWithMinimumProb() # Buscamos el menor numero de la primera probabilidad
        indexMin2 = self.getNodeWithMinimumProb() # Buscamos el menor numero de la segunda probabilidad 
        
        while indexMin1 != -1 and indexMin2 != -1: # != evalúa como verdadero si 2 variables son diferentes
            node = Node() # inicializamos
            node.symbol = "."
            node.encoding = ""
            # llamamos a las dos probabilidades minimas
            prob1 = self.Nodes[indexMin1].probability
            prob2 = self.Nodes[indexMin2].probability
            node.probability = prob1 + prob2 # sumamos las probabilidades
            node.visited = False # false = 1
            node.parent = -1 # restamos la probabilidad a -1
            self.Nodes.append(node)
            self.Nodes[indexMin1].parent = len(self.Nodes) - 1 #  lista o cadena que queremos medir
            self.Nodes[indexMin2].parent = len(self.Nodes) - 1
            
            # Regla: 0 a mayor probabilidad, 1 a menor probabilidad.
            if prob1 >= prob2:
                self.Nodes[indexMin1].encoding = "0"
                self.Nodes[indexMin2].encoding = "1"
            else:
                self.Nodes[indexMin1].encoding = "1"
                self.Nodes[indexMin2].encoding = "0"
            
            indexMin1 = self.getNodeWithMinimumProb()
            indexMin2 = self.getNodeWithMinimumProb()

    def getNodeWithMinimumProb(self): # realizamos una comparacion para obteener el nodo de menor probabilidad
        minProb = 1.0   # La minima probabilidad no puede ser mayor de 1
        indexMin = -1 # indice para restar a la probalidad

        for index in range(0, len(self.Nodes)): # index es el numero de probabilidad 
            if (self.Nodes[index].probability < minProb  and 
               (not self.Nodes[index].visited)):
                minProb = self.Nodes[index].probability
                indexMin = index

        if indexMin != -1:
            self.Nodes[indexMin].visited = True

        return indexMin
   
    def showSymbolEncoding(self, symbol): # designamos un codigo binario a cada simbolo resuelto por el arbol de Huffman
        found = False
        index = 0
        encoding = ""

        for i  in range(0, len(self.Nodes)):
            if self.Nodes[i].symbol == symbol:
                found = True
                index = i
                break 
        
        if found: # encontro 
            while index != -1: # si son diferentes
                encoding = "%s%s" % (self.Nodes[index].encoding, encoding)      
                index = self.Nodes[index].parent
        else:
            encoding = "simbolo desconocido"

        return encoding

    def buildDictionary(self): # creamos un diccionario, guardamos todos los simbolos con sus respectivos codigos binarios
                               # resueltos por el arbol de Huffman
        for symbol in self.probs:
            encoding = self.showSymbolEncoding(symbol)
            self.dictEncoder[symbol] = encoding
                
    def encode(self, plain): # agrupa los codigos binarios codificados de acuerdo al mensaje escrito en consola
        encoded = ""
        for symbol in plain:
            encoded = "%s%s" % (encoded, self.dictEncoder[symbol])

        return encoded

    # INICIO DE LA DECODIFICACION ....................................................................................................................................................
    def decode(self, encoded): # recibe la cadena del codigo binario enviado desde el emisor para decodificar
        index = 0
        decoded = ""
    

        while index < len(encoded): # mientras buscamos en la longitud de la parte codificada

    
            founf = False # establesemos una variable
    
            aux = encoded[index:] # va a buscar a cada parte codificada un simbolo
                                  # no va ser fija va ir buscando cual es compatible con cada una

    
            for symbol in self.probs:
                if aux.startswith(self.dictEncoder[symbol]): # se comprueba si la cadena es verdadera o falsa. si la parte axuliar inicia dentro del diccionario encodificado  nos va a dar
                    decoded = "%s%s" % (decoded, symbol) # parte decodificada
                    index = index + len(self.dictEncoder[symbol]) # busqueda para cada simbolo a cada probabilidad
                    break 
        
        return decoded

    #FIN DE LA DECODIFICACION ..........................................................................................................................................................

    




if __name__=="__main__":
    
    print "INGRESAR LOS SIMBOLOS O UN MENSAJE QUE DESEA COMPRIMIR:"
    print " " 
    mensaje = raw_input()
    print " "

    print "NUMERO TOTAL DE SIMBILOS O BITS INTRODUCIDOS PARA SER ENVIADOS:  %s" % (len(mensaje))
    print " "
    print "[ 1 PASO]: NUMERO DE SIMBOLOS O BITS, ERRADOS O REPETIDOS "
    print " "
    simbolos=''
    probabilidad=[]
    msm=mensaje
    d=0
    
    for i in mensaje:
        if i in msm:
            print i,"=",int ( msm.count(i))
            simbolos+=i
            probabilidad.append(float(float ( msm.count(i))/float(len(mensaje))))
            msm=msm.replace(i,'')
            d+= 1
         
    symbols=dict(zip(simbolos, probabilidad))
    print " "
    print "NUMERO DE SIMBOLOS COMPRIMIDOS=",d
    print " "
    print "[ 2 PASO]:PROBABILIDAD DE CADA SIMBOLO P(S)= (numero de bit errados) / (numero total de bit enviados)"
    print " "
    print symbols
    print " "
    print "[ 3-4 PASO]: LA FUNCION [buildTree] DEL CODIGO. ORDENA LAS PROBABILIDADES DE MENOR A MAYOR PROBABILIDAD"
    print "           Y REALIZA LAS OPERACIONES YA EXPLICADAS QUE SE REQUIEREN PARA IR ARMANDO EL ARBOL DE HUFFMAN"
    print " "

    
    tiempo_inicial= time()


    # codificar instancia
    huffman = Huffman(symbols)
    print "..........................................................................."
    print "...........................CODIFICACION...................................."
    print "..........................................................................."
    print " "
    print " "
    print "[ 5 PASO]:CODIFICACION BINARIA USANDO EL ARBOL DE HUFFMAN:"
    print " "
    for symbol in symbols:
        print "Simbolo: %s; Codificacion: %s" % (symbol, huffman.showSymbolEncoding(symbol))

    encoded = huffman.encode(mensaje)
    print " "
    print "Mensaje que se esta codificando: %s;" % (mensaje)
    print " "
    print "Codificacion en bits : %s" % (encoded)
    print " "
    print "La longitud de codigo binario es:  %s" % (len(encoded))
    
    data = encoded
   
    print " "
    print "Codigo codificado que esta siento enviado al receptor:  %s" % (data)

    # DECODIFICACION
    print " "
    print " "
    print " "
    print " "
    print "..........................................................................."
    print "...........................DECODIFICACION.................................."
    print "..........................................................................."
    print " "
    print " "
    print "Esperando el mensaje del emisor para su decodificacion......"

    
    decoded = huffman.decode(data)
    print " "
    print "CODIGO BINARIO RECIBIDO ES :", data 
    print " "
    print "DECODIFICANDO EL CODIGO...................................."
    print " "
    print "Mensaje decodificado : %s " % (decoded)

    # FIN


    tiempo_final= time()
    tiempo_ejecucion= tiempo_final - tiempo_inicial
    print " "
    print 'El tiempo de transmisiOn es:',tiempo_ejecucion #En segundos

    

os._exit(0)

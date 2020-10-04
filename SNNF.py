"""System Nemotechnic Number Form.
    ---ÈS]---
    Simulación computacional de las operaciones mentales realizadas por
    un experto en técnicas de memoria aplicadas a la memorización
    de series de números enteros. Usando las técnicas de número forma,
    y método de la cadena.
    
    El programa simula la memoria sensorial, la memoria de corto plazo,
    la memoria de trabajo y la memoria de largo plazo, ademas del foco
    de atención.
    
    Se puede lograr ejecutar un conjunto de operaciones mentales de
    tipo simbólico. Éste programa es una representación abstracta
    de bajo nivel de talles. Pero representa los estados internos
    de un nemonista a nivel general.
    ---[EN]---
        Computer simulation of the mental operations performed by
    an expert in memory techniques applied to memorization
    of integer series. Using the number form techniques,
    and chain method.
    
    The program simulates the sensory memory, the short term memory,
    working memory and long-term memory, in addition to the focus
    of attention.
    
    A set of mental operations can be achieved by
    symbolic type. This program is an abstract representation
    of bjao size level. But it represents the internal states
    of a nemonist on a general level.
    
    Fuentes:
    https://es.stackoverflow.com/questions/238067/imprimir-elementos-de-una-lista-de-3-en-3-en-python
    https://stackoverflow.com/questions/5389507/iterating-over-every-two-elements-in-a-list
    https://www.chessprogramming.org/index.php?title=EPAM&mobileaction=toggle_view_mobile
    https://www.chessprogramming.org/MAPP
    https://www.chessprogramming.org/Chunking
    https://www.chessprogramming.org/Herbert_Simon
    https://www.chessprogramming.org/Kevin_J._Gilmartin
    https://www.chessprogramming.org/CHREST
"""
import time
import random 
# Entrada de datos númericos en bruto.
lectura = input("Leer números: ")

# Diccionario interno para codificar los dígitos.
codificación = {0:'pelota', 1:'bastón', 2:'pato',
                3:'culo', 4:'barco de vela', 5:'garfio',
                6:'palo de golf', 7:'pipa',8:'gafas',
                9:'raqueta'}

# Lista de posibles asociaciones para enlazar codificaciones.
asociación = [' salta en ', ' empuja a ', ' muerde a ',
              ' quema a ', ' golpea a ', ' escupe a ']

decodificación = {value : key for (key, value) in codificación.items()}

def grouper(iterable, n):
    """Iterador que devuelve en cada iteración una tupla con n elementos
    que va extrayendo del iterable"""

    args = [iter(iterable)] * n
    return zip(*args)

def is_blacklisted(frase, palabras):
     """ Filtra de una lista elementos prohibidos""" 
     for palabra in palabras:
         if palabra in frase:
             return True
     return False

# Verificamos que son dígitos.
if lectura.isdigit():
    sensorial = [] # Memoria sensoral
    foco=[]
    # Lee la lista de datos y agrupa por
    # orden creciente de dos en dos.
    # Listas pares cómo impares.
    time.sleep(0.5) # 500 milisegundos por operación mínima.
    pares=zip(lectura,lectura[1:])
    # bucle que lee los números.
    for par in pares:
        # Tripleta del foco.
        sensorial.append(par)
    for bit in sensorial: # Lee cada par
        # Agrega el primer digito del par.
        time.sleep(0.5) # 500 milisegundos por operación mínima.
        foco.append(codificación[int(bit[0])])
        # asocia el dato 1 con ...
        time.sleep(0.5) # 500 milisegundos por operación mínima.
        foco.append(random.choice(asociación))
        # ... dato dos.
        time.sleep(0.5) # 500 milisegundos por operación mínima.
        foco.append(codificación[int(bit[1])])
    # Imprime lo memorizado.
    print(foco)
    print("Leo nemotécnias para recuperar los dígitos.")
    for trio in grouper(foco, 3):
        time.sleep(0.5) # 500 milisegundos por operación mínima.
        for linea in trio:
            print(linea)
        print("---")
    print("Una vez recuperadas, recito los números")
    time.sleep(0.5) # 500 milisegundos por operación mínima.
    filtradas = [foc for foc in foco if not is_blacklisted(foc,asociación)]
    time.sleep(0.5) # 500 milisegundos por operación mínima.
    for filtro in filtradas:
        time.sleep(0.5) # 500 milisegundos por operación mínima.
        print(decodificación[filtro])
else:
    print('No son números')

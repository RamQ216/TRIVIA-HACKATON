#Utilizamos el modulo random de python, que nos ayuda a utilizar las funciones propias del archivo 'random'.  

import random

#Definimos la funcion elegir preguntas. El parametro que se define seria una lista.
def elegir_pregunta(preguntas):

#Utilizamos 'len' para saber si la lista contiene aun elementos.
#Entonces si la lista ya no tiene elementos retorna nada

    if len(preguntas) == 0:
        return None


#con randint lo que hacemos es generar un numero aleatorio entre 0 y n (depende de la longitud de la lista)
#de manera que las preguntas sean aleatorias.

    indice = random.randint(0, len(preguntas) - 1)
    

#Utilizamos .pop para que la pregunta que haya salido se saque de la lista, asi no se repiten las preguntas
#Pop hace esta tres cosas
#1️⃣ toma un elemento de la lista
#2️⃣ lo devuelve
#3️⃣ lo elimina de la lista

    pregunta = preguntas.pop(indice)
    
    return pregunta

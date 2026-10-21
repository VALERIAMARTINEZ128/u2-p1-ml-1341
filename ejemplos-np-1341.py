import numpy as np 

califas=np.array([60,70,90])
print("----------  eje 1  imprimir califas -----")
print(califas) # imprime la lista de califas
print(type(califas)) # muestra el tipo de arreglo 
print("----------  eje 0  dimensiones de una array  -----")
califas=np.array(60)
print(califas)
print("dimension :", califas.ndim)
print("----------  eje 1  dimension de una array  -----")
califas=np.array([60,70,90])
print(califas)
print("dimension :", califas.ndim)
print("----------  eje 2  dimensiones de una array  -----")
califas=np.array([
    [60,70,90],
    [50,80,98]
    ]) # un arreglo de 2 dimensiones es como una tabla  en excel
print(califas)
print("dimension :", califas.ndim)
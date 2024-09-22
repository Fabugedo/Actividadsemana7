#Actividad semana 7
#Actividad matrices
import numpy as np
arregloA = np.random.randint(0, 101, size=(3,3))
print(arregloA)
print("promedio de los elementos: ", arregloA.mean())
print("suma de los elementos: ", arregloA.sum())
print("elemento mayor: ", arregloA.max())
print("elemento menor: ", arregloA.min())
print("diagonal principal: ", np.diag(arregloA))

#actividad matrices con 0 y diagonal 1-2-3
import numpy as np
matriz = np.zeros((3, 3))
matriz = np.diag([1, 2, 3])
print(matriz)
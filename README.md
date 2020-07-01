# N-queens
N queens 

# Resolviendo el problema de las N reinas con Python, PyQt5 y Pygame

El problema de las N-reinas consiste en la resolución de un problema matemático de origenes antiguos. 

Su temática es, dado un tablero de ajedrez de tamaño NxN, colocar N reinas de forma que ninguna de ellas sea capaz de matarse.

Un ejemplo de ello, sería la configuración para un tablero de 4x4 como la siguiente:

E R E E
E E E R
R E E E
E E R E

Donde cada espacio vacío es representado por la letra E y una reina por la letra R


Para resolver este problema se utilizó el algoritmo de Evolución Diferencial (Differential Evolution), generando un conjunto de soluciones candidatas y mejorando
su performance para así llegar a la solución óptima, la cuál se entiende como un acomodo perfecto de las reinas en el tablero.


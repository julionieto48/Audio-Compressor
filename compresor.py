import math

A=[1,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10]
r = 2 #input('ingrese valor de entrada ')  #entrada maxima

tresh = 5 # entrada en dB
attack = 3#500 #milisegundos
release = 0,0002

instante_maximo_ataque = math.log(r, math.e)
atake = 3 #int(attack/(1000*float(44100)))  #relacion cuadros milisegundos
T = 1 #/44100
f = []
for j in range(1, atake+1):
    R = math.log(j * T, math.e)
    f.append(R)

print f
n = 1 #valor que cambia

for i in range(len(A)):
    A[i] = A[i]/float(n)
    if A[i] > tresh:
        n = math.log(i * T, math.e)
    if i == attack:
        n = instante_maximo_ataque

print A

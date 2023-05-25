from math import sqrt

# Calcular el área y perimetro de un triangulo conociendo sus tres lados
# Esta se calcula utilizando la formula de Herón
#  por lo general tiene un mayor uso en los triangulos escalenos
# es por eso que asumieremos que el programa se va a utilizar 
# para los calculos relacionados con estos triangulos

la = float(input("Ingresa el lado a: "))
lb = float(input("Ingresa el lado b: "))
lc = float(input("Ingresa el lado c: "))

# calcular el semiperímetro

s = (la + lb + lc) / 2
# Calcualar el area
a = sqrt(s * (s -la) * (s-lb) * (s-lc))

# Calcualar el perimetro de un triangulo escaleno

p = la + lb + lc

print("Área del rectangulo es: {:.1f}".format(a))
print("Perímetro del triangulo: {:.1f}".format(p))

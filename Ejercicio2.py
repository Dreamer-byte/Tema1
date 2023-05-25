b = float(input("Ingresa la base del rectangulo: "))
h = float(input("Ingresa la altura del rectangulo: ")) 

#Area base x altura
a = b*h
# Perimetro es 2xb + 2xh

p = 2*b + 2*h

# Estas son medidas cuadradas por lo que
# si las medidas fueran cm seria cm^2 (centimetros cuadrados)
print("El área del rectangulo es: {}".format(a))
print("El perímetro del rectangulo es: {}".format(p))
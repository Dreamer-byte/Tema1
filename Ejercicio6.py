c = float(input("Ïngresa el capital incial: "))
x = float(input("Ingresa la tasa de interes: "))
n = int(input("Ingresa la cantidad de años: "))

capital_Final = c * (1+x/100) ** n

print(f"{c}$ al {x}% de interes anual se convierte en {capital_Final:.2f}$ al cabo de {n} años ")
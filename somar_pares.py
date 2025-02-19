numeros = 0
somar = 0

while numeros <= 100:
    if(numeros % 2 == 0):
        print("numeros: ", numeros)
        somar += numeros
    numeros += 1

print("Somatória: ", somar)

def converter_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def converter_fahrenheit(celsius):
    fahrenheit = celsius * 1.8 + 32 
    return fahrenheit

tipo = 0 

while tipo != 1 and tipo != 2:
    tipo = int(input("(1): C to F // (2): F to C: "))

if tipo == 1:
    temp_celsius = float(input("Digite a temperatura em Celsius: "))
    print("Temperatura convertida para Fahrenheit: ", converter_fahrenheit(temp_celsius))
elif tipo == 2:
    temp_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    print("Temperatura convertida para Celsius:", converter_celsius(temp_fahrenheit))
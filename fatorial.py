def calculo_fatorial(numero):
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial

numero = int(input("Digite um número: "))  # Convertemos a entrada para inteiro
print("Fatorial:", calculo_fatorial(numero))
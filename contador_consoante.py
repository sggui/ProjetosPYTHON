def contar_vogais(palavra):
    vogais = "aeiouAEIOU"
    contador = 0
    
    for letra in palavra:
        if letra in vogais:
            contador += 1
            
    return contador

palavra = input("Digite uma palavra: ")
print("Quantidade de vogais:", contar_vogais(palavra))
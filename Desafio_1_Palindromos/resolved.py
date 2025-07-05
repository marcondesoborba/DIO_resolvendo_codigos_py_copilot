#Descrição: Vamos testar se uma palavra é um palíndromo?! 
#Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.
def main():
    # Recebe uma palavra do usuário
    palavra = input("Digite uma palavra: ")
    
    # Inverte a palavra
    palavra_invertida = palavra[::-1]
    
    # Verifica se a palavra é um palíndromo
    if palavra.lower() == palavra_invertida.lower():
        print(f"A palavra '{palavra}' é um palíndromo.")
    else:
        print(f"A palavra '{palavra}' não é um palíndromo.")
if __name__ == "__main__":
    main()
# # Exemplo de uso:
# # Digite uma palavra: arara
# # A palavra 'arara' é um palíndromo.
# # Digite uma palavra: python
# # A palavra 'python' não é um palíndromo
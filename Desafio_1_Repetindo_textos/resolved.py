#Descrição: Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado. 
def main():
    # Recebe a string do usuário
    texto = input("Digite uma string: ")
    
    # Recebe o número inteiro do usuário
    numero = int(input("Digite um número inteiro: "))
    
    # Repete a string o número de vezes informado
    resultado = texto * numero
    
    # Exibe o resultado
    print("Resultado da repetição:", resultado)
if __name__ == "__main__":

    main()
# 
# Exemplo de uso:
# Digite uma string: Python
# Digite um número inteiro: 3
# Resultado da repetição: PythonPythonPython
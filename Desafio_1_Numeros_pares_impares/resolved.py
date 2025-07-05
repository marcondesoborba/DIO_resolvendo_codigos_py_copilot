#Descrição: Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. 
#Uma dica é: Utilize condicionais para realizar a verificação e, se possível, faça uso do Github Copilot(ou outra IA) para otimizar a estrutura do código.

def main():
    # Recebe um número inteiro do usuário
    numero = int(input("Digite um número inteiro: "))
    
    # Verifica se o número é par ou ímpar
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")
if __name__ == "__main__":
    main()
# # Exemplo de uso:
# # Digite um número inteiro: 4
# # O número 4 é par.
# # Digite um número inteiro: 7
# # O número 7 é ímpar.
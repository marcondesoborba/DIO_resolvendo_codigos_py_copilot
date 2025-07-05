#Descrição: Agora vamos calcular a média de três notas fornecidas na entrada do usuário. Uma dica é: Utilize operadores aritméticos para realizar o cálculo da média.
def main():
    # Recebe as três notas do usuário
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    
    # Calcula a média
    media = (nota1 + nota2 + nota3) / 3
    
    # Exibe o resultado
    print(f"A média das notas é: {media:.2f}")
if __name__ == "__main__":
    main()
# # Exemplo de uso:
# # Digite a primeira nota: 7.5
# # Digite a segunda nota: 8.0
# # Digite a terceira nota: 9.0
# # A média das notas é: 8.17
# # Digite a primeira nota: 6.0
# # Digite a segunda nota: 5.5
# # Digite a terceira nota: 7.0
# # A média das notas é: 6.17
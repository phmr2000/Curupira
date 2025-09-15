from ast import main


def ler_dados ():
    for  i in range(5):
        nome, idade = ler_dados()
        resultado = verificar_idade(idade)
        exibir_resultado(nome, resultado)

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    return nome, idade

def verificar_idade(idade):
    return "Maior de idade" if idade >= 18 else "Menor de idade"

def exibir_resultado(nome,resultado):
    print(f"{nome} é {resultado}")

    def main():
     verificar_idade()
     exibir_resultados()

    

if __name__ == "__main__":
    main()
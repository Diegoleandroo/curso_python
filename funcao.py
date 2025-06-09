# 1 - Função para imprimir uma mensagem de boas-vindas
def boas_vindas():
    print("Bem-vindo ao sistema de filmes")

# Chama a função para exibir a mensagem de boas-vindas
boas_vindas()


# 2 - Função para calcular a média de notas de um filme
def calcular_media():
    # Solicita ao usuário a quantidade de avaliações
    num_avaliacoes = int(input("Digite quantas avaliações deseja fazer para o filme: \n"))
    total = 0  # Inicializa a variável que acumulará a soma das notas

    # Laço para receber as notas do usuário
    for i in range(num_avaliacoes):
        nota = float(input("Digite a nota para o filme: \n"))
        total += nota  # Soma cada nota ao total

    # Calcula a média se houver avaliações
    if num_avaliacoes > 0:
        media = total / num_avaliacoes
    else:
        media = 0  # Caso nenhuma avaliação tenha sido feita, a média será zero

    return media  # Retorna a média calculada

# Imprime a média formatada com duas casas decimais
print(f"A média de avaliações é: {calcular_media():.2f}")


# 3 - Função para cadastrar um filme
def cadastrar_filme():
    # Solicita ao usuário as informações do filme
    nome = input("Digite o nome do filme: ")
    ano_lancamento = int(input("Digite o ano de lançamento do filme: \n"))
    preco = float(input("Digite o preço do filme: \n"))
    nota = float(input("Digite a nota do filme: \n"))

    # Exibe os dados do filme formatados
    print(f"{nome} ({ano_lancamento}) - R$ {preco:.2f} - Nota: {nota}")

# Chama a função duas vezes para cadastrar dois filmes
cadastrar_filme()
cadastrar_filme()

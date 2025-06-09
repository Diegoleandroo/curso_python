# 1 - Função para imprimir um nome completo
def nome_completo(primeiro_nome, sobrenome):
    # Imprime o nome completo usando interpolação de strings (f-string)
    print(f"Nome é: {primeiro_nome} {sobrenome}")

# Chama a função passando o primeiro nome e o sobrenome
nome_completo("Leandro", "Lima")


# 2 - Função para somar dois números
def somar_numeros(a, b):
    # Retorna a soma de 'a' e 'b'
    return a + b

# Imprime o resultado da soma de 10 + 50
print(f"Soma é: {somar_numeros(10, 50)}")


# 3 - Função com parâmetro padrão (default)
def endereco(pais="Brasil"):
    # Exibe o país onde a pessoa mora, usando o valor padrão se nenhum for passado
    print(f"Eu moro em: {pais}")

# Chamada sem argumento usa o valor padrão "Brasil"
endereco()
# Chamada com argumento substitui o valor padrão
endereco("Portugal")

# 4 - Função para avaliar um filme
def avaliar_filme(num_avaliacoes, nome_filme):
    total = 0  # Variável para acumular as notas

    # Laço para coletar as notas informadas pelo usuário
    for i in range(num_avaliacoes):
        nota = float(input("Digite a nota para o filme: \n"))
        total += nota  # Soma a nota ao total

    # Se o número de avaliações for maior que 0, calcula a média
    if num_avaliacoes > 0:
        media = total / num_avaliacoes
    else:
        media = 0  # Se não houver avaliações, a média é 0

    # Exibe a média formatada com duas casas decimais
    print(f"Média de avaliação do filme {nome_filme} é: {media:.2f}")

# Chamada da função passando 2 avaliações para o filme "Sonic"
avaliar_filme(2, "Sonic")

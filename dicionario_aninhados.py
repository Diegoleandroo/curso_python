# Importa o módulo pprint, que serve para imprimir estruturas de dados de forma mais legível
import pprint

# Cria um dicionário chamado filmsDict que contém informações sobre filmes
filmsDict = {
    # Primeira chave do dicionário principal: nome do filme
    "inception": {
        # Ano de lançamento do filme
        "yearRelease": 2010,
        # Nota do filme no IMDb
        "imdbRating": 8.8,
        # Lista com os gêneros do filme
        "genre": ["Sci-fi", "Action", "Thriller"]
    },

    # Segunda entrada: outro filme
    "interstellar": {
        "yearRelease": 2014,
        "imdbRating": 8.6,
        "genre": ["Sci-fi", "Drama"]
    },

    # Terceira entrada: filme com nome contendo letras maiúsculas e espaço
    "The Dark Knight": {
        "yearRelease": 2008,
        "imdbRating": 9.0,
        "genre": ["Action", "Drama", "Crime"]
    }
}

# Cria um objeto PrettyPrinter com profundidade máxima de 4 níveis para impressão formatada
pp = pprint.PrettyPrinter(depth=4)

# Usa o pprint para imprimir o conteúdo do dicionário de forma organizada
pp.pprint(filmsDict)

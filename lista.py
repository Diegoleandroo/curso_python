filmsList = ["Inception", "The Shawshank Redemption", 
             "The Dark Kgnith", "Pulp Fiction", "Interstellar"]


# 1 - Tamanho da lista
print(len(filmsList))

# 2 - Recuperar um item da lista pelo nome
print(filmsList.index("Interstellar")) 

# 3 - Adiccionar um item ao final da lista
filmsList.append("The lord of the Rings")
print(filmsList)

# 4 - Ordenar a lista
filmsList.sort()
print(filmsList)

# 5 - Copiar os itens de um lista para outra
filmsCopy = filmsList.copy()
filmsCopy.remove("Pulp Fiction")
print(filmsCopy)

# 6 - Remove todos os itens da lista
filmsList.clear()
print(filmsList)


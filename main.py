# Type Hint
# Dica de tipagem
# Definir quais serão os tipos das variaveis

# idade: int = 30
# altura: float = 1.75
# nome: str = "Marcelo"
# is_estudante: bool = True

#List
# lista:list = ["Sapato",39,10.38, True]

# dicionario:dict = {
#     "nome":"Sapato",
#     "quantidade":39,
#     "preco":10.38,
#     "disponibilidade": True
# }

# produto01:dict = {
#     "nome":"Sapato",
#     "quantidade":39,
#     "preco":10.38,
#     "disponibilidade": True
# }

# produto02:dict = {
#     "nome":"Televisao",
#     "quantidade":2,
#     "preco":1000.38,
#     "disponibilidade": True
# }

# carrinho:list = []
# carrinho.append(produto01)
# carrinho.append(produto02)

# print(carrinho)
# from typing import Dict, Any #Biblioteca de tipagem
# #Após definir o tipo da variavel livro para dicionario se passa o parametro para definir quais serão 
# #Os tipos de campos dentro do dicionario, por exemplo para Titulo o seu tipo será string
# # E Any indica que dos demais serão de tipos dinâmicos
# livro: dict[str,Any] = {
#     "Titulo": "Game of Thrones",
#     "Autor": "Estagiario",
#     "Ano":2005
# }
# lista_elementos:list = livro.items()
# for elemento in lista_elementos:
#     print(elemento)


# print (livro)

# # Exercise one
# list_1_10:list = list(range(1,11))

# # for i in range(1,11):

# for i in list_1_10:
#     print(i**2)

# # Exercise two
# Language:list = ["Python", "Java", "C++", "JavaScript"]
# Language.remove("C++")
# Language.insert(2,"Ruby")
# #### OR

# Language.append("Ruby2")

# print(Language)

# Exercise tree

Livro:dict = {
    "titulo":"Governance Data",
    "Autor":"Barbieri",
    "Ano":2010
}

List_Itens = Livro.items()
for elemento in List_Itens:
    print(elemento)


print(Livro["titulo"])
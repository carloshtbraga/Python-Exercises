import json  # json é um modulo que vem embutido, porém precisamos importá-lo


with open("pokemon.json") as file:  # leitura do arquivo
    pokemons = json.load(file)[
        "results"
    ]  # o conteúdo é transformado em estrutura python equivalente,
    # dicionário neste caso.
    # acessamos a chave results que é onde contém nossa lista de pokemons
    for poke in pokemons:
        print(poke['name'])

print(pokemons[0])  # imprime o primeiro pokemon da lista

import json

# leitura de todos os pokemons
with open("pokemon.json") as file:
    pokemons = json.load(file)["results"]

# separamos somente os do tipo grama
gtpkmn = [pokemon for pokemon in pokemons if "Electric" in pokemon["type"]]

# abre o arquivo para escrita
with open("eletric_pokemons.json", "w") as file:
    # escreve no arquivo já transformando em formato json a estrutura
    json.dump(gtpkmn, file)

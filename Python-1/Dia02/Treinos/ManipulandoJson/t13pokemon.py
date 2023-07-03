import json

# Leitura de todos os pokemons
with open("pokemon.json") as file:
    pokemons = json.load(file)["results"]

# Separamos somente os do tipo grama
ftypkn = [pokemon for pokemon in pokemons if "Fire" in pokemon["type"]]

# Abre o arquivo para escrevermos apenas o pokemons do tipo grama
with open("fire_pokemons.json", "w") as file:
    json_to_write = json.dumps(
        ftypkn
    )  # conversão de Python para o formato json (str)
    file.write(json_to_write)

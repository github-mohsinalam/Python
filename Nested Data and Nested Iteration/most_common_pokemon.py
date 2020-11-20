#Provided is a dictionary that contains pokemon go player data, where each player reveals the amount of candy each of their pokemon have.
#If you pooled all the data together, which pokemon has the highest number of candy? Assign that pokemon to the variable most_common_pokemon.



pokemon_go_data = {'bentspoon':
                  {'Rattata': 203, 'Pidgey': 120, 'Drowzee': 89, 'Squirtle': 35, 'Pikachu': 3, 'Eevee': 34, 'Magikarp': 300, 'Paras': 38},
                  'Laurne':
                  {'Pidgey': 169, 'Rattata': 245, 'Squirtle': 9, 'Caterpie': 38, 'Weedle': 97, 'Pikachu': 6, 'Nidoran': 44, 'Clefairy': 15, 'Zubat': 79, 'Dratini': 4},
                  'picklejarlid':
                  {'Rattata': 32, 'Drowzee': 15, 'Nidoran': 4, 'Bulbasaur': 3, 'Pidgey': 56, 'Weedle': 21, 'Oddish': 18, 'Magmar': 6, 'Spearow': 14},
                  'professoroak':
                  {'Charmander': 11, 'Ponyta': 9, 'Rattata': 107, 'Belsprout': 29, 'Seel': 19, 'Pidgey': 93, 'Shellder': 43, 'Drowzee': 245, 'Tauros': 18, 'Lapras': 18}}

candy_count = {}
for player in pokemon_go_data:
    for pokemon in pokemon_go_data[player]:
        candy_count[pokemon] = candy_count.get(pokemon, 0) + pokemon_go_data[player][pokemon] 

most_common_pokemon = list(candy_count.keys())[0]
for key in candy_count:
    if candy_count[key] > candy_count[most_common_pokemon]:
        most_common_pokemon = key
    

# OPTIONS
######################################################

startingPoint = 1           # The first pokemon number to be queried
pokemonToBeQueried = 150   # The number of pokemon to be queried.
writeMode = "w"             # To overwite existing file:        "w"
#                           # To append exiting file:           "wa"
filename = 'poke_data2.json'
filename_types = 'poke_types2.json'

apiWaitTime = 0.2
apiURLs = {
    "pokemonURL": "https://pokeapi.co/api/v2/pokemon/",
    "descriptionURL": "https://pokeapi.co/api/v2/pokemon-species/",
    "typesURL": "https://pokeapi.co/api/v2/type/"
}
bootMessage = 'Initializing...\n'
terminationMessage = 'Execution Complete'


# Data OPTIONS
######################################################

dataOptionsDict = {
    'pokemonImage': 'n',
    'pokemonRegion': 'y',
    'pokemonDescription': 'y'
}

# OPTIONS
######################################################

startingPoint = 152           # The first pokemon number to be queried
pokemonToBeQueried = 100   # The number of pokemon to be queried.
writeMode = "w"             # To overwite existing file:        "w"
#                           # To append exiting file:           "wa"
filename = 'johto.json'
filename_types = 'johto_types.json'

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
    'pokemonImage': 'y',
    'pokemonRegion': 'y',
    'pokemonDescription': 'y'
}

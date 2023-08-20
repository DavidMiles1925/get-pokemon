# OPTIONS
######################################################

startingPoint = 1  # The first pokemon number to be queried
pokemonToBeQueried = 2  # The number of pokemon to be queried.
writeMode = "w"  # # To write a new file each time:    "w"
#                  # To append exiting file:           "wa"
filename = 'poke_data.json'

apiWaitTime = 1
apiURLs = {
    "pokemonURL": "https://pokeapi.co/api/v2/pokemon/",
    "descriptionURL": "https://pokeapi.co/api/v2/pokemon-species/"
}
bootMessage = 'Initializing...\n'
terminationMessage = 'Press any key...'

import requests
import utils.options

# GET REQUESTS
######################################################


def getPokemonData(pokeNumber):
    pokemonURL = utils.options.apiURLs['pokemonURL'] + pokeNumber

    resPoke = requests.get(pokemonURL)
    dataPoke = resPoke.json()

    return dataPoke


def getDescriptionData(pokeNumber):
    descURL = utils.options.apiURLs['descriptionURL'] + pokeNumber

    resDesc = requests.get(descURL)
    dataDesc = resDesc.json()

    return dataDesc


def getRegionData(dataDesc):
    regionURL = dataDesc['generation']['url']

    resRegion = requests.get(regionURL)
    dataRegion = resRegion.json()

    return dataRegion


def getSpriteData(pokeNumber, dataPoke):
    spriteURL = dataPoke['sprite']['front_default']
    filename = f'{pokeNumber}.jpg'

    resSprite = requests.get(spriteURL)
    dataSprite = resSprite.content

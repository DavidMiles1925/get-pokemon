import requests
import utils.options
from PIL import Image
from io import BytesIO


# GET POKEMON REQUESTS
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


def getSpriteData(dataPoke):
    spriteURL = dataPoke['sprites']['front_default']
    number = str(dataPoke['id'])
    filename = f'{number}.jpg'

    resSprite = requests.get(spriteURL)
    dataSprite = resSprite.content

    image = Image.open(BytesIO(dataSprite)).convert('RGB')
    image.save(filename, "JPEG")
    print(f"Image saved as {filename}\n")

# GET TYPE REQUESTS
######################################################


def getTypeData(number):
    number = str(number)
    typesURL = utils.options.apiURLs['typesURL'] + number
    resTypes = requests.get(typesURL)
    dataTypes = resTypes.json()
    return dataTypes

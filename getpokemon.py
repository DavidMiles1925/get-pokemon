import requests
import string
import time


# OPTIONS
######################################################

startingPoint = 1  # The first pokemon number to be queried
pokemonToBeQueried = 1008  # The number of pokemon to be queried.
writeMode = "w"  # # To write a new file each time:    "w"
#                  # To append exiting file:           "wa"

apiWaitTime = 1
apiURLs = {
    "pokemonURL": "https://pokeapi.co/api/v2/pokemon/",
    "descriptionURL": "https://pokeapi.co/api/v2/pokemon-species/"
}
bootMessage = 'Initializing...\n'
terminationMessage = 'Press any key...'

# UTILITY FUNCTIONS
######################################################


def displayTerminate():
    print('****************************** ')
    print('Program returned ', (pokemonToBeQueried), ' pokemon.')
    print('******************************\n')
    input(terminationMessage)


# WRITE FUNCTIONS
######################################################


def writeNameNumber(dataPoke):
    number = dataPoke['id']
    name = dataPoke['name']

    fout.write('"number": "' + str(number) + '",\n')
    fout.write('"name": "' + name.capitalize() + '",\n')


def writeRegion(dataRegion):
    region = dataRegion['main_region']['name']
    fout.write('"region": "' +
               region.capitalize() + '",\n')


def writeTypes(dataPoke):
    counter = 0
    for x in dataPoke['types']:
        pokeType = dataPoke['types'][counter]['type']['name']

        fout.write('"type_' + str(counter) + '" : "' +
                   pokeType.capitalize() + '",\n')

        counter = counter + 1


def writeHeightWeight(dataPoke):
    height = dataPoke['height']
    weight = dataPoke['weight']

    fout.write('"height": "' + str(height) + '",\n')
    fout.write('"weight": "' + str(weight) + '",\n')


def writeDescription(dataDesc):
    counter = 0
    for x in dataDesc['flavor_text_entries']:
        if x['language']['name'] == "en":
            break
        counter = counter + 1

    rawDescriptionText = dataDesc['flavor_text_entries'][counter]['flavor_text']
    modDescriptionText = rawDescriptionText.replace("\x0c", " ")
    descriptionText = modDescriptionText.replace("\n", " ")

    fout.write('"description": "' + descriptionText + '",\n')


# BUILD SEQUENCE
######################################################


def buildFile(dataPoke, dataDesc, dataRegion):
    pokemonName = dataPoke['name']
    fout.write('{\n')

    print('Writing: ', pokemonName.capitalize(), '\n')

    writeNameNumber(dataPoke)
    writeRegion(dataRegion)
    writeTypes(dataPoke)
    writeHeightWeight(dataPoke)
    writeDescription(dataDesc)

    fout.write("},\n")


# GET REQUESTS
######################################################


def getPokemonData(pokeNumber):
    pokemonURL = apiURLs['pokemonURL'] + pokeNumber

    resPoke = requests.get(pokemonURL)
    dataPoke = resPoke.json()

    return dataPoke


def getDescriptionData(pokeNumber):
    descURL = apiURLs['descriptionURL'] + pokeNumber

    resDesc = requests.get(descURL)
    dataDesc = resDesc.json()

    return dataDesc


def getRegionData(dataDesc):
    regionURL = dataDesc['generation']['url']

    resRegion = requests.get(regionURL)
    dataRegion = resRegion.json()

    return dataRegion


# REQUEST SEQUENCE
######################################################


def getRequests(pokeNumber):
    pokeNumber = str(pokeNumber)

    dataPoke = getPokemonData(pokeNumber)
    dataDesc = getDescriptionData(pokeNumber)
    dataRegion = getRegionData(dataDesc)

    buildFile(dataPoke, dataDesc, dataRegion)


# REQUEST LOOP
######################################################


def requestLoop():
    for x in range(startingPoint, rangeEnd):
        pokeNumber = x

        print('Requesting: ', pokeNumber)

        getRequests(pokeNumber)
        time.sleep(apiWaitTime)


# MAIN FUNTION
######################################################


if __name__ == "__main__":
    print(bootMessage)
    rangeEnd = startingPoint + pokemonToBeQueried

    fname = 'poke_data.json'
    fout = open(fname, 'w', encoding='utf-8')

    requestLoop()

    displayTerminate()

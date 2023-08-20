import requests
import time
import modules.getRequests
import modules.writePokemon
import utils.options


# UTILITY FUNCTIONS
######################################################


def displayTerminate():
    print('****************************** ')
    print('Program returned ', (utils.options.pokemonToBeQueried), ' pokemon.')
    print('******************************\n')
    input(utils.options.terminationMessage)


# BUILD SEQUENCE
######################################################


def buildFile(dataPoke, dataDesc, dataRegion):
    pokemonName = dataPoke['name']
    fout.write('{\n')

    print('Writing: ', pokemonName.capitalize(), '\n')

    modules.writePokemon.writeNameNumber(dataPoke, fout)
    modules.writePokemon.writeRegion(dataRegion, fout)
    modules.writePokemon.writeTypes(dataPoke, fout)
    modules.writePokemon.writeHeightWeight(dataPoke, fout)
    modules.writePokemon.writeDescription(dataDesc, fout)

    fout.write("},\n")


# REQUEST SEQUENCE
######################################################


def getRequests(pokeNumber):
    pokeNumber = str(pokeNumber)

    dataPoke = modules.getRequests.getPokemonData(pokeNumber)
    dataDesc = modules.getRequests.getDescriptionData(pokeNumber)
    dataRegion = modules.getRequests.getRegionData(dataDesc)

    buildFile(dataPoke, dataDesc, dataRegion)


# REQUEST LOOP
######################################################


def requestLoop():
    for x in range(utils.options.startingPoint, rangeEnd):
        pokeNumber = x

        print('Requesting: ', pokeNumber)

        getRequests(pokeNumber)
        time.sleep(utils.options.apiWaitTime)


# MAIN FUNTION
######################################################


if __name__ == "__main__":
    print(utils.options.bootMessage)
    rangeEnd = utils.options.startingPoint + utils.options.pokemonToBeQueried

    fname = utils.options.filename
    fout = open(fname, utils.options.writeMode, encoding='utf-8')

    requestLoop()

    fout.close()

    displayTerminate()

import utils.options
import utils.constants
import modules.writePokemon
import modules.getRequests
import requests
import time

# UTILITY FUNCTIONS
######################################################


def displayEstimatedRunTime():
    estRunTimeAdjuster = 1.4

    estRunTime = ((utils.options.apiWaitTime *
                  utils.options.pokemonToBeQueried) * estRunTimeAdjuster)
    if estRunTime < utils.constants.SECONDS_IN_A_MINUTE:
        print('Estimated run time: ', estRunTime, 'seconds\n')
    else:
        print('Estimated run time: ', estRunTime /
              utils.constants.SECONDS_IN_A_MINUTE, 'minutes\n')


def displayTerminate(time_start):
    print('****************************** ')
    print('Program returned ', (utils.options.pokemonToBeQueried), ' pokemon.')
    print('******************************\n')

    time_stop = time.perf_counter()
    time_total = time_stop - time_start

    if time_total > utils.constants.SECONDS_IN_A_MINUTE:
        time_total = time_total / utils.constants.SECONDS_IN_A_MINUTE
        unit = 'minutes'
    else:
        unit = 'seconds'

    print(f'Total run time: {time_total} {unit}\n')
    print(utils.options.terminationMessage)
    input('Press any key...')


# BUILD SEQUENCE
######################################################


def buildFile(dataPoke, dataDesc, dataRegion):
    pokemonName = dataPoke['name']
    fout.write('{\n')

    print(f'Writing: {pokemonName.capitalize()}')

    modules.writePokemon.writeNameNumber(dataPoke, fout)
    modules.writePokemon.writeRegion(dataRegion, fout)
    modules.writePokemon.writeTypes(dataPoke, fout)
    modules.writePokemon.writeHeightWeight(dataPoke, fout)
    modules.writePokemon.writeDescription(dataDesc, fout)

    modules.getRequests.getSpriteData(dataPoke)

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
    time_start = time.perf_counter()

    print(utils.options.bootMessage)
    displayEstimatedRunTime()

    rangeEnd = utils.options.startingPoint + utils.options.pokemonToBeQueried

    fname = utils.options.filename
    fout = open(fname, utils.options.writeMode, encoding='utf-8')

    requestLoop()

    fout.close()
    displayTerminate(time_start)

import requests
import time
import modules.getRequests
import modules.writePokemon
import utils.constants
import utils.options


# UTILITY FUNCTIONS
######################################################


def displayEstimatedRunTime():
    estRunTimeAdjuster = 1.6

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

    print('Total run time: ', time_total, ' seconds.\n')
    print(utils.options.terminationMessage)
    input('Press any key...')


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
    time_start = time.perf_counter()

    print(utils.options.bootMessage)
    displayEstimatedRunTime()

    rangeEnd = utils.options.startingPoint + utils.options.pokemonToBeQueried

    fname = utils.options.filename
    fout = open(fname, utils.options.writeMode, encoding='utf-8')

    requestLoop()

    fout.close()
    displayTerminate(time_start)

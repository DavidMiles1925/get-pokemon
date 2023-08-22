import requests
import time
from modules.getRequests import getDescriptionData, getPokemonData, getRegionData, getSpriteData
from modules.writePokemon import writeDescription, writeHeightWeight, writeNameNumber, writeRegion, writeTypes
from utils.constants import SECONDS_IN_A_MINUTE
from utils.options import apiWaitTime, bootMessage, dataOptionsDict, filename, pokemonToBeQueried, startingPoint, terminationMessage, writeMode


# UTILITY FUNCTIONS
######################################################


def checkOptions(name):
    if dataOptionsDict[name] == 'y' or dataOptionsDict[name] == 'Y':
        return True
    else:
        return False


def displayEstimatedRunTime():
    estRunTimeAdjuster = 1.4

    estRunTime = ((apiWaitTime * pokemonToBeQueried) * estRunTimeAdjuster)
    if estRunTime < SECONDS_IN_A_MINUTE:
        print('Estimated run time: ', estRunTime, 'seconds\n')
    else:
        print('Estimated run time: ', estRunTime /
              SECONDS_IN_A_MINUTE, 'minutes\n')


def displayTerminate(time_start):
    print('****************************** ')
    print('Program returned ', (pokemonToBeQueried), ' pokemon.')
    print('******************************\n')

    time_stop = time.perf_counter()
    time_total = time_stop - time_start

    if time_total > SECONDS_IN_A_MINUTE:
        time_total = time_total / SECONDS_IN_A_MINUTE
        unit = 'minutes'
    else:
        unit = 'seconds'

    print(f'Total run time: {time_total} {unit}\n')
    print(terminationMessage)
    input('Press any key...')


# BUILD SEQUENCE
######################################################


def buildFile(dataPoke, dataDesc, dataRegion):
    pokemonName = dataPoke['name']
    fout.write('{\n')

    print(f'Writing: {pokemonName.capitalize()}')

    writeNameNumber(dataPoke, fout)
    if checkOptions('pokemonRegion'):
        writeRegion(dataRegion, fout)
    writeTypes(dataPoke, fout)
    writeHeightWeight(dataPoke, fout)

    if checkOptions('pokemonDescription'):
        writeDescription(dataDesc, fout)

    if checkOptions('pokemonImage'):
        getSpriteData(dataPoke)

    fout.write("},\n")


# REQUEST SEQUENCE
######################################################


def getRequests(pokeNumber):
    pokeNumber = str(pokeNumber)

    dataPoke = getPokemonData(pokeNumber)           # .

    if checkOptions('pokemonDescription'):
        dataDesc = getDescriptionData(pokeNumber)   # Desciption
    else:
        dataDesc = {}
    if checkOptions('pokemonRegion'):
        dataRegion = getRegionData(dataDesc)        # Region
    else:
        dataRegion = {}

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
    time_start = time.perf_counter()

    print(bootMessage)
    displayEstimatedRunTime()

    rangeEnd = startingPoint + pokemonToBeQueried

    fname = filename
    fout = open(fname, writeMode, encoding='utf-8')

    requestLoop()

    fout.close()
    displayTerminate(time_start)

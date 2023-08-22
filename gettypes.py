import requests
import time
from modules.getRequests import getTypeData
from utils.options import filename_types, writeMode


def getList(source):
    tList = []

    counter = 0
    for x in source:
        name = source[counter]['name']
        tList.append(name)
        counter = counter + 1

    return tList


def writeFile(dataTypes):
    name = dataTypes['name']

    double_damage_from = getList(
        dataTypes['damage_relations']['double_damage_from'])

    half_damage_from = getList(
        dataTypes['damage_relations']['half_damage_from'])

    no_damage_from = getList(dataTypes['damage_relations']['no_damage_from'])

    double_damage_to = getList(
        dataTypes['damage_relations']['double_damage_to'])

    half_damage_to = getList(
        dataTypes['damage_relations']['half_damage_to'])

    no_damage_to = getList(dataTypes['damage_relations']['no_damage_to'])

    print(f'Writing: {name}')

    fout.write('{\n')
    fout.write(f'"name": "{name}",\n')
    fout.write('"data": {\n')
    fout.write(f'\t"double_damage_from": {double_damage_from},\n')
    fout.write(f'\t"half_damage_from": {half_damage_from},\n')
    fout.write(f'\t"no_damage_from": {no_damage_from},\n')
    fout.write(f'\t"double_damage_to": {double_damage_to},\n')
    fout.write(f'\t"half_damage_from": {half_damage_to},\n')
    fout.write(f'\t"no_damage_from": {no_damage_from},\n')
    fout.write('\t}\n')
    fout.write("},\n")


if __name__ == "__main__":
    fname = filename_types
    fout = open(fname, writeMode, encoding='utf-8')

    for x in range(1, 19):
        dataTypes = getTypeData(x)
        writeFile(dataTypes)
        time.sleep(0.1)
    fout.close()

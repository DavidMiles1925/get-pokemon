# WRITE FUNCTIONS
######################################################


def writeNameNumber(dataPoke, fout):
    number = dataPoke['id']
    name = dataPoke['name']

    fout.write('"number": "' + str(number) + '",\n')
    fout.write('"name": "' + name.capitalize() + '",\n')


def writeRegion(dataRegion, fout):
    region = dataRegion['main_region']['name']
    fout.write('"region": "' +
               region.capitalize() + '",\n')


def writeTypes(dataPoke, fout):
    counter = 0
    for x in dataPoke['types']:
        pokeType = dataPoke['types'][counter]['type']['name']

        fout.write('"type_' + str(counter) + '" : "' +
                   pokeType.capitalize() + '",\n')

        counter = counter + 1


def writeHeightWeight(dataPoke, fout):
    height = dataPoke['height']
    weight = dataPoke['weight']

    fout.write('"height": "' + str(height) + '",\n')
    fout.write('"weight": "' + str(weight) + '",\n')


def writeDescription(dataDesc, fout):
    counter = 0
    for x in dataDesc['flavor_text_entries']:
        if x['language']['name'] == "en":
            break
        counter = counter + 1

    rawDescriptionText = dataDesc['flavor_text_entries'][counter]['flavor_text']
    modDescriptionText = rawDescriptionText.replace("\x0c", " ")
    descriptionText = modDescriptionText.replace("\n", " ")

    fout.write('"description": "' + descriptionText + '",\n')

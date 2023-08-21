import requests

image = requests.get(
    'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/132.png')

print(type(image))
print(image.content)

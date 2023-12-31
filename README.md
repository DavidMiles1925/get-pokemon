# GetPokemon

GetPokemon was initially created to gather data for an app that delivers a random "Pokemon of the Day". I found that PokeAPI is a wonderful resource, but I wanted to be able to run the app offline, and I only needed a small sliver of what PokeAPI has to offer.

Now, I have made many improvements to make the program usable by anyone who finds a need for it.

## Installation

- You will need Git installed. [Git Installation](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

1. In your terminal, navigate to the directory where you would like GetPokemon to live.
2. Clone the git repository and enter the directory with these commands:

```bash
git clone https://github.com/DavidMiles1925/get-pokemon.git
cd get-pokemon
```

3. Adjust the options in `\utils\options.py`.
4. Run the program with this command:

```bash
python GetPokemon.py
```

\*NOTE: Depending on your operating system this command may look slightly different. Google how to run a python script for your operating system if necessary.

## FAQ

### What does GetPokemon do?

This code is used to buid a custom JSON file by pulling data from PokeAPI.

### Why do I need GetPokemon? (use cases)

- Building your own file means easier access to the data you want. PokeAPI is a great resource, but it can be hard to navigate for beginners.
- Build a JSON file to reference while your app is offline.

### How do I use GetPokemon?

See the installation instructions at the top of this document.

## Documetation

### Options

To change the run options, edit the file `options.py` in the `/utils` directory.

### Resources

**PokeAPI documentation:**
[PokeApi](https://pokeapi.co/)

### Dependencies

**Pillow:**
`python -m pip install pillow`

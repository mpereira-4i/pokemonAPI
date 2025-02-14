from fastapi import FastAPI
from pokemon_db import PokemonDB

app = FastAPI()
pokemonDB = PokemonDB()

@app.get("/")
def read_root():
    return {"API is running"}

@app.get("/pokemons")
def get_all():
    pokemons = pokemonDB.read_all()
    return pokemons

@app.get("/pokemons/{pokemon_id}")
def get_pokemon(pokemon_id: int):
    pokemon = pokemonDB.read_pokemon(pokemon_id)
    return pokemon
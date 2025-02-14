from fastapi import FastAPI
from models.pokemon_db import PokemonDB
from models.pokemon import Pokemon

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

@app.post("/pokemons")
def add_pokemon(pokemon: Pokemon):
    pokemonDB.insert_pokemon(pokemon)
    return {"message": "Pokemon added successfully"}
from fastapi import FastAPI
from services.pokemon import PokemonService
from schemas.pokemon import Pokemon

app = FastAPI()
pokemon_service = PokemonService()

@app.get("/")
def read_root():
    return {"API is running"}

@app.get("/pokemons")
def get_all():
    pokemons = pokemon_service.get()
    return pokemons

@app.get("/pokemons/{pokemon_id}")
def get_pokemon(pokemon_id: int):
    pokemon = pokemon_service.get_by_id(pokemon_id)
    return pokemon

@app.post("/pokemons")
def add_pokemon(pokemon_input: Pokemon):
    pokemon = pokemon_service.create(pokemon_input)   
    return pokemon
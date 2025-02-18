from fastapi import APIRouter, Query
from services.pokemon import PokemonService
from schemas.pokemon import Pokemon

router = APIRouter(
    prefix="/pokemons",
    tags=["pokemons"],
)

pokemon_service = PokemonService()

@router.get("/")
async def get_all(page: int = Query(1), page_size: int = Query(50)):
    pokemons = pokemon_service.get(page, page_size)
    return pokemons

@router.get("/{pokemon_id}")
async def get_pokemon(pokemon_id: int):
    pokemon = pokemon_service.get_by_id(pokemon_id)
    return pokemon

@router.post("/", status_code=201)
async def add_pokemon(pokemon_input: Pokemon):
    pokemon = pokemon_service.create(pokemon_input)   
    return pokemon

@router.put("/{pokemon_id}")
async def update_pokemon(pokemon_id: int, pokemon: Pokemon):
    pokemon = pokemon_service.update(pokemon_id, pokemon)
    return pokemon

@router.delete("/{pokemon_id}")
async def delete_pokemon(pokemon_id: int):
    pokemon = pokemon_service.delete(pokemon_id)
    return pokemon
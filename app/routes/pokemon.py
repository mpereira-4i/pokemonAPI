from fastapi import APIRouter
from services.pokemon import PokemonService
from schemas.pokemon import Pokemon

router = APIRouter(
    prefix="/pokemons",
    tags=["pokemons"],
)

pokemon_service = PokemonService()

@router.get("/")
async def get_all():
    pokemons = pokemon_service.get()
    return pokemons

@router.get("/{pokemon_id}")
async def get_pokemon(pokemon_id: int):
    pokemon = pokemon_service.get_by_id(pokemon_id)
    return pokemon

@router.post("/")
async def add_pokemon(pokemon_input: Pokemon):
    pokemon = pokemon_service.create(pokemon_input)   
    return pokemon
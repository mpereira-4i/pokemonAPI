from fastapi import HTTPException
from repositories.pokemon import PokemonRepository
from schemas.pokemon import Pokemon

from bson.json_util import dumps
import json

class PokemonService:
    
    def __init__(self):
        self._pokemon_repository = PokemonRepository()

    def json_helper(self, data):
        data = dumps(data)
        data = json.loads(data)
        return data
    
    def get_by_id(self, pokemon_id):
        pokemon = self._pokemon_repository.get_by_id(pokemon_id)
        pokemon = self.json_helper(pokemon)

        if not pokemon:
            raise HTTPException(status_code=404, detail="Pokemon not found")

        return pokemon
    
    def get(self, page, page_size):
        pokemons = self._pokemon_repository.get(page, page_size)
        pokemons = self.json_helper(pokemons)
        return pokemons

    def create(self, pokemon: Pokemon):
        created_pokemon = str(self._pokemon_repository.create(pokemon))
        if not created_pokemon:
            raise HTTPException(status_code=400, detail="Error creating pokemon")
        
        return created_pokemon
    
    def update(self, pokemon_id, pokemon: Pokemon):
        updated_pokemon = self._pokemon_repository.update(pokemon_id, pokemon)
        if not updated_pokemon:
            raise HTTPException(status_code=404, detail="Pokemon not found")
        
        return updated_pokemon
    
    def delete(self, pokemon_id):
        deleted_pokemon = self._pokemon_repository.delete(pokemon_id)
        if not deleted_pokemon:
            raise HTTPException(status_code=404, detail="Pokemon not found")
        
        return deleted_pokemon

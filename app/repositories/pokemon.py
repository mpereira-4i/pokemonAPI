from pydantic import BaseModel
from config.database import get_database

class PokemonRepository:

    def __init__(self):
        self.db = get_database()
        self._collection_name = "pokedex"
        self._pokemon_collection = self.db[self._collection_name]
    
    def get_by_id(self, pokemon_id):
        pokemon = self._pokemon_collection.find_one({"id": pokemon_id})
        return pokemon
    
    def get(self):
        pokemons = self._pokemon_collection.find().limit(50)
        return pokemons

    def create(self, pokemon):
        result = self._pokemon_collection.insert_one(pokemon.dict())
        return result.inserted_id
    


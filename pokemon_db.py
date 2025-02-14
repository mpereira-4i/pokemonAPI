from pydantic import BaseModel
from mongo_connection import get_database

from bson.json_util import dumps
import json

class PokemonDB(BaseModel):
    
    def open_db(self):
        try:
            data = get_database()
            data = data["pokedex"]
        except Exception as e:
            print(e)
        return data
    
    def json_helper(self, data):
        data = dumps(data)
        data = json.loads(data)
        return data

    def read_all(self):
        pokemons = self.open_db().find()
        pokemons = self.json_helper(pokemons)
        return pokemons
    
    def read_pokemon(self, pokemon_id):
        pokemon = self.open_db().find({"id": pokemon_id})
        pokemon = self.json_helper(pokemon)
        return pokemon
    
    

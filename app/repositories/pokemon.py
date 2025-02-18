from config.database import get_database

class PokemonRepository:

    def __init__(self):
        self.db = get_database()
        self._collection_name = "pokedex"
        self._pokemon_collection = self.db[self._collection_name]
    
    def get_by_id(self, pokemon_id):
        pokemon = self._pokemon_collection.find_one({"id": pokemon_id})
        return pokemon
    
    def get(self, page=1, page_size=50):
        skip = (page - 1) * page_size
        pokemons = self._pokemon_collection.find().skip(skip).limit(page_size)
        return list(pokemons)

    def create(self, pokemon):
        result = self._pokemon_collection.insert_one(pokemon.dict())
        return result.inserted_id

    def update(self, pokemon_id, pokemon):
        result = self._pokemon_collection.update_one({"id": pokemon_id}, {"$set": pokemon.dict()})
        return result.modified_count
    
    def delete(self, pokemon_id):
        result = self._pokemon_collection.delete_one({"id": pokemon_id})
        return result.deleted_count
    


from fastapi import FastAPI
from routes.pokemon import router as pokemon_router

app = FastAPI()

app.include_router(pokemon_router)

@app.get("/")
async def root():
    return {"message": "Bem-vindo à API de Pokémons!"}
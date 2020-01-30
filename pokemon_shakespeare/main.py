from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root() -> str:
    return "Hello, world!"


@app.get("/pokemon/{pokemon}")
def read_pokemon(pokemon: str):
    return pokemon

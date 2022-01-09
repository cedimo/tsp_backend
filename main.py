from fastapi import Request, FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
from fastapi.params import Body
import requests

from config import ors_key

app = FastAPI()

# origins from which API calls are allowed
origins = [
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/")
async def test(request: Request):
    frontend_data = await request.json()

    try:
        # ACHTUNG: Alle JSON Objekte für OpenRouteService Aufrufe müssen " statt ' enthalten
        url = 'https://api.openrouteservice.org/v2/matrix/foot-walking'
        headers = {
            'Authorization': ors_key,
            'Content-Type': 'application/json; charset=utf-8',
            'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8'
        }
        # replace double quotes
        data = str(frontend_data).replace("\'", "\"")
        matrix = requests.post(url, data=data, headers=headers)

    except:
        print('OpenRouteService Error occured')

    return matrix.json()

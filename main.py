from fastapi import Request, FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

from optimization import optimize
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
        # --------------- MATRIX API CALL ---------------
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
        matrix = matrix.json()


        # --------------- OPTIMIZATION ---------------
        tour = optimize(matrix)


        # --------------- DIRECTIONS API CALL ---------------
        coordinates = []
        for i in tour:
            coordinates.append(matrix['destinations'][i]['location'])
        
        # add starting point as last point again
        coordinates.append(matrix['destinations'][tour[0]]['location'])

        coords_dict = dict.fromkeys(["coordinates"], coordinates)

        url = 'https://api.openrouteservice.org/v2/directions/foot-walking/geojson'
        data = str(coords_dict).replace("\'", "\"")

        route = requests.post(url, data=data, headers=headers)

        return route.json()

    except:
        return 'OpenRouteService Error occured'

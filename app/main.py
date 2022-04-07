from fastapi import Request, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.helpers import console_output, openrouteservice
from app.algorithms import gurobi, brute_force, nearest_neighbor

app = FastAPI()

# origins from which API calls are allowed (port 8080 for devmode, 80 for prodmode)
origins = [
    "http://localhost:8080",
    "http://localhost",
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
        matrix = openrouteservice.getMatrix(frontend_data)
    except:
        return 'OpenRouteService Error occured'


    # --------------- OPTIMIZATION ---------------
    # matrix and one algorithm are required
    # tour returned by first algorithm will be used for directions and frontend
    # optional algorithms get calculated for comparison of time and accuracy

    # ! function in algorithm must be named optimize(matrix)

    tour = console_output.solve(matrix, gurobi, brute_force, nearest_neighbor)


    try:
        route = openrouteservice.getRoute(matrix, tour)
    except:
        return 'OpenRouteService Error occured'

    return route.json()

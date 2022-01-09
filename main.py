from fastapi import Request, FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

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
    data = await request.json()
    data = json.dumps(data)
    data = json.loads(data)

    # array with all coordinates
    # Format: Longitude, Latitude
    coords = data['coords']

    return coords

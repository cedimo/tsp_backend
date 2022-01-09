from fastapi import Request, FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
    x = await request.json()

    # TODO

    return x

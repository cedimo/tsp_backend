# TSP Backend

## Credentials
Das Backend greift auf eine Schnittstelle von Openrouteservice zu, welche einen API-Key benötigt.
Ein gültiger API-Key kann über https://openrouteservice.org/ bezogen und muss als Environment-Variable mit dem Namen ORS_KEY gesetzt werden.

Windows:

    $Env:ORS_KEY = '<ORS_KEY>'

Linux & macOS:

    export ORS_KEY = '<ORS_KEY>'

Der Key wird innerhalb des Backends ausschließlich für Requests an die Schnittstelle von Openrouteservice verwendet und nicht gespeichert.

## Bibliotheken
Um effizient zu arbeiten, wird nicht das komplette Venv geteilt. Die benötigten Bibliotheken werden in der [requirements.txt](requirements.txt) 
Datei gespeichert.

Form der [requirements.txt](requirements.txt) Datei:

    pkg1
    pkg2
    pkg3>=1.0,<=2.0

## Installation der benötigten Bibliotheken
    pip install -r requirements.txt

## Starten des Servers
    uvicorn app.main:app --reload

## Deployment auf neuem Server (venv erstellen und Bibliotheken installieren)
    virtualenv --no-site-packages --distribute .env && source .env/bin/activate && pip install -r requirements.txt

## Docker

### Build image

    docker build -t username/tsp-backend .


### Run image
<ORS_KEY> is the API Key for Openrouteservice

    docker run -it -p 8000:8000 -d --name tsp-backend -e ORS_KEY='<ORS_KEY>' username/tsp-backend


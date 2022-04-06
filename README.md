# TSP Backend

## ACHTUNG: Alle OpenRouteService Calls benötigen `"` statt `'`

## Credentials
Alle sensiblen Daten werden in einer `config.py` Datei abgelegt und in der Anwendung importiert und verwendet (keine Datenzuweisung). Diese Datei wird nicht geteilt und nur lokal angelegt.

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
    uvicorn main:app --reload

## Deployment auf neuem Server (venv erstellen und Bibliotheken installieren)
    virtualenv --no-site-packages --distribute .env && source .env/bin/activate && pip install -r requirements.txt

## Docker

### Build image
```
docker build -t username/tsp-backend .
```

### Run image
```
docker run -it -p 8000:8000 -d --name tsp-backend username/tsp-backend
```

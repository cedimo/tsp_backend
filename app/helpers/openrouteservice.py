import requests
import os

ors_key = os.getenv('ORS_KEY')
print(ors_key)

headers = {
        'Authorization': ors_key,
        'Content-Type': 'application/json; charset=utf-8',
        'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8'
    }


def getMatrix(frontend_data):
    # --------------- MATRIX API CALL ---------------
    # ACHTUNG: Alle JSON Objekte für OpenRouteService Aufrufe müssen " statt ' enthalten
    url = 'https://api.openrouteservice.org/v2/matrix/foot-walking'
    
    # replace double quotes
    data = str(frontend_data).replace("\'", "\"")
    
    matrix = requests.post(url, data=data, headers=headers)
    matrix = matrix.json()

    return matrix


def getRoute(matrix, tour):
    coordinates = []
    for i in tour:
        coordinates.append(matrix['destinations'][i]['location'])
    
    # add starting point as last point again
    coordinates.append(matrix['destinations'][tour[0]]['location'])

    coords_dict = dict.fromkeys(["coordinates"], coordinates)

    url = 'https://api.openrouteservice.org/v2/directions/foot-walking/geojson'
    data = str(coords_dict).replace("\'", "\"")

    route = requests.post(url, data=data, headers=headers)

    return route
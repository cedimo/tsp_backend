# TSP Frontend

Um effizient zu arbeiten, wird nicht das komplette Venv geteilt. Die benötigten Bibliotheken werden in der [requirements.txt](requirements.txt) 
Datei gespeichert.


Form der [requirements.txt](requirements.txt) Datei:

    pkg1
    pkg2
    pkg3>=1.0,<=2.0

### Installation der benötigten Bibliotheken
    pip install -r requirements.txt

### Deployment auf neuem Server (venv erstellen und Bibliotheken installieren)
    virtualenv --no-site-packages --distribute .env && source .env/bin/activate && pip install -r requirements.txt
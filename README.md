# DjangoBnB

## Description

DjangoBnB est une application web de gestion de lieux, d'utilisateurs, de pays, de villes, de commodités et de critiques. Cette application utilise Django pour la gestion des vues et des modèles et DRF-YASG pour la documentation de l'API.

## Prérequis

- Python 3.10
- pip
- virtualenv

## Installation

1. Cloner le dépôt :

    ```bash
    git clone https://github.com/Guillom8769/djangobnb.git
    cd djangobnb
    ```

2. Créer et activer un environnement virtuel :

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Sur Windows utilisez .venv\Scripts\activate
    ```

3. Installer les dépendances :

    ```bash
    pip install -r requirements.txt
    ```

## Commandes Django

1. Appliquer les migrations :

    ```bash
    python manage.py migrate
    ```

2. Démarrer le serveur de développement :

    ```bash
    python manage.py runserver
    ```

3. Charger les données des pays depuis un fichier CSV :

    ```bash
    python manage.py load_countries_csv
    ```

4. Accéder à l'interface d'administration :

    - [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

5. Accéder à la documentation de l'API :

    - Swagger : [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
    - ReDoc : [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

## Fonctionnalités

- Gestion des utilisateurs (CRUD)
- Gestion des lieux (CRUD)
- Gestion des critiques (CRUD)
- Gestion des commodités (CRUD)
- Gestion des pays (CRUD)
- Gestion des villes (CRUD)
- Documentation interactive de l'API avec Swagger et ReDoc

## Mise à jour du fichier `requirements.txt`

```txt
Django==3.2.8
djangorestframework==3.12.4
drf-yasg==1.20.0

Pages Web Disponibles

    Page d'accueil : http://127.0.0.1:8000/
    Liste des utilisateurs : http://127.0.0.1:8000/users/
    Liste des lieux : http://127.0.0.1:8000/places/
    Liste des critiques : http://127.0.0.1:8000/reviews/
    Liste des commodités : http://127.0.0.1:8000/amenities/
    Liste des pays : http://127.0.0.1:8000/countries/
    Liste des villes : http://127.0.0.1:8000/cities/
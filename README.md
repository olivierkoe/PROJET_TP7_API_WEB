# FastAPI & SQLAlchemy

## Description

Ce projet est un exemple d'application utilisant **FastAPI** et **SQLAlchemy**. Il a été développé dans le cadre de la session 2024-D11 de Diginamic, une formation en **cybersécurité** appliquée, utilisant des technologies comme **Bash** et **Python**.

## Auteurs

**Groupe 2 : Alexandre SACKS, Olivier KOENIG, Sylvie TCHOUMI, Maxime GODINEAU**  
Formation **Diginamic - Session 2024-D11**
## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

- **Python 3.8+**
- **Git & Github**

## Architecture

Le projet est structuré de la manière suivante :

```bash
PROJET_TP7_API_WEB/
│
├── src/
│   ├── main.py            # Point d'entrée principal de l'application
│   ├── database.py        # Configuration et gestion de la base de données
│   ├── models.py          # Définition des modèles de données (tables)
│   ├── repositories/      # Contient les classes pour accéder aux données (logique d'accès à la BDD)
│   ├── services/          # Contient la logique métier de l'application
│   ├── schemas/           # Définitions des schémas de validation des données (Pydantic)
│   └── routers/           # Contient les routes API (endpoints)
│
├── .gitignore             # Fichier de configuration Git pour ignorer certains fichiers/dossiers
├── README.md              # Documentation du projet
├── requirements.txt       # Liste des dépendances du projet
├── .venv/                 # Environnement virtuel Python
└── .env                   # Fichier de configuration des variables d'environnement
```

## Installation

### 1. Cloner le projet

Clonez le projet depuis GitHub :

```bash
git clone https://github.com/olivierkoe/PROJET_TP7_API_WEB.git
cd PROJET_TP7_API_WEB
```

### 2. Créer un environnement virtuel

#### Sous Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### Sous Linux/MacOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Installer les dépendances

Installez les bibliothèques nécessaires en exécutant la commande suivante :

```bash
pip install -r requirements.txt
```

### 4. Configuration

1. Créez une base de données "fromagerie_com" avec votre Système de Gestion de Base de Données (SGDB) préféré.
2. Modifiez la **connection string** dans le fichier `database.py` pour vous connecter à votre base de données.

### 5. Lancer le serveur

Pour démarrer le serveur de développement, exécutez la commande suivante :

```bash
uvicorn src.main:app --reload
```

Cela démarrera le serveur FastAPI via uvicorn, accessible à l'adresse suivante : [http://127.0.0.1:8000](http://127.0.0.1:8000).

### 6. Utilisation

Une fois le serveur démarré, vous pouvez accéder à la documentation interactive générée automatiquement par Swagger à l'adresse suivante : [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

Cette interface vous permettra de tester les différentes API de manière simple et intuitive.

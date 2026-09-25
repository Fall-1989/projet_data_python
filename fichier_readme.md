# Projet Data Python : Gestion de Données & Pipeline ETL Iris

Ce projet en Python est articulé autour de deux fonctionnalités majeures :
1. **Gestion orientée objet de données "Personne"** : Création d'objets, stockage dans un fichier Excel et exportation en masse vers une base de données relationnelle **PostgreSQL**.
2. **Pipeline ETL & Calcul Scientifique sur le jeu de données Iris** : Récupération en streaming depuis un dépôt GitHub, nettoyage de données, analyses statistiques complètes, enregistrement sous forme de rapport multi-feuilles Excel et visualisation graphique.

---

## 📋 Table des Matières
- [Architecture & Fonctionnalités](#-architecture--fonctionnalités)
- [Jeu de Données (Dataset Iris)](#-jeu-de-données-dataset-iris)
- [Prérequis et Installation](#-prérequis-et-installation)
- [Configuration de la Base de Données](#-configuration-de-la-base-de-données)
- [Utilisation](#-utilisation)
- [Auteur](#-auteur)

---

## 🚀 Architecture & Fonctionnalités

### Partie 1 : Gestion des Données "Personne"
* **Modélisation Orientée Objet** : Définition de la classe `Person` (attributs : `nom`, `prenom`, `age`).
* **Exportation Excel** : Génération automatisée du fichier `Fichier personne.xlsx` à l'aide d'**`openpyxl`**.
* **Insertion PostgreSQL** : Connexion à la base `BD_Personne` et insertion optimisée en masse avec `cur.executemany()` via la bibliothèque **`psycopg`**.

### Partie 2 : Pipeline ETL et Traitement Pandas (Dataset Iris)
* **Extraction (E)** : Chargement en direct du dataset CSV `dataset_61_iris.csv` depuis un dépôt distant GitHub.
* **Transformation / Nettoyage (T)** :
  * Détection et suppression des doublons.
  * Imputation des valeurs manquantes par la moyenne des colonnes numériques.
  * Calcul des statistiques descriptives synthétiques (Moyenne, Médiane, Écart-type, Minimum, Maximum).
* **Chargement (L)** : Ajout des données nettoyées et des statistiques dans une seconde feuille nommée `Iris_Traite` au sein du fichier Excel existant.
* **Visualisation** : Génération de graphiques exploratoires avec `matplotlib` et `seaborn` (`pairplot` structuré par espèce `class`).

---

## 🌸 Jeu de Données (Dataset Iris)

Le jeu de données de référence **Iris** contient les mesures (en cm) de la longueur et de la largeur des sépales et pétales de 150 fleurs issues de 3 espèces distinctes :
* *Iris setosa*
* *Iris versicolor*
* *Iris virginica*

* **Source** : [GitHub - Fall-1989/projet_data_python](https://raw.githubusercontent.com/Fall-1989/projet_data_python/refs/heads/master/dataset_61_iris.csv)

---

## 🛠️ Prérequis et Installation

### 1. Cloner le projet
```bash
git clone https://github.com/Fall-1989/projet_data_python.git
cd projet_data_python
```

### 2. Dépendances requises
Installez l'ensemble des bibliothèques nécessaires avec `pip` :

```bash
pip install pandas openpyxl psycopg[binary] matplotlib seaborn
```

---

## 🗄️ Configuration de la Base de Données

Avant d'exécuter le script, assurez-vous d'avoir une instance PostgreSQL en cours d'exécution.

1. **Créer la base de données** dans PostgreSQL / pgAdmin :
   ```sql
   CREATE DATABASE "BD_Personne";
   ```

2. **Créer la table `personne`** :
   ```sql
   CREATE TABLE personne (
       person_id SERIAL PRIMARY KEY,
       prenom VARCHAR(50),
       nom VARCHAR(50) NOT NULL,
       age INT
   );
   ```

3. **Mettre à jour les identifiants** dans le fichier `person.py` :
   ```python
   DB_CONFIG = {
       "dbname": "BD_Personne",
       "user": "postgres",
       "password": "VOTRE_MOT_DE_PASSE",
       "host": "localhost",
       "port": "5432"
   }
   ```

---

## 🖥️ Utilisation

Exécutez simplement le fichier principal Python :

```bash
python person.py
```

### Résultats attendus :
1. Affichage de la liste des personnes dans le terminal.
2. Création et alimentation du fichier Excel `Fichier personne.xlsx`.
3. Confirmation de l'insertion des personnes dans la table PostgreSQL.
4. Affichage dans la console des métriques de nettoyage et des statistiques calculées sur le dataset Iris.
5. Création de la feuille `Iris_Traite` dans le fichier Excel avec le dataset et sa synthèse.
6. Affichage des graphiques d'analyse exploratoire des données Iris (`pairplot`).

---

## 👤 Auteur
Projet développé par **Fall-1989**.
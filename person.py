import openpyxl
from openpyxl import load_workbook
import psycopg
import pandas as pd

class Person:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def __str__(self):
        return f"{self.prenom} {self.nom}, {self.age} ans"

    def __repr__(self):
        return self.__str__()


personnes = []
personnes.append(Person("Diop", "Awa", 22))
personnes.append(Person("Ndiaye", "Moussa", 25))
personnes.append(Person("Fall", "Fatou", 30))

for p in personnes:
    print(p)
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "personnes"
    ws.append(["Nom", "Prenom", "Age"])
    for p in personnes:
        ws.append([p.nom, p.prenom, p.age])

    wb.save("Fichier personne.xlsx")
    print("Fichier personnes.xlsx créé avec succes.")

#inserer les personnes dans une base de postgresql BD_personne
#Parametre de connexion a PostgreSQL 
DB_CONFIG = {
   "dbname": "BD_Personne",
   "user": "postgres",
   "password": "F@ll1989",
   "host": "localhost",
   "port": "5432",
}

#connexion et insertion des données
with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            #conversion du tableau d'objets en liste de tuples
            donnes = [(p.prenom, p.nom, p.age) for p in personnes]

            #Requete d'insertion dans la table existant "personne"
            query = """
            INSERT INTO personne (prenom, nom, age)
            VALUES (%s, %s, %s)
            """

            #on execute l'insetion des données
            cur.executemany(query, donnes)

            #Insertion en masse
            conn.commit()

            print(f"Succés : {len(personnes)} personnes ajoutées a la table.")


    #ETL sur les données d'iris traitement en straiming
import pandas as pd
url = "https://raw.githubusercontent.com/Fall-1989/projet_data_python/refs/heads/master/dataset_61_iris.csv"

iris = pd.read_csv(url)
print("---Information avant nettoyage ---")
print("f Nombre de lignes initiales : {len(iris)}")
print(f" Nombre de doublon : {iris.duplicated().sum}")
print("Valeur manquantes par colonne :")
print(iris.isnull().sum())
print("-" * 40)

print(iris.head())
print(iris.head(3))
print(iris.tail(3))

print(iris.dtypes)

print(iris.columns)
print(iris.index)

#Montron la dimention du tableau de données
print(iris.shape)

#Suppression des doublons
iris_nettoye = iris.drop_duplicates()

#Remplacements des valeurs manquant par la moyenne (pour les colonnes numériques)
#Sélection des collonne numérique uniquement
colonnes_numeriques = iris_nettoye.select_dtypes(include=['float64', 'int64']).columns

#Imputation par la moyenne
for col in colonnes_numeriques:
    moyenne_colonne = iris_nettoye[col].mean()
    iris_nettoye[col] = iris_nettoye[col].fillna(moyenne_colonne)

    print("---Information apres nettoyage ---")
    print("f Nombre de lignes restantes : {len(iris_nettoye)}")
    print("Valeur manquantes restantes :")
    print(iris_nettoye.isnull().sum())
    print("-" * 40)

#Calcul des statistique descriptives sur les données nettoyées
    print(iris_nettoye.describe())

#Calcul séparé de la moyenne et médiane
    print(iris_nettoye.mean(numeric_only=True))
    print(iris_nettoye.median(numeric_only=True))

#Traitement des données (calcul des statistique)
mean_df = iris_nettoye.mean(numeric_only=True).to_frame(name="Monyenne") 
median_df = iris_nettoye.median(numeric_only=True).to_frame(name="Médiane")   
std_df = iris_nettoye.std(numeric_only=True).to_frame(name="Ecart-Type")
min_df = iris_nettoye.min(numeric_only=True).to_frame(name="Minimum")
max_df = iris_nettoye.max(numeric_only=True).to_frame(name="Maximum")

#Combinaison de tous les statistique dans un seul DataFrame synthétique
iris_stats = pd.concat([mean_df, median_df, std_df, min_df, max_df], axis=1)
iris_stats.index.name = "Variable"

#Affichage des résultats dans le console
print("---Statistique calculées---")
print(iris_stats)

#accés au élément du colones sepalleegth
iris_nettoye.sepallength
print(iris_nettoye["sepallength"])
print(iris_nettoye.loc[0, "sepallength"])
print(iris_nettoye.loc[0:3, "sepallength"])
print(iris_nettoye["sepallength"]>4.0)

#Exporter les données nottoyer et traiter dans un fichier excel
mon_fichier_excel = "Fichier personne.xlsx"
feuille2 = "Iris_Traite"
with pd.ExcelWriter(mon_fichier_excel, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
    iris_nettoye.to_excel(writer, sheet_name=feuille2, index=False) 
ligne_depart = len(iris_nettoye) + 3
with pd.ExcelWriter(mon_fichier_excel, engine="openpyxl", mode="a", if_sheet_exists="overlay",) as writer:
    iris_stats.to_excel(writer, sheet_name=feuille2, startrow=ligne_depart, index=True) 

print(f"Les données traitées ont été exportées avec succes dans la" f" feuille '{feuille2}' .")

#la visualisation des données avec pandas
import seaborn as sns
import matplotlib.pyplot as plt

#Graphique de base
iris.plot()
iris.hist()
iris.boxplot()

#Graphiques avancés avec l'objet 'plot'
iris.plot.scatter(x='sepallength', y='sepalwidth')

#Tracés avec seaborn
sns.pairplot(iris)
sns.pairplot(iris, hue='class')
plt.show()





    
    

    
    

import openpyxl
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
    
    #ETL sur les données d'iris traitement en straiming
    import pandas as pd
    url = "https://raw.githubusercontent.com/Fall-1989/projet_data_python/refs/heads/master/dataset_61_iris.csv"

    iris = pd.read_csv(url)
    print(iris.head())
    print(iris.head(3))
    print(iris.tail(3))

    print(iris.dtypes)

    print(iris.columns)
    print(iris.index)

#Montron la dimention du tableau de données
    print(iris.shape)

#Calcul des statistique descriptives
    print(iris.describe())

#Calcul séparé de la moyenne et médiane
    print(iris.mean(numeric_only=True))
    print(iris.median(numeric_only=True))

#accés au élément du colones sepalleegth
    iris.sepallength
    print(iris["sepallength"])
    print(iris.loc[0, "sepallength"])
    print(iris.loc[0:3, "sepallength"])
    print(iris["sepallength"]>7.0)
#Exporter les données nottoyer et traiter dans un fichier excel

#la visualisation des données avec pandas
import seaborn as sns
import matplotlib.pyplot as plt

#Basic plots
iris.plot()
iris.hist()
iris.boxplot()

#advanced plots with 'plot' objet
iris.plot.scatter(x='sepallength', y='sepalwidth')

#plots with seaboern
sns.pairplot(iris)
sns.pairplot(iris, hue='class')
plt.show()





    
    

    
    

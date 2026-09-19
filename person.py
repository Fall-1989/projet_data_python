import openpyxl
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
        

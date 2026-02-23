class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix


class Commande:
    def __init__(self):
        self.liste = []
    def passer_commande(self, Produit):
        print(f"Le {Produit.nom} avec un prix de {Produit.prix} est ajouté au panier avec succès")
        dic = {
            "nom" : Produit.nom,
            "prix" : Produit.prix
        }
        self.liste.append(dic)
    def calcul_total(self):
        total = 0
        for element in self.liste:
            total += element["prix"]
        print(f" le montant final à payer est {total}")
        return total
    def paiement(self):
        print(f" {client} La commande a été bien validée | montant : {self.calcul_total()} ")
        
client = "Amath"

p1 = Produit("Coque Simple", 5000)
p2 = Produit("Coque Personnalisée", 7000)

c = Commande()

c.passer_commande(p1)
c.passer_commande(p2)
print("")
c.calcul_total()
c.paiement()

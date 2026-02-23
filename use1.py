class Restaurant:
    def __init__(self, nom, statut, client):
        self.nom = nom
        self.statut = statut
        self.client = client
    def passer_commande(self):
        print(f"Bonjour {self.client}, | Commande : {self.nom}| En {self.statut} chez Katy")

class Livreur:
    def __init__(self, position, livreur):
        self.position = position
        self.livreur = livreur
    def update_by_livreur(self, restaurant):
        print(f"{restaurant.nom} est en {restaurant.statut} de {self.position} vers {restaurant.client}")
    def commande_confirme(self, restaurant):
        print(f"Bonjour je suis {self.livreur}, j'ai livré la commande à {restaurant.client}")
    

resto = Restaurant("Burger", "préparation", "Moussa")
resto.passer_commande()

resto.statut = "livraison"

livreur = Livreur("Chez Katy", "Modou")
livreur.update_by_livreur(resto)
livreur.commande_confirme(resto)
class Article:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

    def presenter(self):
        return f"Article : {self.nom} - {self.prix}FCFA"


class Coque(Article):
    def __init__(self, nom, prix, modele,):
        super().__init__(nom, prix)
        self.modele = modele
        if not self.nom.isalpha():
            raise ValueError("Format invalide")
        if not self.prix.isdigit():
            raise ValueError("Format invalide")
        if not self.modele.isalpha():
            raise ValueError("Format invalide")
    def presenter(self):
        print(f"{self.nom} | {self.modele} | Prix : {self.prix} FCFA")


class Accessoire(Article):
    def __init__(self, nom, prix, type_accessoire):
        super().__init__(nom, prix)
        self.type_accessoire = type_accessoire
        if not self.nom.isalpha():
            raise ValueError("Format invalide")
        if not self.prix.isdigit():
            raise ValueError("Format invalide")
        if not self.type_accessoire.isalpha():
            raise ValueError("Format invalide")
    def presenter(self):
        print(f"{self.type_accessoire} | {self.nom} | {self.prix}")
    

class Panier:
    def __init__(self):
        self.panier = []

    def content_panier(self, Article):
        self.panier.append(Article)
        print(f"Article ajouté au panier !!! Le nombre d'article : {len(self.panier)}")
    def __add__(self, autre_panier):
        nouveau_panier = Panier()
        # concaténer les deux listes d'articles
        nouveau_panier.panier = self.panier + autre_panier.panier
        return nouveau_panier


class Menu:
    def __init__(self):
        self.total_panier = []
    
    def lancer(self):
        while True:
            menu = "Menu"
            print(menu.center(80, "*"))
            print("1 - Créer panier 1")
            print("2 - Crér panier 2")
            print("3 - Ajouter Accessoire")
            print("4 - Ajouter Coque")
            print("5 - Fusionner les deux paniers")
            print("0 - Quitter")

            print("\n=====================================")
            choix = input("Choisissez une option : ").strip()
            try:
                match choix:
                    case "1":
                        panier1 = Panier()
                        print("Panier 1 créé.")
                    case "2":
                        panier2 = Panier()
                        print("Panier 1 créé.")
                    case "3":
                        nom = input("Nom : ")
                        prix = input("Prix : ")
                        typeAccessoire = input("typeAccessoire : ")
                        accessoire = Accessoire(nom, prix, typeAccessoire)
                        accessoire.presenter()
                        panier1.content_panier(accessoire)
                    case "4":
                        nom = input("Nom : ")
                        prix = input("Prix : ")
                        modele = input("modele : ")
                        mod = Coque(nom, prix, modele)
                        mod.presenter()
                        panier2.content_panier(mod)
                    case "5":
                        if not panier1 or not panier2:
                            print("Créez d'abord les deux paniers (options 1 et 2).")
                            continue
                        self.total_panier = panier1 + panier2
                        print(f"Les paniers ont été fusionnés. Avec {len(self.total_panier.panier)} article")

                    case _:
                        exit()
            except Exception as e:
                print(f"Erreur : {e}")

menu = Menu()
menu.lancer()

            




from abc import ABC,  abstractmethod

class ModePaiement(ABC):
    """Classe abstraite représentant un mode de paiement"""

    @abstractmethod
    def payer(self, montant):
        pass


    
class client:
    """Classe représentant un client avec un solde"""

    def __init__(self, nom):
        self.nom =nom
        self.__solde= 0


    def consulter_solde(self):
        """Méthode pour consulter le solde du client"""
        return self.__solde
    

    def alimenter_solde(self, montant):
        """Méthode pour alimenter le solde du client"""

        # Vérification du montant avant d'alimenter le solde
        if montant > 0:
            self.__solde += montant
            print(f"\nVotre solde a été alimenté de {montant}.")
        else:
            print("Le montant invalide")
    

    def retirer(self, montant):
        """Méthode pour retirer un montant du solde du client"""

        # Vérification du montant avant de procéder au retrait
        if montant <= 0:
            print("\nMontant invalide")
            return False
        
        if self.__solde >= montant:
            self.__solde -= montant
            return True
        
        else:
            print("\nSolde insuffisant")
            return False


class PaiementSolde(ModePaiement):
    """Classe représentant un mode de paiement utilisant le solde du client"""

    def __init__(self, client):
        self.client = client

    def payer(self, montant):
        """Méthode pour effectuer un paiement en utilisant le solde du client"""

        print(f"\nPaiement de {montant} Fcfa en utilisant le solde du client {self.client.nom}")

        # Vérification du montant avant de procéder au paiement
        if self.client.retirer(montant):
            print("\nRetrait effectuer avec succes")
        else:
            print("Echec de la transaction")



client1= client("Amath")
client1.alimenter_solde(10000)

print("Solde actuel :", client1.consulter_solde(), "FCFA")


paiement = PaiementSolde(client1)
paiement.payer(4000)
print("Solde actuel :", client1.consulter_solde(), "FCFA")

paiement.payer(7000)
print("Solde final :", client1.consulter_solde(), "FCFA")







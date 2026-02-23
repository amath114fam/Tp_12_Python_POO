class Vehicule:
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele


class Moto(Vehicule):
    def __init__(self, marque, modele, est_bequille = False):
        self.est_bequille = est_bequille
        super().__init__(marque, modele)

    def demarrer(self):
        if not self.est_bequille:
            print("La moto est en arrêt")
        else:
            print("La moto a démaré")


    def lever_bequille(self):
        self.est_bequille = True
        print("La bequille est levée")

moto = Moto("Yamaha", "TMAX")

moto.demarrer()
print("")
moto.lever_bequille()
print("")
moto.demarrer()
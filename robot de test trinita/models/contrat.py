class Contrat:
    def __init__(self, assureur, apporteur_affaire, gamme, type_vente, date_souscription, date_effective, mode_fractionnement, jour_prelevement, mode_paiement, iban, banque,solde_attendre):
        self.assureur = assureur
        self.apporteur_affaire = apporteur_affaire
        self.gamme = gamme
        self.type_vente = type_vente
        self.date_souscription = date_souscription
        self.date_effective = date_effective
        self.mode_fractionnement = mode_fractionnement
        self.jour_prelevement = jour_prelevement
        self.mode_paiement = mode_paiement
        self.iban = iban
        self.banque = banque
        self.solde_attendre= solde_attendre

    def __str__(self):
        return (f"Contrat:\n"
                f"Assureur: {self.assureur}\n"
                f"Apporteur d'affaire: {self.apporteur_affaire}\n"
                f"Gamme: {self.gamme}\n"
                f"Type de vente: {self.type_vente}\n"
                f"Date de souscription: {self.date_souscription}\n"
                f"Date effective: {self.date_effective}\n"
                f"Mode de fractionnement: {self.mode_fractionnement}\n"
                f"Jour de prélèvement: {self.jour_prelevement}\n"
                f"Mode de paiement: {self.mode_paiement}\n"
                f"IBAN: {self.iban}\n"
                f"Banque: {self.banque}\n"
                f"Solde attendre: {self.solde_attendre}\n_______________________")
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            assureur = data.get('assureur'),
            apporteur_affaire = data.get('apporteur_affaire'),
            gamme = data.get('gamme'),
            type_vente = data.get('type_vente'),
            date_souscription = data.get('date_souscription'),
            date_effective = data.get('date_effective'),
            mode_fractionnement = data.get('mode_fractionnement'),
            jour_prelevement = data.get('jour_prelevement'),
            mode_paiement = data.get('mode_paiement'),
            iban = data.get('iban'),
            banque = data.get('banque'),
            solde_attendre = data.get('solde_attendre'),
        )
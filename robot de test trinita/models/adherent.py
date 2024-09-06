class Adherent:  # initialisation d'objet
    def __init__(self, civilite, nom, prenom, date_naissance, nom_rue, code_postal, ville, tel_type, prefixe, numero_telephone):
        self.civilite = civilite
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.nom_rue = nom_rue
        self.code_postal = code_postal
        self.ville = ville
        self.tel_type = tel_type
        self.prefixe = prefixe
        self.numero_telephone = numero_telephone

    def __str__(self):   # comment representer
        return (f"Adherent: {self.civilite} {self.nom} {self.prenom}, "
                f"Date de Naissance: {self.date_naissance}, "
                f"Adresse: {self.nom_rue}, {self.code_postal} {self.ville}, "
                f"Telephone: {self.prefixe} {self.numero_telephone} ({self.tel_type})")

    @classmethod
    def from_dict(cls, data):
        """Create an Adherent instance from a dictionary."""
        return cls(
            civilite=data.get('civilite'),
            nom=data.get('nom'),
            prenom=data.get('prenom'),
            date_naissance=data.get('date_naissance'),
            nom_rue=data.get('nom_rue'),
            code_postal=data.get('code_postal'),
            ville=data.get('ville'),
            tel_type=data.get('tel_type'),
            prefixe=data.get('prefixe'),
            numero_telephone=data.get('numero_telephone'),
        )

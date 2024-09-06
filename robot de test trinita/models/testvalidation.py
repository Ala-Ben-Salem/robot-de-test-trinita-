class Testvalidation:
    def __init__(self, numero_contrat, solde_attendu):
        self.numero_contrat = numero_contrat
        self.solde_attendu = solde_attendu

    def __str__(self):   # comment representer
        return (f"numero_contrat: {self.numero_contrat} , "
                f"solde_attendru: {self.solde_attendu} "
                )

    @classmethod
    def from_dict(cls, data):
        """Create an Adherent instance from a dictionary."""
        return cls(
            numero_contrat = data.get('numero_contrat'),
            solde_attendu=data.get('solde_attendu'),
        )
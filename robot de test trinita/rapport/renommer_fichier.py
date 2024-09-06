import os

def renommer_fichier_word(dossier, ancien_nom, nouveau_nom):
    ancien_chemin = os.path.join(dossier, ancien_nom)
    nouveau_chemin = os.path.join(dossier, nouveau_nom)
    
    if os.path.isfile(ancien_chemin):
        os.rename(ancien_chemin, nouveau_chemin)
        print(f"Le fichier '{ancien_nom}' a été renommé en '{nouveau_nom}'.")
    else:
        print(f"Le fichier '{ancien_nom}' n'existe pas dans le dossier '{dossier}'.")

'''# Exemple d'utilisation de la fonction
renommer_fichier_word(
    dossier="rapport",
    ancien_nom="rapport final.docx",  # Nom actuel du fichier
    nouveau_nom="rapport final renomme.docx"  # Nouveau nom souhaité
)'''

import os

def supprimer_fichiers_word(dossier):
    # Vérifier si le dossier existe
    if os.path.exists(dossier):
        # Lister tous les fichiers dans le dossier
        for fichier in os.listdir(dossier):
            chemin_fichier = os.path.join(dossier, fichier)
            # Supprimer uniquement les fichiers Word (ignorer les autres fichiers et dossiers)
            if os.path.isfile(chemin_fichier) and fichier.endswith('.docx'):
                os.remove(chemin_fichier)
                print(f"Le fichier Word '{fichier}' a été supprimé.")
        print(f"Tous les fichiers Word dans le dossier '{dossier}' ont été supprimés.")
    else:
        print(f"Le dossier '{dossier}' n'existe pas.")

'''# Exemple d'utilisation de la fonction
supprimer_fichiers_word("rapport")'''

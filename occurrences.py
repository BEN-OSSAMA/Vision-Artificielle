import numpy as np
from PIL import Image
import os

def convertir_et_analyser_image():
    nom_image = input("Entrez le nom de l'image : ")
        
    if not os.path.exists(nom_image):
        print(f"Erreur : Le fichier '{nom_image}' n'existe pas.")
        input("Appuyez sur Entrée pour quitter...")
        return
        
    try:
        # Charger l'image et la convertir en niveaux de gris
        image = Image.open(nom_image).convert('L')
        image_array = np.array(image)
        
        # Convertir les niveaux de gris (0-255) en (0-15)
        image_reduite = image_array // 16
        
        # Créer la nouvelle image avec les niveaux réduits
        image_finale = Image.fromarray((image_reduite * 16).astype(np.uint8))
        nom_sortie = "reduit_" + nom_image
        image_finale.save(nom_sortie)
        print(f"\nImage convertie sauvegardée sous '{nom_sortie}'")
        
        # Calculer et afficher les occurrences
        print("\nTableau d'occurrences :")
        print("Niveau | Occurrences")
        print("-" * 20)
        
        for niveau in range(16):
            occurrences = np.sum(image_reduite == niveau)
            if occurrences > 0:
                print(f"{niveau:6d} | {occurrences:10d}")
        
        # Pause avant de quitter
        input("\nAppuyez sur Entrée pour quitter...")
        
    except Exception as e:
        print(f"Erreur lors du traitement de l'image : {str(e)}")
        input("Appuyez sur Entrée pour quitter...")

if __name__ == "__main__":
    convertir_et_analyser_image()
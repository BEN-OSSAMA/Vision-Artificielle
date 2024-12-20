from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
from scipy.ndimage import generic_filter
from os import path

# Fonction pour appliquer le filtre de Nagao (Question 5)
def nagao_filter(block):
    block = block.reshape((5, 5))
    regions = [
        block[:3, :3], block[:3, 1:4], block[:3, 2:],
        block[1:4, :3], block[1:4, 1:4], block[1:4, 2:],
        block[2:, :3], block[2:, 1:4], block[2:, 2:]
    ]
    min_variance = float('inf')
    mean_value = 0
    for region in regions:
        variance = np.var(region)
        if variance < min_variance:
            min_variance = variance
            mean_value = np.mean(region)
    return mean_value

# Fonction pour afficher l'histogramme d'une image couleur (Question 2)
def afficher_histogramme_couleur(nom_image):
    image = Image.open(nom_image)
    pixels = np.array(image)
    plt.figure()
    if pixels.ndim == 3:
        plt.hist(pixels[..., 0].ravel(), bins=256, color='red', alpha=0.5, label='Rouge')
        plt.hist(pixels[..., 1].ravel(), bins=256, color='green', alpha=0.5, label='Vert')
        plt.hist(pixels[..., 2].ravel(), bins=256, color='blue', alpha=0.5, label='Bleu')
    else:
        print("L'image n'est pas en couleur.")
    plt.legend()
    plt.title("Histogramme de l'image couleur")
    plt.xlabel("Intensité")
    plt.ylabel("Nombre de pixels")
    plt.show()

# Fonction pour convertir une image en niveaux de gris ou en binaire (Question 3)
def conversion_gris_binaire(nom_image):
    def seuil_binaire(x):
        return 255 if x > 127 else 0

    print("Choisissez le type de conversion :\n1. Niveaux de gris\n2. Binaire")
    choix = input("Entrez votre choix (1 ou 2) : ")
    if choix == "1":
        profondeur_bits = int(input("Entrez la profondeur de couleur (1-8) : "))
        image = Image.open(nom_image)
        image_profondeur = image.convert("P", palette=Image.ADAPTIVE, colors=2**profondeur_bits)
        image_gris = image_profondeur.convert("L")
        image_gris.show()
        print("Image en niveaux de gris créée avec succès.")
    elif choix == "2":
        image = Image.open(nom_image)
        image_binaire = image.convert("L").point(seuil_binaire, mode='1')
        image_binaire.show()
        print("Image binaire créée avec succès.")

# Fonction pour afficher l'histogramme en niveaux de gris (Question 4)
def afficher_histogramme_gris(nom_image):
    image = Image.open(nom_image).convert("L")
    pixels = np.array(image)
    plt.figure()
    plt.hist(pixels.ravel(), bins=255, color="blue", alpha=0.7)
    plt.title("Histogramme des niveaux de gris")
    plt.xlabel("Niveaux de gris")
    plt.ylabel("Nombre de pixels")
    plt.show()

# Fonction pour appliquer le filtre de Nagao (Question 5)
def appliquer_filtre_nagao(nom_image):
    grayscale_image = Image.open(nom_image).convert("L")
    image_array = np.array(grayscale_image)
    filtered_image_array = generic_filter(image_array, nagao_filter, size=(5, 5))
    filtered_image = Image.fromarray(filtered_image_array.astype(np.uint8))
    filtered_image.show()
    print("Filtre de Nagao appliqué avec succès.")
    filtered_image.save("output_nagao_filter.png")
    print("Image filtrée enregistrée sous 'output_nagao_filter.png'")

# Menu principal
def main():
    while True:
        print("\nMenu:")
        print("1 - Exécuter la Question 1")
        print("2 - Exécuter la Question 2 : Histogramme de l'image couleur")
        print("3 - Exécuter la Question 3 : Conversion en niveaux de gris ou binaire")
        print("4 - Exécuter la Question 4 : Histogramme de niveau de gris")
        print("5 - Exécuter la Question 5 : Filtre de Nagao")
        print("0 - Quitter")
        choix = input("Choisissez une option : ")
        
        if choix == "1":
            print("Fonctionnalité de la Question 1 à implémenter.")
        
        elif choix == "2":
            nom_image = input("Entrez le nom du fichier image : ")
            if path.exists(nom_image):
                afficher_histogramme_couleur(nom_image)
            else:
                print("Image non trouvée.")
                
        elif choix == "3":
            nom_image = input("Entrez le nom du fichier image : ")
            if path.exists(nom_image):
                conversion_gris_binaire(nom_image)
            else:
                print("Image non trouvée.")
                
        elif choix == "4":
            nom_image = input("Entrez le nom du fichier image : ")
            if path.exists(nom_image):
                afficher_histogramme_gris(nom_image)
            else:
                print("Image non trouvée.")
                
        elif choix == "5":
            nom_image = input("Entrez le nom du fichier image : ")
            if path.exists(nom_image):
                appliquer_filtre_nagao(nom_image)
            else:
                print("Image non trouvée.")
                
        elif choix == "0":
            print("Programme terminé.")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()

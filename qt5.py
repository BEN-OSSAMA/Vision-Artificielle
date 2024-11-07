import numpy as np
from PIL import Image
from scipy.ndimage import generic_filter
import matplotlib.pyplot as plt

# Définir la fonction pour appliquer le filtre de Nagao
def nagao_filter(block):
    # Reshape du bloc en une fenêtre de 5x5
    block = block.reshape((5, 5))

    # Définir les 9 sous-régions de la fenêtre de 5x5
    regions = [
        block[:3, :3],  # Haut-gauche 3x3
        block[:3, 1:4], # Haut-centre 3x3
        block[:3, 2:],  # Haut-droite 3x3
        block[1:4, :3], # Milieu-gauche 3x3
        block[1:4, 1:4],# Centre 3x3
        block[1:4, 2:], # Milieu-droite 3x3
        block[2:, :3],  # Bas-gauche 3x3
        block[2:, 1:4], # Bas-centre 3x3
        block[2:, 2:]   # Bas-droite 3x3
    ]

    # Calculer la variance et la moyenne de chaque région
    min_variance = float('inf')
    mean_value = 0
    for region in regions:
        variance = np.var(region)
        if variance < min_variance:
            min_variance = variance
            mean_value = np.mean(region)

    return mean_value

# Charger l'image en niveau de gris
image_name = input("Entrez le nom de l'image (avec extension, ex: image.jpg): ")
try:
    grayscale_image = Image.open(image_name).convert("L")
    image_array = np.array(grayscale_image)
    
    # Appliquer le filtre de Nagao à l'image
    filtered_image_array = generic_filter(image_array, nagao_filter, size=(5, 5))
    
    # Convertir le résultat en image
    filtered_image = Image.fromarray(filtered_image_array.astype(np.uint8))
    
    # Afficher et sauvegarder l'image filtrée
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Image Originale")
    plt.imshow(grayscale_image, cmap='gray')
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.title("Image avec Filtre de Nagao")
    plt.imshow(filtered_image, cmap='gray')
    plt.axis('off')
    
    plt.show()
    
    filtered_image.save("output_nagao_filter.png")
    print("Image filtrée enregistrée sous 'output_nagao_filter.png'")
except Exception as e:
    print(f"Erreur lors du chargement ou traitement de l'image: {e}")

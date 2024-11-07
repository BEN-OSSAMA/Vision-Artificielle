from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
from os import path

# Demande à l'utilisateur le nom de l'image
imageName = input("Enter the image name (in the same dir as this script): ")

# Vérifie si le fichier existe
if not path.exists(imageName):
    print("Image Not Found!")
    exit()

# Ouvre l'image et la convertit en niveaux de gris
im = Image.open(imageName).convert("L")  # "L" pour niveaux de gris
pxl = list(im.getdata())

# Convertit les données de pixel en tableau numpy
a = np.array(pxl)

# Affiche l'histogramme
plt.hist(a, bins=255, color="blue", alpha=0.7)  # 'bins=255' pour chaque niveau de gris
plt.title("Histogramme de niveau de gris")
plt.xlabel("Niveaux de gris")
plt.ylabel("Nombre de pixels")
plt.show()

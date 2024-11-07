from os import path
from PIL import Image

# Fonction pour définir le seuil pour l'image binaire
def get_threshold(x):
    return 255 if x > 127 else 0

# Fonction pour sécuriser l'entrée utilisateur
def try_get_input():
    try:
        value = int(input())
    except ValueError:
        value = -1
    return value

# Demande le nom de l'image à l'utilisateur
print("Entrez le nom de l'image (dans le même dossier que ce script, avec l'extension, ex: 'image.jpg') : ")
image_name = input().strip()
if not path.exists(image_name):
    print("Image introuvable !")
    exit()

# Demande à l'utilisateur de choisir le type de conversion
print("Pour une image en niveaux de gris, tapez 1 ; pour une image binaire, tapez 2 : ")
while True:
    option = try_get_input()
    if option == 1 or option == 2:
        break
    print("Entrée incorrecte, veuillez entrer 1 ou 2.")

# Si l'utilisateur choisit l'image en niveaux de gris
if option == 1:
    print("Entrez le nombre de bits pour la profondeur de couleur (1 à 8) : ")
    while True:
        bit_depth = try_get_input()
        if 1 <= bit_depth <= 8:
            break
        print("Entrée incorrecte, veuillez entrer un nombre entre 1 et 8.")

    # Ouverture et conversion de l'image en fonction de la profondeur de bits
    original_image = Image.open(image_name)
    bit_depth_image = original_image.convert("P", palette=Image.ADAPTIVE, colors=2**bit_depth)
    gray_image = bit_depth_image.convert("L")

    # Sauvegarde et affichage des images
    bit_depth_image.save(f"{image_name.split('.')[0]}_{bit_depth}BitDepth.png")
    gray_image.save(f"{image_name.split('.')[0]}_GrayScale.png")
    print("Images en niveaux de gris créées avec succès.")
    original_image.show()
    bit_depth_image.show()
    gray_image.show()

# Si l'utilisateur choisit l'image binaire
elif option == 2:
    original_image = Image.open(image_name)
    binary_image = original_image.convert("L").point(get_threshold, mode='1')
    
    # Sauvegarde et affichage de l'image binaire
    binary_image.save(f"{image_name.split('.')[0]}_Binary.png")
    print("Image binaire créée avec succès.")
    original_image.show()
    binary_image.show()

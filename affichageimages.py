from PIL import Image

# Charger et afficher I1 et I2
try:
    I1_image = Image.open("I1.pbm")
    I1_image.show()

    I2_image = Image.open("I2.pbm")
    I2_image.show()
except Exception as e:
    print("Erreur lors du chargement de l'image :", e)

from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import os


image_name = input("Entrez le nom de l'image (incluez l'extension, par exemple, 'portrait.jpg') : ")


if not os.path.isfile(image_name):
    print(f"L'image '{image_name}' n'a pas été trouvée dans le répertoire actuel.")
else:
 
    image = Image.open(image_name)

    
    pixels = np.array(image)

   
    plt.figure()
    plt.hist(pixels[..., 0].ravel(), bins=256, color='red', alpha=0.5, label='Red')
    plt.hist(pixels[..., 1].ravel(), bins=256, color='green', alpha=0.5, label='Green')
    plt.hist(pixels[..., 2].ravel(), bins=256, color='blue', alpha=0.5, label='Blue')
    plt.legend()
    plt.show()

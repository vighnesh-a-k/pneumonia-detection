import numpy as np
from PIL import Image



image = Image.open("image.jpg")

pimage= image.resize((512, 512))

imarray=np.array(pimage)


stacked_img = np.stack((imarray)*3, axis=-1)

pil_image=Image.fromarray(imarray)

print(image)

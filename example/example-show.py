import numpy as np
import matplotlib.pyplot as plt

# Carregar imagem
# imagem = np.load('../output/train/images/1_0_320.npy')
imagem = np.load('../output/train/labels/1_0_320_bushes.npy')
# imagem = np.load('../output/train/labels/1_16_176_map.npy')

# Se a imagem tiver múltiplos canais (ex: RGB)
if len(imagem.shape) == 3:
    imagem_plot = imagem[:, :, 0:3]
else:
    imagem_plot = imagem

# Mostrar imagem
plt.imshow(imagem_plot)
plt.title("Imagem")
plt.axis('off')  # remove eixos
plt.show()

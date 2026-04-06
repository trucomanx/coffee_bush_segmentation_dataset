#!/usr/bin/python

from osgeo import gdal
import numpy as np

def tiff_to_array(archivo_tiff, normalize=True, dtype=np.uint8):  
    ds = gdal.Open(archivo_tiff)
    
    if ds is None:
        raise ValueError(f"Error opening file: {archivo_tiff}")

    # Obtener el número de bandas (capas)
    num_bandas = ds.RasterCount

    # Iterar sobre cada banda
    bands = []
    for i in range(1, num_bandas + 1):
        # Leer la banda actual
        banda = ds.GetRasterBand(i)
        # Convertir la banda en una matriz numpy
        matriz_banda = banda.ReadAsArray()
        
        if normalize:
            min_val, max_val = matriz_banda.min(), matriz_banda.max()
            
            if max_val > min_val:
                matriz_banda = (matriz_banda - min_val) / (max_val - min_val) * 255
            else:
                matriz_banda = np.zeros_like(matriz_banda)

        matriz_banda = matriz_banda.astype(dtype)
                
        bands.append(matriz_banda)

    del ds
        
    if not bands:
        raise ValueError("No bands found in TIFF")
    
    h, w = bands[0].shape
    array = np.zeros((h, w, num_bandas), dtype=dtype)

    for i, b in enumerate(bands):
        array[:, :, i] = b

    return array
    

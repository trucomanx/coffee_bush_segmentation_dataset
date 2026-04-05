#!/usr/bin/env python3

from osgeo import gdal
import numpy as np
import os
import imageio
import argparse

def tiff_to_bmp(archivo_tiff, output, image_names=['Red.bmp','Green.bmp','Blue.bmp','Nir.bmp','RedEdge.bmp']):
    os.makedirs(output, exist_ok=True)
    
    ds = gdal.Open(archivo_tiff)
    
    if ds is None:
        raise ValueError(f"Error opening file: {archivo_tiff}")

    # Obtener el número de bandas (capas)
    num_bandas = ds.RasterCount

    # Iterar sobre cada banda
    for i in range(1, num_bandas + 1):
        # Leer la banda actual
        banda = ds.GetRasterBand(i)
        # Convertir la banda en una matriz numpy
        matriz_banda = banda.ReadAsArray()
        
        min_val = np.min(matriz_banda)
        max_val = np.max(matriz_banda)
        
        if max_val > min_val:
            matriz_banda_normalizada = (matriz_banda - min_val) / (max_val - min_val) * 255
        else:
            matriz_banda_normalizada = np.zeros_like(matriz_banda)
        
        matriz_banda_enteros = matriz_banda_normalizada.astype(np.uint8)
        
        nome = image_names[i-1] if i-1 < len(image_names) else f"band_{i}.bmp"
        
        imageio.imwrite(os.path.join(output, nome), matriz_banda_enteros)

    ds = None


def main():
    parser = argparse.ArgumentParser(
        description="Convert TIFF multiband image to BMP bands using GDAL"
    )
    
    parser.add_argument(
        "--input-tiff",
        help="Path to input TIFF file"
    )
    
    parser.add_argument(
        "--output-dir",
        help="Directory to save BMP images"
    )
    
    parser.add_argument(
        "--names",
        nargs="+",
        default=['Red.bmp','Green.bmp','Blue.bmp','Nir.bmp','RedEdge.bmp'],
        help="Optional list of output filenames for bands"
    )

    args = parser.parse_args()

    tiff_to_bmp(
        args.input_tiff,
        args.output_dir,
        args.names
    )


if __name__ == "__main__":
    main()

'''
python3 script.py \
  --input-tiff ../input/0-raw/bgrne_23.tiff \
  --output-dir ../input/1-preprocessed/train/images/1 \
  --names 'Red.bmp' 'Green.bmp' 'Blue.bmp' 'Nir.bmp' 'RedEdge.bmp'
'''

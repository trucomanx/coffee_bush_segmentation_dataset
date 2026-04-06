#!/usr/bin/env python3

from lib_geotiff import tiff_to_array

import os
import imageio
import argparse


def tiff_to_bmp(archivo_tiff, output, image_names=['Red.bmp','Green.bmp','Blue.bmp','Nir.bmp','RedEdge.bmp']):
    os.makedirs(output, exist_ok=True)
    
    array = tiff_to_array(archivo_tiff)
    num_bandas = array.shape[2]

    for i in range(num_bandas):
        nome = image_names[i] if i < len(image_names) else f"band_{i}.bmp"
        
        imageio.imwrite(os.path.join(output, nome), array[:,:,i])

def process_tiff_directory( input_dir, 
                            output_base_dir,
                            image_names=['Red.bmp','Green.bmp','Blue.bmp','Nir.bmp','RedEdge.bmp'],
                            valid_ext = ('.tiff', '.tif') ):
    
    tiff_files = []

    # Percorrer diretório recursivamente
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith(valid_ext):
                full_path = os.path.join(root, file)
                tiff_files.append(full_path)

    # Ordenar (importante para consistência)
    tiff_files.sort()

    if not tiff_files:
        print("No TIFF files found.")
        return

    print(f"Found {len(tiff_files)} TIFF files")


    os.makedirs(output_base_dir, exist_ok=True)

    # Processar cada TIFF
    for idx, tiff_path in enumerate(tiff_files):
        output_dir = os.path.join(output_base_dir, str(idx))
        os.makedirs(output_dir, exist_ok=True)
        
        print(f"[{idx:04d}] {os.path.relpath(tiff_path, input_dir)}")
        
        tiff_to_bmp(tiff_path, output_dir, image_names)
        
def main():
    parser = argparse.ArgumentParser(
        description="Convert TIFF multiband image to BMP bands using GDAL"
    )
    
    parser.add_argument(
        "--input-dir",
        required=True,
        help="Path to input directory of TIFF files"
    )
    
    parser.add_argument(
        "--output-dir",
        required=True,
        help="Directory to save BMP images"
    )
    
    parser.add_argument(
        "--names",
        nargs="+",
        default=['Red.bmp','Green.bmp','Blue.bmp','Nir.bmp','RedEdge.bmp'],
        help="Optional list of output filenames for bands"
    )

    args = parser.parse_args()

    process_tiff_directory(
        args.input_dir,
        args.output_dir,
        args.names
    )


if __name__ == "__main__":
    main()

'''
python3 prog_tiff2bmp.py \
  --input-dir ../input/0-raw \
  --output-dir ../input/1-preprocessed/train/images \
  --names 'Red.bmp' 'Green.bmp' 'Blue.bmp' 'Nir.bmp' 'RedEdge.bmp'
'''
